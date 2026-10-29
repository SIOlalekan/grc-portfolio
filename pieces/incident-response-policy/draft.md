# Incident Response Policy

> **AI-ASSISTED DRAFT – PENDING HUMAN REVIEW**
> This document was drafted with AI assistance using publicly available guidance. It is **not** approved and **must not be adopted** until reviewed, amended and formally approved by authorised people in the organisation. It makes no claim of certification or compliance with any standard, law or scheme. Legal and regulatory points marked **⚑ LEGAL REVIEW** depend on jurisdiction and sector and must be checked by a qualified person. Items marked **[[PLACEHOLDER]]** are unknown and must be completed. All response targets are **suggestions only** and need organisational approval.

---

## 1. Purpose and Scope

**Purpose:** To set out how [[PLACEHOLDER: organisation name]] prepares for, detects, responds to, recovers from and learns from information security incidents, so that harm to people, operations, data and reputation is limited.

**Scope:**
- All staff, contractors, volunteers and third parties with access to organisational systems or data.
- All information assets: devices, networks, cloud services, applications, data (including personal data) and physical records.
- Incidents involving suppliers or processors that affect our assets or data.

**Out of scope / handled elsewhere:** [[PLACEHOLDER: e.g. business continuity plan, health and safety, HR disciplinary, physical security procedures]].

**Framework alignment (informational only):** This policy draws on the Respond and Recover functions of NIST CSF 2.0 (supported by Govern, Identify, Protect and Detect), the lifecycle in NIST SP 800-61, and the UK NCSC's incident management guidance. Alignment is indicative and is not a claim of conformity. [[PLACEHOLDER: confirm current versions of the referenced publications]].

---

## 2. Definitions

| Term | Meaning |
|---|---|
| **Event** | Any observable occurrence in a system or network. |
| **Security incident** | An event that actually or potentially compromises the confidentiality, integrity or availability of information or systems, or breaches security policy. |
| **Personal data breach** | A security incident leading to accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data. ⚑ LEGAL REVIEW: confirm the definition under applicable law. |
| **Incident Lead** | The person coordinating the response to a specific incident. |
| **IRT** | Incident Response Team (Section 4). |
| **Containment** | Actions that stop an incident spreading or worsening. |
| **Eradication** | Removal of the cause and artefacts of an incident. |
| **Chain of custody** | A documented record of who handled evidence, when and why. |
| **Indicator of compromise (IoC)** | Technical evidence suggesting a compromise (e.g. malicious IP, file hash). |

---

## 3. Document Control

| Field | Entry |
|---|---|
| Document title | Incident Response Policy |
| Version | 0.1 (AI-assisted draft) |
| Status | **Draft – not approved** |
| Policy owner | [[PLACEHOLDER: role]] |
| Author / reviewer | [[PLACEHOLDER]] |
| Approved by | [[PLACEHOLDER: name, role]] |
| Approval date | [[PLACEHOLDER]] |
| Effective date | [[PLACEHOLDER]] |
| Next review date | [[PLACEHOLDER]] (suggested: at least annually, see Section 22) |
| Classification | [[PLACEHOLDER: e.g. Internal]] |
| Storage location | [[PLACEHOLDER]] (must be accessible if main systems are unavailable) |
| Related documents | [[PLACEHOLDER: data protection policy, business continuity plan, acceptable use policy, supplier register, asset register]] |

**Version history**

| Version | Date | Author | Summary of change |
|---|---|---|---|
| 0.1 | [[PLACEHOLDER]] | AI-assisted draft | Initial draft for review |

---

## 4. Roles and Responsibilities

Roles may be combined in a small organisation. Named individuals, deputies and out-of-hours contact details are held in the contact list (Section 6).

