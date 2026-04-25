# Deep Dive: Why competitive-intel Agent Hallucinates

**Thesis**: The competitive-intel agent is fundamentally **evidence-blind**. It confuses *search results* with *verification*, has no structural way to distinguish hallucinations from facts, and lacks the feedback loops that make your architecture actually work.

---

## Part 1: The Core Architectural Failure

You need **EvidenceRegistry + EvidenceAuditor** system that works like this:

```
INPUT → Research Query
  ↓
[Dual-Source Minimum Rule]
  ├─ Source A (Primary: press release, SEC filing, company blog)
  ├─ Source B (Corroborating: TechCrunch, analyst report, competitor mention)
  ↓
[EvidenceRegistry - Structure]
  ├─ Claim: "Google released TurboQuant algorithm"
  ├─ Source 1: Link + date + quote + credibility score
  ├─ Source 2: Link + date + quote + credibility score
  ├─ Metadata: Published date, update date, confidence level
  ↓
[EvidenceAuditor - Rules]
  ├─ If Source 1 contradicts Source 2 → Flag as DISPUTED
  ├─ If no Source 2 → Status = UNVERIFIED
  ├─ If both sources agree + primary source is official → CONFIRMED
  ├─ Temporal logic: Don't use outdated data as current fact
  ↓
OUTPUT → Daily Brief
  └─ Every claim has traceable evidence lineage
  └─ Confidence levels are explicit
  └─ Disputes are surfaced, not hidden
```

**You need a system that enforces evidence discipline at the structure level**, not just at the instruction level. You can't write a claim without evidence attached. You can't emit an EXIT signal without a quantifiable catalyst.

---

### The competitive-intel Agent Model (Current)

The agent says it will do this:

```
Step 1: Identify top 5 competitors
Step 2: Search each competitor systematically
Step 3: Organize findings into categories
Step 4: Write report with sources
```

But **the structure is completely decoupled from verification**. Here's what actually happens:

```
Research Loop (Per Competitor):
  ├─ For each category (Product, Pricing, Funding, Reviews, Exec):
  │   ├─ Run web_search: "[competitor] [category] [query]"
  │   ├─ Get top 10 results (NO verification that results are accurate)
  │   ├─ Extract findings from snippets
  │   ├─ (CRITICAL FAILURE) No dual-source check
  │   ├─ (CRITICAL FAILURE) No explicit confidence scoring
  │   ├─ Write into report
  │   └─ Move to next category
  ↓
Report Generation:
  ├─ Create markdown table: Category | Finding | Date | Source
  ├─ (CRITICAL FAILURE) Source = search result URL, not verified
  ├─ (CRITICAL FAILURE) No distinction between rumor and confirmed fact
  ├─ (CRITICAL FAILURE) No temporal validation
  └─ Emit report as if complete
```

The agent **has no structural way to know if a finding is hallucinated**. It only has:
- A list of search results
- Instructions to "cite everything"
- Instructions to "distinguish rumors from facts"

But **instructions are not structural enforcement**. The instructions say "cite sources" — but a citation doesn't verify a source. A hallucinated claim with a made-up URL citation is still hallucination.

---

## Part 2: Where This Agent Specifically Hallucinates

### 1. **Search Snippet Confusion**

The agent runs:
```
web_search: "[competitor] funding round"
```

Gets back 10 results with snippets like:
```
"TechCrunch reported that Ironclad raised $50M Series B in March 2026"
```

The agent reads this snippet and writes:
```markdown
| Funding | Ironclad raises $50M Series B in March 2026 | Mar 2026 | TechCrunch |
```

**The hallucination**: The agent has no way to know if:
1. TechCrunch actually reported this (result could be a snippet from a competing article)
2. The $50M number is correct (snippet truncation could have changed context)
3. The date is the publication date or the funding announcement date (usually different)
4. This is still accurate as of today (funding could have fallen through, announcement could have been retracted)

**Your should prevents this by requiring**:
- Primary source verification (link to official announcement, not press coverage)
- Corroborating source (second independent verification)
- Temporal metadata (when was this published, when was it last updated)
- Confidence score (CONFIRMED vs. LIKELY vs. UNVERIFIED)

---

### 2. **Absence of Non-Findings**

The instructions say:
> "If no meaningful updates exist in a category, explicitly state 'No significant updates found in the last 30 days'"

But the agent doesn't actually enforce this. If a search returns zero results, what does the agent do?

