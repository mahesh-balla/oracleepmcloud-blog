---
title: 'Managing EPM Cloud Identity Domains and User Provisioning'
description: 'A complete guide to managing users, groups, and roles in the EPM Cloud OCI Identity Domain, including bulk provisioning via CSV, SCIM, and role assignment strategies.'
product: 'epm-cloud-updates'
subcategory: 'epm-cloud-platform'
pubDate: '2026-04-03'
---

## Identity Domain Overview

EPM Cloud uses Oracle Cloud Infrastructure (OCI) Identity Domain as its user and access management system. This replaces the older IDCS (Identity Cloud Service) architecture and provides tighter integration with OCI services.

Your OCI Identity Domain is the central source of truth for:

- User accounts and credentials
- Group memberships
- Role assignments
- Multi-factor authentication policies
- Single sign-on (SSO) integrations

Unlike traditional on-premises directory systems, the OCI Identity Domain is cloud-native, scalable, and integrated directly with your EPM Cloud provisioning.

## Accessing the Identity Domain Console

To manage users, groups, and roles:

1. Log into your Oracle Cloud Console (the main infrastructure dashboard, not EPM Cloud).
2. Navigate to **Identity and Security > Domains**.
3. Click on your EPM Cloud's domain name (typically `Default` or named after your organization).
4. You're now in the Identity Domain admin console.

From here, you can create users, manage groups, assign roles, and configure security policies.

## User Lifecycle Management

### Creating Users Manually

1. In the Identity Domain console, select **Users**.
2. Click **Create User**.
3. Fill in required fields:
   - **Username**: Unique identifier (often email format, e.g., `john.smith@company.com`).
   - **First Name, Last Name**: Display name components.
   - **Email**: Contact email.
4. Set **Password Option**: Temporary password (user must change on first login) or send activation email.
5. Click **Create**.

**Best Practice**: Use email as the username for consistency and easier identification.

### Bulk User Provisioning via CSV Import

For organizations adding 10+ users at once, CSV import is efficient:

1. In the Identity Domain console, select **Users**.
2. Click **Import Users** (or **Bulk Actions > Import**).
3. Prepare a CSV file with columns:
   ```
   username,givenname,familyname,email,active
   john.smith@company.com,John,Smith,john.smith@company.com,true
   jane.doe@company.com,Jane,Doe,jane.doe@company.com,true
   ```
4. Upload the CSV.
5. Review the import preview and confirm.

Oracle processes the import asynchronously. Users are created with temporary passwords; they must set their password on first login.

### Bulk User Provisioning via EPM Automate

For automation, use the `addUsers` EPM Automate command:

```
epmautomate addUsers -File users.txt
```

The file format (tab-delimited) is:

```
username email firstname lastname directoryid groupname role
jsmith john.smith@company.com John Smith DEFAULT admins ServiceAdministrator
jdoe jane.doe@company.com Jane Doe DEFAULT users User
```

This approach integrates user creation directly into your provisioning scripts and CI/CD pipelines.

### User Activation and First Login

When a new user is created:

1. They receive an activation email with a link.
2. Clicking the link takes them to an Oracle Identity page where they set their password.
3. On first login to EPM Cloud, they're presented with their password reset prompt.

**Pro Tip**: Coordinate new user announcements with IT to ensure users understand they need to activate their accounts. Monitor failed login attempts to catch users who haven't activated yet.

### Deactivating Users (Offboarding)

When a user leaves your organization:

1. In the Identity Domain console, find the user.
2. Click **Deactivate** (or **More Actions > Deactivate**).
3. Deactivated users cannot log in but their account remains in the system for audit purposes.

**Alternative**: Delete the user entirely if no audit trail is needed. Deletion is permanent and cannot be undone.

## Predefined Roles

EPM Cloud provides a set of built-in roles controlling what users can do:

### Identity Domain Administrator

