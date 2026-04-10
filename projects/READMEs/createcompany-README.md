# Create Company Agent 

## Overview
Claude Code agent for company deep-dives across company overviews, competitors, markets, and product specs. Evaluated agent against Claude outputs to double accuracy in subsequent iterations with prompt engineering.

## 🛠 Challenges and Solutions 

### Challenge 1: API Rate Limits
* **Problem:** Parallel searches triggered Brave Search rate limits, causing the AI to skip data and "hallucinate" to fill the gaps.
* **Solution:** Forced a **sequential search pattern with a `sleep 2` delay**. 
* **Result:** 100% data retrieval. The 14-second overhead is a negligible trade-off for complete data.

### Challenge 2: The Accuracy Gap
I audited the output and found a major split in AI accuracy:
* **Facts (76% accurate):** Dates and funding rounds are usually accurate.
* **Qualitative (32% accurate):** Strategic claims (e.g., "The only platform that...") are where the AI often fails.

## 📈 Improving V2 Results
I moved the accuracy from a failing grade to **75%+** by changing the engineering logic:

* **The "Coverage Gate":** The agent must produce a status map of all 8 queries *before* writing. If a search fails, it must label the section `[SEARCH FAILED]` instead of guessing.
* **Direct Competitor Audits:** The agent is banned from using a company’s own website to describe its rivals. It must run independent searches for every competitor.
* **The "Staleness" Rule:** Any figure older than 12 months is automatically tagged as `[UNVERIFIED]`.

**Result:**
Reduced the competitive landscape error rate from **64% to about 0-25%**. 
Every error flagged in V2 was simply data that had gone stale since the research date or represented minor over/underselling. Because every claim is now grounded in a specific source and date, the output is always verifiable. 
