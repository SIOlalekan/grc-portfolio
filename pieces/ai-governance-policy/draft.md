> **Note: AI-assisted draft pending human review.** This policy was drafted with AI assistance and has not been reviewed by a person. Before adoption, a qualified person should check it against your organisation's context, legal obligations and risk appetite. Legal or data protection advice is recommended. Items shown as **[PLACEHOLDER: …]** must be completed or removed.

---

# AI Governance Policy

| Item | Detail |
|---|---|
| Organisation | [PLACEHOLDER: organisation name] |
| Policy owner | [PLACEHOLDER: role/name] |
| Approved by | [PLACEHOLDER: role/name, date] |
| Version / effective date | [PLACEHOLDER: v0.1 draft / date] |
| Next review | [PLACEHOLDER: date; suggested every 12 months or after a major incident or tool change] |
| Primary framework | NIST AI Risk Management Framework 1.0 (Govern, Map, Measure, Manage) |
| Supporting public references | NIST Generative AI Profile (NIST AI 600-1); [PLACEHOLDER: applicable data protection law, e.g. UK GDPR / EU GDPR / state law] |

## 1. Purpose and scope

This policy sets out how [PLACEHOLDER: organisation] uses AI safely, lawfully and accountably. It applies to all staff, contractors and volunteers, and to any AI system used for organisational work. This includes generative AI chatbots, AI features built into other software, automated decision tools, and AI that we build or configure ourselves. It applies on both organisational and personal devices when they are used for work.

## 2. Principles

1. **Accountability:** a named person owns every AI use case and its outcomes.
2. **Human judgement:** AI supports decisions but does not replace responsibility.
3. **Proportionality:** controls scale with the potential for harm.
4. **Data minimisation:** share only what is necessary.
5. **Transparency:** people are told when AI materially affects them.
6. **Fairness and safety:** we look for and address bias, inaccuracy and misuse.

## 3. Roles and responsibilities (Govern)

| Role | Responsibilities |
|---|---|
| Leadership / Board | Sets risk appetite, approves this policy, receives [PLACEHOLDER: quarterly/annual] AI risk reports |
| AI Governance Lead [PLACEHOLDER: name/role] | Maintains the policy and the AI register, approves tools and use cases, coordinates incidents |
| Data Protection Lead [PLACEHOLDER: name/role, or DPO if required] | Reviews privacy impacts, advises on lawful basis, contracts and data transfers |
| IT / Security Lead [PLACEHOLDER: name/role] | Assesses vendor security, manages access and logging |
| Use Case Owner | Accountable for a specific AI use: risk assessment, review process, monitoring |
| All users | Follow this policy, complete training, report concerns and incidents promptly |

In a very small team one person may hold several roles. Where possible, the person who approves a use case should not be the person who proposes it.

## 4. Approved use

### 4.1 Use categories

| Category | Examples | Requirement |
|---|---|---|
| **Permitted** (low risk) | Drafting or editing non-sensitive text, brainstorming, summarising public material, code assistance on non-confidential code, meeting preparation without personal data | Approved tool only; user checks output before use |
| **Conditional** (medium/high risk) | Customer communications, analysis of internal business data, summarising documents with personal data, HR or recruitment support, financial or legal drafting, public-facing chatbots | Written approval from AI Governance Lead; risk assessment (§6); defined human review (§5); Data Protection Lead sign-off if personal data is involved |
| **Prohibited** | See §4.2 | Not allowed |

### 4.2 Prohibited uses

- Fully automated decisions with legal or similarly significant effects on individuals (e.g. hiring, dismissal, credit, benefits, disciplinary action) without human decision-making.
- Entering **Restricted** data (see §7) into any tool not approved for it.
- Using unapproved tools or personal AI accounts for organisational work.
- Generating deceptive content, impersonation, or synthetic media of real people without their consent.
- Emotion recognition, biometric identification or social scoring of individuals. [PLACEHOLDER: confirm against applicable law and organisational mission]
- Presenting AI output as verified fact, professional advice or original expert work without review.
- Attempting to bypass tool safeguards or security controls.
- [PLACEHOLDER: other organisation-specific prohibitions]

### 4.3 Tool and use case approval

