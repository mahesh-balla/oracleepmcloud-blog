---
title: 'Oracle EPM Cloud 25.02 (February 2025) Update Summary'
description: 'Summary of Oracle EPM Cloud 25.02 — HTTPS required for connections, Pipeline table view, Account Reconciliation improvements, and Financial Reporting deprecation timeline.'
product: 'epm-cloud-updates'
subcategory: 'previous-releases-summary'
pubDate: '2025-02-07'
---

## Oracle EPM Cloud 25.02 Release Overview

February 2025 brings critical security enhancements, operational improvements to Pipeline Management, and significant upgrades to Account Reconciliation functionality. The 25.02 release also marks an important deprecation milestone for Financial Reporting users.

## Security Enhancements

### HTTPS Required for Connections

A major security milestone in 25.02 is the enforcement of **HTTPS for all Connections screens and Update Connections REST APIs**. This requirement strengthens data protection in transit and ensures that all credential and connection information is encrypted during transmission. Organizations must update any automation scripts or integrations that rely on these APIs to use HTTPS endpoints exclusively.

## Pipeline Management Improvements

### New Table View

Pipeline Management introduces a **new table view optimized for large pipelines**, providing users with better visibility and navigation when working with complex data integration scenarios. This view complements the existing card-based interface and allows teams to manage many pipelines more efficiently.

**Important Change**: Auto-save functionality has been removed from Pipeline Management. Users must now **manually save their pipeline configurations** to ensure changes are preserved. This change emphasizes the importance of confirming pipeline modifications before deployment.

## Account Reconciliation Enhancements

The Account Reconciliation module receives several critical improvements in 25.02:

- **Customizable Unmatched Transactions Layout**: Organizations can now tailor the display and organization of unmatched transactions to match their specific reconciliation workflows
- **Enhanced Matching Search**: Improved search capabilities make it faster and easier to locate and match transactions during the reconciliation process
- **OCI Object Storage for Attachments**: Attachments are now stored in OCI Object Storage, providing better scalability, reliability, and integration with the broader OCI ecosystem

## Financial Consolidation Updates

### YTD Data Input in Forms

Financial Consolidation forms now support **Year-to-Date (YTD) data entry**, enabling organizations to manage YTD balances directly in the application without requiring manual adjustments or workarounds.

### Configuration Improvements

New export and import commands for **configurable consolidation rulesets** provide greater flexibility in managing and deploying consolidation rules across environments.

## EPM Automate Command Additions

Three new commands have been added to EPM Automate:

- **runPipeline**: Execute Data Integration pipelines programmatically
- **compactCube**: Optimize cube storage and performance
- **updateGuidedLearningSettings**: Configure guided learning preferences

## Navigation Flow Enhancements

The Navigation Flow module includes several usability improvements:

- **Hidden Forms Visibility**: Previously hidden forms are now visible and accessible
- **Enhanced Column Display**: New Created and Last Modified columns provide better tracking of artifact history
- **Reload Functionality**: Improved reload icon and process for refreshing navigation data

## Smart View Enhancements

Smart View receives two important updates in 25.02:

- **POV Preview for Mac/Browser**: Point of View preview is now available on Mac and Browser platforms, bringing feature parity across all platforms
- **Auto Predict Improvements**: Enhanced machine learning capabilities for automatic value prediction in planning applications

## Platform Security & Authentication

**OAuth 2.0 Authentication** is now available for the EPM Cloud Adapter, providing more secure and flexible authentication options for integrations and third-party applications.

## Deprecation Notice: Financial Reporting

Organizations using **Financial Reporting must prepare for deprecation in June 2025**. The Reports module is becoming the primary reporting solution. Teams should plan their transition strategy during this window and leverage the migration tools provided by Oracle.

[Read the full Oracle documentation →](https://docs.oracle.com/en/cloud/saas/readiness/epm/2025/epm-feb25/index.html)