| Role | Assigned to | Responsibilities |
|---|---|---|
| **Executive Sponsor / Senior Leader** | [[PLACEHOLDER]] | Owns the policy; approves major decisions (e.g. shutting down services, ransom-related decisions, public statements); ensures resources. |
| **Incident Lead** | [[PLACEHOLDER]] (deputy: [[PLACEHOLDER]]) | Declares and coordinates the incident; assigns tasks; maintains the incident log; makes escalation decisions; runs the post-incident review. |
| **Technical / IT Lead** (internal or outsourced) | [[PLACEHOLDER]] | Technical triage, containment, investigation, eradication and recovery; preserves evidence. |
| **Data Protection Lead / DPO** (if appointed) | [[PLACEHOLDER]] | Leads personal data breach assessment; advises on notification; maintains the breach register. |
| **Communications Lead** | [[PLACEHOLDER]] | Prepares and approves internal and external messages. |
| **Legal / Compliance Adviser** | [[PLACEHOLDER: internal or external]] | Advises on legal duties, privilege, contracts and notifications. |
| **HR Lead** | [[PLACEHOLDER]] | Handles insider-related incidents and staff welfare. |
| **Scribe / Log Keeper** | [[PLACEHOLDER]] | Records timeline, decisions and actions. |
| **All staff** | – | Report suspected incidents immediately; follow instructions; do not tamper with affected systems; do not discuss externally. |
| **Suppliers / processors** | – | Notify us of incidents as required by contract [[PLACEHOLDER: confirm contractual terms]]. |

---

## 5. Reporting and Escalation

**5.1 How to report.** Anyone who suspects an incident must report it **immediately**, without waiting to confirm, through:
- Primary: [[PLACEHOLDER: email/ticketing address]]
- Phone / out-of-hours: [[PLACEHOLDER: number]]
- Fallback if systems are down: [[PLACEHOLDER: personal mobile list, messaging channel, in-person]]

**5.2 What to include:** who you are, what you saw, when, affected systems or data, actions already taken. Do not delete, wipe or "fix" anything unless instructed.

**5.3 No-blame reporting.** Prompt, honest reporting is expected and will not itself lead to disciplinary action. [[PLACEHOLDER: HR/leadership to confirm wording; deliberate or reckless misconduct is handled separately]].

**5.4 Escalation path**

| Step | Action |
|---|---|
| 1 | Reporter notifies the contact point (5.1). |
| 2 | Receiver logs the report and informs the Incident Lead. |
| 3 | Incident Lead triages and assigns severity (Sections 7–8). |
| 4 | Medium or above: inform Executive Sponsor. High or Critical: activate full IRT and consider external support. |
| 5 | Where personal data may be involved: engage the Data Protection Lead immediately (Section 14). |
| 6 | Re-assess severity whenever new information emerges; escalate or de-escalate and log the reason. |

If the Incident Lead is unavailable or conflicted, the deputy takes over. If the incident involves leadership, escalate to [[PLACEHOLDER: e.g. board chair / trustee]].

---

## 6. External Support Contacts

Verify and test all details at each policy review. Store a copy offline.

| Organisation / function | Purpose | Contact details | Contract / account ref |
|---|---|---|---|
| IT / managed service provider | Technical support | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| Incident response / forensics provider | Specialist investigation (consider a pre-agreed retainer; the NCSC operates an assured Cyber Incident Response scheme in the UK) | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| Cyber insurer / broker | Policy notification conditions and approved vendors | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| Legal counsel | Legal and regulatory advice | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| Data protection regulator | Personal data breach notification | [[PLACEHOLDER: regulator and portal]] ⚑ | – |
| National cyber authority / CERT | Reporting and advice (e.g. UK NCSC) | [[PLACEHOLDER]] | – |
| Law enforcement / cybercrime reporting | Criminal activity, fraud, extortion | [[PLACEHOLDER: e.g. national fraud/cybercrime reporting service]] | – |
| Sector / other regulators | Sector-specific duties | [[PLACEHOLDER]] ⚑ | – |
| Banks / payment providers | Fraud or payment compromise | [[PLACEHOLDER]] | – |
| Key suppliers / cloud / SaaS vendors | Service-specific support | [[PLACEHOLDER]] | – |
| Public relations support (optional) | External communications | [[PLACEHOLDER]] | – |

