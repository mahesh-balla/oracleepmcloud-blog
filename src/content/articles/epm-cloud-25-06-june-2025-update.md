---
title: 'Oracle EPM Cloud 25.06 (June 2025) Update Summary'
description: 'Summary of Oracle EPM Cloud 25.06 — Reports becomes primary reporting solution, TLS 1.3 enforced, Dashboard 2.0 enhancements, Groovy Excel/ZIP capabilities, and Data Exchange security.'
product: 'epm-cloud-updates'
subcategory: 'previous-releases-summary'
pubDate: '2025-06-06'
---

## Oracle EPM Cloud 25.06 Release Overview

June 2025 represents a major milestone in the EPM Cloud evolution with significant security enhancements, the consolidation of reporting capabilities, and powerful new capabilities for data processing and dashboard analytics. The 25.06 release reflects Oracle's commitment to modernization while providing extended transition periods for critical changes.

## Reporting Consolidation

### Reports Becomes Primary Solution

A pivotal change in 25.06 is the designation of **Reports as the primary reporting solution**. Organizations have prepared for this transition throughout 2025, and **Financial Reporting is now de-supported**. This consolidation:

- **Streamlines Reporting Architecture**: Eliminates redundancy and simplifies the reporting platform
- **Improves Maintenance**: Reduces the complexity of maintaining multiple reporting engines
- **Enhances Performance**: Focuses development resources on optimizing the Reports module
- **Provides Migration Paths**: Organizations complete their transition away from Financial Reporting

Teams should ensure all critical Financial Reporting templates have been migrated to the Reports module or alternative solutions.

### Forms and Dashboard Timeline Extended

Due to the scope of required migrations, the de-support date for **Forms 1.0 and Dashboard 1.0 has been extended from June to October 2025**. This extended timeline provides organizations with additional time to:

- **Complete Migrations**: Move legacy dashboards and forms to 2.0 versions
- **Test Thoroughly**: Validate that new versions meet business requirements
- **Train Users**: Ensure teams are prepared for the user interface changes
- **Plan Strategically**: Address migration priorities without rushed implementations

## Security Enhancements

### TLS 1.3 Exclusively Supported

A critical security milestone in 25.06 is the **exclusive support of TLS 1.3** for all encrypted connections. **TLS 1.2 is being phased out** across the platform. Organizations should:

- **Verify Client Compatibility**: Ensure all client applications support TLS 1.3
- **Update Connection Strings**: Confirm that connections explicitly support TLS 1.3
- **Test Connectivity**: Validate that all integrations function with TLS 1.3 before the transition
- **Update Documentation**: Ensure teams understand the security requirements

This change strengthens the security posture of the entire platform and protects against known vulnerabilities in earlier TLS versions.

## Dashboard 2.0 Enhancements

The Dashboard 2.0 module receives significant new capabilities in 25.06:

- **Analyze Function**: New menu option enables deeper analysis of dashboard data
- **Open in Smart View**: Direct integration allowing dashboards to be opened and analyzed in Smart View
- **Spreadsheet Export**: Export dashboard data to Excel spreadsheets for further analysis
- **Enhanced Interactivity**: Users can move more fluidly between dashboards, Smart View, and spreadsheet tools

These enhancements make Dashboard 2.0 a more comprehensive analytics and reporting platform.

## Groovy Scripting Enhancements

### Excel and ZIP File Creation

Groovy scripting capabilities are significantly expanded in 25.06, enabling users to:

- **Create Excel Workbooks**: Generate Excel files directly from Groovy scripts, enabling automated report generation
- **Create ZIP Archives**: Package multiple files into ZIP archives for distribution and storage
- **Send to Inbox/Outbox**: Route generated files to EPM Cloud Inbox/Outbox for user access
- **Automate File Generation**: Eliminate manual file creation in many business processes

These capabilities enable powerful automation scenarios, such as generating daily Excel reports or packaging multiple files for distribution.

## Data Exchange Security

### Location Security Settings

Data Exchange receives important security enhancements in 25.06 through **new location security settings**. These settings provide:

- **Feature Parity with Data Management**: Consistent security controls across data management tools
- **Granular Access Control**: Control which users can access specific data locations
- **Compliance Support**: Ensure sensitive data is protected and accessible only to authorized users
- **Audit Trail**: Better tracking of who accesses which data locations

These enhancements strengthen the overall security posture of data movement within EPM Cloud.

## Predictive Cash Forecasting

### Enhanced Standard Items and What-If Analysis

Predictive Cash Forecasting receives important enhancements in 25.06:

- **Cash Buffer and Over Buffer Standard Items**: Cash buffer metrics are now standard items, enabling consistent cash forecasting across organizations
- **What-If Analysis Dashboards**: New dashboard capabilities enable scenario analysis and sensitivity testing
- **Enhanced Forecasting**: Better ability to model cash scenarios and prepare for financial contingencies

These enhancements make cash forecasting more accessible to organizations of all sizes.

## Smart View for Google Workspace

### Connection Switching

Smart View for Google Workspace gains the ability to **switch connections between environments**, enabling users to:

- **Access Multiple Environments**: Easily move between development, test, and production environments
- **Maintain Workflow Continuity**: Stay within Google Sheets while working across environments
- **Improve Efficiency**: Reduce context switching and manual configuration

## Migration and Preparation

Organizations should use the extended Forms/Dashboard timeline to:

- **Test Dashboard 2.0 Thoroughly**: Validate all dashboard functionality in the new interface
- **Train Users on New Features**: Ensure teams understand analyze, Smart View integration, and export capabilities
- **Plan TLS 1.3 Transition**: Verify compatibility and test all connections
- **Evaluate Groovy Capabilities**: Identify automation opportunities enabled by Excel/ZIP creation
- **Implement Location Security**: Plan and test data access controls

[Read the full Oracle documentation →](https://docs.oracle.com/en/cloud/saas/readiness/epm/2025/epm-jun25/index.html)
