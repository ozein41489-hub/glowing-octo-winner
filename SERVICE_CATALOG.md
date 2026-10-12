# Omar Local Research Agent — Service Catalog

## 1. Public-Web Research Brief

**Input:** A focused research question or topic.

**Output:** Concise answer, key findings, source links, and a short limitations note.

**Best for:** Market research, company/product research, policy/background research, fact gathering, and comparison questions.

## 2. Source & Claim Verification

**Input:** A list of claims, statements, or URLs.

**Output:** Supported / unsupported / unclear classification with evidence and source links.

**Best for:** Article review, research QA, fact checking, and evidence audits.

## 3. Structured Information Collection

**Input:** A public-web research target and required fields.

**Output:** Clean structured records suitable for JSON or CSV.

**Best for:** Competitive datasets, company/product lists, public-resource directories, and structured research.

## 4. Competitive / Market Snapshot

**Input:** A company, product, market, or shortlist of competitors.

**Output:** Compact comparison, differentiators, public evidence, and notable gaps/risks.

## 5. Data Cleanup & Categorization

**Input:** User-provided text, JSON, or CSV-like data.

**Output:** Normalized, deduplicated, categorized, and summarized data.

## Quality standard

Every autonomous delivery should pass a second QA check. Research work must preserve source evidence. If information cannot be verified, the agent should say so rather than inventing an answer.

## Safety boundary

The service does not perform credential theft, CAPTCHA/MFA bypass, malware, unauthorized access, impersonation, spam, financial transactions, purchases, regulated professional advice, or tasks that prohibit AI/automation.
