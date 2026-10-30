# DRAFT – PENDING HUMAN REVIEW AND ORGANISATIONAL APPROVAL

# Business Continuity and Disaster Recovery Policy

**Organisation:** [[PLACEHOLDER: organisation name]]

> **Status notice:** This is an unapproved template. It has not been reviewed, approved, adopted, certified or accredited by any organisation or body. It must not be used operationally until it has been tailored, reviewed by competent people and formally approved by [[PLACEHOLDER: approving authority, e.g. board/director/trustees]]. Every item marked **[[PLACEHOLDER]]** must be completed by the organisation. No recovery targets or organisation-specific facts have been assumed.

## 0. Document control

| Item | Detail |
|---|---|
| Version | [[PLACEHOLDER]] (draft v0.1) |
| Policy owner | [[PLACEHOLDER: role]] |
| Author / reviewer(s) | [[PLACEHOLDER]] |
| Approval status | **Not approved** |
| Approval authority, date and record | [[PLACEHOLDER: to be completed only after formal approval]] |
| Next review date | [[PLACEHOLDER]] |
| Related documents | Incident response plan, information security policy, data protection policy, supplier register, asset register, contact lists [[PLACEHOLDER: document references]] |

### Required before operational use

- [ ] Content checked by someone with business continuity, IT and data protection knowledge (internal or external).
- [ ] All placeholders completed and evidence-based (see Section 4).
- [ ] Legal, regulatory, contractual and insurance obligations checked [[PLACEHOLDER: e.g. sector regulator, funders, cyber insurer]].
- [ ] External references checked for currency (Section 2).
- [ ] Formal approval recorded by the approving authority.
- [ ] Staff and responders briefed on their roles.

## 1. Purpose, scope and principles

**Purpose:** To set out how [[PLACEHOLDER: organisation]] will prepare for, respond to and recover from disruption, so that critical services continue or are restored within tolerable limits and people, data and reputation are protected.

**Scope:** All staff, contractors, volunteers [[PLACEHOLDER: confirm]], sites [[PLACEHOLDER]], systems, data and suppliers supporting critical services. **Exclusions:** [[PLACEHOLDER]].

**Disruption scenarios covered:**

| Scenario | Examples |
|---|---|
| Loss of premises | Fire, flood, utilities failure, restricted access |
| Loss of people | Illness, industrial action, severe weather, transport disruption |
| Loss of technology | Hardware failure, cloud/SaaS outage, network failure |
| Cyber incident | Ransomware, account compromise, data breach, denial of service |
| Supplier failure | Insolvency, outage, supplier cyber incident |

**Principles**
- Protect life and safety first.
- Restore the most critical services first, based on assessed impact, not convenience.
- Keep plans simple, accessible when systems are down, and tested.
- Decide and record who has authority to act.
- Learn from incidents and exercises, and improve.

## 2. Public guidance used

This policy draws on the following public sources. They are used for ideas and structure only. This draft does not claim conformity with any of them.

| Source | Use in this policy |
|---|---|
| NCSC – Small Business Guide: Response and Recovery; Small Business Guide: Backing up your data | Planning, backups, recovery |
| NCSC – Incident management guidance; 10 Steps to Cyber Security | Cyber incident handling and governance |
| NCSC – Exercise in a Box | Exercises |
| NCSC – Ransomware guidance; Supply chain security guidance | Cyber scenarios, supplier risk |
| NCSC – Cyber Essentials | Baseline controls that reduce likelihood and impact |
| Business Continuity Institute – Good Practice Guidelines; ISO 22301 and ISO/IEC 27031 (concepts only) | BIA, strategies, exercising, improvement |
| UK Government / Cabinet Office business continuity and emergency preparedness guidance; Local Resilience Forum information | Local risks and preparedness |
| ICO guidance on UK GDPR security (Article 32) and personal data breaches | Availability, resilience, breach reporting |

*Reviewer action: confirm current titles, versions and links before approval.* [[PLACEHOLDER: add sector-specific guidance]]

## 3. Critical services

List each service the organisation delivers or relies on. Add rows as needed.

| ID | Critical service / activity | Service owner | Key dependencies (people, systems, data, sites, suppliers) | Legal / contractual driver |
|---|---|---|---|---|
| S1 | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| S2 | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| S3 | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |

Supporting functions to consider: payroll, finance, customer/client contact, safeguarding or safety functions, IT and identity services, email and telephony, website, HR, regulatory reporting.

