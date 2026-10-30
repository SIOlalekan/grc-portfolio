# Changelog

All notable changes to **TrustReady GRC** will be documented in this file.

The project uses versioned releases to provide a transparent record of the development of its Governance, Risk and Compliance capabilities.

---

## [Unreleased]

### Planned

- Expand the machine-readable control library.
- Add ISO/IEC 27001 control mappings.
- Add NIST Cybersecurity Framework mappings.
- Develop a structured evidence register.
- Develop a risk register and risk-scoring engine.
- Introduce remediation recommendations.
- Develop a compliance dashboard.
- Add control ownership and review tracking.
- Introduce evidence-expiry monitoring.
- Expand automated compliance checks.
- Conduct independent practitioner review and external testing.

---

## [0.1.0] - 2026-10-30

### Initial TrustReady GRC Baseline

This version establishes the first structured baseline of the TrustReady GRC project.

### Added

#### GRC Artefact Portfolio

- Added 16 practical Governance, Risk and Compliance artefacts.
- Added governance policies, assessment tools, templates and supporting compliance materials.
- Structured the artefacts within the `pieces/` directory.

#### Machine-Readable Control Library

- Added the TrustReady machine-readable GRC control library.
- Introduced unique control identifiers.
- Added framework and domain classifications.
- Added control requirements.
- Added evidence expectations.
- Added control severity classifications.
- Added assessment questions.
- Added automation-potential indicators.
- Added initial UK GDPR controls.
- Added initial Cyber Essentials controls.

#### Cross-Framework Mapping

- Added UK GDPR to Cyber Essentials control mappings.
- Introduced practical relationships between regulatory requirements and technical security controls.
- Added supporting rationale for mapped controls.
- Added examples of reusable compliance evidence.
- Documented that mappings do not represent regulatory or certification equivalence.

#### Compliance Assessment Engine

- Added a Python-based GRC assessment engine.
- Added support for the following assessment statuses:
  - Compliant
  - Partially Compliant
  - Non-Compliant
  - Not Applicable
- Added severity-weighted compliance scoring.
- Added identification of priority compliance gaps.
- Connected the assessment engine to the machine-readable control library.

#### Automated Validation

- Added the TrustReady GRC GitHub Actions validation workflow.
- Added automated checks for required repository components.
- Added Python syntax validation.
- Added control-library structure validation.
- Added duplicate control-ID detection.
- Added severity-value validation.
- Added evidence-requirement validation.
- Added cross-framework mapping validation.
- Added GRC artefact portfolio validation.
- Added assessment scoring tests.
- Confirmed the full validation workflow passes successfully.

#### Repository Documentation

- Expanded the project README.
- Documented the TrustReady architecture and objectives.
- Added repository structure documentation.
- Added compliance-model documentation.
- Added assessment-engine instructions.
- Added automated-validation documentation.
- Added project roadmap.
- Added professional-use and certification disclaimers.
- Added a live GitHub Actions validation status badge.

#### Open Contribution Framework

- Added `CONTRIBUTING.md`.
- Added guidance for professional and academic reviewers.
- Added contribution guidance for controls, mappings, evidence requirements and code.
- Added Pull Request guidance.
- Added confidentiality and responsible-contribution expectations.

#### GitHub Issue Templates

- Added a structured Control or Mapping Review issue template.
- Added a structured Technical Issue template.
- Enabled reviewers to submit evidence-based improvement recommendations.

### Current Status

TrustReady GRC v0.1.0 establishes the initial working foundation for the project:

```text
GRC Artefacts
      ↓
Machine-Readable Controls
      ↓
Cross-Framework Mapping
      ↓
Compliance Assessment
      ↓
Severity-Weighted Scoring
      ↓
Automated Validation
      ↓
Continuous Improvement
```

The next stage of development will focus on independent practitioner review, real-world testing, additional framework mappings and greater compliance automation.
