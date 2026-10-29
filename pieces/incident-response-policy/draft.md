# Incident Response Policy

> **AI-ASSISTED DRAFT, PENDING HUMAN REVIEW**
> This document was drafted with AI assistance from publicly available guidance. It has **not** been reviewed, validated or approved by the organisation, legal counsel, or a qualified security or data protection professional. **Human review and formal approval are required before adoption.**
>
> - Items marked **[[PLACEHOLDER]]** are unknown and must be completed by the organisation. Nothing has been invented about the organisation.
> - Items marked **⚖ LEGAL REVIEW** depend on jurisdiction, sector or contract and must be confirmed by a suitably qualified person.
> - Items marked **🎯 SUGGESTED TARGET** are starting points only and **require organisational approval** before they become commitments.
> - Nothing in this document claims or implies certification, accreditation or compliance with any standard, law or framework. References to NIST and NCSC guidance show where ideas were drawn from, not conformity.
> - Check that the referenced guidance is the current version before adoption. For example, NIST SP 800-61 has been revised (Revision 3 aligns with CSF 2.0), so confirm which revision the organisation intends to follow.

---

## 1. Document Control

| Field | Entry |
|---|---|
| Document title | Incident Response Policy |
| Organisation | [[PLACEHOLDER: legal entity name]] |
| Version | 0.1 (AI-assisted draft) |
| Status | Draft, not approved |
| Policy owner | [[PLACEHOLDER: role/title]] |
| Author / drafter | [[PLACEHOLDER]] (initial draft AI-assisted) |
| Reviewer(s) | [[PLACEHOLDER]] |
| Approver | [[PLACEHOLDER: e.g. director / board / owner]] |
| Approval date | [[PLACEHOLDER]] |
| Effective date | [[PLACEHOLDER]] |
| Next review date | [[PLACEHOLDER]] (see Section 23) |
| Storage location | [[PLACEHOLDER]] |
| Distribution | [[PLACEHOLDER: all staff / managers / contractors]] |
| Related documents | [[PLACEHOLDER: Information Security Policy, Data Protection Policy, Business Continuity Plan, Acceptable Use Policy, supplier contracts, cyber insurance policy]] |

**Revision history**

| Version | Date | Author | Summary of change | Approved by |
|---|---|---|---|---|
| 0.1 | [[PLACEHOLDER]] | AI-assisted draft | Initial draft | Not approved |

---

## 2. Purpose and Scope

### 2.1 Purpose
This policy sets out how [[PLACEHOLDER: organisation name]] prepares for, detects, responds to, recovers from and learns from information security incidents. Its aims are to:

- limit harm to people, operations, data and reputation;
- restore normal operations in a controlled way;
- meet legal, regulatory and contractual obligations (see Sections 15–16);
- keep a reliable record of what happened and why decisions were made; and
- improve defences over time.

### 2.2 Scope
This policy applies to:

- all employees, directors, contractors, temporary staff, volunteers and others with access to organisational systems or data ([[PLACEHOLDER: confirm categories]]);
- all information, systems, devices, cloud services, accounts and networks owned, operated or used on the organisation's behalf, including personally owned devices if permitted ([[PLACEHOLDER: BYOD position]]); and
- incidents at third-party suppliers that affect the organisation's data or services.

**Out of scope or handled elsewhere:** [[PLACEHOLDER: e.g. physical safety emergencies, fraud investigations, HR disciplinary processes, business continuity events not involving information security]]. Where incidents overlap with these areas, the Incident Lead must coordinate with the relevant owner.

### 2.3 Guiding approach
This policy draws on the public guidance below, in original wording:

- **NIST Cybersecurity Framework (CSF) 2.0**: the Govern, Identify, Protect, Detect, Respond and Recover functions, particularly the Respond (incident management, analysis, reporting and communication, mitigation) and Recover (recovery plan execution and communication) outcomes.
- **NIST SP 800-61**: the Computer Security Incident Handling Guide, covering preparation, detection and analysis, containment, eradication and recovery, and post-incident activity.
- **UK NCSC guidance**: including its incident management and small-business response and recovery guidance. [[PLACEHOLDER: confirm the specific NCSC documents the organisation will rely on.]]

---

## 3. Definitions

| Term | Meaning in this policy |
|---|---|
| **Event** | Any observable occurrence in a system or network (e.g. a failed login, an alert). Most events are harmless. |
| **Incident** | An event, or series of events, that actually or potentially compromises the confidentiality, integrity or availability of information or systems, or breaches security policy or law. |
| **Security incident** | An incident with a cyber or information security cause (e.g. malware, account compromise, data theft, denial of service, insider misuse, lost device). |
| **Personal data** | Information relating to an identified or identifiable living individual, as defined by applicable law. ⚖ LEGAL REVIEW: confirm definition for [[PLACEHOLDER: jurisdiction(s)]]. |
| **Personal data breach** | A security incident leading to accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data. ⚖ LEGAL REVIEW: confirm statutory definition. |
| **Incident Lead** | The person appointed to coordinate response to a specific incident (Section 5). |
| **Containment** | Actions that stop an incident spreading or worsening. |
| **Eradication** | Removal of the cause and artefacts of an incident (e.g. malware, unauthorised accounts). |
| **Recovery** | Restoring systems and services to normal, verified operation. |
| **Evidence** | Data, logs, devices, images or records that may help establish what happened, and which may be needed for legal, regulatory, insurance or law-enforcement purposes. |
| **Chain of custody** | A record of who handled evidence, when, and what they did with it. |
| **Indicators of compromise (IoCs)** | Technical artefacts (IP addresses, file hashes, domains, account names) suggesting compromise. |
| **Critical systems / data** | [[PLACEHOLDER: list or criteria, e.g. finance system, customer database, email, backups]] |

---

## 4. Policy Statements

1. All suspected incidents **must** be reported promptly, without fear of blame for good-faith reports.
2. Every reported incident **must** be logged, triaged and assigned an owner.
3. Response decisions **should** be proportionate to severity and made by authorised people (Section 5).
4. Evidence **must** be preserved before systems are altered, wherever this is practical and safe (Section 12).
5. Possible personal data breaches **must** be assessed promptly against legal notification deadlines (Sections 15–16).
6. Every significant incident **must** receive a post-incident review, with tracked corrective actions (Sections 18–20).
7. This policy **must** be tested and reviewed (Sections 22–23).

---

## 5. Roles and Responsibilities

Small organisations often have one person in several roles. Roles may be combined, but each must be assigned, and a named deputy must exist. Avoid a single point of failure.

| Role | Assigned to | Deputy | Key responsibilities |
|---|---|---|---|
| **Executive Sponsor / Approver** | [[PLACEHOLDER]] | [[PLACEHOLDER]] | Owns the policy; approves resources, major decisions (e.g. ransom-related questions, public statements, regulator notifications); receives