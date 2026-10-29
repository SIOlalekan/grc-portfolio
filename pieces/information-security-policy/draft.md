# Information Security Policy

> > **DRAFT – PENDING HUMAN REVIEW AND ORGANISATIONAL APPROVAL**
> This document is a portfolio draft and has not been formally adopted by an organisation. Organisation-specific placeholders must be completed, and the document must be reviewed against applicable legal, regulatory, contractual and security requirements before operational use..

---

## 1. Document Control

| Item | Detail |
|---|---|
| Organisation | [[PLACEHOLDER: legal name]] |
| Policy owner | [[PLACEHOLDER: role, e.g. Director / IT Lead]] |
| Approved by | [[PLACEHOLDER: name/role]] |
| Version / status | 0.1 DRAFT, not approved |
| Approval date | [[PLACEHOLDER]] |
| Next review | [[PLACEHOLDER: at least annually]] |
| Related documents | [[PLACEHOLDER: Privacy Notice, Retention Schedule, Incident Plan, Acceptable Use Policy, etc.]] |

## 2. Purpose, Scope and Principles

**Purpose:** To protect the confidentiality, integrity and availability of information held or processed by [[PLACEHOLDER: organisation]], and to set out clear expectations for everyone who handles it.

**Scope:** This policy applies to all staff, directors, volunteers, contractors and temporary workers, and to all information, systems, devices, cloud services and premises used for organisational business, including personal devices if permitted ([[PLACEHOLDER: BYOD allowed? Y/N]]).

**Principles:**
- **Risk-based:** controls are proportionate to the risks we identify.
- **Least privilege:** people get only the access they need.
- **Defence in depth:** no single control is relied on alone.
- **Shared responsibility:** security is everyone's job.
- **Continual improvement:** we learn from incidents, reviews and changing threats.

**Framework references (informal):** This policy is *informed by* the NCSC's *10 Steps to Cyber Security* and small-organisation guidance, ISO/IEC 27001 concepts (risk management, defined responsibilities, continual improvement) and CIS Critical Security Controls v8 (see Appendix A). Use of these references does not imply conformity with them.

## 3. Governance

- **Leadership accountability:** [[PLACEHOLDER: Director/Board]] is accountable for information security and approves this policy.
- **Risk management:** A simple information risk register is kept at [[PLACEHOLDER: location]]. It is reviewed at least [[PLACEHOLDER: e.g. every 6/12 months]] and after major changes or incidents. Each risk has an owner, a rating and a treatment decision (reduce, accept, transfer or avoid).
- **Legal and regulatory awareness:** The organisation identifies the laws and contractual requirements that apply to it, for example UK GDPR, the Data Protection Act 2018, customer contracts and [[PLACEHOLDER: sector rules, e.g. FCA, CQC, PCI DSS, funder requirements]].
- **Reporting:** Security status (incidents, risks, outstanding actions) is reported to leadership at least [[PLACEHOLDER: frequency]].
- **Exceptions:** Any deviation from this policy needs a written risk assessment and approval from the Policy Owner, a recorded expiry date and compensating controls.
- **Enforcement:** Breaches of this policy may lead to disciplinary action or contract termination, as set out in [[PLACEHOLDER: HR policy/contract terms]].

## 4. Roles and Responsibilities

| Role | Key responsibilities |
|---|---|
| **Leadership / Board** | Set direction, provide resources, approve policy, accept residual risk |
| **Information Security Lead** ([[PLACEHOLDER: name/role]]) | Maintain policy and risk register, coordinate incident response, oversee training and reviews, report to leadership |
| **IT support** (internal or [[PLACEHOLDER: provider]]) | Secure configuration, patching, backups, account administration, logging |
| **Data Protection Lead / DPO** ([[PLACEHOLDER: name or "DPO not appointed"]]) | Advise on UK GDPR, maintain records of processing, handle data subject requests and breach assessments |
| **Line managers** | Ensure joiner/mover/leaver steps are completed, and that team members are trained and follow policy |
| **All personnel** | Follow this policy, complete training, protect credentials and devices, and report incidents and concerns immediately |
| **Contractors / suppliers** | Meet contractual security obligations and report incidents promptly |

## 5. Access Control

