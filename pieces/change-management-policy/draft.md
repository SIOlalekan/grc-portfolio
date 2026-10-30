**DRAFT – PENDING HUMAN REVIEW AND ORGANISATIONAL APPROVAL**

# Change Management Policy

*This draft has not been approved or adopted by any organisation. It is a starting template and must be reviewed, tailored and formally approved by [[PLACEHOLDER: approving body/role]] before use. Text marked [[PLACEHOLDER]] must be completed or deleted. Legal, data protection and technical advice should be taken where needed.*

---

## 1. Document Control

| Item | Detail |
|---|---|
| Organisation | [[PLACEHOLDER: organisation name]] |
| Document owner | [[PLACEHOLDER: role, e.g. IT Manager / Director]] |
| Version / status | 0.1 – Draft, not approved |
| Approval | [[PLACEHOLDER: approver name, role, date – to be completed only after formal approval]] |
| Next review date | [[PLACEHOLDER: e.g. 12 months after approval, or after major incident or organisational change]] |
| Related documents | [[PLACEHOLDER: Information Security Policy, Incident Management, Backup, Access Control, Supplier Management, Risk Register, Data Protection Policy]] |

## 2. Purpose

This policy sets out how changes to [[PLACEHOLDER: organisation name]]'s information systems and services are requested, assessed, approved, tested, implemented, reviewed and recorded. It aims to reduce disruption and security incidents and to protect the confidentiality, integrity and availability of information.

## 3. Scope

**In scope:** changes to the following, whether in-house, cloud-hosted or supplier-managed:
- Hardware, network devices, servers, endpoints and mobile devices
- Operating systems, applications, databases and configurations
- Cloud and SaaS settings, including identity and access configuration
- Firewall rules, security tooling, backups and email/domain settings
- Software releases and scripts
- Supplier or hosting changes that affect the organisation
- Significant changes to supporting processes (e.g. a new onboarding workflow) where they affect systems or data

**Out of scope:** [[PLACEHOLDER: e.g. routine user password resets, content updates on non-critical systems, or other activities already covered by a documented procedure]].

This policy applies to employees, contractors and suppliers making changes to in-scope systems.

## 4. Definitions

| Term | Meaning |
|---|---|
| Change | Any addition, modification or removal that could affect services, systems, security or data |
| Standard change | Low-risk, repeatable change following a pre-approved procedure (e.g. [[PLACEHOLDER: routine OS patching, new-starter account creation]]) |
| Normal change | Any change that is not standard or emergency; assessed and approved before implementation |
| Emergency change | Urgent change needed to resolve or prevent a major incident or serious security threat, where the normal process would cause unacceptable delay |
| Change owner | The person accountable for the change request from submission to closure |
| Approver | The person or group authorised to approve a change at a given risk level |
| Rollback | Restoring the previous known-good state if a change fails |

## 5. Roles and Responsibilities

In a small organisation one person may hold more than one role, subject to Section 11 (Segregation of Duties).

| Role | Responsibilities |
|---|---|
| Management / [[PLACEHOLDER: Director]] | Owns this policy, provides resources, approves high-risk changes and exceptions |
| Change Manager [[PLACEHOLDER: name/role]] | Maintains the change log, checks completeness, coordinates the schedule, and convenes approvers |
| Change Owner | Submits the request, completes the risk assessment, and ensures testing, implementation and review |
| Implementer | Carries out the approved change as planned and records the outcome |
| Approver(s) | Assess risk and benefit and approve, reject or defer |
| Reviewer / Tester | Independently verifies testing and results where required |
| Security / Data Protection Lead [[PLACEHOLDER]] | Advises on security and personal data impacts |
| Suppliers | Follow this policy, or an agreed equivalent, for changes affecting the organisation |

## 6. Change Requests

- All non-standard changes must be submitted through [[PLACEHOLDER: ticketing system / form / shared log]]. Verbal requests are not sufficient.
- Each request must include the minimum fields in Appendix A.
- The Change Manager checks completeness within [[PLACEHOLDER: e.g. 2 working days]] and returns incomplete requests.
- Standard changes require an approved procedure listed in the standard change catalogue [[PLACEHOLDER: location]]. They are logged but do not need individual approval. The catalogue is reviewed at least [[PLACEHOLDER: annually]].
- Changes must not be made outside this process, except as allowed under Section 12.

## 7. Risk Assessment and Classification

The change owner assesses **impact** and **likelihood of failure** before approval, considering:
- Systems, users, data and services affected
- Personal or sensitive data involved
- Security controls affected
- Dependencies and suppliers
- Availability of a tested rollback
- Timing, such as a busy business period or limited staff cover
- Previous similar changes