- Full administrative access to the Identity Domain.
- Can create/deactivate users, manage groups, configure SSO.
- Limited application-level access (not an EPM application admin by default).

### Service Administrator

- Full administrative access to EPM Cloud applications.
- Can manage application settings, create/modify cubes, assign application-level roles.
- Cannot create or delete users (that's Identity Domain Administrator's job).

### Power User

- Can create and modify business rules, reports, and planning models.
- Can create and manage users within the application (not the identity domain).
- Can load data and execute jobs.
- Cannot modify application structure (dimensions, members).

### User

- Standard application user.
- Can view, query, and submit data.
- Cannot create reports or modify business rules.
- Role is application-specific; a User in Planning might be a Viewer in FCCS.

### Viewer

- Read-only access to reports and dashboards.
- Cannot modify any data or metadata.
- Lowest privilege level.

## Application-Specific Roles

Beyond the predefined global roles, many EPM Cloud applications define custom roles:

- **Planning Module**: Planner, Analyst, Reviewer roles control visibility and modification rights to different plan types.
- **Financial Consolidation**: Consolidation Manager, Intercompany Manager roles control close process steps.
- **Narrative Reporting**: Template Designer, Report Contributor, Report Viewer roles control report creation and access.

Assign application-specific roles after assigning a global role. For example:

1. Assign global role: **Service Administrator**
2. Assign application role: **Planning Analyst** (within the Planning application)

## Role Assignment Strategies

### Principle of Least Privilege

Assign the minimum role necessary for a user to perform their job:

- Month-end close data reviewers: **User** role.
- Business rule developers: **Power User** role.
- Platform operations: **Service Administrator** role.

Avoid over-provisioning to the **Service Administrator** role. It's a high-privilege role; use it sparingly.

### Bulk Role Assignment

Assign roles to groups, not individuals, for scalability:

1. Create a group: `epm_power_users`
2. Add users to the group.
3. Assign the **Power User** role to the group.

Now, any user added to `epm_power_users` automatically inherits the **Power User** role. This is far more maintainable than assigning roles to 50 individual users.

### Role Hierarchy Example

For a typical mid-sized organization:

| Role | Team Size | Responsibility |
|------|-----------|---|
| Service Administrator | 1-2 | Platform ops, updates, monitoring |
| Power User | 10-20 | Business rule development, reporting, advanced analytics |
| User | 50-100 | Planning, data entry, month-end close |
| Viewer | 20-50 | Executive dashboards, read-only reporting |

## Group Management

### Creating Groups

1. In the Identity Domain console, select **Groups**.
2. Click **Create Group**.
3. Provide a **Name** and optional **Description**.
4. Click **Create**.

### Adding Members to Groups

1. Open the group.
2. Click **Add Members**.
3. Search and select users.
4. Click **Add**.

### Mapping Groups to Roles

1. In EPM Cloud, navigate to **Administration > Security > User Management** (or similar, depending on your application).
2. Find the group and assign it a role (e.g., assign `epm_power_users` group to **Power User** role).

Now all members of `epm_power_users` inherit the **Power User** role.

## Bulk User Provisioning via SCIM API

For enterprise environments with centralized identity management (e.g., Okta, Azure AD, Workday), SCIM (System for Cross-domain Identity Management) enables two-way user synchronization.

### What is SCIM?

SCIM is an open standard for user provisioning. Your identity provider (IdP) can automatically create, update, and delete users in your OCI Identity Domain without manual intervention.

### Configuration Steps

1. In your OCI Identity Domain, navigate to **Integrations > SCIM**.
2. Note your SCIM endpoint and generate a bearer token.
3. In your IdP (e.g., Okta), add a new SAML/SCIM integration for OCI.
4. Configure the SCIM endpoint and token.
5. Map identity provider user attributes (email, first name, last name) to OCI Identity Domain attributes.
6. Enable provisioning and test with a pilot user.

