# Access Control Policy

**DRAFT – PENDING HUMAN REVIEW AND ORGANISATIONAL APPROVAL**

> **Notice:** This is a draft template. It has not been approved, adopted, certified or accredited by any organisation. It does not claim compliance with, or certification to, any standard or scheme. All text marked **[[PLACEHOLDER]]** must be completed or confirmed. Suggested values are starting points only. Qualified people within the organisation must review the draft, adapt it to actual systems and risks, and obtain formal approval before operational use. Legal, HR and data protection advice should be sought where needed.

## Document Control

| Item | Detail |
|---|---|
| Organisation | [[PLACEHOLDER: organisation name]] |
| Document owner | [[PLACEHOLDER: role/title]] |
| Approver | [[PLACEHOLDER: role/title, e.g. director or board]] |
| Version / status | 0.1 – Draft |
| Approval date | [[PLACEHOLDER: to be completed only after formal approval]] |
| Next review date | [[PLACEHOLDER: suggested at least every 12 months]] |
| Related documents | [[PLACEHOLDER: information security policy, acceptable use policy, HR procedures, incident response plan, supplier policy]] |

## 1. Purpose and Scope

**Purpose:** To ensure that access to information, systems and facilities is granted only to authorised people, only as needed, and is monitored and removed when no longer required.

**Scope:** This policy applies to:
- All employees, directors, contractors, volunteers, temporary staff and third parties who access [[PLACEHOLDER: organisation name]] systems or data.
- All organisation-owned and personally owned ("BYOD") devices, if permitted ([[PLACEHOLDER: BYOD permitted? Y/N]]).
- Systems in scope: [[PLACEHOLDER: e.g. Microsoft 365/Google Workspace, finance software, CRM, file storage, network devices, cloud platforms, line-of-business apps]].
- Physical access is covered in [[PLACEHOLDER: physical security policy / or add section]].

## 2. Roles and Responsibilities

| Role | Responsibilities |
|---|---|
| Senior management | Approves the policy, resources it, and accepts residual risk and exceptions. |
| Policy owner | Maintains the policy, tracks exceptions, and coordinates reviews. |
| IT administrator / provider | Implements technical controls, creates and removes accounts, maintains logs. [[PLACEHOLDER: internal role or managed service provider]] |
| Line managers | Request access for their team, confirm it is appropriate, and report role changes and leavers promptly. |
| System/data owners | Decide who may access their system or data and take part in access reviews. |
| HR / People lead | Notifies IT of joiners, movers and leavers. [[PLACEHOLDER: role]] |
| All users | Protect credentials, use only the access they are given, and report suspected compromise immediately. |

## 3. Core Principles

- **Least privilege:** Users receive the minimum access needed for their current role.
- **Need to know:** Access to sensitive data ([[PLACEHOLDER: e.g. personal data, financial, HR, client confidential]]) is restricted to those with a defined business need.
- **Default deny:** Access is not available unless explicitly granted.
- **Individual accountability:** Each account is attributable to one person or one documented service.
- **Role-based access:** Where practicable, access is assigned through defined roles or groups rather than ad hoc individual permissions.
- **Separation of duties:** Where practicable, one person should not both request and approve their own access, or control a critical process end to end.

## 4. User Access Management

1. **Request:** Access requests must be made in writing (e.g. [[PLACEHOLDER: ticketing system/email/form]]), stating the person, system, access level and business reason.
2. **Approval:** Requests must be approved by the line manager and, for sensitive systems, the system/data owner. Nobody may approve their own request.
3. **Provisioning:** IT creates unique named accounts and applies standard role-based access where possible.
4. **Records:** A register of accounts and access rights is maintained ([[PLACEHOLDER: location/tool]]), including owner, system, privilege level and approval evidence.
5. **Account types:** Standard user, privileged/administrator, service/system, shared (see section 10), and third-party/guest accounts. Each must be identifiable by type.
6. **Default and unused accounts:** Default credentials must be changed or the accounts disabled. Accounts unused for [[PLACEHOLDER: suggested 60–90 days]] must be reviewed and disabled if not needed.
7. **Data access:** Permissions on file shares, cloud storage and applications should be granted to groups, not to individuals, where practicable. Organisation-wide or public sharing links require [[PLACEHOLDER: approval requirement]].

## 5. Joiners, Movers and Leavers