| | Likelihood Low | Likelihood Medium | Likelihood High |
|---|---|---|---|
| **Impact High** | Medium | High | High |
| **Impact Medium** | Low | Medium | High |
| **Impact Low** | Low | Low | Medium |

Impact guide: **Low** is a few users, non-critical, and easily reversed. **Medium** is a team or non-critical service, or limited data exposure risk. **High** is organisation-wide or critical service, significant data or security exposure, or hard to reverse.

Significant risks identified are recorded in [[PLACEHOLDER: risk register]], with a plan to mitigate or accept them.

## 8. Approvals

| Risk level | Minimum approval | Additional requirements |
|---|---|---|
| Standard | Pre-approved via catalogue | Logged |
| Low | [[PLACEHOLDER: IT Manager or delegate]] | Independent check where feasible |
| Medium | [[PLACEHOLDER: IT Manager + business/system owner]] | Security review (Section 10) |
| High | [[PLACEHOLDER: Director + IT Manager + system owner]] | Security review, tested rollback, and a communication plan |

- Approval must be recorded in the change record before implementation, with name, date and any conditions.
- Approvers must not approve their own change (see Section 11).
- Approval lapses if the scope or timing materially changes, or if the change is not implemented within [[PLACEHOLDER: e.g. 30 days]]. It must then be reconfirmed.
- Rejected or deferred changes are recorded with reasons.

## 9. Testing

- Changes are tested before production in a test or staging environment, or by another method suited to the change, such as a pilot group or a vendor-supported preview.
- The test plan covers expected function, security-relevant behaviour (e.g. access and logging), and the rollback procedure for medium and high-risk changes.
- Test data should not contain live personal data unless necessary, authorised and protected [[PLACEHOLDER: align with Data Protection Policy]].
- Results, tester and any defects are recorded. Unresolved defects need documented acceptance by an approver.
- Where testing is not feasible, this must be stated in the request and the risk accepted by the approver.

## 10. Security Review

Medium and high-risk changes, and any change affecting the following, require a documented security review by [[PLACEHOLDER: Security Lead/role]]:
- Authentication, access rights or privileged accounts
- Network boundaries, remote access or firewall rules
- Encryption, logging, monitoring or backup configuration
- Personal or special category data
- New suppliers, software or cloud services

The review considers:
- Vulnerabilities and supplier support status
- Least privilege and secure configuration
- Impact on logging and monitoring
- Supplier due diligence
- Whether a Data Protection Impact Assessment is needed under UK GDPR
- Whether ICO or customer notification obligations could arise if the change fails

Changes that weaken security controls require explicit approval from [[PLACEHOLDER: senior role]], and compensating controls must be recorded.

## 11. Segregation of Duties

- The person who requests or implements a change should not be the sole approver of it.
- Where practicable, the implementer and the tester or reviewer should be different people.
- Changes to privileged access, security controls and financial systems must have independent approval.
- Where staffing makes separation impossible, compensating controls must be used and recorded. Examples are review by a director, an external IT provider or another independent party; after-the-fact log review within [[PLACEHOLDER: e.g. 5 working days]]; and system-generated audit trails.
- Supplier administrators must not approve their own changes to the organisation's systems.

## 12. Emergency Changes

- Emergency changes are limited to resolving or preventing a major incident or serious security threat, such as active exploitation of a vulnerability.
- Approval is given verbally or electronically by [[PLACEHOLDER: Emergency Approver and named deputy]] and recorded as soon as practicable.
- A minimum risk check is made before implementation, covering what could go wrong and how to roll back.
- A full change record must be completed within [[PLACEHOLDER: e.g. 2 working days]] of implementation.
- Every emergency change receives a post-implementation review (Section 15). Emergency changes are monitored for misuse, and repeated use triggers a process review.
- Where the emergency is also a security incident or personal data breach, follow [[PLACEHOLDER: Incident Response Procedure]].

## 13. Implementation

- Changes are scheduled to minimise disruption, and avoid [[PLACEHOLDER: peak periods, e.g. month-end]] unless justified.
- Before implementation, confirm approval, a current backup or recovery point where relevant, a rollback plan and the availability of required staff.
- Affected users and stakeholders are told in advance of planned disruption through [[PLACEHOLDER: channel]].
- Implementers follow the approved plan. Deviations are recorded and, if material, referred back to the approver.
- Changes are verified after implementation against agreed success criteria.
- Changes to access rights are made using named accounts, not shared accounts.
- The change is closed only when verification is complete and documentation is updated.

