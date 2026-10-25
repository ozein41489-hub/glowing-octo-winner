# Omar Research & Data Agent

## Available now — $30 CSV cleanup & duplicate review

**One small non-sensitive CSV, up to 100 data rows. Written-only service; no call required.**

- Review headings, formatting inconsistencies, and potential duplicate records
- Provide a proposed cleaned copy and a clear list of items needing your decision
- Preserve the original and **never automatically delete uncertain rows**
- Include one minor revision after we agree on the scope; final price and delivery timing are confirmed before acceptance
- Human-reviewed, AI-assisted work when permitted and disclosed as appropriate

**See exactly how the review works before paying:**

- [28-row fictional inventory demo: original, proposed review, and nine flagged rows](demos/csv-cleanup-28/README.md)
- [8-row reproducible sample with Python script and automated tests](demos/csv-cleanup/README.md)
- [Free five-step CSV cleanup checklist — no signup or purchase required](https://ozein41489.systeme.io/eb0524ed)

**[Request the $30 service on Contra](https://contra.com/s/QmMWgq2U-spreadsheet-cleanup-and-duplicate-check-or-dollar30-csv-service)**

For a safe first review, describe the problem without sending private information. Do not publish or send medical, financial, banking, employee, contact, or other sensitive personal records. This is not a claim of paid client work or guaranteed results.

---


A small autonomous service prototype built around the same local research/data engine used for Omar's Bounty worker.

## Goal
Create one reusable worker that can earn across multiple agent-native marketplaces and direct client work without pretending to be a human worker.

## Initial paid services

1. **Public-web research brief** — answer a focused question using public sources and return a concise cited brief.
2. **Fact/source verification** — check claims against public sources and report supported / unsupported / unclear with citations.
3. **Structured web research** — collect public facts into JSON/CSV-ready structure.
4. **Data cleanup & categorization** — normalize, classify, deduplicate, and summarize provided text/CSV/JSON data.
5. **Competitive / market snapshot** — concise public-information comparison with source links.

## Marketplace targets

- Bounty — existing primary worker.
- ClawMolt — free-tier agent deployment target.
- BasedAgents — task-claiming target; payout wallet required before paid claims.
- OKX AI — target as an Agent Service Provider (A2A first; A2MCP later when a public paid endpoint is ready).
- Direct service — this repository is the prototype/specification for a standalone offering.

## Safety and operating rules

The agent must not claim work it cannot complete with its installed tools. It must reject tasks involving credential theft, CAPTCHA/MFA bypass, malware, deception/impersonation, purchases or money transfer, regulated professional advice, unsolicited spam, or private-system access without authorization. It should use public/read-only research unless the user explicitly approves a different supported workflow.

For autonomous submissions, factual work requires evidence and a second QA pass. If evidence is insufficient, hold the job rather than fabricate an answer.

## Build order

1. Reuse the existing local Qwen + public-web research executor.
2. Add a marketplace adapter for ClawMolt.
3. Add a BasedAgents adapter for browse/claim/deliver.
4. Add OKX Onchain OS + Agentic Wallet onboarding, then register an A2A ASP.
5. Expose the research/data engine as a small API for direct clients and OKX A2MCP.
6. Add a simple public landing page and pricing once the first workflows are proven.

## Status

Prototype repository. No financial transactions, wallet transfers, paid subscriptions, or public production endpoint are enabled by this repository alone.
