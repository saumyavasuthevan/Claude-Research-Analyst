# Create Company Agent 

## Overview
Claude Code agent for company deep-dives across company overviews, competitors, markets, and product specs. Evaluated agent against Claude outputs to double accuracy in subsequent iterations with prompt engineering.

## 🛠 Challenges and Solutions

### Challenge 1: API Rate Limits
* **Problem:** Parallel searches triggered Brave Search rate limits, causing the AI to skip data and "hallucinate" to fill the gaps.
* **Solution:** Forced a **sequential search pattern with a `sleep 2` delay**. 
* **Result:** 100% data retrieval. The 14-second overhead is a negligible trade-off for complete data.

### Challenge 2: Accuracy 
* **Problem:** An audit revealed a significant split in AI accuracy between quantitative and qualitative data.
    * **Facts (76% accurate):** Dates and funding rounds are usually reliable.
    * **Qualitative (32% accurate):** Strategic claims (e.g., "The only platform that...") are prone to failure.
* **Solution:** Implemented the **"Coverage Gate"**—the agent must produce a status map of all 8 queries *before* writing. If a search fails, it must label the section `[SEARCH FAILED]` instead of guessing.

### Challenge 3: Competitive Bias
* **Problem:** Agents often relied on a company’s own website to describe its rivals, leading to skewed or inaccurate competitive analysis.
* **Solution:** The agent is now **banned from using a company’s own domain** to describe its competitors. It must run independent, third-party searches for every rival listed.

### Challenge 4: Outdated data
* **Problem:** Outdated financial or headcount figures were being presented as current.
* **Solution:** Established the **"Staleness" Rule**. Any figure older than 12 months is automatically tagged as `[UNVERIFIED]` to ensure the user is aware of the data's age.

---

## 📈 Result
Reduced the competitive landscape error rate from **64% to about 0-25%**. 
Every error flagged in V2 was simply data that had gone stale since the research date or represented minor over/underselling. Because every claim is now grounded in a specific source and date, the output is always verifiable. 