## 14. Rollback

- Every non-standard change has a documented rollback plan covering triggers, steps, responsible person, estimated time and data considerations.
- The rollback decision-maker and failure criteria, such as time limit or failed checks, are set before implementation.
- For high-risk changes, the rollback is tested where feasible.
- Where rollback is not possible, such as irreversible data migrations, this must be stated, with alternative recovery measures approved by the approver.
- Invoked rollbacks are recorded as failed or partially failed changes and reviewed.

## 15. Post-Implementation Review

| Change type | Review requirement |
|---|---|
| Standard | Periodic sample review [[PLACEHOLDER: e.g. quarterly]] |
| Low / Medium | Outcome check within [[PLACEHOLDER: e.g. 5 working days]] |
| High, emergency, failed or rolled back | Formal review within [[PLACEHOLDER: e.g. 10 working days]] |

Reviews confirm whether objectives were met, whether unplanned impact or security issues occurred, whether documentation and asset records were updated, and what lessons or process improvements follow. Actions are assigned and tracked to completion.

## 16. Documentation

Where affected, the following are updated on completion of the change:
- Asset and configuration records [[PLACEHOLDER: location]]
- Network diagrams and system documentation
- Access control lists and user guidance
- Backup and recovery documentation
- Standard change catalogue
- Risk register and supplier records

## 17. Record Keeping

Change records include the request, risk assessment, approvals, test results, security review, implementation notes, rollback details, post-implementation review and closure. Records must be accurate, protected against unauthorised alteration and retrievable for audit or investigation.

| Record | Retention period |
|---|---|
| Change records and approvals | [[PLACEHOLDER: e.g. X years]] |
| Test evidence and security reviews | [[PLACEHOLDER]] |
| Emergency change records | [[PLACEHOLDER]] |
| System audit logs relating to changes | [[PLACEHOLDER]] |

Retention periods should reflect legal, contractual and operational needs, and should avoid keeping personal data longer than necessary under UK GDPR. Confirm with [[PLACEHOLDER: legal/DPO adviser]].

## 18. Monitoring, Exceptions and Non-Compliance

- The Change Manager reports to management [[PLACEHOLDER: e.g. quarterly]] on indicators such as the number of changes by type, failed or rolled-back changes, emergency changes, unauthorised changes and overdue reviews.
- Unauthorised changes are treated as security events and investigated under [[PLACEHOLDER: Incident Procedure]].
- Exceptions to this policy must be requested in writing, risk-assessed, approved by [[PLACEHOLDER: role]], time-limited and recorded.
- Breaches may lead to action under [[PLACEHOLDER: disciplinary/contractual process]].

## 19. Policy Review

This policy is reviewed at the interval stated in Section 1, and after significant incidents, system changes or regulatory changes. Updates require re-approval by [[PLACEHOLDER: approving body/role]].

## 20. Informative Framework References

These public frameworks informed the structure of this draft. Use of them does not imply conformity, certification or compliance:
- ISO/IEC 27001 / 27002 (change management and related controls) – published standards, consulted by name only
- ITIL 4 *Change Enablement* practice (concepts of standard, normal and emergency changes)
- NCSC (UK) guidance on secure system management and Cyber Essentials requirements
- UK GDPR and Data Protection Act 2018; ICO guidance on DPIAs and security
- NIST SP 800-128 (security-focused configuration management)

## 21. Review and Approval Record

*To be completed only after human review and formal organisational approval. Until then this document remains a draft.*

| Reviewed by | Role | Date | Comments |
|---|---|---|---|
| [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |

| Approved by | Role | Date | Signature / evidence |
|---|---|---|---|
| [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] | [[PLACEHOLDER]] |

---

## Appendix A – Minimum Change Request Fields

| Field | Content |
|---|---|
| Reference / date | Unique ID, date submitted |
| Requester / change owner | Names and roles |
| Description and reason | What is changing and why |
| Systems and data affected | Including personal data, suppliers and users |
| Change type | Standard / Normal / Emergency |
| Risk rating | Impact, likelihood, overall, with notes |
| Security review needed? | Yes/No, with outcome and reviewer |
| Test plan and results | Summary and evidence location |
| Implementation plan | Steps, date/time, implementer, communications |
| Rollback plan | Triggers, steps, owner |
| Approvals | Name, role, decision, date, conditions |
| Outcome | Successful / partial / failed / rolled back |
| Post-implementation review | Date, findings, actions |
| Documentation updated | Yes/No, with references |

**DRAFT – PENDING HUMAN REVIEW AND ORGANISATIONAL APPROVAL**