| Area | Requirement |
|---|---|
| **Principle** | Access is granted on a need-to-know, least-privilege basis and approved by the information owner or line manager. |
| **Unique accounts** | Each person has their own account. Shared accounts are prohibited unless risk-assessed and documented ([[PLACEHOLDER: exceptions]]). |
| **Authentication** | Enable multi-factor authentication (MFA) on email, cloud services, remote access and all administrator accounts. Where MFA is not possible, use strong unique passwords. |
| **Passwords** | Follow NCSC guidance: long, hard-to-guess passwords (e.g. three random words), no reuse across services, use of an approved password manager ([[PLACEHOLDER: tool]]), and no forced periodic changes unless compromise is suspected. Default passwords are changed before use. |
| **Privileged access** | Administrator rights are limited, separate from day-to-day accounts, and reviewed at least [[PLACEHOLDER: e.g. quarterly]]. |
| **Joiners / movers / leavers** | Access is provisioned on approval, changed when roles change, and removed on the last working day (immediately for high-risk departures). Devices and credentials are returned or revoked. |
| **Access reviews** | User access to key systems is reviewed at least [[PLACEHOLDER: e.g. every 6 months]]. Dormant accounts are disabled after [[PLACEHOLDER: e.g. 30–90 days]] of inactivity. |
| **Remote and mobile working** | Use only approved devices and secure connections ([[PLACEHOLDER: VPN/zero-trust tool]]). Avoid public Wi-Fi for sensitive work unless protected. Lock screens when unattended. |
| **Physical access** | Premises, server/comms equipment and paper records are secured by [[PLACEHOLDER: locks, keys, visitor sign-in, clear-desk rules]]. |

## 6. Asset Management

- **Inventory:** Maintain an inventory of hardware (laptops, phones, servers, network equipment), software and cloud services, and information assets, each with an owner. The inventory is held at [[PLACEHOLDER: location]] and reviewed at least [[PLACEHOLDER: frequency]].
- **Secure configuration:** Devices use supported operating systems and software. Unnecessary services and accounts are removed, and a firewall is enabled. Standard build settings are documented at [[PLACEHOLDER]].
- **Patching:** Security updates are applied promptly. Critical and high-risk updates are applied within [[PLACEHOLDER: e.g. 14 days or sooner if actively exploited]]. Unsupported software is replaced or isolated.
- **Malware protection:** Anti-malware or equivalent built-in protection is enabled and kept up to date on all endpoints ([[PLACEHOLDER: product]]). Email and web filtering are enabled where available.
- **Encryption:** Laptops, mobile devices and removable media holding organisational data use device encryption. Data is encrypted in transit.
- **Information classification:**

| Level | Description | Examples | Handling |
|---|---|---|---|
| **Public** | Approved for release | Website content | No restrictions |
| **Internal** | Business information not for public release | Policies, internal emails | Organisation systems only |
| **Confidential** | Sensitive business or personal data | HR, customer, financial records | Restricted access, encryption, no personal accounts |
| **Special category / highly sensitive** | Special category or criminal offence data, security credentials | Health, biometrics, passwords | Strictest access, encryption, minimal sharing |

  [[PLACEHOLDER: adjust levels to the organisation]]
- **Removable media:** Use only when necessary, and only if encrypted and approved. Scan before use.
- **Disposal:** Devices and media are securely wiped or destroyed before reuse or disposal, with records kept. Paper is shredded or disposed of via confidential waste.
- **Software and cloud adoption:** New systems and services must be approved by [[PLACEHOLDER: role]] before use. "Shadow IT" is not permitted.

## 7. Data Protection

