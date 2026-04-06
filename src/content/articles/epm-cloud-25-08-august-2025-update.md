---
title: 'Oracle EPM Cloud 25.08 (August 2025) Update Summary'
description: 'Summary of Oracle EPM Cloud 25.08 — Advanced Predictions in Planning, Groovy Script Validator, Account Reconciliation Pipeline integration, and Java 17 requirement.'
product: 'epm-cloud-updates'
subcategory: 'previous-releases-summary'
pubDate: '2025-08-08'
---

## Oracle EPM Cloud 25.08 Release Overview

August 2025 delivers significant artificial intelligence capabilities, important platform dependency updates, and major enhancements across multiple modules. The 25.08 release marks a critical inflection point in platform modernization and the integration of machine learning into financial planning processes.

## Advanced Planning Intelligence

### Advanced Predictions in Planning

A transformational addition to the Planning module in 25.08 is **Advanced Predictions**, which leverages machine learning to enhance forecasting and planning processes:

- **Machine Learning Algorithms**: Proprietary ML models analyze historical data to identify patterns and trends
- **OCI Data Science Cloud Integration**: Seamless integration with Oracle's Data Science Cloud capabilities
- **Four Selectable Algorithms**: Organizations can choose from multiple prediction algorithms optimized for different scenarios:
  - Linear regression for trend-based forecasting
  - Time-series analysis for seasonal patterns
  - Advanced ensemble methods combining multiple approaches
  - Custom algorithms for specialized domains

- **Automated Insights**: Predictions are automatically generated and surfaced to planning teams
- **Forecast Confidence**: Indicators show prediction confidence levels, enabling teams to assess reliability

This capability is particularly valuable for sales planning, demand forecasting, and financial projections where historical data is abundant and patterns are consistent.

## Account Reconciliation Evolution

### Pipeline Integration

The Account Reconciliation module undergoes significant expansion in 25.08 through **integration with Data Integration Pipeline**. New job types enable:

**Create Reconciliation**: Programmatically create reconciliation records
**Generate Report**: Automatically generate reconciliation reports
**Import Balances**: Bulk import account balances from external systems
**Run Auto Match**: Automatically match transactions using configured rules
**Set Period Status**: Manage reconciliation period status through pipeline automation

These pipeline integrations enable:

- **End-to-End Automation**: Fully automated reconciliation workflows from data import through reporting
- **Scheduled Processing**: Execute reconciliation tasks on configured schedules
- **Consistent Processing**: Eliminate manual steps and ensure consistent execution
- **Better Audit Trails**: Automatic execution provides complete audit records

## Financial Consolidation Updates

### Ownership Management Changes

Financial Consolidation receives important enhancements:

- **Ownership Management Improvements**: Enhanced capabilities for managing intercompany ownership scenarios
- **Consolidation Settings**: New settings for managing Translation Rules
- **Flexibility**: Better support for complex consolidation scenarios

## Narrative Reporting Enhancements

### Generative AI Notes Summarization

Narrative Reporting gains a powerful new capability in 25.08:

- **AI-Powered Summarization**: Generative AI automatically summarizes narrative notes and comments
- **Time Savings**: Reduce time required to review narrative documentation
- **Consistency**: Ensure consistent summarization across all narratives
- **Visibility**: Summarized notes provide quick understanding of key narrative points

This feature is valuable for organizations managing large volumes of narrative documentation alongside financial data.

## Tax Reporting Improvements

### Pillar Two Safe Harbor Provisions

Tax Reporting is enhanced to support **Pillar Two Safe Harbor provisions**, reflecting the evolving global tax environment:

- **Global Minimum Tax Compliance**: Support for OECD Pillar Two provisions
- **Safe Harbor Calculations**: Automated support for qualifying safe harbor elections
- **Multi-Jurisdiction Support**: Simplified management of Pillar Two compliance across jurisdictions

### FX Rate Translation Enhancements

Enhanced functionality for managing foreign exchange rate translation:

- **Flexible Rate Management**: Greater control over which rates apply to which balances
- **Real-Time Updates**: More responsive FX rate translation
- **Audit Trail**: Better tracking of FX translation decisions

## Platform Modernization

### Java 17 Requirement

A critical platform update in 25.08 is the **discontinuation of Java 8 for EPM Automate**. The requirement changes in August:

- **Java 17 Now Mandatory**: EPM Automate no longer supports Java 8
- **Immediate Action Required**: Organizations must upgrade to Java 17 before the August 2025 update
- **Performance Benefits**: Java 17 offers improved performance and security
- **Long-term Support**: Java 17 is a long-term support version ensuring stability

Linux and UNIX users were previously notified to plan for this transition. Organizations should complete Java 17 upgrades before the August update to avoid disruptions.

### Groovy Script Validator

A new **Groovy Script Validator** is introduced to help organizations prepare for stricter Groovy engine validation:

- **Early Validation**: Identify Groovy scripts that may fail with stricter validation
- **Proactive Remediation**: Fix scripts before they cause production issues
- **Preparation Period**: Time to update scripts before enforcement
- **Better Visibility**: Clear identification of problematic scripts

Teams should use this validator to audit existing Groovy scripts and update any that may be non-compliant.

## Smart View and Forms 2.0 Improvements

### Dynamic Variable Default Values

Forms 2.0 and Smart View receive an enhancement for dynamic user variables:

- **Auto-Set Default Values**: Default values are automatically set based on user context
- **Simplified Configuration**: Reduce manual configuration of user variables
- **Consistent Experience**: Users get appropriate defaults automatically
- **Reduced Errors**: Fewer opportunities for users to select incorrect values

## Product Integration Updates

### Content Consolidation

Sales Planning and Strategic Workforce Planning "What's New" content is merged into the main Cloud EPM documentation, improving navigation and eliminating redundant documentation across products.

## Preparation Checklist

Organizations should prepare for the 25.08 update by:

- **Complete Java 17 Migration**: Finalize Java 17 deployment across all systems
- **Test Groovy Scripts**: Run the Groovy Script Validator against all custom scripts
- **Plan Reconciliation Automation**: Identify reconciliation processes suitable for pipeline automation
- **Evaluate Advanced Predictions**: Assess planning applications that could benefit from ML-based predictions
- **Train Teams**: Prepare users for new AI capabilities and updated interfaces

[Read the full Oracle documentation →](https://docs.oracle.com/en/cloud/saas/readiness/epm/2025/epm-aug25/index.html)
