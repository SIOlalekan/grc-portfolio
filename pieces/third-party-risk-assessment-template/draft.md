**DRAFT – PENDING HUMAN REVIEW AND ORGANISATIONAL APPROVAL**

# Third-Party Risk Assessment Template
**Organisation:** [[ORGANISATION NAME]]
**Template version:** [[VERSION]] | **Date prepared:** [[DATE]] | **Prepared by:** [[NAME / ROLE]]
**Status:** Draft. Not approved, adopted or certified by any organisation.

> This template supports a structured assessment. It is not legal advice. Have a suitably qualified person review the data protection and contractual sections before use. Complete one form per supplier and record only facts the supplier has provided or evidenced. Where information is missing, enter "Not provided" and raise a treatment action.

---

## 0. Document Control

| Field | Entry |
|---|---|
| Assessment reference | [[REF]] |
| Supplier assessed | [[SUPPLIER NAME]] |
| Assessment type | ☐ New supplier ☐ Periodic review ☐ Contract renewal ☐ Change/incident trigger |
| Assessor(s) | [[NAME / ROLE]] |
| Date started / completed | [[DATE]] / [[DATE]] |
| Related documents | [[DPIA REF]], [[CONTRACT REF]], [[PREVIOUS ASSESSMENT REF]] |

## 1. Method and Scales

**Status key (Sections 5–13):** M = Met | P = Partially met | N = Not met | NE = Not evidenced | NA = Not applicable (give reason)

**Risk score = Likelihood (1–5) × Impact (1–5)**

| Score | Rating | Suggested response (organisation to confirm) |
|---|---|---|
| 1–4 | Low | Accept and monitor |
| 5–9 | Medium | Treat if proportionate; owner sign-off |
| 10–15 | High | Treat before onboarding or within [[TIMEFRAME]] |
| 16–25 | Very high | Do not proceed or continue without senior approval [[ROLE]] |

| Scale | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Likelihood | Rare | Unlikely | Possible | Likely | Almost certain |
| Impact | Negligible | Minor | Moderate | Major | Severe (harm to individuals, legal breach, or prolonged loss of critical service) |

**Frameworks referenced (all public):** UK GDPR and Data Protection Act 2018; ICO controller/processor and security guidance; NCSC Supply Chain Security Guidance; NCSC Cloud Security Principles; Cyber Essentials requirements; NIST Cybersecurity Framework 2.0 (Govern: supply chain risk management).

---

## 2. Supplier Profile

| Field | Entry |
|---|---|
| Legal entity name | [[SUPPLIER LEGAL NAME]] |
| Trading name(s) | [[TRADING NAME]] |
| Company registration no. / country | [[NUMBER]] / [[COUNTRY]] |
| Registered address | [[ADDRESS]] |
| ICO registration (if applicable) | [[ICO REF or "Not provided"]] |
| Supplier contact (commercial / security / data protection) | [[NAMES, EMAILS]] |
| Service description | [[DESCRIPTION]] |
| Contract owner (internal) | [[NAME / ROLE]] |
| Contract start / end / notice period | [[DATES]] |
| Contract value (annual) | [[AMOUNT]] |
| Supplier size / ownership (if relevant) | [[INFORMATION PROVIDED BY SUPPLIER]] |
| Due diligence checks done | ☐ Companies House ☐ Financial standing ☐ Sanctions/adverse media ☐ Other: [[SPECIFY]] |

## 3. Service Criticality

| Question | Response |
|---|---|
| Which business process(es) depend on this supplier? | [[PROCESSES]] |
| Maximum tolerable downtime | [[HOURS/DAYS]] |
| Workaround available if service fails? | ☐ Yes ☐ Partial ☐ No – [[DETAIL]] |
| Single point of failure? | ☐ Yes ☐ No |
| Ease of replacement | ☐ Easy (<1 month) ☐ Moderate (1–6 months) ☐ Difficult (>6 months) |
| Regulatory or customer obligations dependent on service | [[DETAIL or "None identified"]] |