## 4. Business impact analysis (BIA)

The service owner and [[PLACEHOLDER: BC lead]] will complete a BIA for each critical service. They will do so at least [[PLACEHOLDER: frequency]] and after significant change. Evidence for targets should come from managers, finance, customers, contracts and regulators, not guesswork.

**Impact categories:** safety/wellbeing; legal/regulatory; financial; contractual; customer/service user; reputational; data/privacy; operational.

**Impact rating scale** (organisation to define the thresholds):

| Rating | Definition |
|---|---|
| Low | [[PLACEHOLDER]] |
| Medium | [[PLACEHOLDER]] |
| High | [[PLACEHOLDER]] |
| Severe | [[PLACEHOLDER]] |

**BIA record (per service):**

| Service ID | Impact over time (e.g. hours/days/weeks, as defined) | Peak periods / deadlines | Minimum acceptable service level | Dependencies and workarounds | Maximum tolerable period of disruption (MTPD) |
|---|---|---|---|---|---|
| S1 | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |

## 5. Recovery priorities

Services are assigned to tiers using BIA results.

| Tier | Description | Services | Order of recovery |
|---|---|---|---|
| 1 | Immediate – safety, legal or severe impact if unavailable | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| 2 | Urgent | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| 3 | Important | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| 4 | Deferrable | [[PLACEHOLDER]] | [[PLACEHOLDER]] |

**Recovery sequence (to be tailored):** (1) people safety and incident control → (2) identity, network and core infrastructure → (3) Tier 1 systems and data → (4) Tier 2 and below → (5) validation and return to business as usual. Dependencies should be restored before the services that rely on them.

## 6. Recovery objectives

Targets must be set by [[PLACEHOLDER: approving authority]] based on the BIA, cost and feasibility. Targets are never to be inferred from this template.

| Service / system | Tier | RTO (time to restore) | RPO (acceptable data loss) | MBCO (minimum service level) | Currently achievable? (tested evidence) |
|---|---|---|---|---|---|
| [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER: Y/N, date, evidence]] |

*RTO = recovery time objective. RPO = recovery point objective. MBCO = minimum business continuity objective.*

Where tested capability is worse than the target, the gap must be recorded in the risk register and given to the approving authority with remediation options [[PLACEHOLDER: owner and timescale]].

## 7. Backups and data recovery

**Requirements** (aligned with NCSC backup guidance; the organisation must confirm and adapt them):
- Identify the data, systems, configurations and SaaS data needed to restore each critical service, including data held by suppliers.
- Keep multiple copies, with at least one stored separately and protected from ransomware (offline, immutable or otherwise isolated). Apply the "3-2-1" principle or an equivalent justified approach: [[PLACEHOLDER: chosen approach]].
- Backup frequency must support the RPO: [[PLACEHOLDER]].
- Encrypt backups and restrict access using least privilege and multi-factor authentication for backup administration.
- Keep backup administrator credentials separate from normal domain or user credentials.
- Do not assume SaaS or cloud providers back up data to the organisation's needs. Check contract terms and shared responsibility.
- Monitor backup jobs and act on failures within [[PLACEHOLDER]].
- Test restoration of files and full systems at least [[PLACEHOLDER: frequency]], and record results against RTO/RPO.
- Retain backups per [[PLACEHOLDER: retention schedule]], consistent with UK GDPR storage limitation and legal retention needs.
- Keep offline copies of key recovery documents (this policy, contact lists, system build and recovery steps, licence keys, supplier contacts).

