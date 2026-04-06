---
title: 'Oracle EPM Cloud 25.07 (July 2025) Update Summary'
description: 'Summary of Oracle EPM Cloud 25.07 — Oracle Access Governance integration, Data Integration enhancements, additional BSO cubes, and new User/Group APIs.'
product: 'epm-cloud-updates'
subcategory: 'previous-releases-summary'
pubDate: '2025-07-04'
---

## Oracle EPM Cloud 25.07 Release Overview

July 2025 introduces enterprise-grade identity and access management capabilities, expands data integration flexibility, and provides new programmatic interfaces for user and group management. The 25.07 release addresses key enterprise requirements for security, scalability, and operational control.

## Identity and Access Management

### Oracle Access Governance Integration

A transformational enhancement in 25.07 is the **integration with Oracle Access Governance**. This integration provides organizations with:

- **Streamlined Identity Orchestration**: Automated management of user identities across EPM Cloud and related systems
- **Automated Onboarding**: Reduce manual onboarding processes and ensure consistent provisioning
- **Lifecycle Management**: Automated deprovisioning and role transitions for departing or transferring employees
- **Compliance Controls**: Better visibility and control over who has access to sensitive financial data
- **Audit Capabilities**: Enhanced tracking of provisioning and access changes for compliance reporting

The Oracle Access Governance integration is particularly valuable for large organizations managing complex identity scenarios across multiple systems. It significantly reduces the manual overhead of user management and improves compliance posture.

## Data Integration Enhancements

### Role-Based Separation of Duties

The 25.07 release introduces **new roles enabling separation of duties** between application administrators and Data Integration administrators. This capability:

- **Reduces Risk**: Prevents single individuals from controlling all aspects of data movement
- **Enforces Controls**: Implements principle of least privilege for data administration
- **Improves Compliance**: Supports segregation of duties requirements in regulated industries
- **Enables Specialization**: Allows organizations to assign DI administration to specialized teams

### Automatic Integration Execution

Data Integration receives an important new feature: the ability to **automatically run integrations on specified dimensions**. This enhancement enables organizations to:

- **Reduce Manual Steps**: Eliminate manual integration execution for standard processes
- **Improve Consistency**: Ensure consistent data movement without manual intervention
- **Enable Automation**: Build fully automated data pipelines with minimal human interaction
- **Improve Efficiency**: Reduce the time required to execute routine data integration tasks

These enhancements make Data Integration more powerful and more aligned with enterprise-grade automation expectations.

## Cube Storage Expansion

### Additional Block Storage Cubes

The 25.07 release expands the availability of **additional Block Storage Cubes (BSO)** through a controlled rollout. Organizations requiring additional BSO cubes can:

- **Request Additional Capacity**: Submit a Service Request to Oracle for additional BSO cubes
- **Scale Planning Applications**: Support larger planning and analysis models
- **Support Specialized Scenarios**: Deploy specialized cubes for specific business requirements
- **Manage Resources**: Better align cube capacity with business needs

The Service Request process ensures that additional BSO cubes are provisioned appropriately and that organizations are supported in deploying them effectively.

## User and Group Management APIs

### Enhanced Programmatic Access

Two new APIs provide enhanced programmatic access to user and group information:

**List Users API**: Retrieve comprehensive user information including:
- User identities and contact information
- Group membership for each user
- Role assignments and privileges
- User status and provisioning details

**Group Management API**: Manage group structure and membership programmatically:
- Query group membership
- Manage group definitions
- Track group hierarchies
- Automate group-based provisioning

These APIs enable organizations to:

- **Automate User Management**: Synchronize user and group information from external systems
- **Build Custom Workflows**: Create custom user provisioning and deprovisioning automation
- **Improve Reporting**: Generate user access and role reports programmatically
- **Support Integration**: Connect EPM Cloud user management to broader identity systems

## Enterprise-Scale Deployments

The July 2025 updates position EPM Cloud for enterprise-scale deployments with improved:

- **Identity Management**: Oracle Access Governance integration handles complex identity scenarios
- **Data Governance**: Role-based separation of duties enforces data control policies
- **Automation**: New APIs and automatic integration execution enable end-to-end automation
- **Scalability**: Additional BSO cubes support larger deployments and more specialized use cases

## Planning for Implementation

Organizations should prepare for the 25.07 update by:

- **Evaluating Access Governance**: Assess how Oracle Access Governance can improve identity management
- **Planning Role Separation**: Design new DI administrator roles and responsibilities
- **Identifying Automation Opportunities**: Find data integrations that could benefit from automatic execution
- **Testing New APIs**: Develop and test scripts using the new User/Group Management APIs
- **Assessing Cube Requirements**: Determine if additional BSO cubes are needed

[Read the full Oracle documentation →](https://docs.oracle.com/en/cloud/saas/readiness/epm/2025/epm-jul25/index.html)
