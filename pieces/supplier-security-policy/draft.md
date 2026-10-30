DRAFT – PENDING HUMAN REVIEW AND ORGANISATIONAL APPROVAL

# Supplier Security Policy

**This is a draft template. It has not been approved, adopted, certified or accredited by any organisation. It does not claim or imply compliance with any law, standard or scheme. Legal, data protection and information security reviewers must check it, and an authorised person must approve it, before use. Complete or replace every item marked [[PLACEHOLDER]].**

## Document control

| Item | Detail |
|---|---|
| Organisation | [[PLACEHOLDER: legal name]] |
| Policy owner | [[PLACEHOLDER: role]] |
| Reviewer(s) | [[PLACEHOLDER: e.g. DPO or data protection lead, IT/security lead, legal adviser]] |
| Approver | [[PLACEHOLDER: role/body]] |
| Version / status | 0.1 – Draft |
| Approval date | [[PLACEHOLDER: not approved]] |
| Next review date | [[PLACEHOLDER: e.g. 12 months after approval]] |

## 1. Purpose and scope

**Purpose:** To set out how [[PLACEHOLDER: Organisation]] ("we") manages information security risk arising from suppliers, so that supplier access to our information, systems and services is justified, controlled and reviewed.

**Scope:** This policy applies to all third parties that supply goods or services and that process, store, transmit or access our information, or that support our systems or critical operations. Examples are cloud and SaaS providers, IT support, payroll, marketing, consultants, contractors and professional advisers. It applies to all staff who select, procure, manage or use suppliers.

**Out of scope:** [[PLACEHOLDER: e.g. suppliers with no access to information or systems, such as office stationery]]

## 2. Reference sources (informational only)

This draft draws on public guidance. Using it does not mean we meet any standard.

- UK NCSC: Supply chain security guidance, Cloud security guidance, Vulnerability management guidance, Incident management guidance, Cyber Essentials requirements and the 10 Steps to Cyber Security.
- ISO/IEC 27001 concepts: supplier relationships, security in supplier agreements, ICT supply chain, monitoring and review of supplier services, cloud services, and ICT readiness for business continuity.
- UK data protection: UK GDPR and Data Protection Act 2018, and ICO guidance on controllers and processors, contracts, security, international transfers and personal data breaches.

[[PLACEHOLDER: add sector-specific or contractual requirements, e.g. customer, regulator or funder obligations]]

## 3. Roles and responsibilities

| Role | Responsibilities |
|---|---|
| Senior management / approver | Approves policy and accepts residual risks above the agreed threshold. |
| Policy owner | Maintains the policy and supplier register, and reports on supplier risk [[PLACEHOLDER: frequency]]. |
| Supplier relationship owner (business) | Names a supplier's business need, completes the assessment, manages the day-to-day relationship, and reports concerns. |
| IT/security lead | Assesses technical controls, advises on access and reviews evidence. |
| Data protection lead / DPO [[PLACEHOLDER: confirm if a DPO is required or appointed]] | Reviews personal data processing, DPIA needs, contracts and transfers. |
| Legal / procurement [[PLACEHOLDER]] | Reviews and executes contracts. |
| All staff | Use only approved suppliers for in-scope activities and report supplier incidents promptly. |

## 4. Supplier register and risk tiering

We maintain a supplier register recording: supplier name and contacts, service, relationship owner, tier, data types and volumes, personal data (Y/N), access method, hosting and processing locations, sub-processors, contract dates, evidence held, last and next review dates, and exit plan status.

| Tier | Criteria (adjust) | Minimum assurance |
|---|---|---|
| **Tier 1 – Critical/High** | Processes special category, criminal offence or large-scale personal data; has privileged or network access; or the service is critical to operations ([[PLACEHOLDER: define threshold, e.g. outage tolerance]]) | Full due diligence, security-reviewed contract, annual review, exit plan |
| **Tier 2 – Medium** | Processes limited personal or confidential data; no privileged access | Standard questionnaire and evidence, contract terms, review every [[PLACEHOLDER: e.g. 24 months]] |
| **Tier 3 – Low** | No access to personal or confidential data or systems | Basic checks, standard terms, review on change |

The tier is assigned before onboarding and revisited when scope changes.

## 5. Supplier due diligence

Before contract signature or data sharing:

1. Document the business need and the data, systems and access involved.
2. Assign a tier (section 4). Where personal data is involved, consult the data protection lead on whether a DPIA is needed.
3. Gather evidence proportionate to the tier. Examples:
   - Company details, ownership, and financial or continuity standing (Tier 1).
   - Security certifications or assessments claimed by the supplier, such as Cyber Essentials or ISO/IEC 27001. We check scope, validity and issuer, and treat them as evidence to be considered, not proof of adequacy.
   - Completed security questionnaire covering the requirements in section 6.
   - Policies or summaries covering access control, encryption, backup, vulnerability management, incident response and staff vetting and training.
   - Penetration test or audit summaries, where available (Tier 1).
   - Sub-processor list and data locations.
   - Insurance, where relevant [[PLACEHOLDER]].
4. Record gaps, risks and agreed remediation. The IT/security lead and, where personal data is involved, the data protection lead give input.
5. Document the risk decision. Tier 1 risks need approval by [[PLACEHOLDER: role]].

No supplier may receive personal or confidential data, or system access, until due diligence is complete and a suitable contract is in place. Exceptions follow section 17.

## 6. Information security requirements

Requirements are scaled to the tier and the service. Suppliers should, as appropriate:

| Area | Expectation |
|---|---|
| Governance | Named security contact; documented security responsibilities and policies. |
| People | Appropriate screening, confidentiality commitments and security awareness training for staff with access. |
| Access | Least privilege, unique accounts, multi-factor authentication for remote and administrative access, prompt removal of leavers. |
| Data protection | Encryption in transit and at rest where appropriate; data segregation; secure disposal. |
| Secure operations | Supported, patched software; malware protection; secure configuration; logging and monitoring. |
| Backup and recovery | Tested backups protected from tampering. |
| Physical/environment | Suitable controls for premises or data centres holding our data. |
| Development | Secure development and change practices where the supplier builds or customises software. |
| Cloud | Assessed against the NCSC cloud security principles, or equivalent, where cloud services are used. |
| Assurance | Willingness to provide evidence and, for Tier 1, to support audit or assessment. |

Minimum baseline for all Tier 1 and Tier 2 suppliers: [[PLACEHOLDER: e.g. Cyber Essentials-equivalent controls, or documented alternative assurance]].

## 7. Contracts

Written contracts or agreements must be in place before service starts. Legal review is required for Tier 1 and for any contract involving personal data. Contracts should cover, as appropriate:

- Scope of services, service levels and responsibilities.
- Security requirements from section 6 and compliance with our reasonable security instructions.
- Confidentiality, and permitted use of our information only for the contracted purpose.
- Data protection terms (section 8).
- Sub-processor and subcontracting controls (section 10).
- Incident notification duties and cooperation (section 11).
- Vulnerability and patching expectations (section 12).
- Business continuity, disaster recovery and resilience commitments (section 13).
- Rights to evidence, assessment or audit, proportionate to tier.
- Notification of material changes, including ownership, hosting location, services and security posture.
- Return or secure deletion of data, exit assistance and data portability (section 16).
- Liability, indemnity and insurance [[PLACEHOLDER: legal advice]].
- Governing law and jurisdiction [[PLACEHOLDER]].

Where a supplier's standard terms cannot be changed, we record the gaps, assess the risk and obtain approval under section 17.

## 8. Data processing and data protection

- **Roles:** Before sharing personal data, determine and record whether the supplier is a processor, a controller or a joint controller.
- **Processor contracts:** Where a supplier acts as our processor, the written contract must include the terms required by UK GDPR Article 28. In summary: processing only on documented instructions; confidentiality; security measures; sub-processor conditions; assistance with data subject rights, security, breach notification and DPIAs; deletion or return of data; and information and audit support. [[PLACEHOLDER: legal reviewer to confirm clause wording against current ICO guidance]]
- **Processing details:** The contract or annex records the subject matter, duration, nature and purpose of processing, data types and data subject categories.
- **Data minimisation:** Share only the data necessary for the service.
- **International transfers:** Personal data must not be transferred or made accessible outside the UK unless a valid UK transfer mechanism is in place and recorded. Examples are UK adequacy regulations, the UK IDTA or the UK Addendum to the EU SCCs, with a transfer risk assessment where needed. [[PLACEHOLDER: approved countries/hosting locations]]
- **Records:** Update our records of processing and privacy information where required. [[PLACEHOLDER: owner]]
- **Data subject requests:** Suppliers must pass on requests they receive within [[PLACEHOLDER: e.g. 2 working days]] and help us respond in time.