**Most likely scenario**: The agent runs one search query, gets zero results, then **rewrites the query** until it gets *something*, then reports that "something" as if it's meaningful.

Example hallucination path:
```
Search 1: "[competitor] new feature announcement April 2026"
Result: 0 hits

Agent's behavior (likely):
Search 2: "[competitor] product update 2026"
Result: 3 hits (but from January 2026, outside 30-day window)

Agent writes: "Competitor announced product updates in recent months"
(No—outside window. Hallucination.)
```

**Your should prevents this by**:
- Requiring explicit date filtering in the evidence
- Flagging findings outside the lookback window as ARCHIVAL, not CURRENT
- Not allowing a "finding" to exist without explicit timestamp validation

---

### 3. **Rumor vs. Confirmed Fact Collapse**

The instructions say:
> "Distinguish confirmed facts from rumors or unverified reports"

But the report structure doesn't enforce this. The markdown table is just:

```markdown
| Category | Finding | Date | Source |
```

There's no "Confidence" or "Status" column. An agent writing this table will naturally collapse rumors and facts into the same row because the structure doesn't differentiate them.

Example hallucination:
```markdown
| Exec Moves | CEO John Smith departs in Q2 2026 | April 2026 | LinkedIn |
```

Is this:
- A confirmed departure? 
- A rumor from someone's LinkedIn post?
- An internal announcement not yet public?
- A restructuring that doesn't include a full departure?

**The agent's instructions say to distinguish**, but the **report structure allows them to collapse into one row**. An LLM optimizing for report completion will collapse ambiguity rather than expand it.

**Your should prevents this by**:
- Having explicit CONFIDENCE columns in EvidenceRegistry
- Refusing to emit findings without confidence scoring
- Flagging low-confidence findings differently in output

---

### 4. **Authority Inversion**

The agent confuses *mention* with *confirmation*.

Example hallucination path:
```
Search: "[competitor] acquisition 2026"

Result: Article titled 
"Competitor X could be acquired by Google, says analyst"

Agent writes:
| Funding | Competitor acquired by Google | Date | Analyst report |

(This is hallucination. Analyst *speculation* ≠ acquisition.)
```

The agent's instructions say:
> "Prioritize primary sources: official press releases, company blog posts..."

But if the search results don't surface the primary source, the agent will **rationalize secondary sources as sufficient**. The instructions are aspirational; the results are deterministic.

**Your should prevents this by**:
- Requiring PRIMARY source as first evidence (press release, SEC filing, official announcement)
- REFUSING to emit a finding without primary source
- Scoring source credibility explicitly (Official: 100, Primary news: 80, Secondary news: 60, Rumor: 20)

---

### 5. **Temporal Hallucinations**

The 30-day lookback window is stated in instructions but **not enforced in structure**.

Example hallucination:
```
Search: "[competitor] pricing 2025"
Result: "Competitor raised prices in Q2 2025"

Agent writes: "Found recent pricing change"
(Not recent. Outside 30-day window. Hallucination.)
```

The agent's search for "2025" will naturally return old results. The instruction to validate against "30 days" is manual filtering, not structural. Manual filtering in LLMs degrades over time as context grows.

**Your should prevents this by**:
- Storing PUBLISHED_DATE and LOOKBACK_DATE explicitly
- Refusing to emit findings where PUBLISHED_DATE < (TODAY - 30 days)
- Raising a FLAG if evidence is older than lookback window

---

## Part 3: Why Instructions Don't Work (And Why Your Structure Does)

### The Instruction-Reality Gap

The competitive-intel agent's instructions state:

1. "Note the date and source for every finding"
2. "Distinguish confirmed facts from rumors"
3. "If no meaningful updates exist, explicitly state this"
4. "Prioritize primary sources"

These are **aspirational instructions**. They describe what *should* happen. But they don't **constrain the output structure** to make hallucinations impossible.

An LLM operating under aspirational instructions will:
- Optimize for **completion** over accuracy
- Rationalize secondary sources as "close enough"
- Collapse ambiguity into a simpler narrative
- Assume search results = verified facts

**Your need content stored like**:

```python
class Evidence:
    claim: str
    source_1: {
        url: str,
        date: datetime,
        quote: str,
        credibility_score: 0-100,
        verification_status: "CONFIRMED" | "DISPUTED" | "UNVERIFIED"
    }
    source_2: {  # REQUIRED—no claim without dual source
        url: str,
        ...
    }
    confidence_level: float  # Derived from sources
    temporal_check: bool  # Is this within lookback window?

# CANNOT emit a claim without these fields populated
# LLM cannot hallucinate because structure prevents it
```

