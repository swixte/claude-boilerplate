# Explain: $ARGUMENTS

I'm a product manager, not a developer. Explain this in plain English.

**Target:** $ARGUMENTS (can be a file, folder, function, or feature name)

## How to Explain

### 1. Find the Code
- If it's a file path, read it
- If it's a feature name, search the codebase for relevant files
- If it's a folder, summarize what that area of the code handles

### 2. Explain in Layers

**One-Sentence Summary**
What does this do in the simplest terms? Start with "This [verb]s [what] for [who/why]."

**What Problem It Solves**
Why does this exist? What user need or business requirement does it address?

**How It Works (No Code)**
Walk through the logic like you're explaining to a smart colleague who doesn't code. Use analogies if helpful.

**What It Connects To**
- What other parts of the system does this talk to?
- What would break if this disappeared?
- What features depend on this?

**Key Concepts** (if any jargon is unavoidable)
Define technical terms in plain language. Example:
- "API endpoint" → "A URL that other software can call to get data or trigger actions"
- "Middleware" → "Code that runs automatically between receiving a request and sending a response"

### 3. Answer These Questions
- If I wanted to change how this works, who would I talk to?
- What's the riskiest part of this code? (most likely to cause bugs if changed)
- Is this code simple or complex? Why?
- Are there any known limitations or shortcuts ("tech debt") I should know about?

## Format

Keep it scannable. Use short paragraphs, not dense technical prose.

Avoid:
- Code snippets (unless I specifically ask)
- Technical jargon without definitions
- Implementation details that don't affect product decisions

Include:
- Analogies to real-world concepts
- Impact on user experience
- Connections to features I'd recognize

## Example Output

**Target:** `src/services/payment.js`

### Summary
This handles everything related to charging customers — processing credit cards, handling failures, and recording transactions.

### Why It Exists
Users need to pay for subscriptions. This code talks to Stripe (our payment processor) and makes sure charges go through reliably.

### How It Works
When a user clicks "Subscribe," this code:
1. Validates their card info
2. Sends the charge request to Stripe
3. If it fails, retries up to 3 times with small delays
4. Records the result in our database
5. Triggers a confirmation email

### What It Connects To
- **User accounts** — needs to know who's paying
- **Subscription plans** — needs to know how much to charge
- **Email service** — sends receipts and failure notices
- **Analytics** — tracks conversion rates

### Risk Areas
The retry logic is the most sensitive part. If someone changes the timing, we could accidentally double-charge customers or give up too quickly on cards that would have worked.

### Limitations
Currently only supports credit cards. Adding PayPal or Apple Pay would require significant changes here.

---

Now explain: $ARGUMENTS