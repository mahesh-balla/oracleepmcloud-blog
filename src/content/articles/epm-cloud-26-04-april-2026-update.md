---
title: 'Oracle EPM Cloud 26.04 (April 2026) Update Summary'
description: 'A comprehensive summary of the Oracle EPM Cloud 26.04 patch — the first monthly update since the Essbase 21c pause. Covers new features across Planning, Narrative Reporting, Account Reconciliation, and more.'
product: 'epm-cloud-updates'
subcategory: 'latest-release'
pubDate: '2026-04-06'
heroImage: '../../assets/blog-placeholder-4.jpg'
---

Oracle EPM Cloud monthly updates are back. The **26.04 release** (April 2026) is the first monthly patch since Oracle paused updates in late 2025 after identifying application-specific issues with the Essbase 21.7.x version shipped in the 25.11 update. With 26.04, Oracle resumes its regular cadence — and this release packs a cumulative set of enhancements spanning nearly five months (25.12 through 26.03) for non-Essbase business processes, alongside targeted Essbase 21c fixes.

**Deployment timeline:** Test environments April 3, 2026 | Production environments April 17, 2026.

## Why the Pause Happened

Starting with the 25.11 update, Oracle identified sporadic performance and data-accuracy issues in EPM business processes that rely on Essbase (Financial Consolidation and Close, FreeForm, Planning, Profitability and Cost Management, and Tax Reporting). As a precaution, Oracle halted monthly updates for all production environments through 25.12, 26.01, 26.02, and 26.03. The 26.04 patch marks the official resumption, with Essbase 21c fixes at its core.

## Essbase Fixes and Enhancements

The primary focus of 26.04 is resolving the Essbase 21c issues that triggered the pause. Key Essbase improvements include:

- Support for **@QUERYBOTTOMUP** and **@NONEMPTYTUPLE** MDX functions
- A new **essbaseBlockAnalysisReport** enhancement that calculates the percentage of data cells with values close to zero, helping administrators identify performance-impacting blocks
- **Snapshot import validation** improvements — note that imports will fail when metadata contains Essbase reserved words (e.g., "COUNT") or non-unique sibling names after whitespace normalization, so metadata remediation may be required before importing

## Infrastructure and Administration

**Environment migration** now supports migrating environments to different SKUs, regions, cloud accounts, or IAM domains while maintaining the existing URL — previously impossible without losing access credentials.

**Gen AI regional availability** has expanded: all regions in the OC1 realm now have Gen AI capabilities available. Important: beginning **July 2026**, only environments running 26.04 or later will retain access to GenAI features.

**EPM Automate for Windows** has a new default installation path (`Program Files\Oracle\EPM Automate`). Runtime data, logs, and password files now save within this directory, which may affect existing scripts that reference the old default location.

## New REST APIs for Agentic AI

Three new REST APIs designed for agentic AI interactions with EPM Cloud have been introduced:

- **Get Application Summary** — returns AI-focused summaries of EPM applications
- **Export Data** — delivers JSON data grids for programmatic dataset exports
- **Export Form Data** — returns JSON grids containing form-slice data

These APIs enable programmatic AI-driven interactions with EPM Cloud, aligning with Oracle's broader AI strategy.

## Planning and Data Entry

**Upper-level data entry in FreeForm** is now supported. Users can enter data directly at parent members in FreeForm grids (BSO cubes), enabling top-down planning approaches without workarounds.

**Customizable integration roles** allow Service Administrators to customize the "Integration – Create" and "Integration – Run" roles, providing more granular permission management for data mapping and execution tasks.

## Groovy and Automation

**Enhanced data copying** — Groovy rules now support copying relational data, Essbase data, comments, attachments, and supporting details, automating processes that previously required manual effort.

**Task Manager pipeline customization** — Run Pipeline automation tasks now support custom variables for more flexible workflow designs.

**Mandatory Groovy engine update coming in 26.05** — Stricter validation rules arrive in May 2026. Oracle recommends reviewing and correcting Groovy scripts now to prevent failures after the next update.

## Narrative Reporting

- **AutoTextSummary Criteria Manager** — Criteria definitions can replace direct parameters in AutoTextSummary functions, enabling reusable configurations within individual reports
- **Analytics image integration** — Oracle Analytics Cloud dashboards can now be embedded directly into Narrative Reports
- **Multiple ML property files** — Support for multiple machine learning property files provides customization flexibility for GenAI implementations
- **Updated Smart View extension** for Narrative Reporting

## Account Reconciliation and Transaction Matching

New options to **customize and filter data** when managing adjustment and support attributes in transaction matching. Enhanced filtering for journal column data within transaction matching processes streamlines reconciliation workflows and improves data precision.

The **IDCS audit enhancement** adds a groupAssignmentAuditReport command and associated REST API to retrieve audit information for specified date ranges.

## Predictive Cash Forecasting

**ERP integration** with Oracle Cloud ERP is now generally available (previously beta-only). Data flows seamlessly for Accounts Receivable, Accounts Payable, and Cash Management, with drill-through to analytical views. Prediction definitions now require a **minimum of two input drivers** to ensure better prediction results.

## Reporting Enhancements

New **LeftTrim** and **RightTrim** functions enable delimiter-based text trimming in Reports, improving flexibility over character-count-based methods.

## Opt-Out Process

If you need to skip the 26.04 update, note that you **cannot self-initiate a skip** for this release. Instead, submit a Service Request (SR) following the documentation at *Requesting to Skip Automatic Updates for Environments*.

## What to Do Now

1. **Review your Groovy scripts** — The 26.05 update (May 2026) will enforce stricter validation. Use the time between 26.04 and 26.05 to audit and fix any scripts that may not comply.
2. **Check EPM Automate scripts** — If you have automation scripts referencing the old default installation path on Windows, update them to the new `Program Files\Oracle\EPM Automate` location.
3. **Plan your GenAI upgrade path** — Environments must be on 26.04 or later by July 2026 to retain GenAI access.
4. **Test on your test environment first** — The 26.04 update lands on test environments on April 3. Use the two-week window before the April 17 production rollout to validate your configurations.

This is a significant release that catches up on months of accumulated enhancements. Take advantage of the test window to get familiar with the changes before they hit production.