The structure **makes hallucination impossible**, not just discouraged.

---

## Part 4: Specific Failure Modes of the competitive-intel Agent

### Failure 1: Web Search → Report Direct Mapping

Current agent logic:
```
For each competitor:
  For each category:
    results = web_search(query)
    for result in results:
      extract_finding(result)
      write_to_table(finding)
```

**Problem**: `extract_finding(result)` is an **unsupervised LLM operation**. The agent is reading a snippet and inferring a fact without verification.

**What could go wrong**:
- Snippet is truncated; agent infers wrong context
- Snippet is from a reply/comment, not main article
- Snippet mentions competitor by accident (e.g., "Unlike Competitor X...")
- Search result ranking is biased; agent assumes top = most true

**Your should enforces**:
- Must fetch full URL, not rely on snippet
- Must identify claim-supporting quote within full text
- Must reject if quote is secondary (reply, comment, example)
- Must verify date and source type before accepting

### Failure 2: No Temporal Validation Layer

The agent runs:
```
web_search("[competitor] pricing 2025 2026")
```

This query is **deliberately ambiguous** about the lookback window. A search engine will return:
- Some 2025 articles (outside window)
- Some 2026 articles (in window)
- Some mixed

The agent will then write them all into the report, and the reader (you) has to figure out which are old.

**Your should have something like**:
```python
def fetch_evidence(query, lookback_days=30):
    results = web_search(query)
    now = today()
    filtered = [r for r in results if (now - r.date).days <= lookback_days]
    
    if not filtered:
        return {
            "status": "NO_FINDINGS",
            "reason": "No results within 30-day window"
        }
    
    return filtered
```

**Temporal validation is not optional**. It's enforced before evidence is accepted.

### Failure 3: No Credibility Scoring

The agent's report table has:
```markdown
| Category | Finding | Date | Source |
```

All sources are treated equally:
- Official Google press release
- TechCrunch article
- Someone's Hacker News comment
- LinkedIn post from a random person

All are just "sources." No credibility gradient.

**Your should have something like**:
```python
SOURCE_CREDIBILITY = {
    "official_announcement": 100,  # company.com/news
    "sec_filing": 95,              # sec.gov
    "primary_news": 80,            # TechCrunch, VentureBeat
    "secondary_news": 60,          # aggregators, blogs
    "social": 30,                  # LinkedIn, Twitter
    "unverified": 10,              # rumor, hearsay
}

# Findings must have PRIMARY source at 80+
# Cannot emit finding if max(source_credibility) < 60
```

**Credibility is not decorative**. It determines whether a finding is emitted at all.

### Failure 4: No Dispute Resolution

The agent might find:
- Source A: "Competitor raised $50M in April"
- Source B: "Competitor raised $75M in April"

What does the agent do? **Most likely**: writes both into the report and leaves it ambiguous.

**Your need something like**:
```python
if source_1.amount != source_2.amount:
    return {
        "status": "DISPUTED",
        "source_1": {"amount": 50M, "url": ...},
        "source_2": {"amount": 75M, "url": ...},
        "recommendation": "Do not emit as CONFIRMED. Flag for manual review."
    }
```

**Disputes are surfaced explicitly.** No ambiguous findings in the output.

---

## Part 5: How to Rebuild competitive-intel as Antihallucinatoin System

### Phase 1: Add Evidence Structure

Instead of:
```markdown
| Category | Finding | Date | Source |
```

Use:
```markdown
| Claim | Source 1 (Primary) | Source 2 (Corroborate) | Confidence | Status |
|---|---|---|---|---|
| Competitor X released Feature Y | Link + date + quote | Link + date + quote | 95% | CONFIRMED |
| Competitor Z acquired Company W | Link + date + verification | UNVERIFIED | 30% | UNVERIFIED |
```

**Rule**: No claim without at least one primary source (100 points) + one corroborating source (60+ points).

### Phase 2: Add Temporal Validation

```python
def validate_finding(finding, lookback_days=30):
    now = today()
    primary_date = parse_date(finding.source_1.date)
    
    if (now - primary_date).days > lookback_days:
        raise ValueError(f"Finding is {(now - primary_date).days}d old. Outside {lookback_days}d window.")
    
    return True
```

