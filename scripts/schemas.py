from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel

SourceType = Literal["tier1_official", "tier2_news"]

Confidence = Literal["CONFIRMED", "UNVERIFIED", "SEARCH_FAILED", "DISPUTED"]

KNOWN_BAD: set[str] = {
    "crunchbase.com",
    "pitchbook.com",
    "statista.com",
    "electroiq.com",
    "businessofapps.com",
    "getlatka.com",
    "similarweb.com",
    "accio.com",
    "tracxn.com",
    "cedcommerce.com",
    # grows as ext-research-eval catches new failures
}

SOURCE_SCORES: dict[str, int] = {
    "tier1_official": 100,
    "tier2_news": 80,
    # anything else → 0 (blocked)
}


class FactSource(BaseModel):
    url: str
    title: str
    fetched_at: str  # ISO date YYYY-MM-DD
    quote: str
    source_type: SourceType  # required — "tier1_official" or "tier2_news" only
    confidence_reason: Optional[str] = None  # appendix-only; e.g. "single_source", "comparison_period_unclear"
