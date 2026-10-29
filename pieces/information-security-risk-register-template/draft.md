# Risk Register Template for a Small UK Organisation

> **DRAFT – PENDING HUMAN REVIEW AND ORGANISATIONAL APPROVAL**
>
> This document is a portfolio draft and has not been formally adopted by an organisation. Organisation-specific placeholders must be completed, and the document must be reviewed against applicable legal, regulatory, contractual and security requirements before operational use.

---

## 1. Purpose and scope

This register records the main risks that could affect the organisation's objectives, how serious each is, who owns it, and what is being done about it.

- **Organisation:** [PLACEHOLDER: name]
- **Scope:** [PLACEHOLDER: whole organisation / project / site]
- **Register owner:** [PLACEHOLDER: role]
- **Approved by / date:** [PLACEHOLDER: board or director / date]
- **Review frequency:** [PLACEHOLDER: e.g. quarterly; high-rated risks monthly]
- **Version:** [PLACEHOLDER: v0.1]

## 2. Public frameworks referenced

Only freely available UK public guidance is used. Check that you are using the current version of each.

| Area | Public source |
|---|---|
| General risk concepts | HM Treasury *Orange Book* (Management of Risk in Government) |
| Cyber security | NCSC Small Business Guide; Cyber Essentials scheme |
| Personal data | ICO guidance on UK GDPR accountability and personal data breaches |
| Health and safety | HSE guidance on managing risks and risk assessment ("five steps") |
| Fraud | Action Fraud and NCSC guidance on phishing and payment fraud |
| Continuity | GOV.UK guidance on preparing for emergencies |
| Charities (if applicable) | Charity Commission guidance on managing risk and financial controls |

## 3. Register field definitions

| Field | What to enter |
|---|---|
| **ID** | Unique reference, e.g. R01 |
| **Category** | Strategic, Financial, Operational, Cyber/Data, Legal/Compliance, People/Safety, Reputation |
| **Description** | Cause → event → consequence, in one or two sentences |
| **Owner** | Named role accountable for managing the risk |
| **Inherent L / I / Score** | Likelihood × Impact with no controls, or ignoring current controls |
| **Existing controls** | What is already in place and working |
| **Residual L / I / Score** | Score taking existing controls into account |
| **Response** | Tolerate, Treat, Transfer or Terminate (see section 4.5) |
| **Further actions** | Specific actions, each with an owner and due date |
| **Target score** | Score you aim to reach after the actions |
| **Status** | Open, Monitoring, Closed, Escalated |
| **Last / next review** | Dates |

## 4. Scoring guidance

### 4.1 Likelihood (over the next [PLACEHOLDER: 12 months])

| Score | Descriptor | Guide |
|---|---|---|
| 1 | Rare | Not expected; would need unusual circumstances |
| 2 | Unlikely | Could happen, but no recent history |
| 3 | Possible | Has happened here or to similar organisations |
| 4 | Likely | Expected to happen at least once |
| 5 | Almost certain | Happening now or repeatedly |

### 4.2 Impact (use the highest-scoring column that applies)

| Score | Financial* | Operations | Legal / regulatory | People / safety | Reputation |
|---|---|---|---|---|---|
| 1 Minor | < [£___] | Disruption under 1 day | Minor internal breach | First aid only | Isolated complaint |
| 2 Moderate | [£___]–[£___] | 1–3 days disrupted | Advice or warning likely | Minor injury or short-term distress | Local or customer-level criticism |
| 3 Significant | [£___]–[£___] | Up to 1 week; key service reduced | Formal regulator enquiry | Over-7-day injury or significant harm | Negative media or sector attention |
| 4 Major | [£___]–[£___] | 1–4 weeks; key service lost | Enforcement action or fine likely | Serious injury or harm | Sustained loss of trust; lost clients or funders |
| 5 Severe | > [£___] | Over 4 weeks; viability threatened | Prosecution, major penalty or loss of licence | Fatality or life-changing harm | Lasting damage; survival at risk |

*\*Set financial thresholds relative to your turnover, reserves, or budget. [PLACEHOLDER: e.g. as percentages of annual income].*

### 4.3 Score matrix (Likelihood × Impact)

| L \ I | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **5** | 5 | 10 | 15 | 20 | 25 |
| **4** | 4 | 8 | 12 | 16 | 20 |
| **3** | 3 | 6 | 9 | 12 | 15 |
| **2** | 2 | 4 | 6 | 8 | 10 |
| **1** | 1 | 2 | 3 | 4 | 5 |

### 4.4 Rating bands and expected response

| Score | Rating | Expectation |
|---|---|---|
| 1–4 | Low | Tolerate; review annually |
| 5–9 | Moderate | Owner manages; review [PLACEHOLDER: quarterly] |
| 10–15 | High | Action plan required; report to [PLACEHOLDER: board/director]; review monthly |
| 16–25 | Very high | Immediate senior attention; interim controls within [PLACEHOLDER: days]; review at every meeting |

**Risk appetite:** [PLACEHOLDER: state the maximum acceptable residual score, overall or by category, e.g. none above 12 without board sign-off.]

### 4.5 Response options

- **Tolerate:** accept the risk, with the decision recorded.
- **Treat:** add or improve controls to reduce likelihood or impact.
- **Transfer:** share the risk, e.g. through insurance or contract terms.
- **Terminate:** stop or change the activity that creates the risk.

### 4.6 Scoring tips

- Score the risk as it is today, not as you hope it will be.
- Residual score should not be lower than inherent unless a control is genuinely in place and working.
- Where unsure, discuss the score with a second person and record the reasoning.
- Re-score after any incident, near miss, or significant change.

