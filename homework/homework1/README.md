# Bank Credit Evaluation System
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
When assessing applications for bank credit cards, officers typically have access to a set of applicant details such as employer, marital status, and monthly income. Beyond these, banks also possess a large volume of information on applicants’ demographic profiles, credit histories, and behavioral records.  
The challenge is to systematically analyze these data, identify behavioral patterns and credit characteristics, and use historical trends to predict future credit performance. By quantifying the likelihood of default for each applicant, the bank can make more informed, consistent, and risk-adjusted lending decisions, reducing credit losses while maintaining customer acquisition goals.

## Stakeholder & User
**Primary Stakeholder:** Bank credit risk management department 
**Primary End Users:** Loan officers and automated decision systems
**Workflow Context:** The model’s predictions will be integrated into the credit approval workflow, providing a default probability score and recommended result at the point of application.

## Useful Answer & Decision
- **Type:** Predictive  
- **Deliverable:** A machine-learning-based credit scoring model that outputs a default probability for each applicant.  
- **Decision Supported:** Approve, decline, or adjust credit terms based on predicted risk, in line with bank policy and regulatory guidelines.

## Assumptions & Constraints
- Sufficient historical applicant and repayment data are available and compliant with privacy and banking regulations.
- Outputs must be interpretable to satisfy internal governance and regulatory requirements.
- Data pipelines must handle monthly updates.

## Known Unknowns / Risks
- Data quality issues such as missing or outdated information.
- Potential bias in historical data leading to fairness or compliance concerns.
- Integration challenges with legacy core banking systems.

## Lifecycle Mapping
Goal → Stage → Deliverable
- Reduce default rates in new credit card accounts → Problem Framing & Scoping (Stage 01) → Project scoping document & data requirements
- Develop predictive credit scoring model → Data Modeling (Stage 02) → Prototype model & evaluation report
- Deploy scoring model into approval system → Deployment (Stage 03) → Integrated, monitored production model

## Repo Plan
/data/, /src/, /notebooks/, /docs/ ; cadence for updates