1. The requester submits a short request: purpose, tool, data involved, affected people, owner.
2. The AI Governance Lead screens the request, with Security and Data Protection input for medium or high risk.
3. Vendor checks cover the points below. Record the results in the AI register.
   - data retention and training-use terms
   - security attestations
   - data location
   - sub-processors
   - the ability to opt out of training on our data
   - the availability of a data processing agreement
4. Approved tools and use cases are entered in the **AI Register** [PLACEHOLDER: location], with risk tier, owner, permitted data classes and review date.
5. Re-approve when the tool's terms, features or our use materially change, and at least [PLACEHOLDER: annually].

## 5. Human review

### 5.1 Review by risk tier

| Tier | Typical use | Human review requirement |
|---|---|---|
| **Low** | Internal drafts, ideas, summaries of public information | The user reads and edits before use and takes responsibility for the content |
| **Medium** | External communications, internal analysis, summaries of internal documents | Check facts, sources and tone before release. A second person reviews [PLACEHOLDER: e.g. for external publications] |
| **High** | Decisions or advice affecting people's rights, employment, finances, health, safety or legal position; public-facing automated tools | A trained, authorised reviewer makes the final decision, with documented reasoning. Reviewers must have the competence and time to disagree with the AI. Individuals can request human reconsideration. Sampling and monitoring apply |

### 5.2 Review standards

- **Verify:** check claims, figures, citations, quotations and code. Treat AI output as unverified until checked.
- **Look for bias:** consider whether output treats groups unfairly or reflects stereotypes.
- **Confirm fitness:** check that the output suits the purpose, audience and applicable rules.
- **Avoid automation bias:** reviewers should not simply approve output. Where practical, they should form a view independently.
- **Record:** for high-tier uses, retain a record of the AI involvement, the reviewer, the outcome and any override. Keep records for [PLACEHOLDER: retention period].
- **Disclosure:** tell people when they are interacting with AI, or when AI materially shaped a decision about them, where required by law or where it would reasonably be expected.
- **Accountability:** staff remain responsible for any work they submit, whether or not AI assisted.

## 6. Risk management lifecycle (NIST AI RMF: Map, Measure, Manage)

| Function | Required activity | Applies to |
|---|---|---|
| **Map** | Complete an **AI Use Case Assessment**: purpose, intended users, affected people, data used, assumptions, known limitations, potential harms (privacy, accuracy, bias, security, IP, reputational, legal), and legal or contractual requirements | All Conditional uses |
| **Measure** | Define success and failure indicators before launch (e.g. error rate, complaint count, bias spot-checks, unsafe output rate). Test with realistic examples, including edge cases. Re-test after changes | Medium and high tiers |
| **Manage** | Prioritise risks and select a response (avoid, reduce, transfer, accept) with the owner's sign-off. Set monitoring frequency and escalation triggers. Maintain the ability to pause or disable the system. Plan decommissioning | All tiers, scaled to risk |
| **Govern** | Maintain this policy, the AI register, roles, training, vendor oversight and incident processes (see §§3, 8, 9) | Organisation-wide |

Generative AI use should also account for known risks such as fabricated output, confidential data exposure, intellectual property concerns, harmful content and over-reliance (see NIST AI 600-1).

## 7. Data protection

### 7.1 Data classes and permitted AI use

| Class | Examples | Use with AI tools |
|---|---|---|
| **Public** | Published web content, marketing material | Any approved tool |
| **Internal** | Internal procedures, non-sensitive business documents | Approved tools whose terms prevent training on our data and meet security checks |
| **Confidential** | Client information, contracts, financial data, unreleased plans, credentials | Only tools specifically approved for Confidential data, with a contract in place and owner approval |
| **Restricted** | Special category or sensitive personal data, children's data, health, biometric or criminal records data, payment card data, authentication secrets | **Not permitted** unless explicitly approved by the Data Protection Lead after a documented impact assessment |

[PLACEHOLDER: align class names with your existing data classification scheme, if any.]

### 7.2 Data protection rules

