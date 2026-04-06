---
title: 'Oracle EPM Cloud 25.10 (October 2025) Update Summary'
description: 'Summary of Oracle EPM Cloud 25.10 — Forms 2.0 and Dashboard 2.0 become default, Smart View 25.200, maintenance optimization, and key deprecations.'
product: 'epm-cloud-updates'
subcategory: 'previous-releases-summary'
pubDate: '2025-10-03'
---

## Oracle EPM Cloud 25.10 Release Overview

October 2025 marks a pivotal milestone with the consolidation of Forms and Dashboard capabilities to their 2.0 versions. The 25.10 release also delivers significant Smart View enhancements, important platform maintenance optimizations, and critical deprecation announcements that reshape how organizations interact with EPM Cloud.

## Forms and Dashboard Consolidation

### End-of-Support for Legacy Versions

October 2025 represents the final milestone for Forms 1.0 and Dashboard 1.0:

- **Forms 1.0 End-of-Support**: Forms 1.0 reaches end-of-support; all environments default to Forms 2.0
- **Dashboard 1.0 End-of-Support**: Dashboard 1.0 reaches end-of-support; all environments default to Dashboard 2.0
- **Automatic Transition**: All remaining legacy forms and dashboards are automatically converted to 2.0
- **Legacy Version Retirement**: The legacy 1.0 interfaces are no longer available

Organizations that have not completed their migration to Forms 2.0 and Dashboard 2.0 must finalize the transition with the October 2025 update:

- **Form Validation**: Ensure all custom forms function correctly in 2.0 interface
- **Dashboard Verification**: Confirm that all dashboards display and perform as expected in 2.0
- **User Training**: Complete any final user training on the new interface
- **Custom Development**: Address any custom extensions or integrations required in 2.0

This consolidation simplifies the platform and allows engineering resources to focus on enhancing the modern 2.0 interfaces.

## Smart View Enhancements

### Smart View 25.200 Release

Smart View receives a significant update to version 25.200 in October 2025:

**User Variable Access Improvements**:
- Enhanced variable handling in queries
- More flexible variable configuration
- Better variable visibility and management

**VBA Options**:
- Improved Visual Basic for Applications (VBA) compatibility
- Enhanced macro support for Excel
- Better integration with Excel automation

**Performance Enhancements**:
- Faster query execution
- Improved spreadsheet responsiveness
- Better handling of large result sets

**Additional Improvements**:
- Enhanced functionality across planning, reporting, and analytics modules
- Better integration with native planning interfaces
- Improved user variable handling across different product modules

These enhancements position Smart View as the primary interface for spreadsheet-based analysis while maintaining strong Excel integration.

## Platform Maintenance Optimization

### Intelligent Artifact Reloading

A significant performance optimization in 25.10 affects how the platform handles maintenance and refreshes:

- **Only Modified Items Reloaded**: During maintenance cycles and dimension refreshes, only artifacts that have been modified are reloaded
- **Reduced Downtime**: Intelligent reloading reduces the time required for maintenance operations
- **Performance Impact**: Infrastructure resources are focused on changed artifacts rather than reloading entire dimension structures
- **Operational Efficiency**: Allows more frequent maintenance and refresh operations without impacting users

This optimization is particularly valuable for organizations with large, complex dimension hierarchies where full reloads would otherwise consume significant resources.

## Enterprise Data Management

### New Accelerator Templates

Enterprise Data Management receives enhanced accelerator templates in 25.10:

**AFCS Accelerator**:
- Asset Finance Consolidation Suite template
- Streamlined setup for asset-heavy organizations
- Pre-configured workflows and validation rules

**DFCS Accelerator**:
- Downstream Functions Consolidation Suite template
- Optimized for organizations with complex downstream operations
- Pre-built consolidation logic for downstream scenarios

These accelerators enable faster implementation of complex consolidation scenarios by providing pre-built templates and best-practice configurations.

## Platform Modernization Requirements

### Java 17 Transition for Linux/macOS

A critical requirement announced in 25.10 is that **Linux and macOS users must transition to Java 17 for EPM Automate**:

- **Java 8 No Longer Supported**: The August update discontinued Java 8 support
- **October Deadline**: By October 2025, all Linux/macOS systems must be running Java 17
- **Performance Benefits**: Java 17 offers improved performance and modern security features
- **Testing Required**: Organizations should test all scripts and integrations with Java 17 before the deadline

Organizations that have not yet completed Java 17 migration should prioritize this work before October.

## Deprecated Features

### Native Mode in Smart View

An important deprecation in 25.10 is the **discontinuation of Native Mode in Smart View**:

- **Native Mode No Longer Supported**: Organizations must use Standard Mode
- **Feature Parity**: Standard Mode provides all functionality previously available in Native Mode
- **User Transition**: Users must switch to Standard Mode for all Smart View operations
- **Configuration Changes**: Any automation or macros relying on Native Mode must be updated

Standard Mode provides superior performance, better feature support, and more consistent behavior across platforms.

## Planning for October 2025

Organizations should prepare comprehensively for the October 2025 update:

### Forms and Dashboard Migration
- Finalize any remaining 1.0 to 2.0 migrations
- Test all custom forms and dashboards in 2.0
- Train all users on the 2.0 interface
- Document any workarounds or custom functionality

### Smart View Readiness
- Test Smart View 25.200 in development environments
- Update any VBA macros for compatibility
- Train users on new variable handling capabilities
- Plan for any custom extensions that require updates

### Java 17 Migration
- Complete Java 17 deployment across all Linux/macOS systems
- Test all scripts and integrations
- Update automated processes if needed
- Verify EPM Automate functionality

### Native Mode Transition
- Audit Smart View usage for Native Mode
- Migrate any Native Mode-dependent workflows to Standard Mode
- Test all macros and automation in Standard Mode
- Train users if needed

### Maintenance Planning
- Plan for reduced maintenance windows with optimized reloading
- Test refresh processes with smaller artifact sets
- Document any changes to maintenance procedures

[Read the full Oracle documentation →](https://docs.oracle.com/en/cloud/saas/readiness/epm/2025/epm-oct25/index.html)