**Criticality tier (assessor judgement):** ☐ Tier 1 Critical ☐ Tier 2 Important ☐ Tier 3 Low
**Rationale:** [[RATIONALE]]

## 4. Information Accessed

| Information type | Accessed / stored / processed? (Y/N) | Classification [[SCHEME]] | Volume / notes |
|---|---|---|---|
| Public information | | | |
| Internal business information | | | |
| Confidential commercial / financial information | | | |
| Intellectual property | | | |
| Authentication data (passwords, keys, tokens) | | | |
| Personal data (see Section 5) | | | |
| Other: [[SPECIFY]] | | | |

**Access method:** ☐ Supplier hosts our data ☐ Supplier remote access to our systems ☐ Supplier on-site ☐ Data transferred periodically ☐ No access
**Highest classification accessed:** [[LEVEL]]

## 5. Personal Data Processing

| Question | Response | Status |
|---|---|---|
| Does the supplier process personal data? | ☐ Yes ☐ No (if No, skip to Section 6) | |
| Supplier role | ☐ Processor ☐ Controller ☐ Joint controller | |
| Categories of individuals | [[e.g. staff, clients, donors]] | |
| Categories of personal data | [[LIST]] | |
| Special category or criminal offence data? | ☐ Yes ☐ No – [[DETAIL]] | |
| Children's data? | ☐ Yes ☐ No | |
| Approximate number of individuals | [[NUMBER]] | |
| Purpose and duration of processing | [[DETAIL]] | |
| Lawful basis (our organisation) | [[BASIS]] | |
| DPIA required / completed? | ☐ Required ☐ Not required – [[REASON]]; ref [[REF]] | |
| Written processor terms meeting UK GDPR Art. 28 | | |
| Processing only on documented instructions | | |
| Staff confidentiality commitments | | |
| Assistance with data subject rights requests | | |
| Breach notification to us without undue delay | | |
| Deletion/return of data at contract end | | |
| Audit and information rights | | |
| Restricted-transfer safeguards in place (if data leaves the UK) | | |
| Retention period agreed | [[PERIOD]] | |

## 6. Security Controls

Obtain evidence (policy, report, screenshot, questionnaire answer). Do not rely on unsupported assertions for Tier 1 suppliers.

| Control area | Question | Status | Evidence ref | Notes |
|---|---|---|---|---|
| Governance | Named security lead and documented information security policy | | | |
| Risk management | Supplier performs regular security risk assessments | | | |
| Secure configuration | Hardened, patched systems; defined patch timescales | | | |
| Vulnerability management | Regular scanning and independent penetration testing | | | |
| Malware/endpoint protection | Managed on all relevant devices | | | |
| Encryption | In transit and at rest; key management described | | | |
| Network security | Segmentation, firewalls, monitoring | | | |
| Logging and monitoring | Security events logged and reviewed; retention [[PERIOD]] | | | |
| Secure development | Secure SDLC, code review, separation of test/live data | | | |
| Data separation | Our data logically separated from other customers' | | | |
| Backup | Regular, protected, restore tested | | | |
| Personnel security | Screening, security and data protection training | | | |
| Physical security | Controls at offices and data centres | | | |
| Asset disposal | Secure deletion/destruction of media | | | |
| Supply chain | Supplier assesses its own suppliers | | | |
| Cyber Essentials-aligned baseline | Firewalls, secure config, updates, access control, malware protection | | | |

## 7. Access Management

| Control | Status | Notes |
|---|---|---|
| Role-based, least-privilege access to our data/systems | | |
| Unique named accounts (no shared credentials) | | |
| Multi-factor authentication for all remote/admin access | | |
| Privileged access restricted, logged and reviewed | | |
| Joiner/mover/leaver process; access removed promptly | | |
| Periodic access reviews (frequency [[FREQUENCY]]) | | |
| Our ability to view/revoke supplier access | | |
| Supplier staff location for remote access | | |
| Our own controls: approved access list owner | [[NAME]] | |

## 8. Hosting Location

