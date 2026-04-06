---
title: 'Oracle EPM Cloud 25.05 (May 2025) Update Summary'
description: 'Summary of Oracle EPM Cloud 25.05 — Copy Pipeline feature in Data Exchange, standalone Data Map execution, and Cube Refresh validation improvements.'
product: 'epm-cloud-updates'
subcategory: 'previous-releases-summary'
pubDate: '2025-05-02'
---

## Oracle EPM Cloud 25.05 Release Overview

May 2025 introduces powerful new data integration capabilities and enhances operational flexibility for organizations managing complex data pipelines. The 25.05 release focuses on improving the productivity of data management teams and providing greater control over data movement and validation processes.

## Data Exchange Enhancements

### Copy Pipeline Feature

A significant new capability in 25.05 is the **Copy Pipeline feature** within Data Exchange. This enhancement enables organizations to:

- **Duplicate Complete Pipelines**: Copy an entire Data Integration Pipeline in a single operation
- **Preserve All Components**: All pipeline components, configurations, and dependencies are replicated
- **Accelerate Setup**: Reduce the time required to create similar pipelines across multiple data flows
- **Streamline Management**: Simplify the creation of parallel pipelines for different data sources or destinations

The Copy Pipeline feature is particularly valuable for organizations that manage numerous similar data integration scenarios, as it dramatically reduces the manual effort required to set up new pipelines.

## Data Map Execution

### Standalone Execution Capability

Data Maps now support **standalone execution** independent of Smart Push operations. This enhancement provides:

- **Greater Flexibility**: Run data maps on-demand without requiring a full Smart Push workflow
- **Dual Console Visibility**: Job details appear in both source and target consoles, providing complete visibility into data movement
- **Better Troubleshooting**: Easier identification and resolution of data mapping issues
- **Improved Audit Trail**: Enhanced tracking of standalone data map executions

This capability is particularly useful for organizations that need to run data transformations outside of their standard push processes or test data mapping logic before implementing full Smart Push operations.

## Platform and Technical Updates

### Java 17 Migration Notification

Users operating on Linux and UNIX platforms are notified in 25.05 that they should **update to Java 17 before the August 2025 update**. This advance notice provides organizations with the time needed to:

- **Test Java 17 Compatibility**: Validate that all applications and scripts function correctly with Java 17
- **Update Systems**: Deploy Java 17 across affected environments
- **Plan Maintenance Windows**: Schedule updates during appropriate maintenance periods
- **Identify Dependencies**: Discover and resolve any Java 8-dependent code or components

Planning ahead for Java 17 migration ensures a smooth transition in the August update and prevents potential disruptions.

## Cube Refresh Enhancements

### Validation Improvements Coming

The 25.05 release includes **future enhancements to Cube Refresh validation** that organizations should be aware of:

- **Conflict Detection**: The Cube Refresh process will validate for conflicting metadata scenarios
- **New Status Option**: A new "Completed with Warnings" status will be introduced to indicate successful completion despite non-critical validation issues
- **Improved Visibility**: Better identification of metadata conflicts that could cause issues during refresh

These enhancements are part of a phased approach to improve the robustness of the cube refresh process and ensure greater reliability in production environments.

## Planning Ahead

Organizations should prepare for the May 2025 update and beyond by:

- **Evaluating Copy Pipeline Usage**: Identify pipelines that could benefit from the copy feature
- **Testing Standalone Data Maps**: Plan how to leverage standalone data map execution in their workflows
- **Beginning Java 17 Preparation**: Start testing and planning Java 17 migration for Linux/UNIX systems
- **Understanding Cube Refresh Changes**: Review cube refresh processes and prepare for the upcoming validation enhancements
- **Training and Documentation**: Update internal documentation to reflect new data integration capabilities

## Performance and Reliability

The 25.05 release includes under-the-hood improvements to ensure reliable execution of data pipelines and data maps, even as organizations scale their data integration operations.

[Read the full Oracle documentation →](https://docs.oracle.com/en/cloud/saas/readiness/epm/2025/epm-may25/index.html)