---

## 7. Severity Classification

The Incident Lead assigns severity using the highest applicable criterion. **The response targets below are suggestions only and must be reviewed and approved by the organisation before use.**

| Severity | Typical criteria | Suggested acknowledgement target | Suggested leadership notification | Suggested team activation |
|---|---|---|---|---|
| **Critical (P1)** | Widespread loss of critical services; confirmed large-scale or sensitive data compromise; active ransomware or extortion; safety risk; major legal or financial impact | [[PLACEHOLDER: suggest ≤ 1 hour]] | [[PLACEHOLDER: suggest immediately]] | Full IRT + external support |
| **High (P2)** | Significant compromise of important systems or accounts; confirmed personal data breach with likely risk to individuals; malware spreading on a limited scale | [[PLACEHOLDER: suggest ≤ 4 hours]] | [[PLACEHOLDER: suggest same day]] | Core IRT |
| **Medium (P3)** | Contained compromise of a single non-critical system or account; policy breach with limited impact; suspected data exposure under investigation | [[PLACEHOLDER: suggest ≤ 1 working day]] | [[PLACEHOLDER: as needed]] | Incident Lead + Technical Lead |
| **Low (P4)** | Minor events with no confirmed impact (e.g. blocked phishing, single failed attack) | [[PLACEHOLDER: suggest ≤ 3 working days]] | Periodic summary | Technical Lead |

**Factors to consider:** data sensitivity and volume; number of people affected; business impact; spread; attacker presence/persistence; legal and contractual consequences; public or media interest; recoverability.

---

## 8. Triage

1. **Record** the report with a unique incident ID and timestamp.
2. **Validate:** is it a genuine incident, a false positive or a non-security fault?
3. **Scope initially:** affected users, systems, data, locations; is it ongoing?
4. **Classify** the type (e.g. phishing, account compromise, malware/ransomware, data loss or exposure, lost device, insider misuse, denial of service, supplier compromise, physical).
5. **Assign severity** (Section 7) and an Incident Lead.
6. **Flag** possible personal data involvement, legal/regulatory triggers and insurer notification needs.
7. **Open the incident log** and set a communication channel. Use an out-of-band channel if the main one may be compromised.
8. **Decide** on immediate containment and escalation.

---

## 9. Containment

Aim to limit damage while preserving evidence. Decisions should weigh business impact against risk of further harm. Document each action and who authorised it.

**Short-term actions (select as appropriate):**
- Isolate affected devices from the network (disconnect rather than power off, unless advised otherwise).
- Disable or reset compromised accounts; revoke sessions, tokens and API keys.
- Block malicious IPs, domains and email senders; remove malicious emails from mailboxes.
- Suspend affected services or integrations.
- Enforce or strengthen multi-factor authentication.
- Protect backups from being encrypted or deleted (e.g. disconnect offline copies).
- Secure physical access where relevant.

**Long-term containment:** apply temporary fixes, segmentation or additional monitoring while eradication is prepared.

**Approvals:** actions causing significant service disruption require Incident Lead approval and notification of the Executive Sponsor [[PLACEHOLDER: confirm authority thresholds]].

**Ransomware / extortion:** Do not engage with or pay attackers without Executive Sponsor decision, legal advice and law enforcement consultation. Public guidance generally discourages payment because it does not guarantee recovery. ⚑ LEGAL REVIEW: sanctions, anti-money-laundering and reporting obligations may apply.

---

## 10. Investigation