| Data / system | Owner | Backup method and location | Frequency | Immutable/offline copy? | Retention | Last restore test |
|---|---|---|---|---|---|---|
| [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |

## 8. Roles and responsibilities

Named deputies must be assigned to every role. Contact details are held in the contact list (Appendix A).

| Role | Responsibilities | Named person | Deputy |
|---|---|---|---|
| Approving authority (e.g. board/director) | Approves policy, targets and resources; informed of major incidents; reviews assurance | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| BC/DR lead | Maintains plans, BIA, testing programme and records; coordinates response | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| Incident lead / decision-maker | Declares and closes incidents; sets priorities; authorises spend and workarounds | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| IT / security lead (internal or outsourced) | Technical containment and recovery; liaison with IT suppliers and the NCSC where applicable | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| Communications lead | Staff, customer, media and stakeholder messages; approved statements only | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| Data protection lead / DPO | Assesses personal data impact; decides on ICO/individual notification | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| People / HR lead | Staff welfare, working arrangements, absence | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| Facilities / health & safety lead | Evacuation, site access, safety checks | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| Finance lead | Emergency purchasing, insurance claims, payments continuity | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| Service owners | Run BIA, workarounds and service recovery for their area | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| All staff | Follow instructions, report incidents promptly, keep contact details current | All | n/a |

**Activation:** Any member of staff reports a disruption to [[PLACEHOLDER: contact route]]. The incident lead (or deputy) decides whether to activate this policy using criteria in [[PLACEHOLDER: e.g. service unavailable beyond X, safety risk, suspected breach]]. Decisions are logged (Appendix B). **Stand-down** is declared by the incident lead once services are stable and the recovery checklist is complete.

## 9. Emergency communications

| Audience | Purpose | Method (primary / fallback) | Owner | Template ready? |
|---|---|---|---|---|
| Staff | Safety, instructions, working arrangements | [[PLACEHOLDER: e.g. messaging app, SMS, phone tree]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| Customers / service users | Service status and alternatives | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| Suppliers / partners | Coordination, support requests | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| Regulators / funders / insurer | Required notifications | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| Emergency services / landlord | Site incidents | [[PLACEHOLDER]] | [[PLACEHOLDER]] | n/a |
| Media / public | Single approved statement | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |

**Rules**
- Hold the contact list in at least one location that does not depend on organisation systems, such as printed or on personal or secure mobile devices [[PLACEHOLDER: approved method]].
- Assume normal email, phone and chat may be unavailable or compromised. Use pre-agreed out-of-band channels.
- Give factual, timely and consistent messages. Do not speculate on cause or blame.
- Only the communications lead (or deputy) issues external statements.
- Record all notifications and times.

## 10. Alternative working arrangements

| Loss | Options (to be assessed and approved) | Pre-requisites |
|---|---|---|
| Premises unavailable | Home or remote working; alternative site, shared/serviced space, partner premises [[PLACEHOLDER]] | Remote access, devices, paper forms, agreements in place |
| Staff shortage | Cross-training, deputies, temporary staff, reduced service level per MBCO | Skills matrix, documented procedures |
| IT or network failure | Manual or paper workarounds, mobile data, alternative devices, supplier failover | Offline procedures, spare equipment [[PLACEHOLDER]] |
| Utility or connectivity loss | Alternative connectivity, power resilience, relocation | [[PLACEHOLDER]] |

**Requirements**
- Remote and alternative working must use secure configurations: MFA, up-to-date and managed devices, encrypted storage, and no bypass of security controls for convenience.
- Document manual workarounds for each Tier 1 and Tier 2 service, including how to reconcile data back into systems afterwards.
- Maintain a list of critical equipment, licences and spares [[PLACEHOLDER]].
- Consider staff welfare, accessibility, health and safety, and lone-working in alternative arrangements.
- Alternative sites: [[PLACEHOLDER: location, capacity, access arrangements, cost authority]].

## 11. Cyber incidents

Cyber incidents are handled under the incident response plan [[PLACEHOLDER: reference]] and this section, following NCSC incident management principles: prepare, detect, respond, recover, learn.

**Preparation**
- Maintain asset, account and data inventories and network diagrams.
- Apply baseline controls (e.g. Cyber Essentials themes: firewalls, secure configuration, access control, malware protection, patching) [[PLACEHOLDER: current status]].
- Enable MFA, logging and alerting appropriate to the organisation [[PLACEHOLDER]].
- Keep an offline incident response contact sheet, including IT provider, insurer helpline, legal and forensic support [[PLACEHOLDER]].
- Check cyber insurance conditions and notification duties [[PLACEHOLDER]].

**Response summary**

| Stage | Key actions |
|---|---|
| 1. Identify and report | Staff report suspicious activity immediately. Triage and log. |
| 2. Assess | Establish scope, systems and data affected, and whether personal data is involved. Preserve evidence. |
| 3. Contain | Isolate affected devices or accounts. Disable compromised credentials. Do not wipe systems before evidence and scope are considered. Avoid using compromised channels. |
| 4. Notify | Insurer, IT/security providers and others as required. **Personal data breaches:** assess and, where the legal threshold is met, report to the ICO without undue delay and within 72 hours of becoming aware. Consider notifying affected individuals. Also consider police/Action Fraud, the NCSC, regulators, funders and contractual partners [[PLACEHOLDER: confirm obligations]]. |
| 5. Eradicate and recover | Remove the cause. Rebuild from known-good sources. Restore from verified, clean backups. Reset credentials. Monitor for reinfection. |
| 6. Review | Post-incident review (Section 14). |

**Ransomware:** The decision on any ransom payment is reserved to [[PLACEHOLDER: approving authority]] after legal, law enforcement and insurer advice. Payment is not assumed or recommended by this policy. NCSC and law enforcement guidance discourages payment. Recovery from backups is the preferred route.

## 12. Supplier dependencies

| Supplier | Service supported | Critical? | Contract / SLA recovery commitments | Supplier BC/security assurance obtained | Alternative / exit option | Owner | Emergency contact |
|---|---|---|---|---|---|---|---|
| [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |

**Requirements**
- Maintain a supplier register identifying those supporting critical services, including IT, cloud/SaaS, telecoms, payment, utilities, payroll and facilities, and their sub-suppliers where known.
- Before contracting and at renewal, assess supplier resilience, security, data location and ability to meet recovery needs (NCSC supply chain guidance).
- Contracts for critical suppliers should address incident notification, recovery commitments, data return/export, support hours and exit [[PLACEHOLDER: legal review]].
- Consider concentration risk and single points of failure.
- Include critical suppliers in plans and, where practical, exercises.
- Know how to contact suppliers if normal channels are down.

## 13. Testing and exercises

| Activity | Purpose | Minimum frequency | Owner |
|---|---|---|---|
| Contact list and call-tree check | Verify contacts and out-of-band channels | [[PLACEHOLDER]] | BC/DR lead |
| Backup restore test | Prove data recovery against RPO/RTO | [[PLACEHOLDER]] | IT/security lead |
| Tabletop (discussion) exercise | Test decisions, roles and communications. NCSC Exercise in a Box can be used. | [[PLACEHOLD
ER]] | BC/DR lead |
| Technical recovery test | Rebuild or fail over a system, or restore it from backup, within RTO | [[PLACEHOLDER]] | IT/security lead |
| Cyber scenario exercise (e.g. ransomware, account compromise) | Test cyber response, containment, notification and recovery decisions | [[PLACEHOLDER]] | IT/security lead with BC/DR lead |
| Alternative working test | Confirm staff can work remotely or from an alternative site securely | [[PLACEHOLDER]] | Facilities lead / IT lead |
| Supplier scenario or joint exercise | Test supplier contacts, escalation and failover where practical | [[PLACEHOLDER]] | Supplier owner |
| Plan walkthrough and staff briefing | Confirm everyone knows their role, the activation route and the safety actions | [[PLACEHOLDER]] and at induction | BC/DR lead / People lead |

**Exercise requirements**
- Maintain a testing schedule approved by [[PLACEHOLDER: approving authority]].
- Each exercise must have written objectives, scope, participants, scenario, safety controls and a named facilitator.
- Exercises must not put live services, data or people at unplanned risk. Technical tests should have rollback plans and be approved in advance.
- Rotate scenarios so that all scenarios in Section 1 are covered over [[PLACEHOLDER: cycle length]].
- Include deputies, and include senior decision-makers in at least one exercise per cycle.
- Record results: what was tested, what worked, what failed, measured recovery times against RTO/RPO, and actions arising.
- Re-test after significant failures or major changes.

## 14. Incidents, lessons learned and improvement

A review is required after every activation of this policy, every significant exercise or test, and any near miss that the BC/DR lead considers significant.

**Process**

| Step | Requirement | Timescale |
|---|---|---|
| 1. Capture | Keep the incident log, decisions, timings and evidence | During the incident |
| 2. Hold review | Run a blameless review with those involved, covering the timeline, impact, what worked and what did not, root causes and contributing factors | Within [[PLACEHOLDER]] of stand-down or exercise |
| 3. Compare | Compare actual recovery times and data loss with the RTO, RPO and MBCO in Section 6 | At the review |
| 4. Record actions | Log each improvement with an owner, priority and due date in an action tracker | At the review |
| 5. Report | Give a summary to [[PLACEHOLDER: approving authority]], including unresolved risks and resource needs | Within [[PLACEHOLDER]] |
| 6. Update | Revise the policy, plans, contact lists, BIA, targets, training and supplier arrangements as needed | By the action due dates |
| 7. Verify | Confirm completed actions are effective, using re-testing where appropriate | [[PLACEHOLDER]] |

**Review questions:** Was the activation timely? Were roles clear? Did communications work without normal systems? Were backups usable and complete? Were the targets realistic? Did suppliers perform as expected? Were legal and notification duties met? Were staff supported?

Where the incident involved personal data, the data protection lead must also record the breach assessment and the reasons for any notification decisions, as required by UK GDPR.

## 15. Policy governance, maintenance and review

- **Review cycle:** at least every [[PLACEHOLDER: frequency]], and sooner after any of the following: a significant incident or exercise failure; changes to services, sites, systems, suppliers or key people; changes in law, regulation, insurance or contractual requirements; new significant risks; or changes to referenced guidance.
- **Reviewers:** the BC/DR lead prepares the review. [[PLACEHOLDER: independent or specialist reviewer]] provides challenge. The approving authority approves material changes.
- **Training and awareness:** all staff are briefed at induction and at least [[PLACEHOLDER: frequency]]. Responders receive role-specific training. Records are kept.
- **Records:** retain BIAs, test results, incident logs, review reports and approvals for [[PLACEHOLDER: period]].
- **Assurance and reporting:** the BC/DR lead reports to [[PLACEHOLDER: approving authority]] at least [[PLACEHOLDER: frequency]] on test results, open actions, target gaps, supplier risks and changes.
- **Compliance and exceptions:** deviations from this policy must be risk-assessed, time-limited and approved by [[PLACEHOLDER: role]], and recorded in the risk register.
- **Distribution:** keep current copies of the policy and key plans offline and in locations accessible during an outage [[PLACEHOLDER: locations and holders]]. Control versions so responders do not use out-of-date copies.

## Appendix A – Emergency contact list (template)

Store a copy outside organisational systems. Review at least [[PLACEHOLDER: frequency]].

| Name / organisation | Role | Primary contact | Alternative contact | Out-of-hours | Last verified |
|---|---|---|---|---|---|
| [[PLACEHOLDER]] | Incident lead | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| [[PLACEHOLDER]] | BC/DR lead | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| [[PLACEHOLDER]] | IT / security provider | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| [[PLACEHOLDER]] | Cyber insurer / helpline | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| [[PLACEHOLDER]] | Legal adviser | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| [[PLACEHOLDER]] | Data protection lead / DPO | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| [[PLACEHOLDER]] | Landlord / facilities | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| [[PLACEHOLDER]] | Critical suppliers (see Section 12) | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |
| [[PLACEHOLDER]] | Regulators / funders | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |

Public bodies to consider (confirm current routes before use): emergency services (999/101), ICO, NCSC, Action Fraud / Police Scotland as applicable, local authority emergency planning, utility providers.

## Appendix B – Incident and decision log (template)

| Date / time | Event or decision | Made by | Reason | Actions and owners | Communications sent |
|---|---|---|---|---|---|
| [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |

## Appendix C – Activation and recovery checklist (summary)

1. Make sure people are safe. Call emergency services if needed.
2. Report to the incident lead. Log the time and details.
3. Decide whether to activate, and assign roles and deputies.
4. Open the incident log. Preserve evidence if the incident is cyber-related.
5. Establish the scope and the affected services, and compare them with the Tier list (Section 5).
6. Use out-of-band communications. Issue the first staff instruction.
7. Assess legal, regulatory, insurance and personal data notification duties, noting deadlines.
8. Start workarounds and alternative arrangements (Section 10).
9. Recover in priority order. Validate data integrity and security before returning services to users.
10. Update stakeholders regularly. Record all decisions.
11. Stand down when services are stable, and reconcile any manual records.
12. Hold the post-incident review (Section 14).

## Appendix D – Review and approval record

This section must be completed only by the organisation after human review and formal approval. Until then, this document remains a draft and must not be relied on operationally.

| Item | Record |
|---|---|
| Reviewed by (name, role, date) | [[PLACEHOLDER]] |
| Specialist or independent review (if any) | [[PLACEHOLDER]] |
| Changes required before approval | [[PLACEHOLDER]] |
| Approved by (name, role) | [[PLACEHOLDER: to be completed only on formal approval]] |
| Date of approval | [[PLACEHOLDER]] |
| Effective date and version | [[PLACEHOLDER]] |
| Next review due | [[PLACEHOLDER]] |
| Communication to staff completed (date) | [[PLACEHOLDER]] |

*End of draft. This template does not constitute legal, regulatory or professional advice. The organisation remains responsible for its own targets, controls and compliance.*