| Item | Entry |
|---|---|
| Primary hosting location(s) | [[COUNTRY / REGION]] |
| Backup / DR location(s) | [[COUNTRY / REGION]] |
| Hosting provider / infrastructure | [[PROVIDER or "Not provided"]] |
| Remote support or access from outside the UK? | ☐ Yes – [[COUNTRIES]] ☐ No |
| Data leaves UK? | ☐ Yes ☐ No |
| Transfer mechanism (if yes) | ☐ UK adequacy regulations ☐ UK IDTA / UK Addendum ☐ Other ICO-recognised safeguard: [[SPECIFY]] |
| Transfer risk assessment completed | ☐ Yes, ref [[REF]] ☐ N/A |
| Alignment with NCSC Cloud Security Principle on data location and legal jurisdiction | Status: [[M/P/N/NE]] |

Check current ICO guidance on restricted transfers at the time of assessment.

## 9. Sub-processors and Fourth Parties

| Sub-processor / fourth party | Service provided | Data accessed | Location | Flow-down terms confirmed? | Status |
|---|---|---|---|---|---|
| [[NAME]] | [[SERVICE]] | [[DATA]] | [[LOCATION]] | ☐ Y ☐ N ☐ NE | |
| [[NAME]] | | | | | |

| Control | Status |
|---|---|
| Supplier provides a current list of sub-processors | |
| Prior notice of changes, with right to object | |
| Supplier remains liable for sub-processors | |
| Equivalent data protection and security obligations imposed | |
| Concentration risk reviewed (e.g. shared cloud provider) | |

## 10. Incident Management

| Question | Status | Notes |
|---|---|---|
| Documented incident response plan, tested [[FREQUENCY]] | | |
| 24/7 or defined-hours incident contact | | [[CONTACT]] |
| Notification time commitment to us (target: [[HOURS]]) | | |
| Notification covers security incidents, not only confirmed personal data breaches | | |
| Information provided: nature, data affected, impact, actions, contacts | | |
| Cooperation with our investigation and ICO/individual notification duties | | |
| Root-cause analysis and lessons learned shared | | |
| Previous material incidents disclosed (last [[YEARS]] years) | | |

Internal reminder: UK GDPR requires notification to the ICO within 72 hours of becoming aware of a notifiable breach. Contractual notice periods must allow us to meet this.

## 11. Business Continuity and Resilience

| Question | Status | Notes |
|---|---|---|
| Documented BC/DR plan, tested [[FREQUENCY]]; summary of results available | | |
| Stated RTO / RPO | | [[RTO]] / [[RPO]] |
| Do RTO/RPO meet our tolerances (Section 3)? | | |
| Resilient hosting (multi-site / multi-zone) | | |
| Service availability target and reporting | | [[SLA %]] |
| Dependence on key individuals or single sites | | |
| Financial stability indicators reviewed | | |
| Exit plan: data export format, assistance, transition period | | |
| Our own contingency (workaround, alternative supplier) | | [[DETAIL]] |

## 12. Certifications and Assurance Evidence

Check scope, issuing body, validity dates and whether the certificate covers the service we use.

| Evidence | Held? | Scope covers our service? | Issuer | Valid until | Doc ref |
|---|---|---|---|---|---|
| Cyber Essentials / Cyber Essentials Plus | ☐ | ☐ | | | |
| ISO/IEC 27001 | ☐ | ☐ | | | |
| SOC 2 Type II or equivalent report | ☐ | ☐ | | | |
| Other (e.g. ISO 22301, PCI DSS): [[SPECIFY]] | ☐ | ☐ | | | |
| Independent penetration test summary | ☐ | ☐ | | | |
| Completed security questionnaire | ☐ | – | – | – | |
| Insurance (cyber / professional indemnity) | ☐ | – | | | |
| Policies provided (security, privacy, BC) | ☐ | – | – | – | |

**Assurance gaps and limitations:** [[DETAIL]]

## 13. Contractual Controls