| Stage | Requirement | Timing |
|---|---|---|
| **Joiner** | HR/manager submits an access request based on role. Accounts are created only after employment or engagement is confirmed. Users must accept the acceptable use policy and complete [[PLACEHOLDER: induction/security awareness]] before or soon after receiving access. | Request at least [[PLACEHOLDER: e.g. 3 working days]] before start date |
| **Mover** | Manager and HR notify IT of the role change. Access no longer needed is removed, and new access is approved as for a joiner. Access must not simply accumulate. | Within [[PLACEHOLDER: e.g. 5 working days]] of change |
| **Leaver** | Accounts are disabled on the last working day (immediately for involuntary or high-risk departures). Active sessions and tokens are revoked, and MFA devices, remote access, and shared credentials known to the leaver are removed or reset. Devices, keys and tokens are recovered. Mailbox and data ownership are transferred as needed. | Disable by end of last working day; delete after [[PLACEHOLDER: retention period]] |

Contractors, temporary staff and volunteers follow the same process, and their accounts must have an end date set where technically possible.

## 6. Privileged Accounts

- Privileged access (e.g. administrator, root, global admin, database admin, domain admin) must be formally approved by [[PLACEHOLDER: role]] and recorded in the register.
- Administrators must use **separate administrative accounts** for administrative tasks and a standard account for email, web browsing and daily work.
- Privileged accounts must not be used to read email or browse the internet.
- MFA is mandatory for all privileged accounts (see section 8).
- The number of privileged accounts must be kept to the minimum necessary. Time-limited or just-in-time elevation should be used where available.
- Privileged activity must be logged and reviewed (see section 14).
- Emergency ("break glass") accounts, if used, must have long unique passwords stored securely offline or in a controlled vault, be excluded from routine use, and have any use reported and reviewed. [[PLACEHOLDER: confirm if applicable]]
- Privileged access is reviewed at least [[PLACEHOLDER: suggested quarterly]] and removed immediately when no longer needed.
- Vendor and super-admin accounts for cloud tenants must be owned by named individuals, not left on a single person's personal credentials without a recovery plan.

## 7. Authentication

- Every user must authenticate with a unique identity before accessing organisational systems and data.
- Authentication methods must be proportionate to the sensitivity of the system and the risk of exposure (internet-facing, remote or privileged access requires stronger methods).
- Devices must be locked with a PIN, password or biometric and set to auto-lock after [[PLACEHOLDER: suggested ≤ 10 minutes]] of inactivity.
- Systems should apply protection against brute-force attacks, such as throttling, lockout or limiting login attempts (e.g. no more than [[PLACEHOLDER: suggested 10]] guesses in 5 minutes), configured so that lockout cannot easily be used for denial of service.
- Single sign-on (SSO) should be used where available to reduce the number of credentials to manage. [[PLACEHOLDER: identity provider]]
- Legacy or basic authentication protocols that cannot support MFA should be disabled where possible.
- Service accounts must not be used for interactive login, must use strong unique secrets, and must have a named owner.

## 8. Multi-Factor Authentication (MFA)

MFA must be enabled for:

| Scope | Requirement |
|---|---|
| All privileged/administrator accounts | Mandatory |
| All remote access (VPN, remote desktop, virtual desktop) | Mandatory |
| All cloud services and email accessed over the internet | Mandatory wherever the service supports it |
| Access to systems holding sensitive or personal data | Mandatory [[PLACEHOLDER: confirm list]] |
| Third-party and guest accounts | Mandatory where technically possible |

- Preferred methods, in order of resilience: phishing-resistant methods (e.g. FIDO2 security keys, passkeys), authenticator apps, then push or one-time codes. SMS codes should be used only if no better option exists. [[PLACEHOLDER: approved methods]]
- Users must report lost or stolen MFA devices immediately. IT must verify identity before resetting or re-enrolling MFA.
- Users should be trained to refuse unexpected MFA prompts and report them (MFA fatigue attacks).
- Backup/recovery codes must be stored securely.
- Where MFA is not available, a compensating control (e.g. a longer password, access restrictions) must be documented as an exception (section 15).

## 9. Password Management

Based on NCSC guidance, the organisation prefers **length and usability over complexity rules and forced periodic changes**.