- **Objectives:** establish what happened, how, when, what was affected, whether the threat persists and whether data was accessed or exfiltrated.
- **Sources:** system, authentication, email, firewall, endpoint and cloud audit logs; backups; affected devices; user interviews; supplier information; threat intelligence.
- **Method:** build and maintain a timeline; form and test hypotheses; identify root cause and contributing factors; record IoCs.
- **Scope check:** search for the same IoCs across the whole environment, not just the first affected system.
- **Competence:** if internal skills are insufficient or the incident is High/Critical, engage a specialist provider (Section 6). Contractual terms should address confidentiality and possible legal privilege ⚑ LEGAL REVIEW.
- **Insider or HR-related matters:** involve HR and Legal before investigating individuals; apply proportionate, lawful monitoring only ⚑ LEGAL REVIEW.
- **Record:** all findings, decisions and rationale in the incident log.

---

## 11. Evidence Preservation

- Preserve relevant logs, images, emails and artefacts before making changes where practicable. Prioritise volatile data (memory, active connections) if capture capability exists.
- Take forensic images or snapshots of affected systems where appropriate; work on copies.
- Maintain **chain of custody** for each item: description, source, collector, date/time, storage location, transfers.
- Use secure, access-controlled, write-protected storage; record cryptographic hashes where possible.
- Extend log retention for affected systems immediately [[PLACEHOLDER: check log retention settings]].
- Keep evidence until the incident is closed and any legal, regulatory or insurance process has ended, then dispose per Section 20.
- If criminal proceedings or litigation are possible, consult Legal and law enforcement before handling evidence further ⚑ LEGAL REVIEW.

---

## 12. Eradication

- Remove malware, unauthorised accounts, persistence mechanisms, malicious rules and backdoors.
- Close the exploited weakness (patch, reconfigure, remove exposure).
- Reset credentials, secrets and keys that may have been exposed, including service accounts and shared credentials.
- Rebuild from trusted images where integrity cannot be assured.
- Verify eradication through scanning, log review and monitoring before recovery begins.
- Confirm third-party and supplier-side remediation where they were involved.

---

## 13. Recovery

- Restore systems and data from verified clean backups; check backup integrity and the date of the last known-good state.
- Return services in priority order agreed by the Incident Lead and business owners [[PLACEHOLDER: link to critical services list / recovery priorities]].
- Test functionality and security before reconnecting to production.
- Apply heightened monitoring for a defined period [[PLACEHOLDER: e.g. suggested 30 days, requires approval]].
- Confirm with business owners that services and data are acceptable and record any data loss.
- Formally declare the incident **resolved** and record the date; hand over to post-incident review.
- Follow recovery time and recovery point objectives set in [[PLACEHOLDER: business continuity plan]].

---

## 14. Personal Data Breach Assessment

⚑ **LEGAL REVIEW:** Definitions, thresholds, deadlines and content requirements vary by jurisdiction. [[PLACEHOLDER: applicable data protection laws, e.g. UK GDPR / EU GDPR / other]]. Some laws set short deadlines, for example 72 hours from awareness for regulator notification under UK/EU GDPR, subject to conditions. Confirm which apply.

**Process (led by Data Protection Lead with Legal):**