Once configured, when you hire a new employee in your IdP, the user is automatically provisioned in the OCI Identity Domain and gains access to EPM Cloud.

### Sunset Old Users Automatically

SCIM also supports deprovisioning: when you deactivate a user in your IdP, they're automatically deactivated in the OCI Identity Domain.

## SSO Integration

The OCI Identity Domain integrates with common SSO providers. See the dedicated SSO configuration article for details on Microsoft Entra ID, Okta, and other identity providers.

When SSO is enabled:

- Users log in with their organization credentials (no separate EPM Cloud password).
- Password policies, MFA, and conditional access are managed by your organization's IdP.
- User lifecycle (create, deactivate, delete) is synchronized from your IdP.

## Best Practices for User Provisioning

### 1. Automate Bulk Operations

- Use CSV import or SCIM for adding users at scale.
- Use EPM Automate `addUsers` for integration with provisioning scripts.
- Avoid manual creation of users one-by-one except in rare cases.

### 2. Implement Role-Based Access Control (RBAC)

- Never assign roles directly to individuals. Use groups.
- Create groups aligned with job functions: `epm_planners`, `epm_closed_loop_reviewers`, etc.
- Make group membership the source of role assignment.

### 3. Conduct Regular Access Reviews

- Quarterly (or semi-annually), audit who has access and their roles.
- Deactivate users who have changed roles or left the organization.
- Update group memberships as teams reorganize.

### 4. Enforce MFA

- Require multi-factor authentication (MFA) for all users, especially Service Administrators.
- In the Identity Domain, navigate to **Authentication Policies** and enforce MFA at login.

### 5. Monitor Sign-In Activity

- Review login logs (Identity Domain > Sign In Logs) for unusual activity.
- Alert on repeated failed login attempts (potential brute force).
- Track admin access (Service Administrator logins) for compliance.

### 6. Plan for Offboarding

- Document your offboarding process: who deactivates users, how quickly.
- Deactivate users immediately upon termination (don't wait for HR paperwork).
- Consider mailbox retention and data access policies post-offboarding.

### 7. Document Role Definitions

- Maintain a matrix of roles and responsibilities.
- Include examples: "A Planner can submit plans but cannot approve them."
- Share with your HR/org development teams so onboarding is consistent.

## Troubleshooting Common Issues

### User Cannot Log In

1. Check if the user is **Activated**: Identity Domain > Users > User Details > Status should be "Active".
2. Check if the user is assigned a **role**: EPM Cloud > Administration > User Management. User should have at least a "User" or "Viewer" role.
3. Check if the account is **locked** due to repeated failed login attempts (reset by Identity Domain admin).
4. If SSO is enabled, verify the user exists in the SSO provider (e.g., Azure AD).

### User Has Old Role After Group Change

- **Issue**: You removed a user from a group but they still have the old role in EPM Cloud.
- **Solution**: EPM Cloud may cache role information. Have the user log out and log back in. If the issue persists, contact Oracle Support to refresh the identity cache.

### Bulk Import Shows Errors

- **Issue**: CSV import shows "Invalid format" or "Email already exists".
- **Solution**: Verify CSV format (correct delimiters, no extra spaces). Check for duplicate emails. Try importing a smaller batch to isolate the problem.

## Key Takeaways

1. **OCI Identity Domain** is the authoritative source of user identity and roles for EPM Cloud.

2. **Bulk provisioning** via CSV, EPM Automate, or SCIM scales better than manual user creation.

3. **Assign roles to groups, not individuals**—it's more maintainable as your organization grows.

4. **Predefined roles** (Service Administrator, Power User, User, Viewer) provide a structured access model.

5. **SSO and SCIM integration** automate the entire user lifecycle and align with enterprise identity governance.

6. **Regular access reviews** ensure users only have the access they need.

With these practices, you'll maintain a secure, scalable, and auditable user provisioning process for EPM Cloud.