| Clause / control | In contract? | Clause ref | Gap / action |
|---|---|---|---|
| UK GDPR Art. 28 terms / data processing agreement | | | |
| Security requirements and minimum standards | | | |
| Confidentiality | | | |
| Breach/incident notification timescale | | | |
| Sub-processor approval and flow-down | | | |
| Data location and transfer restrictions | | | |
| Audit, assurance and information rights | | | |
| Service levels, credits and reporting | | | |
| Business continuity obligations | | | |
| Liability and indemnity (proportionate to risk) | | | |
| Insurance requirements | | | |
| Intellectual property and data ownership | | | |
| Termination rights (including for security/data breach) | | | |
| Exit assistance, data return and certified deletion | | | |
| Change control for material service/security changes | | | |
| Compliance with applicable law (e.g. NIS Regulations if relevant: [[Y/N]]) | | | |

---

## 14. Inherent Risk (before supplier controls)

Score assuming no effective supplier controls. Use Sections 3–5 and 8 as inputs.

| Ref | Risk scenario | Likelihood (1–5) | Impact (1–5) | Score | Rating |
|---|---|---|---|---|---|
| R1 | Unauthorised disclosure of confidential or personal data | | | | |
| R2 | Service outage beyond tolerable downtime | | | | |
| R3 | Unauthorised access via supplier accounts or connections | | | | |
| R4 | Data loss or corruption | | | | |
| R5 | Non-compliance with UK GDPR or other legal duties (including transfers) | | | | |
| R6 | Sub-processor or fourth-party failure | | | | |
| R7 | Delayed or inadequate incident notification | | | | |
| R8 | Supplier failure or lock-in preventing orderly exit | | | | |
| R9 | [[ADDITIONAL RISK]] | | | | |

**Overall inherent risk rating:** [[Low / Medium / High / Very high]] (highest individual rating unless justified otherwise: [[JUSTIFICATION]])

## 15. Residual Risk (after existing controls)

Score using only controls marked **M** and evidenced in Sections 5–13.

| Ref | Controls relied upon (section refs) | Likelihood | Impact | Residual score | Rating | Within appetite? |
|---|---|---|---|---|---|---|
| R1 | | | | | | ☐ Y ☐ N |
| R2 | | | | | | ☐ Y ☐ N |
| R3 | | | | | | ☐ Y ☐ N |
| R4 | | | | | | ☐ Y ☐ N |
| R5 | | | | | | ☐ Y ☐ N |
| R6 | | | | | | ☐ Y ☐ N |
| R7 | | | | | | ☐ Y ☐ N |
| R8 | | | | | | ☐ Y ☐ N |
| R9 | | | | | | ☐ Y ☐ N |

**Overall residual risk rating:** [[RATING]]
**Risk appetite reference:** [[POLICY / STATEMENT]]
**Recommendation:** ☐ Proceed ☐ Proceed with conditions ☐ Defer pending actions ☐ Do not proceed

## 16. Risk Treatment Actions

Treatment options: Reduce | Transfer (e.g. insurance, contract) | Avoid | Accept (requires named acceptor)

| ID | Linked risk / gap | Action | Option | Action owner | Due date | Status | Residual risk after action |
|---|---|---|---|---|---|---|---|
| T1 | | | | [[NAME]] | [[DATE]] | ☐ Open ☐ In progress ☐ Closed | |
| T2 | | | | | | | |
| T3 | | | | | | | |

**Risks accepted:** [[RISK REFS]] | **Accepted by:** [[NAME / ROLE]] | **Rationale and review date:** [[DETAIL]]

## 17. Ownership

| Role | Name | Responsibility |
|---|---|---|
| Supplier relationship owner | [[NAME]] | Day-to-day management, monitoring, escalation |
| Risk owner | [[NAME]] | Accepts residual risk, tracks actions |
| Data protection lead / DPO (if appointed) | [[NAME]] | Reviews Section 5, 8, 9 and DPIA |
| Information security lead | [[NAME]] | Reviews Sections 6, 7, 10, 12 |
| Procurement / legal reviewer | [[NAME]] | Reviews Section 13 |