1. **Identify:** Is personal data involved? Was it lost, altered, destroyed, disclosed or accessed without authority?
2. **Record the time of awareness**, as legal clocks may start then. ⚑
3. **Describe the breach:** data categories (including special category or sensitive data, children's data, financial or credentials), approximate number of individuals and records, whose data (customers, staff, others), and any processors or controllers involved.
4. **Assess risk to individuals:** likelihood and severity of harm (e.g. identity theft, fraud, distress, discrimination, physical safety, loss of confidentiality); consider encryption status, ease of identification, vulnerability of individuals, and whether data was recovered.
5. **Determine outcome** and document reasoning:
   - No risk / unlikely risk → record internally; no external notification (if permitted by law ⚑).
   - Risk → notify regulator.
   - High risk → notify regulator **and** affected individuals (and consider steps to help them protect themselves).
6. **Controller / processor role:** If we act as processor, notify the relevant controller as contracts and law require. If we are controller and a processor is breached, obtain details promptly.
7. **Maintain a breach register** of all personal data breaches, including those not notified, with facts, effects, actions and decision rationale ⚑.
8. **Reassess** as facts develop; phased notifications may be permitted ⚑.

---

## 15. Regulatory and Other Notification

⚑ **LEGAL REVIEW required for the whole section.** The Legal / Compliance Adviser confirms every obligation below before use.

| Possible recipient | Trigger (to be confirmed) | Owner | Deadline (to be confirmed) |
|---|---|---|---|
| Data protection regulator | Personal data breach meeting the legal threshold | Data Protection Lead | [[PLACEHOLDER: per law]] |
| Affected individuals | High risk to individuals (or as law requires) | Data Protection Lead / Comms Lead | [[PLACEHOLDER: per law]] |
| Sector or other regulators | [[PLACEHOLDER: sector rules, e.g. financial, health, charity, critical infrastructure]] | Legal | [[PLACEHOLDER]] |
| National cyber authority / CERT | [[PLACEHOLDER: mandatory or voluntary]] | Incident Lead | [[PLACEHOLDER]] |
| Law enforcement | Crime, fraud, extortion | Incident Lead | Promptly (suggested) |
| Cyber insurer | Policy conditions | Executive Sponsor | [[PLACEHOLDER: per policy]] |
|
| Customers, clients, partners or other contractual parties | Contract terms require notice, or their data or services are affected | Executive Sponsor / Legal | [[PLACEHOLDER: per contract]] |
| Banks / payment providers | Payment fraud or compromised financial accounts | Executive Sponsor / Finance | Immediately (suggested) |
| Other parties (e.g. funders, professional bodies, auditors) | [[PLACEHOLDER: confirm any obligations]] | Legal | [[PLACEHOLDER]] |

**Notification principles:**
- Notify only after the Legal / Compliance Adviser has checked the obligation, unless a statutory deadline is close. In that case, notify on the best available information and update later where the law permits ⚑.
- Notifications should state facts known, facts unknown, likely consequences, actions taken, advice for affected people and a named contact point.
- Record who was notified, when, how and by whom, and keep a copy of what was sent.
- If unsure whether a duty applies, escalate to Legal at once, because the cost of delay may exceed the cost of an unnecessary enquiry.

---

## 16. Communications

**16.1 Principles**
- **One voice:** only the Communications Lead, or a delegate approved by the Executive Sponsor, speaks externally.
- **Accurate and timely:** share confirmed facts only. Do not speculate on cause, blame or numbers.
- **Need to know:** limit sensitive details internally. Mark incident communications [[PLACEHOLDER: e.g. Confidential]].
- **Secure channels:** use out-of-band channels if email or chat may be compromised, and assume attackers may be monitoring.
- **Consistency:** all messages must align with regulatory notifications and legal advice ⚑.

**16.2 Audiences and owners**

| Audience | Content | Owner | Approver |
|---|---|---|---|
| Staff / volunteers | What happened (at an appropriate level), what to do and not do, who to contact | Communications Lead | Executive Sponsor |
| Affected individuals | Plain-language description, likely impact, protective steps, contact point | Data Protection Lead / Comms Lead | Executive Sponsor + Legal |
| Customers / partners | Service impact, actions, next update | Communications Lead | Executive Sponsor |
| Regulators / authorities | Statutory content (Section 15) | Per Section 15 | Executive Sponsor + Legal |
| Insurer / advisers | Facts, timeline, costs incurred | Executive Sponsor | – |
| Media / public | Holding statement, then factual update | Communications Lead | Executive Sponsor + Legal |
| Board / trustees / owners | Severity, impact, decisions needed, status | Incident Lead | – |

**16.3 Other requirements**
- Prepare a **holding statement** and template notices in advance [[PLACEHOLDER: location of templates]].
- Agree update intervals during an active incident [[PLACEHOLDER: e.g. suggested every 4 hours for P1, requires approval]].
- Staff must refer media and external enquiries to the Communications Lead and must not post about the incident on social media.
- Do not communicate with attackers except as directed under Section 9.

---

## 17. Post-Incident Review

- **Trigger:** required for all Critical and High incidents and any personal data breach. Optional for Medium and Low, where a summary record is sufficient [[PLACEHOLDER: confirm criteria]].
- **Timing:** hold the review soon after resolution, while memory is fresh [[PLACEHOLDER: suggested within 10 working days of resolution, requires approval]].
- **Participants:** Incident Lead (facilitator), IRT members, relevant business owners, suppliers where useful.
- **Approach:** blame-free and fact-based, focused on systems, processes and decisions rather than individuals.

**Review questions**

| Area | Questions |
|---|---|
| Detection | How was it detected? Could it have been detected sooner? Were logs and alerts adequate? |
| Response | Were roles clear? Were escalation, severity and decisions timely and appropriate? |
| Containment and recovery | Did actions work? Were backups usable? Were recovery targets met? |
| Root cause | What was the technical and organisational root cause and what contributing factors existed? |
| Communication | Were internal and external messages timely, accurate and consistent? |
| Compliance | Were notification duties identified and met? Was the breach register updated? ⚑ |
| Resources | Were tools, skills, contacts and authority sufficient? |
| Impact | What were the actual costs, downtime, data affected and harm to individuals? |

**Output:** a post-incident report containing a summary, timeline, root cause, impact, what worked, what did not, decisions taken, and recommended actions. Distribute it to the Executive Sponsor and, as appropriate, the board and insurer.

---

## 18. Lessons Learned

- Record lessons in a **lessons-learned log** [[PLACEHOLDER: location]], covering process, people, technology and supplier issues.
- Feed lessons into risk assessments, security awareness training, supplier management, technical controls, this policy and test scenarios.
- Share anonymised, relevant lessons with staff. Consider sharing indicators and useful learning with trusted sector or national bodies, subject to legal and confidentiality review ⚑.
- Update playbooks, contact lists and templates after each significant incident.

---

## 19. Corrective Actions

Every recommendation from the post-incident review must become a tracked action or be explicitly risk-accepted by a person with authority.

| Field | Content |
|---|---|
| Action ID and linked incident ID | [[PLACEHOLDER: numbering scheme]] |
| Description | What will change |
| Type | Corrective (fix the problem) / Preventive (stop recurrence) / Improvement |
| Owner | Named individual |
| Priority and due date | Set by Incident Lead and Executive Sponsor [[PLACEHOLDER: suggested timeframes by priority, requires approval]] |
| Status | Open / In progress / Complete / Risk accepted |
| Verification | How effectiveness was confirmed, and by whom |

- The Incident Lead reports open actions to the Executive Sponsor at [[PLACEHOLDER: frequency, e.g. suggested monthly]].
- Overdue actions are escalated to the Executive Sponsor.
- Risk acceptance must be documented, with the approver's name, rationale and review date.

---

## 20. Record Retention

**Records to keep:** incident reports and logs, timelines, decision records, evidence and chain-of-custody records, breach register entries (including non-notified breaches), notifications sent and received, post-incident reports, corrective action records, test and exercise records, and supplier correspondence.

| Record type | Suggested retention | Notes |
|---|---|---|
| Incident log and report | [[PLACEHOLDER: suggested minimum, e.g. 6 years, requires approval]] | Align with limitation periods and insurer needs ⚑ |
| Personal data breach register | [[PLACEHOLDER]] | ⚑ Check legal requirements |
| Evidence (logs, images) | Until incident closure and the end of any legal, regulatory or insurance process, then [[PLACEHOLDER]] | Dispose securely |
| Notifications and communications | [[PLACEHOLDER]] | – |
| Test / exercise records | [[PLACEHOLDER]] | – |

- Store records securely with restricted access and backups, in a location available if main systems are down.
- Incident records may contain personal or sensitive data. Apply data minimisation, access control and the organisation's data retention policy [[PLACEHOLDER: reference]].
- Apply a legal hold, suspending deletion, where litigation or investigation is possible ⚑.
- Dispose of records securely at the end of retention and record the disposal.

---

## 21. Testing and Exercises

| Activity | Purpose | Suggested frequency (requires approval) |
|---|---|---|
| Contact list verification | Confirm numbers and roles are correct and reachable out of hours | [[PLACEHOLDER: e.g. quarterly]] |
| Tabletop exercise | Walk through a realistic scenario (e.g. ransomware, phishing-led account takeover, lost laptop, supplier breach) with the IRT and leadership | [[PLACEHOLDER: e.g. at least annually]] |
| Technical test | Restore from backup, test isolation capability and log availability | [[PLACEHOLDER: e.g. at least annually]] |
| Communications drill | Test out-of-band channels and approval of holding statements | [[PLACEHOLDER: e.g. annually]] |
| Personal data breach drill | Practise assessment, 72-hour style timelines and register entry ⚑ | [[PLACEHOLDER: e.g. annually]] |
| Staff awareness | Reinforce how to recognise and report incidents | [[PLACEHOLDER: at induction and at least annually]] |

- Record the scenario, participants, findings and actions for each exercise. Findings enter the corrective action process (Section 19).
- Include a scenario where key people or primary systems are unavailable.
- Exercises should be run after significant changes to systems, suppliers or staffing.
- Consider using freely available public exercise resources, such as the UK NCSC "Exercise in a Box" [[PLACEHOLDER: confirm availability and suitability]].

---

## 22. Policy Review and Governance

- **Review cycle:** at least annually [[PLACEHOLDER: confirm]], and after any Critical or High incident, significant organisational or technology change, supplier change, or change in law, regulation or insurance terms ⚑.
- **Review process:** the Policy Owner checks content against current public guidance (NIST CSF 2.0, NIST SP 800-61, UK NCSC) [[PLACEHOLDER: confirm current versions]], exercise findings, lessons learned and legal advice. Changes are approved by [[PLACEHOLDER: approver]] and recorded in the version history.
- **Communication:** all staff are told of material changes and their responsibilities.
- **Exceptions:** only with documented approval from [[PLACEHOLDER: role]], with rationale and an expiry date.
- **Non-compliance:** breaches of this policy are handled under [[PLACEHOLDER: HR / disciplinary procedure]]. Good-faith reporting is protected as stated in Section 5.3.

---

## Approval and Adoption

> This policy is an **AI-assisted draft**. It has no force until reviewed by competent people and formally approved. Reviewers should confirm: (1) all placeholders are completed; (2) all ⚑ legal points are checked for the relevant jurisdiction and sector; (3) all suggested response targets, frequencies and retention periods are consciously accepted or changed; (4) the roles and contacts reflect reality.

| Role | Name | Signature | Date |
|---|---|---|---|
| Policy Owner | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| Legal / Compliance reviewer | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| Data Protection Lead / DPO | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| Executive Sponsor (approver) | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |

---

## Appendix A: Minimum Incident Log Fields

Incident ID · reporter and contact · date/time detected, reported and declared · description · incident type · severity and any changes (with reasons) · systems, data and people affected · personal data involved (Y/N/unknown) and time of awareness · actions taken (time, person, authoriser) · evidence collected and custody · decisions and rationale · notifications made · communications issued · resolution date · review date · linked corrective actions.

## Appendix B: Public Reference Material

Informational only. Use does not imply conformity with any framework. [[PLACEHOLDER: confirm current versions and links before adoption]].
- NIST Cybersecurity Framework (CSF) 2.0: Govern, Identify, Protect, Detect, Respond, Recover functions.
- NIST SP 800-61 (Computer Security Incident Handling Guide): incident response lifecycle and handling practices. Check the current revision.
- UK NCSC: incident management guidance, small organisation guidance, and information on the Cyber Incident Response scheme and Exercise in a Box.
- Data protection regulator guidance on personal data breaches for the relevant jurisdiction ⚑ [[PLACEHOLDER]].

---

*End of document. AI-assisted draft, pending human review and formal approval.*