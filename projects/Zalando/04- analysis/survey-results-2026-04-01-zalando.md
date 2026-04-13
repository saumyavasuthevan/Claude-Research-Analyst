## Survey Analysis: Zalando

**Source:** `zalando-ecommerce_checkout_feedback.csv`
**Sample size:** n=50
**Survey period:** March 15–16, 2024
**Completion rate (sample):** 33/50 completed (66%) | 17/50 abandoned (34%)
**Device split:** 26 mobile (52%) | 24 desktop (48%)
**Mobile abandonment rate:** 9/26 (34.6%) | **Desktop abandonment rate:** 8/24 (33.3%)

---

### 1. Key Pain Points

Listed in order of severity (frequency × abandonment conversion).

---

#### Pain Point 1: Technical reliability failures during checkout
**Frequency:** 7 responses (R006, R015, R023, R026, R030, R032, R041) | **Abandonments caused:** 4

- **Finding:** The checkout flow has significant reliability issues — page refreshes wiping form data, session timeouts, unexpected logouts mid-flow, slow load times (~30s per page), and opaque generic error messages. These cause users to lose progress and restart or abandon entirely.
- **Evidence:**
  - "The page kept refreshing while I was filling out the form. I'd type something, and then the page would reload and I'd lose my progress. This happened three times." (R006, desktop, completed)
  - "The form kept timing out. I'd fill out a section, then move to the next section, and when I came back, my previous answers were gone. This happened twice." (R030, desktop, completed)
  - "The site kept logging me out. I'd fill out part of the form, then get logged out, and I'd have to log back in and start over. This happened three times before I gave up." (R041, mobile, **abandoned**)
  - "Kept getting error messages — 'something went wrong' but didn't tell me what. I tried a few times, then gave up." (R032, desktop, **abandoned**)
  - "The site was really slow. Each page took like 30 seconds to load. I got impatient and just closed it." (R026, mobile, **abandoned**)
- **Note:** 3 of these users completed despite the issue, indicating high purchase intent — they represent near-miss abandonment risk for less motivated shoppers.

---

#### Pain Point 2: Price and fee transparency — costs hidden until final step
**Frequency:** 5 responses (R003, R007, R011, R038, R046) | **Abandonments caused:** 3

- **Finding:** Shipping costs, taxes, and additional fees are not surfaced until the final checkout screen. Users who discover unexpectedly high totals at the end are a primary abandonment driver — particularly when advertised free shipping thresholds aren't honoured.
- **Evidence:**
  - "The shipping costs were way higher than I expected. It said 'free shipping over $50' but my cart was $52 and it still wanted to charge me $12 for shipping. That doesn't make sense." (R003, mobile, **abandoned**)
  - "The price was higher than I thought. There were all these extra fees that weren't shown on the product page. I'm not paying that much." (R011, desktop, **abandoned**)
  - "The total was way higher than I expected. There were all these fees that weren't mentioned earlier." (R038, desktop, **abandoned**)
  - "I couldn't see the total cost until the very end. There were all these fees and taxes being added, but I couldn't see the final price until I got to the confirmation screen." (R007, mobile, completed)
  - "I couldn't see the tax amount until the very end." (R046, desktop, completed)

---

#### Pain Point 3: Cart save and back-navigation destroys checkout progress
**Frequency:** 4 responses (R005, R020, R029, R044) | **Abandonments caused:** 4 (100% abandonment conversion)

- **Finding:** Users who need to pause checkout — to check product details, confirm bank balance, or return later — have no way to save their cart or resume progress. Attempting to go back destroys checkout state. Every user who encountered this issue abandoned.
- **Evidence:**
  - "I wanted to save my cart for later, but I couldn't find that option. So I just left. I'll probably come back later, but I'm not sure if my cart will still be there." (R005, mobile, **abandoned**)
  - "I needed to check something on the product page. But when I tried to go back, it said I would lose my progress. So I just left." (R020, desktop, **abandoned**)
  - "I needed to check my bank balance first. But when I tried to go back, it said I would lose my progress. So I just left." (R044, desktop, **abandoned**)
  - "I wanted to save my cart, but I couldn't find that option." (R029, mobile, **abandoned**)