## 18. Approval

This assessment is not approved until all fields below are completed by authorised individuals.

| Role | Name | Decision | Signature | Date |
|---|---|---|---|---|
| Assessor | [[NAME]] | Submitted | [[SIGNATURE]] | [[DATE]] |
| Risk owner | [[NAME]] | ☐ Approve ☐ Approve with conditions ☐ Reject | [[SIGNATURE]] | [[DATE]] |
| Senior approver (required for High/Very high) | [[NAME / ROLE]] | ☐ Approve ☐ Approve with conditions ☐ Reject | [[SIGNATURE]] | [[DATE]] |

**Conditions of approval:** [[CONDITIONS or "None"]]
**Current status:** Draft, not approved.

## 19. Review Frequency

| Tier | Suggested minimum review (organisation to set) | Selected |
|---|---|---|
| Tier 1 Critical | Every [[12]] months | |
| Tier 2 Important | Every [[12–24]] months | |
| Tier 3 Low | Every [[24–36]] months | |

**Next scheduled review:** [[DATE]]

**Trigger events requiring early review:**
- Security incident or data breach involving the supplier
- Change of ownership, hosting location, sub-processor or service scope
- Loss or expiry of certification or assurance evidence
- Material SLA failure or financial concern
- Change in the data or systems the supplier can access
-
- Expiry or renewal of the contract, or a decision to terminate or exit

**Review actions at each review:**
- Confirm the supplier profile, contacts and sub-processor list are current.
- Re-check certification validity and scope.
- Re-score inherent and residual risk (Sections 14-15).
- Close, escalate or re-date open treatment actions (Section 16).
- Confirm that contract terms still match the service, data and hosting arrangements.

---

## 20. Review Log

| Review date | Reviewer | Trigger (scheduled / event) | Changes identified | Residual risk (before → after) | Next review date |
|---|---|---|---|---|---|
| [[DATE]] | [[NAME / ROLE]] | [[TRIGGER]] | [[SUMMARY]] | [[RATING → RATING]] | [[DATE]] |
| | | | | | |

## 21. Completion Checklist

Complete before submitting for approval.

| Check | Done |
|---|---|
| All [[PLACEHOLDER]] fields completed, or marked "Not provided" with an action raised | ☐ |
| Every status in Sections 5-13 uses M / P / N / NE / NA, and NA entries give a reason | ☐ |
| Evidence references recorded for all Tier 1 controls | ☐ |
| Certificate scope and validity dates checked (Section 12) | ☐ |
| DPIA need considered and recorded (Section 5) | ☐ |
| Restricted transfers and hosting locations confirmed (Section 8) | ☐ |
| Sub-processor list obtained and reviewed (Section 9) | ☐ |
| Contract gaps referred to procurement or legal (Section 13) | ☐ |
| Inherent and residual scores justified (Sections 14-15) | ☐ |
| Each High or Very high risk has a treatment action, owner and due date (Section 16) | ☐ |
| Owners named (Section 17) | ☐ |
| Review frequency and next review date set (Section 19) | ☐ |

## 22. Limitations and Use Notes

- This template is a prompt for assessment. It does not guarantee compliance with any law, standard or framework.
- Frameworks are referenced for guidance only. Check each against its current published version before use.
- Supplier information must come from the supplier or from verifiable sources. Do not assume or infer it.
- Scoring scales, thresholds, timeframes and review periods are suggestions. The organisation must set and confirm its own.
- Obtain qualified legal and data protection advice for contract terms, international transfers and breach notification obligations.
- Store completed assessments securely. They may contain sensitive security and commercial information.

## 23. Template Version History

| Version | Date | Author | Summary of change | Reviewed by |
|---|---|---|---|---|
| [[VERSION]] | [[DATE]] | [[NAME]] | Initial draft | [[PENDING]] |

**End of template.**
**Status:** Draft, pending human review and organisational approval. This document has not been approved, adopted, certified or accredited by any organisation.