- **Lawful and fair use:** identify a lawful basis and purpose before using personal data with AI. Do not reuse data for incompatible purposes.
- **Minimise and de-identify:** remove or mask names, identifiers and unnecessary detail before using a tool. Remember that pseudonymised data is still personal data.
- **Impact assessment:** complete a data protection impact assessment (or equivalent) where AI use is likely to pose high risk to individuals. [PLACEHOLDER: confirm trigger criteria with legal advisor]
- **Vendor terms:** require a data processing agreement where the vendor handles personal data. Confirm retention, deletion, training use, sub-processors and international transfer safeguards.
- **Account controls:** use organisational accounts with multi-factor authentication. Do not use personal accounts or share credentials.
- **Access:** limit AI tool access and data connections (plug-ins, integrations, document uploads) on a least-privilege basis.
- **Security:** treat prompts, uploads and outputs as organisational records. Protect against prompt injection and data leakage when tools access external content or internal systems.
- **Individual rights:** be able to locate and respond to access, correction, deletion and objection requests involving AI-processed personal data within [PLACEHOLDER: statutory timeframe].
- **Intellectual property and confidentiality:** do not input third-party confidential or copyrighted material unless licensing or contract terms allow it. Check outputs for infringing content before publication.
- **Retention:** delete prompts, outputs and training datasets in line with [PLACEHOLDER: retention schedule]. Disable chat history or use enterprise retention controls where available.
- **Own models and fine-tuning:** document training data sources, permissions and quality checks before building or fine-tuning any model.

## 8. Incidents and issue reporting

Examples of reportable incidents:
- Restricted or Confidential data entered into an unapproved tool.
- Harmful, discriminatory or materially inaccurate output reaching a client or the public.
- Security compromise of an AI tool.
- Material tool malfunction.
- Complaints about AI-influenced decisions.

| Step | Action | Target |
|---|---|---|
| Report | Notify [PLACEHOLDER: contact/channel] | Immediately, and within [PLACEHOLDER: e.g. 24 hours] |
| Contain | Stop use, preserve evidence, revoke access if needed | Immediately |
| Assess | Determine impact on individuals, legal notification duties (including personal data breach rules) and contractual duties | [PLACEHOLDER: timeframe] |
| Notify | Inform regulators, affected people or clients where required | Per applicable law: [PLACEHOLDER: e.g. 72 hours for personal data breaches where applicable] |
| Learn | Record root cause and corrective actions; update the register, controls or training | [PLACEHOLDER: timeframe] |

Staff who report in good faith will not be penalised.

## 9. Training, third parties and monitoring

- **Training:** all users complete induction on this policy, and refreshers every [PLACEHOLDER: 12 months]. Topics include safe prompting, data handling, verification and bias. Reviewers of high-tier uses receive additional training.
- **Third parties:** contracts with AI suppliers and with contractors using AI on our behalf should cover data use, security, audit or information rights, incident notification and subcontracting.
- **Monitoring:** the AI Governance Lead reviews the AI register, incidents, metrics and tool changes [PLACEHOLDER: quarterly] and reports to leadership.
- **Shadow AI:** periodically check for unapproved tool use through [PLACEHOLDER: e.g. browser/SaaS discovery or staff survey]. Treat findings as a prompt for review, not only for discipline.

## 10. Compliance, exceptions and review

- Breaches may lead to access removal and disciplinary action under [PLACEHOLDER: relevant HR policy], and to contractual or legal consequences.
- Exceptions require written approval from the AI Governance Lead (and the Data Protection Lead where personal data is involved). They must be time-limited and recorded.
- This policy is reviewed at least annually and whenever there are significant legal, technological or organisational changes.

## Appendix A: NIST AI RMF alignment summary

| RMF function | Where addressed in this policy |
|---|---|
| **Govern** | §§1–4 (scope, principles, roles, approval); §8 (incidents); §9 (training, third parties, monitoring); §10 (compliance, review) |
| **Map** | §4.3 (request and vendor screening); §6 (use case assessment); §7.1 (data classification) |
| **Measure** | §5.2 (review and recording); §6 (metrics, testing); §9 (monitoring) |
| **Manage** | §5.1 (risk-tiered oversight); §6 (risk response, ability to pause); §7.2 (controls); §8 (incident response) |

## Appendix B: Placeholder checklist before adoption

- [ ] Organisation name, policy owner, approver, version and review dates
- [ ] Named role holders (AI Governance, Data Protection, IT/Security)
- [ ] Applicable laws and regulators, confirmed with a qualified advisor
- [ ] Approved tool list and AI register location
- [ ] Data classification alignment and DPIA trigger criteria
- [ ] Retention periods, incident contacts and timeframes
- [ ] Additional prohibited uses and sector-specific requirements
- [ ] Training schedule and monitoring method
- [ ] Human review of the complete document, then removal of the draft note