**Every finding must pass temporal check** before being written to report.

### Phase 3: Add Dispute Flag

```python
def compare_sources(source_1, source_2):
    if source_1.claim == source_2.claim:
        return "CONFIRMED"
    elif contradictory(source_1.claim, source_2.claim):
        return "DISPUTED"
    else:
        return "PARTIALLY_ALIGNED"

# Report includes dispute status
# Disputed findings are not written as fact
```

### Phase 4: Add Confidence Scoring

```python
def score_confidence(primary_source, secondary_source):
    primary_credibility = credibility_map[primary_source.type]  # 100
    secondary_credibility = credibility_map[secondary_source.type]  # 60-95
    
    if primary_source and secondary_source:
        # Both sources agree
        if primary_source.claim == secondary_source.claim:
            return min(primary_credibility, secondary_credibility) 
        else:
            return 0  # Disputed, no confidence
    else:
        # Only one source
        return 0  # Below threshold
    
    return confidence
```

**Findings below 70% confidence are flagged as LOW-CONFIDENCE or UNVERIFIED**, not emitted as fact.

### Phase 5: Add EXIT Signals 

USe signals like:

```
If [competitor feature] + [market shift] + [customer feedback]:
    → Threat Level: HIGH
    → Recommended action: Exit position / Accelerate counter-strategy
```

The competitive-intel agent could do the same:

```
THREAT SIGNAL STRUCTURE:

Threat Candidate = [Competitor feature] AND [Target company exposed weakness] AND [Timing window]

Example:
  Claim: "Competitor X released AI-powered pricing optimization"
  +
  Target company gap: "No AI pricing capability"
  +
  Market timing: "Competitors moving upmarket to enterprise"
  
  → Threat Assessment: HIGH
  → Confidence: 85% (both sources confirm feature, both confirm market trend)
  → Urgency: 90-day response window
  → Recommended action: Accelerate Feature Y roadmap
```

This is **competitive-intel fusion**: evidence-driven threat assessment, not speculative.

---

## Part 6: The Fundamental Difference

### What your target should be:

1. **Evidence is a first-class citizen**, not an afterthought
2. **Structure enforces verification**, not instructions
3. **Confidence is explicit and scored**, not implicit
4. **Disputes are surfaced**, not collapsed
5. **Temporal validation is automatic**, not manual
6. **Ambiguity is forbidden**, not tolerated

### Why competitive-intel Hallucinates

1. Evidence is secondary to report completion
2. Instructions are aspirational, not enforced
3. Confidence is implicit in narrative tone
4. Disputes are rationalized away
5. Temporal windows are suggestions
6. Ambiguity is rationalized as "nuance"

---

## Recommendation: Rebuild competitive-intel as a Dual-Source System

**Do not use this agent as written.** Instead:

1. **Build an Evidence Registry** specific to competitive intelligence:
   ```python
   class CompetitorEvidence:
       competitor: str
       category: str  # Product, Pricing, Funding, Reviews, Exec
       claim: str
       primary_source: {url, date, quote, credibility}
       secondary_source: {url, date, quote, credibility}
       confidence_level: float
       temporal_valid: bool
       dispute_status: "CONFIRMED" | "DISPUTED" | "UNVERIFIED"
       threat_level: "HIGH" | "MEDIUM" | "LOW"
   ```

2. **Implement source verification loop**:
   ```
   query → web_search → fetch primary source → extract quote → 
   fetch secondary source → compare → score confidence → emit
   ```

3. **Add signals** to threat assessment:
   ```
   For each finding:
     If finding.confidence >= 80% AND threat_to_target_company == HIGH:
       → Flag for strategic response (30-day, 90-day, 12-month)
   ```

This turns competitive-intel from a **narrative generator** (hallucinates well) into a **evidence processor** (verifiable).

---

## Conclusion

The competitive-intel agent is **fundamentally untrustworthy** because it:
- Confuses search results with facts
- Lacks structural verification
- Relies on aspirational instructions
- Collapses ambiguity into narrative

Your target system should be **trustworthy** because it:
- Treats evidence as structural requirement
- Enforces dual-source minimum
- Scores confidence explicitly
- Surfaces disputes, not narratives

**Do not use competitive-intel as written for high-stakes decisions.** Rebuild it with your evidence architecture, or stop using it entirely.

The gap between "intelligent-sounding report" and "verified intelligence" is the entire ballgame.