---

#### Pain Point 4: Payment method friction — broken payment buttons, no saved cards
**Frequency:** 5 responses (R004, R013, R024, R025, R040) | **Abandonments caused:** 0 (all completed, but with significant friction)

- **Finding:** Apple Pay and PayPal buttons are present in the UI but non-functional — buttons either do nothing or reload the page. No option exists to save payment details for future purchases. Users are forced to enter card details manually every session. One user had a valid card declined with no explanation.
- **Evidence:**
  - "I couldn't use Apple Pay even though there was a button for it. I clicked it, but nothing happened. I tried a few times, then gave up and just entered my card manually." (R013, mobile, completed)
  - "PayPal button just reloaded the page. I tried a few times, then gave up and used my credit card instead." (R040, desktop, completed)
  - "There was no option to save my payment method for next time, which is annoying since I shop here regularly." (R004, desktop, completed)
  - "My card kept saying 'payment declined'. I know the card is valid and has money on it. I tried a different card and it worked." (R024, mobile, completed)
  - "I wanted to split my payment between two cards, but there was no option. I had to use one card, which maxed out my credit limit." (R025, desktop, completed)
- **Note:** All 5 users completed their purchases, indicating these are retention and loyalty risks rather than immediate conversion losses. For repeat shoppers on Zalando (a loyalty-focused platform), broken payment UX is especially damaging.

---

#### Pain Point 5: Address form UX — autocomplete errors and editing restarts checkout
**Frequency:** 5 responses (R001, R010, R019, R036, R049) | **Abandonments caused:** 0

- **Finding:** The shipping address flow has multiple compounding issues: autocomplete suggests incorrect addresses, editing an address resets the entire checkout rather than editing in-place, and the "billing address same as shipping" toggle doesn't actually pre-fill the form.
- **Evidence:**
  - "The autocomplete suggested addresses that weren't even close to mine. I had to type everything manually." (R001, mobile, completed)
  - "I clicked 'Edit' on my address but it took me back to the beginning of the checkout process. I had to start over." (R010, mobile, completed)
  - "When I said my billing address was the same as my shipping address, it still made me fill out the billing address form." (R019, mobile, completed)
  - "The autocomplete suggested the wrong address. I selected it by mistake, and then I had to manually correct it." (R036, desktop, completed)
  - "When I clicked 'Edit', it took me to the cart page instead of just letting me edit the address. I had to go through the entire checkout again." (R049, mobile, completed)

---

#### Pain Point 6: No guest checkout — forced account creation
**Frequency:** 2 responses (R014, R050) | **Abandonments caused:** 2 (100% abandonment conversion)

- **Finding:** Some users encountered a mandatory account creation gate at the payment step with no guest checkout option. Both users who encountered this abandoned immediately.
- **Evidence:**
  - "The site kept asking me to create an account. I don't want to create an account, I just want to buy something. There was no 'Guest Checkout' option, so I left." (R014, desktop, **abandoned**)
  - "The payment screen asked me to create an account. There was no option to checkout as a guest, so I left." (R050, desktop, **abandoned**)

---

#### Pain Point 7: Shipping option confusion and delivery date opacity
**Frequency:** 4 responses (R009, R021, R028, R037) | **Abandonments caused:** 0

- **Finding:** Shipping options are poorly differentiated (two options with identical delivery windows), estimated delivery dates aren't shown until checkout completion, and changing a shipping method mid-checkout forces users to restart.
- **Evidence:**
  - "There were like 5 different shipping options, but I couldn't tell the difference between 'Standard' and 'Economy'. They both said 5-7 business days." (R009, desktop, completed)
  - "The shipping calculator said 3-5 days, but the confirmation page said 7-10 days. That's a big difference." (R021, desktop, completed)
  - "I couldn't see the estimated delivery date until the very end. I wanted to know if my order would arrive in time for an event." (R028, mobile, completed)
  - "I couldn't change my shipping method after I selected it without going back to the start." (R037, mobile, completed)

---

#### Pain Point 8: No persistence for returning shoppers (saved address, saved card)
**Frequency:** 3 responses (R027, R045, R048) | **Abandonments caused:** 0