## 9. Access control

- Grant supplier access on a need-to-know, least-privilege and time-limited basis, approved by the relationship owner and IT/security lead.
- Use named, individual accounts. Shared or generic accounts need documented approval and compensating controls.
- Require multi-factor authentication for remote, administrative and cloud-console access.
- Provide access through approved, secured methods only, such as a managed VPN, a privileged access tool or a controlled remote session. Avoid permanent privileged access.
- Supplier staff must follow our acceptable use and confidentiality requirements while on our systems or premises.
- Log and, for Tier 1, review privileged supplier activity [[PLACEHOLDER: frequency]].
- Review supplier accounts and permissions at least [[PLACEHOLDER: e.g. quarterly for Tier 1, annually otherwise]]. Remove access immediately when no longer required.
- Store supplier credentials, API keys and certificates securely, rotate them periodically, and revoke them on exit.
- Physical access is escorted or restricted, and logged where appropriate.

## 10. Sub-processors and subcontractors

- Suppliers must not engage sub-processors or subcontractors that handle our data or support our services without our prior written authorisation (specific or general). Under general authorisation, the supplier must give notice of changes of at least [[PLACEHOLDER: e.g. 30 days]] and allow us to object.
- Suppliers must maintain and provide a current list of sub-processors, including locations and services.
- Suppliers must impose written terms on sub-processors that give equivalent data protection and security protection, and remain responsible to us for their performance.
- We review sub-processor changes for risk, location and transfer implications. If an objection is not resolved, we may escalate, apply compensating controls or terminate under the contract.
- For Tier 1, we consider concentration and dependency risks in the wider supply chain, in line with NCSC supply chain guidance.

## 11. Incident notification and management

Suppliers must tell us about actual or suspected security incidents affecting our information, systems or services.

| Requirement | Standard |
|---|---|
| Contact | Supplier notifies [[PLACEHOLDER: email/phone/24-7 contact]]. |
| Timing: personal data breach | Without undue delay and no later than [[PLACEHOLDER: e.g. 24 hours]] after becoming aware, so that we can assess and meet any obligation to notify the ICO within 72 hours of our awareness. |
| Timing: other security incidents | Within [[PLACEHOLDER: e.g. 48 hours]] of becoming aware. |
| Content | Nature and time of the incident, data and systems affected, likely impact, containment and remediation steps, a named contact, and updates as facts emerge. |
| Cooperation | Preserve evidence, help our investigation, and provide root-cause and lessons-learned reports. |
| Communications | Suppliers do not notify regulators, individuals or the media about our data without agreement, unless legally required. |

Our internal steps:
1. Log the incident and follow our incident response procedure [[PLACEHOLDER: reference]].
2. The data protection lead assesses breach reporting and individual notification duties and records the decision.
3. Review supplier risk and contract rights, and decide on remediation or escalation.

We also notify suppliers promptly of incidents on our side that could affect them.

## 12. Vulnerability management

Suppliers must:
- Run a documented vulnerability and patch management process covering systems and software that support our service.
- Apply security updates within timeframes based on severity and exploitation risk. Our expectation: critical and actively exploited vulnerabilities within [[PLACEHOLDER: e.g. 14 days or sooner]], and high-severity within [[PLACEHOLDER: e.g. 30 days]].
- Not use unsupported software or hardware for our services without a documented risk acceptance and compensating controls.
- Notify us of vulnerabilities in their service that materially affect us, and of remediation plans and timescales.
- Conduct periodic independent security testing for Tier 1 services [[PLACEHOLDER: frequency]], and share summary results and remediation status on request.
- Provide a way to report vulnerabilities to them.

We apply patches to our own systems that supplier solutions depend on, and report suspected vulnerabilities in supplier products to the supplier.

## 13. Service continuity and resilience

- For Tier 1 and critical Tier 2 suppliers, identify the business impact of an outage and agree recovery expectations (recovery time and recovery point objectives): [[PLACEHOLDER]].
- Require suppliers to maintain, test and review business continuity and disaster recovery arrangements proportionate to the service. Obtain summary evidence of testing [[PLACEHOLDER: frequency]].
- Check backup arrangements, data location and the ability to restore our data.
- Identify single points of failure and alternative suppliers or manual workarounds for critical services.
- Maintain our own continuity plan for supplier failure, including how we would operate and communicate [[PLACEHOLDER: link to plan]].
- Consider supplier financial viability, ownership changes and end-of-life for critical services. Consider escrow or data export arrangements where appropriate.

