---
title: 'Oracle EPM Cloud 25.11 (November 2025) Update Summary'
description: 'Summary of Oracle EPM Cloud 25.11 — Essbase 21.7 upgrade, FreeForm parent-level entry, idle session timeout changes, and the subsequent update pause.'
product: 'epm-cloud-updates'
subcategory: 'previous-releases-summary'
pubDate: '2025-11-07'
---

## Oracle EPM Cloud 25.11 Release Overview

November 2025 represents a major platform milestone with comprehensive Essbase upgrades across all environments, significant planning enhancements, and important security adjustments. However, the 25.11 release also initiated unexpected circumstances that affected subsequent update schedules, making this release a pivotal moment in the 2025 platform evolution.

## Essbase Platform Upgrade

### Essbase 21.7.xx Upgrade Across All Environments

A transformational change in 25.11 is the **upgrade of Essbase to version 21.7.xx across all environments**, including both new and existing deployments:

- **Comprehensive Rollout**: All customers transition to Essbase 21.7.xx
- **Unified Platform**: Eliminates version fragmentation across customer base
- **Modern Foundation**: Establishes Essbase 21.7.xx as the standard platform version
- **Performance Improvements**: Essbase 21.7.xx includes performance enhancements and bug fixes
- **Feature Alignment**: All environments gain access to the latest Essbase capabilities

This universal upgrade simplifies the support matrix and allows Oracle to focus development resources on a single Essbase version.

### Migration Considerations

Organizations should prepare for the Essbase upgrade by:

- **Testing Compatibility**: Validate that all applications function correctly on Essbase 21.7.xx
- **Reviewing Performance**: Assess performance changes after upgrade completion
- **Cube Optimization**: Consider cube optimization and compression strategies for 21.7.xx
- **Custom Code Review**: Update any custom Essbase code or calc scripts for 21.7.xx compatibility

## Planning Enhancements

### FreeForm Parent-Level Data Entry

An important planning capability is introduced in 25.11: **FreeForm grids now support data entry at parent members** for top-down planning scenarios:

- **Parent Member Entry**: Users can now enter data directly at parent level in FreeForm grids
- **Top-Down Planning**: Enables top-down planning workflows where aggregate levels are planned first
- **Flexibility**: Supports diverse planning methodologies and workflows
- **Efficient Data Entry**: Reduces time required to create top-down plans
- **Hierarchy Preservation**: Parent-level entries cascade appropriately through the hierarchy

This enhancement significantly expands the planning capabilities available within FreeForm, enabling more sophisticated planning scenarios that were previously unavailable.

## Security Enhancements

### Idle Session Timeout Adjustment

An important security change in 25.11 is the **reduction of the default idle session timeout from 75 minutes to 30 minutes**:

- **Shorter Timeout**: Active sessions now expire after 30 minutes of inactivity (previously 75 minutes)
- **Improved Security**: Reduces the window of vulnerability for abandoned sessions
- **User Impact**: Users will be logged out more frequently if idle
- **Configuration Options**: Organizations may have ability to configure timeout settings
- **User Awareness**: Teams should be aware that longer lunch breaks or periods away from desk will result in re-authentication

This security improvement is consistent with modern security best practices for web applications and reduces exposure from abandoned sessions.

## Financial Consolidation Improvements

### Auto Submit/Approve for Reconciliations

Financial Consolidation gains an important automation capability in 25.11:

- **Automatic Submission**: Reconciliations with Data Integration-loaded transactions can be automatically submitted
- **Automatic Approval**: Reconciliations with carried-forward transactions can be automatically approved
- **Workflow Automation**: Reduces manual steps in consolidation processes
- **Conditional Logic**: Automation applies based on transaction source
- **Audit Trail**: Automated actions are fully tracked for audit purposes

This capability streamlines the consolidation process for transactions that have been validated through data integration or carry-forward processes.

## Narrative Reporting Updates

### Updated Narrative Reporting Extension

The Narrative Reporting extension is updated in 25.11 for **compatibility with Smart View 25.200** and other platforms enhancements:

- **Smart View Integration**: Enhanced compatibility with the latest Smart View version
- **Performance Improvements**: Updated extension includes performance optimizations
- **Feature Parity**: Ensures all narrative reporting functionality works consistently across platforms
- **User Experience**: Improved integration with the broader Smart View ecosystem

## Critical Platform Development

### Update Pause and Issue Resolution

**Important Notice**: Following the 25.11 release, Oracle **paused automatic production rollout** after identifying critical issues with **Essbase 21.7.x**. This pause affected subsequent scheduled updates:

- **December 2025 Update**: Held back due to Essbase issues
- **January 2026 Update**: Also held back pending resolution

This pause reflects Oracle's commitment to quality and demonstrates prudent risk management. Organizations should:

- **Monitor Official Communications**: Follow Oracle's official channels for update status and resolution timeline
- **Plan Contingencies**: Develop plans in case updates remain paused longer than expected
- **Prioritize Testing**: Thoroughly test any custom applications on Essbase 21.7.xx
- **Document Issues**: Report any Essbase 21.7.xx issues encountered to Oracle Support
- **Stay Informed**: Monitor Oracle's EPM Cloud blogs and documentation for updates

## Essbase 21.7.x Compatibility

Organizations encountering Essbase 21.7.x issues should:

- **Review Essbase Calc Scripts**: Ensure all custom calc scripts are compatible with 21.7.x
- **Test Applications**: Thoroughly test applications in lower environments
- **Engage Support**: Contact Oracle Support for any Essbase 21.7.x compatibility issues
- **Document Workarounds**: Document any workarounds or configuration changes required
- **Plan Updates**: Prepare for subsequent updates once Essbase 21.7.x issues are resolved

## Update Strategy Going Forward

The pause in automatic updates following 25.11 highlights the importance of:

- **Careful Testing**: Thorough testing before production rollout
- **Phased Adoption**: Consider staggered adoption of updates to manage risk
- **Issue Reporting**: Actively report issues discovered during testing
- **Communication**: Stay informed about update status and known issues
- **Contingency Planning**: Develop plans for extended periods between updates

## Preparation for 25.11

Organizations should prepare for the 25.11 release by:

- **Essbase Testing**: Create comprehensive Essbase 21.7.xx test plans
- **Application Validation**: Test all applications in lower environments
- **Planning Review**: Evaluate use of new parent-level FreeForm entry capabilities
- **Security Assessment**: Understand impact of 30-minute idle timeout
- **Communication**: Prepare user communications about timeout changes
- **Support Readiness**: Ensure support teams are ready for new capabilities and potential issues

[Read the full Oracle documentation →](https://docs.oracle.com/en/cloud/saas/readiness/epm/2025/epm-nov25/index.html)