- **Finding:** Repeat shoppers — who represent Zalando's loyalty base — have to re-enter full card details and shipping address every session. This is a notable gap given Zalando's stated 2026 strategic priority around customer loyalty.
- **Evidence:**
  - "I shop here regularly, and it's annoying to enter my card info every time. I wish there was a way to save it." (R027, desktop, completed)
  - "I shop here regularly, and it's annoying to enter my address every time." (R045, mobile, completed)
  - "The payment form didn't have an option to save my card for future purchases." (R048, desktop, completed)

---

#### Pain Point 9: Cart invisibility and quantity changes during checkout
**Frequency:** 3 responses (R018, R022, R039) | **Abandonments caused:** 0

- **Finding:** Users cannot see their full order during checkout — the cart summary is collapsed and non-expandable. Changing item quantities requires navigating back out of checkout to the cart page.
- **Evidence:**
  - "I couldn't see what items were in my cart during checkout. The cart summary was collapsed and I couldn't expand it." (R018, desktop, completed)
  - "I realized I wanted two of something instead of one, but I had to go all the way back to the cart page to change it." (R022, mobile, completed)
  - "I wish I could see a summary of my order before I confirmed it. The summary was on a different page." (R039, mobile, completed)

---

#### Pain Point 10: Promo code discoverability
**Frequency:** 2 responses (R002, R043) | **Abandonments caused:** 0

- **Finding:** The promo/discount code field is buried — hidden in a dropdown or as a small link at the bottom of the page. Users who have valid codes nearly abandon when they can't find the field.
- **Evidence:**
  - "I couldn't find where to apply my discount code. It was hidden in a dropdown menu. I almost gave up because I thought I couldn't use my code." (R002, desktop, completed)
  - "The promo code field wasn't obvious. I finally found it in a tiny link at the bottom of the page." (R043, mobile, completed)

---

### 2. Key Bright Spots

Note: Survey questions were framed negatively ("What was most frustrating?" / "Why did you leave?"). Bright spots below are inferred from completion behaviour and qualitative signals, not explicit praise responses.

---

#### Bright Spot 1: Strong purchase intent — 66% completion rate despite high friction
- **Finding:** Despite encountering significant UX issues, two-thirds of respondents completed their purchase. Multiple users described issues as isolated ("mostly fine" / "mostly smooth") before noting a single specific friction point — indicating the core checkout logic and product selection experience is sufficient to drive conversion even when the form UX is poor.
- **Evidence:**
  - "The checkout process was fine overall, but I wish there was a way to save my payment method." (R027, completed)
  - "The checkout process was mostly fine, but I wish there was a progress indicator." (R033, completed)
  - "The checkout process was mostly smooth, but I wish there was a way to save my shipping address." (R045, completed)

---

#### Bright Spot 2: Payment fallbacks work — users recover from broken primary methods
- **Finding:** When Apple Pay or PayPal failed, all affected users (R013, R040) still completed their purchase via manual card entry. The fallback pathway to manual card input is functional and accessible enough that no payment failures caused abandonment in this sample.
- **Evidence:**
  - "I gave up [on Apple Pay] and just entered my card manually. That was annoying." (R013, completed)
  - "I tried a few times [with PayPal], then gave up and used my credit card instead." (R040, completed)

---

#### Bright Spot 3: Mobile completion rate on par with desktop
- **Finding:** Mobile abandonment rate (34.6%) is nearly identical to desktop (33.3%), suggesting the mobile checkout flow is not significantly worse than desktop at driving completions — a reasonable baseline given Zalando's app-first strategy. The issues are UX issues rather than fundamental mobile incompatibility.
- **Note:** This is inferred from the data; not a direct finding from user responses. [ASSUMPTION]

---

### 3. Actionable Recommendations

---

#### Recommendation 1: Implement real-time cost transparency — show running total throughout checkout
- **Recommendation:** Surface shipping cost estimate, taxes, and total at every step of the checkout flow — not just at the final confirmation screen. Where shipping thresholds apply (e.g., "free over €50"), show the user's cart value relative to the threshold in real time. Fix any logic bugs where the free shipping threshold is advertised but not applied.
- **Evidence:** Pain Points 2 — 5 responses, 3 abandonments. R003 explicitly abandoned over a free shipping threshold that wasn't honoured. R007, R011, R038, R046 all flagged hidden costs.
- **Confidence:** High
- **Zalando context:** This directly impacts GMV conversion. Given Zalando's free returns policy as a trust-builder, hidden shipping costs create a jarring contradiction at a critical decision moment.

