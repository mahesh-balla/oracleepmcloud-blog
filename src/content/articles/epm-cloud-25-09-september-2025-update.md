---
title: 'Oracle EPM Cloud 25.09 (September 2025) Update Summary'
description: 'Summary of Oracle EPM Cloud 25.09 — strong cipher enforcement, Essbase 21.7 for new environments, Pipeline SFTP support, and folder naming changes.'
product: 'epm-cloud-updates'
subcategory: 'previous-releases-summary'
pubDate: '2025-09-05'
---

## Oracle EPM Cloud 25.09 Release Overview

September 2025 focuses on strengthening security infrastructure, modernizing the Essbase platform for new deployments, and expanding data integration capabilities. The 25.09 release reflects Oracle's ongoing commitment to security and platform modernization.

## Security Enhancements

### Strong Cipher Enforcement

A major security milestone in 25.09 is the **enforcement of strong ciphers for all connections**. This security enhancement:

- **Eliminates Weak Ciphers**: Only cryptographically strong ciphers are supported
- **Improves Compliance**: Meets or exceeds modern security standards and compliance requirements
- **Protects Data in Transit**: Ensures that all data transmitted between clients and servers is protected by strong encryption
- **Reduces Vulnerability Surface**: Eliminates known weaknesses in older cipher suites

Organizations should verify that all client applications and integrations support modern strong cipher suites before the September 2025 update. Clients that rely on legacy weak ciphers will need to be updated or replaced.

## Essbase Platform Modernization

### Version 21.7 for New Environments

A significant platform decision in 25.09 is that **all new environments are created with Essbase 21.7.xxx**. Important considerations include:

- **Platform Version Gap**: Existing environments may continue on earlier Essbase versions while new environments start on 21.7
- **Migration and Cloning Implications**: Organizations planning to migrate or clone existing environments should be aware of potential version compatibility considerations
- **Feature Alignment**: Ensure that any dependent applications or processes support Essbase 21.7 capabilities
- **Long-term Strategy**: Organizations should plan for eventual migration of all environments to Essbase 21.7

This phased approach allows existing customers to maintain stability while establishing Essbase 21.7 as the standard for new deployments.

## Data Integration Enhancements

### SFTP File Movement

Pipeline gains important new capabilities in 25.09 for SFTP operations:

**Copy to SFTP Job Type**: Transfer files from EPM Cloud to SFTP locations
- Automated file delivery to external systems
- Support for scheduled SFTP exports
- Secure file transfer with encryption

**Copy from SFTP Job Type**: Import files from SFTP locations into EPM Cloud
- Automated file retrieval from external systems
- Support for scheduled SFTP imports
- Secure data ingestion with validation

These additions make Pipeline a more comprehensive tool for file-based data integration:

- **Eliminate Manual FTP Transfers**: Automate file movement to/from SFTP servers
- **Support Legacy Systems**: Connect with systems that communicate via SFTP
- **Scheduled Processing**: Configure automatic file movement on schedules
- **Integrated Workflows**: Use SFTP operations within comprehensive pipelines

## File System Improvements

### Folder Naming Changes

The 25.09 release makes important changes to how folder names are handled:

- **Replace "/" Characters**: Forward slashes in folder names are automatically replaced with spaces
- **Prevent Backup Issues**: This change prevents backup-related issues that can occur when folder names contain special characters
- **Existing Folders**: Existing folders with forward slashes are updated automatically
- **New Folders**: All new folders follow the updated naming convention

This change ensures better compatibility with backup processes and reduces potential data integrity issues.

## Platform Consolidation

### Scheduler Migration Deadline

An important reminder in 25.09 is that the "**Migrate Schedules to Platform Job Scheduler**" option has been removed. Organizations should note:

- **Migration Required Before September**: Any schedules that require migration must be completed before the September 2025 update
- **No Automatic Migration Tool**: Manual migration is required; there is no automatic migration in 25.09
- **Evaluate Pipeline Scheduler**: Organizations should transition to using the Pipeline job scheduler for new schedule requirements
- **Plan Transition**: Begin planning the migration of any remaining legacy schedules

This change reflects the platform's consolidation around the modern Pipeline scheduler and eliminates maintenance burden for legacy scheduling systems.

## Implications for Organizations

The September 2025 update requires attention to several key areas:

### Security Readiness
- Verify strong cipher suite support across all clients
- Test connectivity after strong cipher enforcement
- Update any legacy clients that don't support modern ciphers

### Essbase Strategy
- Plan for eventual migration to Essbase 21.7
- Test applications with Essbase 21.7 compatibility
- Understand the implications of version differences for cloned environments

### Pipeline Integration
- Identify use cases for SFTP operations
- Plan for automation of file-based integrations
- Document SFTP sources and destinations

### Folder Management
- Audit existing folder names for special characters
- Prepare for automatic folder name updates
- Update any documentation that references old folder names

## Planning Checklist

Organizations should prepare for the 25.09 update by:

- **Test Strong Ciphers**: Verify all clients support strong cipher suites
- **Review SFTP Needs**: Identify data flows that could benefit from SFTP pipeline jobs
- **Plan Essbase Strategy**: Evaluate Essbase 21.7 readiness and migration timeline
- **Audit Folder Names**: Document folders with special characters
- **Complete Schedule Migration**: Ensure all legacy schedules have been migrated
- **Update Documentation**: Reflect new naming conventions and capabilities

[Read the full Oracle documentation →](https://docs.oracle.com/en/cloud/saas/readiness/epm/2025/epm-sep25/index.html)