- **Legal basis:** Personal data is handled in line with UK GDPR and the Data Protection Act 2018. The data protection principles are: lawfulness, fairness and transparency; purpose limitation; data minimisation; accuracy; storage limitation; integrity and confidentiality; accountability.
- **Records:** A record of processing activities and lawful bases is maintained at [[PLACEHOLDER: location]]. Privacy notices are provided where required.
- **ICO registration:** [[PLACEHOLDER: confirm data protection fee/registration status with the ICO]]
- **Data protection by design:** Consider privacy and security at the start of any new project or system. Carry out a Data Protection Impact Assessment (DPIA) where processing is likely to be high risk.
- **Retention:** Data is kept only as long as necessary, as set out in the Retention Schedule ([[PLACEHOLDER: link and periods]]), then securely deleted.
- **Individual rights:** Requests (access, rectification, erasure, etc.) are forwarded to [[PLACEHOLDER: contact]] immediately and handled within the legal timescale, normally one month.
- **Sharing and transfers:** Personal data is shared only where there is a lawful basis and appropriate agreements. International transfers require a documented safeguard ([[PLACEHOLDER: e.g. UK adequacy regulations, IDTA/Addendum]]).
- **Secure handling:**
  - Use approved storage and file-sharing tools only.
  - Do not use personal email or personal cloud storage for organisational data.
  - Double-check recipients and use encryption or access-controlled links for sensitive information.
  - Keep paper records locked away.
- **Personal data breaches:** Handled under Section 8. The organisation must assess and, where required, report to the ICO within **72 hours** of becoming aware. High-risk breaches also require notifying affected individuals without undue delay.
- **Backups and data recovery:** Covered in Section 10.

## 8. Incident Management

**Definition:** An incident is any event that actually or potentially compromises information or systems. Examples include phishing clicks, lost devices, malware, unauthorised access, misdirected emails, ransomware and supplier breaches.

**Reporting:** Everyone must report suspected incidents **immediately** to [[PLACEHOLDER: email / phone / out-of-hours contact]]. Reporting in good faith will not result in blame.

| Stage | Actions |
|---|---|
| **1. Detect & report** | Report to the Information Security Lead. Log the incident with date, time, reporter and summary at [[PLACEHOLDER: log location]]. |
| **2. Assess & classify** | Determine severity and impact, and whether personal data is involved. Assign an incident lead. |
| **3. Contain** | Isolate affected devices, disable compromised accounts, revoke access and preserve evidence (do not wipe devices without advice). |
| **4. Eradicate & recover** | Remove the cause, restore from clean backups, reset credentials and verify systems before returning to service. |
| **5. Notify** | Where required, notify the ICO (within 72 hours for notifiable personal data breaches), affected individuals, customers, insurers ([[PLACEHOLDER: cyber insurer contact]]), the police/Action Fraud (or Police Scotland), regulators and other parties named in contracts. Consider reporting to the NCSC. Leadership approves external communications. |
| **6. Review** | Hold a post-incident review within [[PLACEHOLDER: e.g. 10 working days]]. Record lessons learned, update the risk register, and track corrective actions to closure. |

- **Key contacts:** [[PLACEHOLDER: IT provider, legal adviser, DPO, insurer, communications lead, ICO/Action Fraud details]]
- **Testing:** The incident process is tested at least [[PLACEHOLDER: annually]], for example with a tabletop exercise such as the NCSC's *Exercise in a Box*.

## 9. Supplier Security

- **Supplier register:** Maintain a list of suppliers that handle our information or provide critical services, including cloud, IT, payroll, and marketing providers ([[PLACEHOLDER: location]]).
- **Due diligence before engagement:** Proportionate to risk, check:
  - the supplier's security practices (e.g. MFA, encryption, patching, certifications or assurance they hold, which we verify rather than assume);
  - data location and sub-processors;
  - breach notification commitments;
  - exit and data return/deletion arrangements.
- **Contracts:** Written agreements include confidentiality, security requirements, incident notification timescales ([[PLACEHOLDER: e.g. within 24–48 hours]]), audit/assurance rights where appropriate, and right to terminate. Where a supplier processes personal data on our behalf, a UK GDPR Article 28-compliant contract is required.
- **Access:** Supplier access is least-privilege, time-limited, MFA-protected and logged. Accounts are removed at contract end.
- **Ongoing oversight:** Review critical suppliers at least [[PLACEHOLDER: annually]], including changes in service, incidents and assurance evidence.
- **Offboarding:** Ensure data is returned or securely deleted, and obtain written confirmation.

## 10. Business Continuity and Resilience

- **Critical services:** Identify the critical business processes, their systems, and the maximum tolerable downtime. See [[PLACEHOLDER: business impact summary]].