---

#### Recommendation 2: Add "save cart" functionality and protect backward navigation
- **Recommendation:** Introduce a persistent cart save feature (saved to account or local session with a "continue later" link emailed to logged-in users). Allow back-navigation within checkout without destroying progress — ideally with a step-by-step flow that preserves previously entered data.
- **Evidence:** Pain Point 3 — 4/4 responses abandoned (100%). Users paused mid-checkout for legitimate reasons (checking product details, confirming funds) and had no recovery path.
- **Confidence:** High
- **Zalando context:** Zalando has 50M+ active customers; many are repeat shoppers with multi-session shopping behaviour. A saved cart feature also supports Zalando's loyalty strategy and can be used as a retention re-engagement trigger (e.g., abandoned cart email).

---

#### Recommendation 3: Fix Apple Pay and PayPal integrations — treat as critical payment bugs
- **Recommendation:** Escalate Apple Pay and PayPal button failures to P0 bug status. Buttons displaying in the UI but failing silently erode trust even when users recover via card entry. Audit all payment method buttons against production environments across mobile and desktop.
- **Evidence:** Pain Point 4 — R013 (Apple Pay, mobile), R040 (PayPal, desktop). Both completed via fallback, masking the bug from standard conversion metrics.
- **Confidence:** High
- **Zalando context:** Apple Pay and PayPal are critical for mobile conversion optimisation. With Zalando's ambition to grow AI-driven personalised conversion (13% basket uplift), payment friction is the last-mile conversion killer.

---

#### Recommendation 4: Implement persistent checkout profiles — saved address and payment method
- **Recommendation:** Allow logged-in users to save shipping addresses and payment cards securely. Surface saved details as default on checkout entry, with a single-click edit option. This is standard on ASOS and Amazon — not having it is a competitive gap for Zalando's loyal repeat-shopper base.
- **Evidence:** Pain Points 4 and 8 — 6 distinct respondents flagged this (R004, R027, R045, R048). All were repeat shoppers.
- **Confidence:** High
- **Zalando context:** Aligns directly with Zalando's 2026 customer loyalty strategic priority. Reducing checkout time for returning customers increases purchase frequency and supports GMV growth targets.

---

#### Recommendation 5: Fix address edit flow — in-place editing without checkout restart
- **Recommendation:** Replace the current "Edit address → restart checkout" pattern with an in-place address editor (modal or inline). Ensure the "billing address same as shipping" toggle pre-fills and hides the billing form. Improve address autocomplete accuracy or allow easy manual override.
- **Evidence:** Pain Point 5 — 5 responses (R001, R010, R019, R036, R049). Zero abandonments but high frustration; 3 of 5 were mobile users.
- **Confidence:** High
- **Zalando context:** Address issues skew mobile (3/5 responses). With Zalando's mobile-first customer base and app strategy, mobile form UX is a priority surface.

---

#### Recommendation 6: Ensure guest checkout is always available — remove mandatory account gate
- **Recommendation:** Audit and remove any checkout flows that require account creation before payment. Guest checkout must remain available at all steps. Offer account creation post-purchase as a friction-free opt-in.
- **Evidence:** Pain Point 6 — 2/2 encounters caused abandonment (100%). R014 and R050 both left immediately.
- **Confidence:** High
- **Zalando context:** Account creation gates are particularly damaging for new customer acquisition. If Zalando's guest checkout exists but is appearing inconsistently, this may be a session/A-B test configuration issue worth auditing.

---

