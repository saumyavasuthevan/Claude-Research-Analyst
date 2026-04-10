# Product Discovery PRD: HPB Plain Language & Support Content

## 1. Background

Singapore's Health Promotion Board's (HPB) Customer Experience (CX) ambition is to be a trusted partner for HPB users, delivering intuitive and personalized health experiences. However, the current state of support content—often laden with jargon and complex phrasing—acts as a barrier to this mission. This discovery study aims to define the problem space for both the HPB users consuming information and the internal teams creating it.

---

## 2. External User: The HPB User

**Target User:** Individuals seeking health information, program details, or support from the Health Promotion Board.

### Problem Statements (External)

- **Having to re-read content multiple times:** HPB users often struggle to understand information the first time they read it, leading to cognitive overload.
- **Difficulty finding what to do next:** HPB users find it difficult to navigate through dense, complex language to find actionable next steps.
- **Content that feels cold or inaccessible:** Overly clinical language can make HPB feel distant or difficult to approach for HPB users.
- **Forced Escalation:** Unclear digital content forces HPB users to call the Contact Centre, delaying resolution.

### Success Measurements (External KPIs)

| Metric Type | KPI | Definition | Source | Target |
|---|---|---|---|---|
| Leading | Search Click-Through Rate (CTR) | % of users who click a result from the search page. Indicates snippet relevance. | GA4 | > 15% |
| Leading | Content Usefulness Rating | Binary (Yes/No) "Was this helpful?" rating at bottom of KAs and FAQs. | HotJar Survey | > 85% Positive |
| Leading | Comprehension Rate | % of users who correctly identify the "call to action" after one reading. | Usability Testing | > 90% |
| Lagging | Self-Service Resolution (SSR) | Review Case Categories for top enquiry drivers. Queries resolved without human contact. | ServiceNow Report | +20% Improvement |
| Lagging | Average Time to Task Completion | Time taken for a user to find and process information needed to act. | Usability Testing | -30% Reduction |

---

## 3. Internal User: The Content Creator

**Target User:** Internal stakeholders involved in the support content lifecycle:

- **HPB Content Creators:** Responsible for drafting and editing user-facing content.
- **Subject Matter Experts (SMEs):** Responsible for providing technical source material, clinical/legal guidance, and final accuracy approvals.
- **Contact Centre Operations:** Responsible for responding to enquiries and surfacing topics with low self-service coverage for content development.

### Problem Statements (Internal)

- **Reliance on individual writing styles:** Quality varies based on who is writing rather than following a unified institutional standard.
- **Jargon:** Approvals prioritize technical accuracy over readability, leading to "safe" but complex language.
- **Inefficient Workflows:** Significant time is wasted in back-and-forth rewriting due to a lack of a shared lexicon.
- **Writing from scratch for every task:** Recurring content types (e.g., "Need Help" sections) are rewritten every time, causing inconsistency.

### Relationship to External Problems

The fact that quality depends on **individual writing styles** makes it **difficult for users to find what to do next**. Without a **content style guide**, technical jargon forces **HPB users to re-read content multiple times** and **content feels cold or inaccessible**.

### Success Measurements (Internal KPIs)

| Metric Type | KPI | Definition | Source | Target |
|---|---|---|---|---|
| Leading | Guideline Adherence | % of content passing automated audits for readability, tone, and lexicon usage. | LLM Evaluating Agent | 95% Compliance |
| Leading | Internal Satisfaction Score | Creator satisfaction and confidence in using the Guide/Lexicon as a reference point for style. | Internal Survey | 4.5 / 5.0 |
| Leading | Escalation to Management | % of content pieces requiring management intervention for final style/tone approval. | Manual Tracking: RACI Audit | < 5% |
| Lagging | Drafting Velocity | Average time spent from first draft to final approved version of a document. | CMS History (Draft to Published) | -40% Time Saved |
| Lagging | Template Coverage | % of content utilizing standardized templates and recurring text elements (e.g., "Need Help" sections). | CMS Analytics | > 70% Usage |

---

## 4. Discovery Objectives

- **ServiceNow Deep Dive:** Analyze top enquiry drivers in ServiceNow to identify "high-friction" content that requires immediate plain-language intervention to provide clearer actionable next steps.
- **Validation:** Verify that "Plain Language" versions of Phase 1 content reduce cognitive load in user testing for HPB users.
- **Baseline Setting:** Establish current "Time to Understand" (Usability Testing) and "Google Analytics 4" (GA4) Click-Through Rate metrics for legacy high-volume Frequently Asked Questions (FAQs).
- **Process Mapping:** Document the current "Content Workflow" to identify where plain language gets "lost" in the approval chain within the Content Management System (CMS).

---

## 5. Risk Mitigation

- **Accuracy vs. Simplicity:** Ensure the Content Guidelines is vetted by Subject Matter Experts (SMEs) to maintain clinical and legal integrity.
- **Internal resistance and adoption barriers:** Initial resistance may stem from a perceived loss of creative autonomy, the fear that simplifying language "dilutes" clinical accuracy, and the added cognitive load of learning new standards.
  - **Change Management Strategy:** Mitigation is achieved by framing the Guide as a productivity tool rather than a restrictive set of rules. We will emphasize that standardizing the "how" allows creators to focus on the "what," ultimately reducing frustrating revision cycles and the time spent negotiating style with SMEs.
  - **Engagement:** Conduct workshops with key "Super-Users" early in Phase 1 to gather feedback on the Content Guidelines, ensuring they feel like co-authors of the new standard rather than recipients of it.