- **Minimum length:** [[PLACEHOLDER: suggested at least 12 characters; if length is lower, additional technical controls such as a blocklist of common passwords must be in place]]. No arbitrary maximum length should be imposed (a sensible technical limit may apply).
- **Passphrases:** Users are encouraged to use three or more random words.
- **Blocklist:** Common, breached or easily guessable passwords (e.g. "password", organisation name, keyboard patterns) must be blocked where the system allows.
- **Uniqueness:** Passwords must never be reused across work and personal accounts, or across different systems.
- **Changes:** Passwords are changed on suspicion or evidence of compromise, not on a fixed schedule, except where a system or contract requires it. Default passwords must be changed before first use.
- **Storage:** Passwords must not be written down in insecure places, shared by email or chat, or stored in unprotected files. Approved password managers ([[PLACEHOLDER: product/approved tool]]) should be used. The password manager master credential must be strong and protected with MFA.
- **Systems:** Passwords must be stored by systems only in salted, hashed form (for systems the organisation controls).
- **Compromise:** Suspected compromised credentials must be reported to [[PLACEHOLDER: contact/helpdesk]] immediately, and the password reset and sessions revoked.

## 10. Shared, Generic and Service Accounts

- Shared accounts are **prohibited by default**, because they remove individual accountability.
- Exceptions are allowed only where there is no practicable alternative (e.g. a social media account, a legacy system, a shared mailbox). Each must have:
  - a named owner and a documented business justification;
  - an approval recorded under section 15;
  - credentials in an approved password manager or vault with access limited to named individuals;
  - MFA where possible, ideally tied to a named person or a controlled device;
  - a password reset when any authorised member leaves or changes role;
  - logging that enables attribution of actions to individuals where possible.
- Shared mailboxes and functional inboxes should use delegated access to named users and not direct shared logins.
- Service and application accounts must be inventoried, have an owner, use the minimum privileges, and be reviewed with other access.

## 11. Access Reviews

| Review type | Scope | Frequency | Reviewer |
|---|---|---|---|
| Privileged access | All admin and elevated accounts | [[PLACEHOLDER: suggested quarterly]] | Policy owner / senior management |
| User access to sensitive systems | Access to finance, HR, client data, etc. | [[PLACEHOLDER: suggested every 6 months]] | System/data owner |
| General user access | All accounts and group memberships | [[PLACEHOLDER: suggested at least annually]] | Line managers with IT |
| Third-party and guest accounts | External users and suppliers | [[PLACEHOLDER: suggested quarterly]] | Relationship owner |
| Dormant accounts | Unused accounts | [[PLACEHOLDER: suggested monthly]] | IT |

- Reviewers must confirm that each access right is still required, appropriate and approved. Reviewers must not approve their own access.
- Excess access must be removed within [[PLACEHOLDER: suggested 5 working days]] of identification.
- Review evidence (date, reviewer, findings, actions) must be retained for [[PLACEHOLDER: retention period]].

## 12. Remote Access

- Remote access to internal resources is permitted only through approved methods ([[PLACEHOLDER: e.g. VPN, zero-trust access, virtual desktop, cloud services with conditional access]]).
- MFA is required for all remote access.
- Remote access is limited to devices that meet the organisation's security baseline: supported operating system, up-to-date patches, active malware protection, firewall enabled, disk encryption where feasible [[PLACEHOLDER: confirm baseline]].
- Personally owned devices may access organisational data only if [[PLACEHOLDER: BYOD conditions, or "not permitted"]].
- Management interfaces (e.g. RDP, SSH, router/firewall admin) must not be exposed directly to the internet without a documented business need, strong authentication and additional restrictions (IP allow-listing, VPN).
- Users must not use public or untrusted networks for sensitive work without a protected connection, and must prevent shoulder-surfing and unauthorised viewing.
- Sessions should time out after [[PLACEHOLDER: suggested inactivity period]].
- Lost or stolen devices must be reported immediately so access can be revoked and remote wipe applied where available.

## 13. Third-Party Access

- Third-party access (suppliers, contractors, IT providers, auditors, partners) requires a business sponsor, a documented purpose, and approval from [[PLACEHOLDER: role]].
- Contracts or agreements must address confidentiality, security expectations, incident notification, and return or deletion of data. [[PLACEHOLDER: link to supplier policy/contract templates]]
- Third parties must receive **named individual accounts**, with least-privilege and time-limited access. They must not share credentials.
- MFA is required, and access must be through approved, monitored methods.
- Access is enabled only for the time needed (e.g. enabled for a support session and then disabled), and has a defined expiry date.
- Third-party activity on sensitive or privileged systems must be logged and, where appropriate, supervised.
- Managed service providers with privileged access must be listed in the register. Their staff changes must be notified to the organisation.
- Third-party access is reviewed under section 11 and revoked at contract end.