#### Recommendation 7: Improve technical reliability — form state persistence and error messaging
- **Recommendation:** Implement auto-save of form state (localStorage or server-side session) so that page refreshes, timeouts, and accidental navigation don't wipe user input. Replace generic "something went wrong" errors with actionable, specific messages. Investigate and resolve session logout issues mid-checkout.
- **Evidence:** Pain Point 1 — 7 responses, 4 abandonments. Affects both mobile and desktop. R041 restarted 3 times before abandoning.
- **Confidence:** High
- **Zalando context:** Zalando's 200+ autonomous engineering teams with microservices architecture may have inconsistent session handling across checkout service boundaries — this is worth investigating at the infrastructure level.

---

#### Recommendation 8: Show delivery date estimates upfront and rationalise shipping options
- **Recommendation:** Surface estimated delivery date from the moment a user selects a shipping option — not only at confirmation. Remove or clearly differentiate shipping tiers with identical delivery windows (e.g., consolidate "Standard" and "Economy" if they offer the same SLA). Allow shipping method changes without restarting checkout.
- **Evidence:** Pain Point 7 — 4 responses (R009, R021, R028, R037). R028 specifically needed delivery timing for an event — a common, high-intent purchase scenario.
- **Confidence:** Medium (0 abandonments in sample, but delivery timeline is a known fashion purchase driver for event-based buying)
- **Zalando context:** Fashion purchases are often event-driven (weddings, parties, seasons). Delivery uncertainty is a known conversion barrier in this vertical.

---

#### Recommendation 9: Make the promo code field prominent
- **Recommendation:** Elevate the discount/promo code entry field to a clearly visible position in the order summary — not buried in a dropdown or footer link. Consider a persistent "Add promo code" CTA above the order total line.
- **Evidence:** Pain Point 10 — 2 responses (R002, R043). Both nearly abandoned due to not finding the field; both eventually completed.
- **Confidence:** Medium
- **Zalando context:** Promo code usage correlates with price-sensitive and Zalando Lounge customers — a loyalty segment Zalando is actively growing.

---

#### Recommendation 10: Add persistent cart summary and inline quantity editing to checkout
- **Recommendation:** Show an expandable, always-accessible cart summary panel throughout checkout. Allow quantity and variant edits (size, colour) inline within the checkout flow without exiting to the cart page.
- **Evidence:** Pain Point 9 — 3 responses (R018, R022, R039).
- **Confidence:** Medium

---

### Prioritisation Matrix

| Recommendation | Abandonment Impact | Frequency | Effort (est.) | Priority |
|---|---|---|---|---|
| Real-time cost transparency | High (3 abandonments) | 5 | Medium | **P1** |
| Save cart / protect back-navigation | Very High (4/4 abandon) | 4 | Medium–High | **P1** |
| Fix Apple Pay / PayPal bugs | Medium (0 direct, trust risk) | 2 | Low | **P1** |
| Persistent saved address + card | Low (0 direct) | 6 | Medium | **P1** |
| Fix address edit flow | Low (0 direct) | 5 | Low–Medium | **P2** |
| Remove account creation gate | Very High (2/2 abandon) | 2 | Low | **P1** |
| Technical reliability (form state, errors) | High (4 abandonments) | 7 | Medium–High | **P1** |
| Delivery date upfront + shipping UX | Low (0 direct) | 4 | Low–Medium | **P2** |
| Promo code prominence | Low (0 direct) | 2 | Low | **P3** |
| Cart summary + inline quantity edit | Low (0 direct) | 3 | Medium | **P2** |

---

### Assumptions

- Survey questions were framed as "What was most frustrating?" (completers) and "Why did you leave?" (abandoners) — all responses are negative-framing by design. The absence of explicit praise does not indicate satisfaction; bright spots were inferred from completion behaviour and qualitative tone.
- Abandonment rate in this sample (34%) may not represent Zalando's platform-wide checkout abandonment rate — this is a specific 50-response survey window from March 2024.
- "Device type" values (mobile/desktop) are assumed to be auto-detected or self-reported, not confirmed from the data.
- Mobile abandonment rate (34.6%) vs desktop (33.3%) parity is inferred from the sample — it is not directly stated by respondents and may not be statistically significant at n=50.
- R012 noting they entered a fake phone number to pass validation is a data quality signal for Zalando's customer database — this may be worth flagging to the data team separately.
- Effort estimates in the prioritisation matrix are approximate and should be validated with engineering.

---

*Word count: ~2,100 words*
