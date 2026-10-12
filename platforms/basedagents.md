# BasedAgents adapter

## Current status

- Agent identity registered as **Omar Local Research Agent**.
- Public profile: https://basedagents.ai/agent/Omar%20Local%20Research%20Agent
- Registration keypair is stored locally on TheFamilycomp under the user's `.basedagents/keys/` directory. It must never be committed to this repository.
- Open tasks can be browsed now.
- A payout wallet on Base is required before claiming paid bounty tasks.

## Intended automation

1. Poll open tasks.
2. Filter out tasks outside the installed executor capabilities or safety rules.
3. Prefer funded escrow tasks with clear acceptance criteria and sufficient payout.
4. Claim only after a payout wallet is configured.
5. Execute with the shared research/data worker.
6. QA the output and submit a signed deliverable.
7. Track acceptance and settlement.

## Safety

Never claim tasks that require credential theft, unauthorized access, malware, CAPTCHA/MFA bypass, deception, spam, purchases, transfers, or unsupported specialist tools. Do not post paid tasks or authorize payments automatically.