## 14. Logging and Monitoring

- The following events must be logged where systems support it: successful and failed logins, MFA failures or changes, account creation, modification, disablement and deletion, privilege or group changes, privileged activity, remote access, password resets, and access to sensitive data. [[PLACEHOLDER: confirm per-system scope]]
- Logs must include sufficient detail (user, time, source, action, outcome) and use synchronised time sources.
- Logs must be protected from unauthorised alteration and deletion, and administrators should not be able to silently alter their own audit trail.
- Retention period: [[PLACEHOLDER: suggested minimum 6–12 months, subject to legal and business needs]].
- Alerts should be configured for high-risk events such as repeated failed logins, new admin accounts, MFA disablement, impossible-travel sign-ins and access outside normal patterns. [[PLACEHOLDER: tool/alert owner]]
- Logs are reviewed [[PLACEHOLDER: frequency, e.g. weekly for privileged activity]] by [[PLACEHOLDER: role]]. Suspicious events are handled under the incident response process ([[PLACEHOLDER: reference]]).
- Monitoring must be proportionate and consistent with privacy and employment law, and staff must be informed of it ([[PLACEHOLDER: privacy notice/ acceptable use policy reference]]).

## 15. Exceptions

- Exceptions to this policy must be requested in writing, with justification, risk assessment, compensating controls, duration and an owner.
- Exceptions must be approved by [[PLACEHOLDER: role, e.g. senior management]] and recorded in an exceptions register ([[PLACEHOLDER: location]]).
- Exceptions must be time-limited (suggested maximum [[PLACEHOLDER: e.g. 12 months]]) and reviewed at expiry or when circumstances change.
- No exception may be made for sharing privileged credentials or removing logging from privileged activity unless explicitly accepted at senior level with documented compensating controls.

## 16. Non-Compliance

Suspected breaches of this policy must be reported to [[PLACEHOLDER: contact]]. Breaches may lead to access being suspended and may be handled under [[PLACEHOLDER: disciplinary/contractual process]]. Possible personal data incidents must be escalated immediately to [[PLACEHOLDER: data protection lead/DPO]] for assessment under UK data protection law.

## 17. Periodic Review and Maintenance

- The policy owner reviews this policy at least [[PLACEHOLDER: annually]], and after significant incidents, major system or supplier changes, organisational changes, or material changes to relevant guidance or legal requirements.
- Reviews should consider access review findings, incidents, exception trends, audit logs, and updates to NCSC, Cyber Essentials, ISO/IEC 27001 and CIS publications.
- Changes require re-approval. Version history is recorded in the document control section.
- Staff are informed of the policy and material changes, and receive awareness training on access, passwords and MFA at induction and [[PLACEHOLDER: e.g. annually]].

## 18. Reference Frameworks (Informational Only)

This policy was drafted with reference to the following public sources for general alignment of concepts. Use of these references does not mean that the organisation complies with, is certified to, or is assessed against any of them. Current versions should be checked before use.

| Source | Relevant concepts used |
|---|---|
| UK NCSC guidance (e.g. password guidance, MFA guidance, 10 Steps to Cyber Security, device and remote working guidance) | Password length/usability, MFA, privileged access management, monitoring, secure remote working |
| Cyber Essentials (NCSC) requirements | User access control, admin account separation, MFA for cloud services, removal of unused accounts, secure configuration, password and brute-force protections |
| ISO/IEC 27001 / 27002 concepts | Access control policy, identity management, access rights provisioning and review, privileged access, secure authentication, logging, supplier access |
| CIS Critical Security Controls (v8 or later) | Account management, access control management, audit log management, MFA, service account inventory |

## 19. Items for Human Review Before Approval

- [ ] All **[[PLACEHOLDER]]** items completed or removed.
- [ ] Systems inventory and account register established.
- [ ] Technical feasibility confirmed (MFA, logging, lockout, conditional access) with IT or the provider.
- [ ] HR, legal and data protection input obtained (monitoring, leaver processes, employment terms).
- [ ] Roles assigned and communicated.
- [ ] Alignment checked with related policies and supplier contracts.
- [ ] Current versions of referenced frameworks checked.
- [ ] Formal approval recorded by the authorised approver; communication and training plan agreed.

| Approval record | |
|---|---|
| Reviewed by | [[PLACEHOLDER: name, role, date]] |
| Approved by | [[PLACEHOLDER: name, role, date – complete only upon formal approval]] |
| Effective date | [[PLACEHOLDER]] |