| Critical service | Owner | Target recovery time (RTO) | Max data loss (RPO) |
|---|---|---|---|
| [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |

- **Backups:**
  - Back up important data and configurations regularly ([[PLACEHOLDER: frequency]]).
  - Follow a "3-2-1" approach where practical: three copies, on two different media types, with one offline or offsite/immutable.
  - Protect backups from tampering with access controls and separate credentials.
  - Test restores at least [[PLACEHOLDER: e.g. every 6 months]] and record the results.
- **Continuity plan:** A documented plan at [[PLACEHOLDER: location]] covers loss of premises, IT, key staff, power/connectivity and key suppliers, and includes contact lists and manual workarounds. A copy is available offline.
- **Ransomware readiness:** Maintain offline backups, restrict administrative privileges, and make sure staff know the reporting route.
- **Exercise and review:** Test the plan at least [[PLACEHOLDER: annually]] and after significant change. Update it with lessons learned.

## 11. Training and Awareness

| Audience | Training | Timing |
|---|---|---|
| **All personnel** | Induction on this policy, phishing and social engineering, password/MFA use, data handling, reporting incidents, safe remote working | On joining, then at least [[PLACEHOLDER: annually]] |
| **Administrators / IT** | Secure configuration, patching, logging, privileged access, incident response | On role start and annually |
| **Managers** | Joiner/mover/leaver duties, risk ownership, supplier oversight | On role start and annually |
| **Data protection roles** | UK GDPR obligations, DPIAs, breach assessment, rights requests | On role start and annually |

- Short awareness reminders (e.g. phishing examples) are shared at least [[PLACEHOLDER: e.g. quarterly]].
- Attendance and completion records are kept by [[PLACEHOLDER: role]].
- Staff are told that they can report mistakes without fear of blame.

## 12. Monitoring and Assurance

- **Logging:** Enable and retain logs for key systems (email, identity/authentication, cloud services, firewalls, endpoints) for at least [[PLACEHOLDER: e.g. 90 days–12 months]]. Access to logs is restricted.
- **Alerting:** Configure alerts for high-risk events such as repeated failed logins, new administrator accounts, mail-forwarding rules, malware detections and unusual data transfers. Alerts are reviewed by [[PLACEHOLDER: role]] at least [[PLACEHOLDER: frequency]].
- **Vulnerability management:** Scan or review systems for vulnerabilities at least [[PLACEHOLDER: frequency]] and track remediation. Consider subscribing to the NCSC's free services (e.g. Early Warning) and to supplier security advisories.
- **Testing:** Consider independent security testing of internet-facing systems at least [[PLACEHOLDER: e.g. annually or after major change]], proportionate to risk.
- **Lawful and transparent monitoring:** Monitoring of staff use of systems is proportionate, lawful and communicated through [[PLACEHOLDER: privacy notice / acceptable use policy]]. Monitoring data is used only for security, operational and legal purposes.
- **Metrics:** Track and report simple indicators to leadership, for example:
  - percentage of devices fully patched;
  - MFA coverage;
  - training completion;
  - incidents and time to resolve;
  - last successful restore test;
  - overdue access reviews.
- **Internal checks:** Review compliance with this policy at least [[PLACEHOLDER: annually]]. Findings are logged as corrective actions with owners and due dates.
- **External assurance:** [[PLACEHOLDER: state any planned independent assurance, e.g. working towards Cyber Essentials, only if genuinely intended]]

## 13. Policy Review and Communication

- This policy is reviewed at least **annually**, and sooner after a significant incident, legal change, major system change or organisational change.
- Reviews consider incidents, audit findings, risk register changes, new threats and updated guidance (NCSC, ICO).
- Approved versions are communicated to all in scope, and acknowledgement is recorded ([[PLACEHOLDER: method]]).
- Version history is retained.

| Version | Date | Author | Summary of change | Approved by |
|---|---|---|---|---|
| 0.1 | [[PLACEHOLDER]] | AI-assisted draft | Initial draft, pending human review | Not approved |

---

## Appendix A: Informal Reference Mapping

This mapping is for orientation only. It does not demonstrate conformity with any framework.

| Policy section | NCSC guidance (public) | ISO/IEC 27001 concepts | CIS Controls v8 |
|---|---|---|---|
| 3 Governance | 10 Steps: Risk management | Leadership, risk assessment and treatment, continual improvement | Overall governance context |
| 4 Responsibilities | 10 Steps: Engagement and training | Roles, responsibilities and authorities | n/a |
| 5 Access control | Password and MFA guidance; user access | Access control, authentication, privileged access | 5, 6 |
| 6 Asset management | Device security; secure configuration; vulnerability management | Asset inventory, classification, secure disposal | 1, 2, 3, 4, 7, 9, 10 |
| 7 Data protection | Guidance aligned to ICO/UK GDPR | Privacy and PII protection, legal and regulatory requirements | 3 |
| 8 Incident management | Incident management guidance | Incident planning, response and learning | 17 |
| 9 Supplier security | Supply chain security guidance | Supplier relationships and cloud services | 15 |
| 10 Business continuity | Backing up your data; ransomware guidance | ICT readiness for business continuity | 11 |
| 11 Training | Engagement and training; phishing guidance | Awareness, education and training | 14 |
|
| 12 Monitoring and assurance | Logging and monitoring; vulnerability management; Early Warning service | Monitoring, measurement, internal audit, technical vulnerability management | 7, 8, 13, 18 |
| 13 Policy review | 10 Steps: Risk management; governance guidance | Documented information, management review, continual improvement | Overall governance context |

*Note: Control numbers refer to CIS Critical Security Controls v8. Check them against the current published version before relying on them.*

---

## Appendix B: Pre-Adoption Checklist

Complete these steps before this policy is approved or circulated.

| # | Action | Owner | Done |
|---|---|---|---|
| 1 | Review the full draft for accuracy against actual practice | [[PLACEHOLDER]] | ☐ |
| 2 | Complete or remove every `[[PLACEHOLDER]]` | [[PLACEHOLDER]] | ☐ |
| 3 | Confirm legal and contractual obligations (UK GDPR, sector rules, customer and funder requirements) with a qualified adviser | [[PLACEHOLDER]] | ☐ |
| 4 | Confirm ICO data protection fee/registration status | [[PLACEHOLDER]] | ☐ |
| 5 | Check that stated controls (MFA, backups, patching, logging) are actually in place, or record a plan and date | [[PLACEHOLDER]] | ☐ |
| 6 | Align related documents (Acceptable Use, Privacy Notice, Retention Schedule, Incident Plan, HR policies) | [[PLACEHOLDER]] | ☐ |
| 7 | Build the initial risk register, asset inventory and supplier register | [[PLACEHOLDER]] | ☐ |
| 8 | Check the framework references and CIS control numbers against current public versions | [[PLACEHOLDER]] | ☐ |
| 9 | Obtain leadership approval and record it in Section 1 | [[PLACEHOLDER]] | ☐ |
| 10 | Communicate the policy to all in scope and record acknowledgements | [[PLACEHOLDER]] | ☐ |

## Appendix C: Suggested First 90 Days

Prioritise these steps if resources are limited. Adjust them to your own risk assessment.

| Timeframe | Priority actions |
|---|---|
| **Days 0–30** | Enable MFA on email, cloud and admin accounts. Confirm backups exist and run a test restore. Turn on automatic updates. Appoint the Information Security Lead. Publish the incident reporting contact. |
| **Days 31–60** | Create the asset inventory and supplier register. Remove unsupported software or isolate it. Review admin rights and leaver accounts. Deliver initial awareness training. |
| **Days 61–90** | Complete the risk register and the record of processing. Review contracts with key suppliers. Run a tabletop incident exercise. Set up monitoring metrics and report them to leadership. |

## Appendix D: Approval and Acknowledgement

| Item | Detail |
|---|---|
| Approved by (name/role) | [[PLACEHOLDER]] |
| Signature | [[PLACEHOLDER]] |
| Date approved | [[PLACEHOLDER]] |
| Effective date | [[PLACEHOLDER]] |
| Acknowledgement method | [[PLACEHOLDER: e.g. LMS sign-off, signed form, email confirmation]] |

---

**Closing statement:** This is an AI-assisted draft and remains unapproved until reviewed, completed and formally adopted by [[PLACEHOLDER: organisation]]. It does not represent certification, accreditation or legal compliance. Seek qualified legal, data protection and security advice where needed.

*End of document.*