## 14. Ongoing monitoring

| Activity | Tier 1 | Tier 2 | Tier 3 |
|---|---|---|---|
| Service level and performance review | [[PLACEHOLDER: e.g. quarterly]] | [[PLACEHOLDER: e.g. annually]] | As needed |
| Security evidence refresh (certificates, test summaries) | Annually | At reassessment | As needed |
| Access review | [[PLACEHOLDER]] | [[PLACEHOLDER]] | On change |
| Sub-processor and hosting changes | On notice | On notice | On notice |
| Incident and complaint tracking | Continuous | Continuous | Continuous |
| Public news and breach monitoring | [[PLACEHOLDER]] | Ad hoc | Ad hoc |

Findings are recorded in the supplier register. Issues are tracked to closure with an owner and due date. Persistent or serious failures are escalated to [[PLACEHOLDER: role]].

## 15. Reassessment

Reassess suppliers:
- At the intervals in the tier table in section 4.
- On a significant change, such as a change in service scope, data types, hosting location, ownership or sub-processors.
- After a significant incident, audit finding or service failure.
- Before renewal or extension of the contract.

Reassessment repeats the relevant due diligence steps, reviews evidence, and confirms the tier, risks and contract terms remain appropriate. Outcomes are: continue, continue with conditions, escalate, or plan exit.

## 16. Termination and offboarding

Plan for exit at onboarding. For Tier 1, document an exit plan before signature.

| Step | Action |
|---|---|
| 1. Notice and planning | Confirm notice terms, transition needs, data inventory and an offboarding owner. |
| 2. Access removal | Disable supplier accounts, remove VPN or remote access, revoke API keys and certificates, rotate shared secrets, and retrieve equipment, badges and assets. |
| 3. Data return/migration | Obtain our data in an agreed, usable format and verify completeness. |
| 4. Deletion | Require secure deletion of our data (including backups within an agreed period [[PLACEHOLDER]]) and written confirmation. Where law requires retention, require continued protection and limits on use. |
| 5. Sub-processors | Confirm deletion or return has also been carried out by sub-processors. |
| 6. Confidentiality | Remind the supplier that confidentiality obligations survive termination. |
| 7. Records | Update the supplier register, records of processing and asset inventory. Archive contract and review records for [[PLACEHOLDER: retention period]]. |
| 8. Lessons learned | Record issues for future procurement. |

For urgent termination (for example after a serious incident), the IT/security lead may suspend access immediately. The decision is then documented and reported to [[PLACEHOLDER: role]].

## 17. Exceptions

Where a requirement cannot be met, the relationship owner records the reason, risk, compensating controls and a time limit. The IT/security lead and, if personal data is involved, the data protection lead review it, and [[PLACEHOLDER: approver role]] approves it. Exceptions are logged and reviewed at least [[PLACEHOLDER: e.g. every 6 months]].

## 18. Compliance, review and enforcement

- Non-compliance with this policy may lead to action under [[PLACEHOLDER: disciplinary or contract procedure]].
- The policy owner reviews this policy at least annually and after major incidents, legal or regulatory change, or business change.
- Any statement by the organisation about compliance with legislation, standards or certifications must be based on separate formal assessment and approval. This policy does not constitute such a statement.

## Appendix A – Quick onboarding checklist

- [ ] Business need and relationship owner recorded
- [ ] Tier assigned; supplier added to register
- [ ] Personal data role identified; DPIA need considered
- [ ] Due diligence evidence reviewed; risks documented and approved
- [ ] Contract reviewed and signed (security, data protection, sub-processors, incidents, exit)
- [ ] Transfer mechanism confirmed if data leaves the UK
- [ ] Access approved on least-privilege basis with MFA
- [ ] Incident contacts exchanged
- [ ] Continuity and exit plan in place (Tier 1)
- [ ] Review dates set

## Appendix B – Items for human reviewers

1. Confirm the organisation's size, sectors, regulators and contractual obligations, and add any additional requirements.
2. Have a qualified legal adviser check contract and data protection wording against current law and ICO guidance, including recent legislative changes.
3. Set realistic timeframes and thresholds in every [[PLACEHOLDER]] to match capacity.
4. Align with existing incident response, business continuity, access control and data protection policies.
5. Confirm the roles, approval route and version control before issue. Do not circulate as an approved policy until formal approval is recorded.