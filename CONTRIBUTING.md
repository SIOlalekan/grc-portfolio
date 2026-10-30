# Contributing to TrustReady GRC

Thank you for your interest in reviewing or contributing to TrustReady GRC.

TrustReady is a practical Governance, Risk and Compliance project focused on translating regulatory and cybersecurity requirements into structured controls, assessments, evidence requirements and increasingly automated compliance processes.

Professional review, constructive criticism and practical contributions are welcome.

## Ways to Contribute

You can contribute by:

- reviewing the control library;
- identifying incorrect or unclear control requirements;
- suggesting improvements to UK GDPR or Cyber Essentials mappings;
- reviewing evidence requirements;
- identifying missing governance or security controls;
- testing the assessment engine;
- reporting technical problems;
- suggesting improvements to scoring or risk logic;
- reviewing GRC artefacts and templates;
- proposing additional framework mappings;
- improving documentation; or
- contributing code or automated checks.

## Reporting an Issue

If you identify a problem, please open a GitHub Issue.

When possible, include:

- the relevant control ID or file;
- the problem you identified;
- why you believe it should be changed;
- the framework, regulation or recognised practice supporting your recommendation;
- your suggested improvement; and
- any supporting reference.

Example:

```text
Control: TR-CE-004

Issue:
The MFA evidence requirement could more clearly distinguish between
general user accounts and privileged/cloud-service accounts.

Suggested improvement:
Clarify the expected MFA evidence and identify where stronger
authentication requirements apply.
```

## Reviewing Control Mappings

Cross-framework mappings are intended to identify practical relationships between controls and evidence.

They do not claim that one framework automatically provides compliance or certification against another framework.

When reviewing a mapping, please consider:

- whether the relationship is accurate;
- whether it is too broad;
- whether relevant controls are missing;
- whether the supporting rationale is clear; and
- whether the proposed evidence is appropriate.

## Reviewing GRC Artefacts

The `pieces/` directory contains practical governance, risk and compliance artefacts.

Reviewers are encouraged to consider:

- clarity;
- completeness;
- usability;
- regulatory alignment;
- implementation practicality;
- evidence expectations; and
- suitability for SMEs and mission-led organisations.

Please avoid including confidential organisational information or personal data in issues or contributions.

## Code Contributions

For code changes:

1. Fork the repository.
2. Create a separate branch.
3. Make and test your changes.
4. Confirm the TrustReady GRC validation workflow passes.
5. Submit a Pull Request explaining the change and its purpose.

Where applicable, include testing evidence.

## Pull Request Guidance

A Pull Request should explain:

- what was changed;
- why the change is needed;
- which controls or components are affected;
- how the change was tested; and
- any relevant framework or regulatory references.

## Constructive Review

TrustReady is intended to improve through genuine professional scrutiny.

Critical feedback is welcome when it is:

- specific;
- evidence-based;
- constructive; and
- relevant to governance, risk, compliance, cybersecurity or digital trust.

The purpose of review is not simply to approve the project, but to identify weaknesses and improve the quality of the framework.

## Validation

Changes to relevant project components are automatically checked through the TrustReady GRC GitHub Actions validation workflow.

The workflow currently validates areas including:

- required repository components;
- Python syntax;
- control-library structure;
- duplicate control IDs;
- control severity values;
- evidence requirements;
- cross-framework mappings;
- GRC artefact presence; and
- assessment scoring logic.

Contributors should ensure validation passes before a change is considered complete.

## Professional and Academic Review

Cybersecurity, privacy, GRC, digital trust, audit, risk, compliance and academic professionals are particularly encouraged to review the project.

Independent observations, practical testing and evidence-based recommendations are welcome.

## Code of Conduct

Please keep discussions professional and respectful.

Do not:

- publish confidential information;
- expose personal data;
- submit proprietary material without permission;
- misrepresent regulatory requirements; or
- make unsupported claims about certification or legal compliance.

## Important Notice

TrustReady GRC is an experimental professional GRC implementation project.

It is not legal advice and does not itself provide certification against any referenced framework.

Contributions and mappings should therefore be presented as practical governance and security guidance rather than legal or certification determinations.
