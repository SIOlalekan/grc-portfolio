# GRC & Digital Trust Portfolio

## TrustReady GRC

[![TrustReady GRC Validation](https://github.com/SIOlalekan/grc-portfolio/actions/workflows/grc-validation.yml/badge.svg)](https://github.com/SIOlalekan/grc-portfolio/actions/workflows/grc-validation.yml)

**Sodeeq Ipadeola Olalekan**  
Digital Trust | Cybersecurity Governance | Risk | Compliance

TrustReady GRC is a practical Governance, Risk and Compliance project designed to help UK SMEs, Charities and Community Interest Companies (CICs) translate regulatory requirements, cybersecurity controls, evidence, risk and compliance assessments into structured and increasingly automated processes.

The project goes beyond static policy documentation by combining governance artefacts with machine-readable controls, cross-framework mapping, assessment logic and automated repository validation.

---

## Project Objectives

TrustReady GRC is designed to explore how UK SMEs, Charities and Community Interest Companies (CICs) can:

- understand their compliance obligations;
- assess their current control environment;
- identify compliance and security gaps;
- connect regulatory requirements to practical controls;
- identify appropriate evidence for implemented controls;
- prioritise remediation based on risk;
- reuse evidence across related frameworks;
- improve consistency through automation; and
- build stronger digital trust.

---

## Current Capabilities

The repository currently includes:

### 1. GRC Artefact Portfolio

The `pieces/` directory contains **16 practical GRC artefacts**, including policies, governance documents, compliance tools and assessment templates.

These artefacts are designed to demonstrate how governance requirements can be translated into usable organisational documentation.

---

### 2. Machine-Readable Control Library

The `controls/` directory contains a structured control library covering areas including:

- UK GDPR;
- Cyber Essentials;
- governance and accountability;
- lawful processing;
- security of personal data;
- secure configuration;
- vulnerability management;
- user access control;
- multi-factor authentication; and
- malware protection.

Each control can include information such as:

- unique control ID;
- framework;
- control domain;
- requirement;
- evidence expectations;
- risk severity;
- assessment question; and
- automation potential.

This allows compliance requirements to be processed programmatically rather than existing only as written policies.

---

### 3. Cross-Framework Mapping

The `mappings/` directory contains mappings between UK GDPR and Cyber Essentials controls.

This demonstrates how one technical control or evidence item may support multiple governance or compliance requirements.

For example:

```text
UK GDPR Security Requirement
            ↓
TrustReady Control
            ↓
Cyber Essentials Controls
            ↓
Technical Evidence
```

Cross-framework mapping can help reduce duplicated compliance work while preserving the distinction between different regulatory and certification requirements.

---

### 4. Compliance Assessment Engine

The repository contains a Python-based assessment engine in:

```text
scripts/assessment_engine.py
```

The engine reads the structured control library and supports assessment statuses such as:

```text
Compliant
Partially Compliant
Non-Compliant
Not Applicable
```

It then uses control severity to calculate a weighted compliance score and identify priority gaps.

Example workflow:

```text
Control Library
      ↓
Assessment Questions
      ↓
Organisation Responses
      ↓
Severity Weighting
      ↓
Compliance Score
      ↓
Priority Gaps
```

---

### 5. Automated GRC Validation

TrustReady includes an automated GitHub Actions validation workflow:

```text
.github/workflows/grc-validation.yml
```

The workflow automatically validates important components of the repository.

Checks currently include:

- required project components;
- Python syntax;
- control-library structure;
- required control fields;
- duplicate control IDs;
- valid severity classifications;
- evidence requirements;
- cross-framework mappings;
- references to valid controls;
- GRC artefact presence;
- empty artefact detection; and
- assessment scoring logic.

The automated validation workflow is currently passing successfully.

---

## Repository Structure

```text
grc-portfolio/
│
├── .github/
│   └── workflows/
│       ├── grc-validation.yml
│       └── weekly-draft.yml
│
├── controls/
│   └── control-library.yml
│
├── mappings/
│   └── ukgdpr-cyberessentials.yml
│
├── pieces/
│   └── GRC artefacts and templates
│
├── scripts/
│   ├── assessment_engine.py
│   └── draft.py
│
├── README.md
├── queue.yml
└── requirements.txt
```

---

## Compliance Model

TrustReady currently follows this model:

```text
Regulation / Framework
          ↓
Structured Controls
          ↓
Cross-Framework Mapping
          ↓
Assessment
          ↓
Evidence
          ↓
Risk Prioritisation
          ↓
Remediation
          ↓
Continuous Validation
```

The long-term aim is to develop this further into a lightweight compliance-as-code approach suitable for organisations that need practical GRC capability without unnecessarily complex enterprise tooling.

---

## Frameworks

Current work focuses primarily on:

- **UK GDPR**
- **Cyber Essentials**

Future development may extend the control-mapping model to areas such as:

- ISO/IEC 27001;
- NIST Cybersecurity Framework;
- supplier risk;
- privacy impact assessment;
- incident management;
- business continuity; and
- broader digital trust governance.

---

## Running the Assessment Engine

Install the required Python dependency:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python scripts/assessment_engine.py
```

The assessment engine reads the control library and produces a weighted compliance assessment based on the responses provided.

---

## Automated Validation

The repository uses GitHub Actions to validate the GRC project automatically.

Validation runs when relevant changes are made to areas such as:

```text
controls/
mappings/
pieces/
scripts/
requirements.txt
```

The workflow can also be triggered manually through GitHub Actions.

---

## Development Approach

TrustReady is being developed incrementally.

The project uses:

- structured control design;
- version-controlled governance artefacts;
- machine-readable YAML;
- Python-based compliance logic;
- automated validation;
- cross-framework mapping; and
- evidence-driven GRC thinking.

The development history and commits provide a transparent record of how the project has evolved.

---

## Roadmap

Planned development areas include:

- expanded control library;
- ISO/IEC 27001 mapping;
- NIST CSF mapping;
- structured evidence register;
- risk register engine;
- automated remediation recommendations;
- compliance dashboard;
- control ownership and review tracking;
- evidence-expiry monitoring;
- policy review automation;
- additional automated control checks; and
- external testing and practitioner contribution.

---

## Important Notice

TrustReady GRC is a professional portfolio and experimental GRC implementation project.

It is not legal advice, does not replace professional regulatory advice, and does not itself provide certification against any referenced framework.

Cross-framework mappings indicate practical relationships between controls and evidence. They do not imply regulatory or certification equivalence.

---

## Contributions and Feedback

Professional feedback, testing and constructive contributions are welcome.

The project is intended to develop through practical use, peer review and continued improvement in digital trust, cybersecurity governance, risk and compliance.