## 5. Blank register template

| ID | Category | Description | Owner | Inh. L | Inh. I | Inh. Score | Existing controls | Res. L | Res. I | Res. Score | Response | Further actions (owner, date) | Target | Status | Last / next review |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R__ | | | [Role] | | | | | | | | | | | | [Date] |

## 6. Ten example risks

*Illustrative only. Replace with risks specific to your organisation.*

### 6.1 Description and scoring

| ID | Category | Risk (cause → event → consequence) | Inh. L×I | Res. L×I | Rating (residual) |
|---|---|---|---|---|---|
| R01 | Cyber/Data | Phishing or unpatched systems → ransomware encrypts files → work stops and data may be lost or exposed | 4×5 = **20** | 3×4 = **12** | High |
| R02 | Legal/Data | Misdirected email or lost device → personal data breach → ICO reporting duty, harm to individuals, possible penalty | 3×4 = **12** | 2×4 = **8** | Moderate |
| R03 | People | Sole holder of key knowledge or relationships leaves or is absent → delivery delays and lost continuity | 4×3 = **12** | 3×3 = **9** | Moderate |
| R04 | Financial | Loss of largest client or funder, or late payment → cash shortfall → inability to meet commitments | 3×5 = **15** | 3×4 = **12** | High |
| R05 | Financial | Fraudulent email impersonating a supplier or director → payment to wrong account → financial loss | 3×4 = **12** | 2×3 = **6** | Moderate |
| R06 | People/Safety | Inadequate risk assessment or maintenance → serious workplace accident → injury, HSE action, claims | 2×5 = **10** | 1×5 = **5** | Moderate |
| R07 | Operational | Key supplier or cloud service fails → service interruption → missed deadlines or service levels | 3×3 = **9** | 2×3 = **6** | Moderate |
| R08 | Legal/Compliance | Missed filing, tax, licensing or sector-regulator deadline → penalties and loss of standing | 2×4 = **8** | 1×4 = **4** | Low |
| R09 | Operational | Fire, flood, or prolonged power or network outage at premises → site unusable → service disruption | 2×4 = **8** | 2×3 = **6** | Moderate |
| R10 | Reputation | Poorly handled complaint or adverse social media post → loss of trust → reduced income or referrals | 3×3 = **9** | 2×3 = **6** | Moderate |

### 6.2 Controls, ownership and actions

| ID | Owner | Existing controls | Response | Further actions | Target |
|---|---|---|---|---|---|
| R01 | [Role: IT lead / director] | Anti-malware; automatic updates; multi-factor authentication on email; staff phishing awareness | Treat | Work towards Cyber Essentials certification; test restoring from offline backups; write an incident response plan. [Due: date] | 8 |
| R02 | [Role: data protection lead] | Data protection policy; encrypted laptops; staff induction on data handling | Treat | Create a breach log and 72-hour reporting procedure; review the ICO registration (fee) position; annual refresher training. [Due: date] | 4 |
| R03 | [Role: director] | Informal handovers; shared drive | Treat | Document key processes; identify and train deputies; review notice periods and succession plans. [Due: date] | 6 |
| R04 | [Role: finance lead] | Monthly management accounts; 12-month budget | Treat / Transfer | Build a 13-week cash-flow forecast; set a client or funder concentration limit; agree reserves target of [PLACEHOLDER: months]; consider credit insurance. [Due: date] | 8 |
| R05 | [Role: finance lead] | Bank dual authorisation above [£___] | Treat | Add a call-back check on any change of bank details; run fraud awareness briefings; limit who can add payees. [Due: date] | 4 |
| R06 | [Role: H&S lead] | Written risk assessments; accident book; first aiders | Treat | Review assessments annually and after changes; check employer's liability insurance certificate is current; record inspections. [Due: date] | 5 |
| R07 | [Role: operations lead] | Contracts in place; supplier contact list | Treat / Transfer | List critical suppliers; check service terms and exit options; identify alternatives; keep local copies of key data. [Due: date] | 4 |
| R08 | [Role: company secretary / finance lead] | Compliance calendar | Tolerate / Monitor | Assign named owners for each deadline; set reminders 30 days ahead. [Due: date] | 4 |
| R09 | [Role: premises / operations lead] | Buildings and contents insurance; fire risk assessment | Treat / Transfer | Write a short continuity plan; set up remote-working capability; test a call-out list; review business interruption cover. [Due: date] | 4 |
| R10 | [Role: communications lead] | Complaints procedure | Treat | Set response-time targets; draft a holding-statement template; assign social media monitoring and escalation. [Due: date] | 4 |

## 7. Using and maintaining the register

1. **Identify:** use team input, incident logs, audit findings, and a review of the public guidance above.
2. **Score:** assess inherent risk, list the controls, then score residual risk.
3. **Decide:** choose a response and record any risk accepted above appetite.
4. **Act:** give every action an owner and date, and track completion.
5. **Review:** update at the agreed frequency and after incidents, then report High and Very high risks to [PLACEHOLDER: board/director] with trends since the last review.

## 8. Placeholder checklist for the reviewer

- [ ] Organisation details, scope, version, approval
- [ ] Financial impact thresholds
- [ ] Likelihood time horizon
- [ ] Risk appetite statement
- [ ] Review frequency and escalation timescales
- [ ] Owners, dates, and cost or reserves figures
- [ ] Risk list tailored to your sector, legal form (e.g. charity, company, CIC), and regulators
- [ ] Confirmation that the referenced guidance is current and legal obligations are met, with professional advice where needed
