---
title: 'Configuration of SSO in EPM Cloud with Microsoft Entra ID'
description: 'A step-by-step guide for EPM administrators with IDCS roles to configure SAML-based Single Sign-On between Oracle EPM Cloud and Microsoft Entra ID, including coordination tasks for the Entra ID engineer and bulk user provisioning via CSV.'
product: 'epm-cloud-updates'
subcategory: 'tutorials'
pubDate: '2026-04-06'
---

Configuring Single Sign-On (SSO) between Oracle EPM Cloud and Microsoft Entra ID (formerly Azure AD) is a collaborative effort between your **EPM administrator** (who holds an Identity Domain Administrator role in IDCS/OCI IAM) and your **Entra ID engineer** (who holds a Global Administrator or Application Administrator role in the Microsoft Entra portal).

This article walks through the end-to-end process from the EPM resource's perspective. Where tasks must be completed by the Entra ID engineer, they are clearly marked so you can share the relevant sections with your counterpart.

---

## Prerequisites

Before you begin, confirm the following are in place:

- **Oracle EPM Cloud** subscription is active and accessible.
- You have **Identity Domain Administrator** access to the OCI IAM console (IDCS).
- Your Entra ID engineer has **Global Administrator**, **Cloud Application Administrator**, or **Application Administrator** privileges in Microsoft Entra.
- An AD security group called **EPMUSERS** has been provisioned in Entra ID. Client users who need EPM access will be added to this group.
- You have a list of users (email addresses) to provision in the EPM identity domain. A CSV file will be used for bulk upload.
- Both teams have agreed that **email address** will be the common identifier (NameID) across both platforms.

---

## Architecture Overview

The SSO flow uses **SAML 2.0** federation:

1. A user navigates to the EPM Cloud sign-in page.
2. The Oracle Identity Domain (IDCS) redirects the user to Microsoft Entra ID for authentication.
3. Entra ID authenticates the user (via the EPMUSERS group membership and enterprise app assignment).
4. Entra ID sends a SAML assertion back to IDCS with the user's email as the NameID.
5. IDCS matches the NameID to an existing user in the EPM identity domain and grants access.

**Key point:** Users must exist in both Entra ID *and* the EPM identity domain. The SAML federation handles authentication, but authorization (roles, access) is managed within EPM Cloud.

---

## Phase 1: Export Service Provider Metadata from Oracle (EPM Resource)

You need to export your Oracle identity domain's SAML metadata and share it with the Entra ID engineer.

### Step 1 — Enable Client Access to the Signing Certificate

1. Sign in to the **OCI Console** at [https://cloud.oracle.com](https://cloud.oracle.com).
2. Navigate to **Identity & Security** > **Domains**.
3. Click on the identity domain associated with your EPM Cloud subscription.
4. Go to **Settings** > **Domain settings**.
5. Under **Access signing certificate**, check **Configure client access**.
6. Click **Save changes**.

### Step 2 — Download the SP Metadata File

1. From the identity domain overview page, copy the **Domain URL**. It will look like:
   ```
   https://idcs-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.identity.oraclecloud.com
   ```
2. In a new browser tab, append `/fed/v1/metadata` to the Domain URL:
   ```
   https://idcs-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.identity.oraclecloud.com/fed/v1/metadata
   ```
3. The SAML metadata XML will display in the browser.
4. Save it as **OCIMetadata.xml**.

### Step 3 — Share with Entra ID Engineer

Send the **OCIMetadata.xml** file to your Entra ID engineer along with the following information:

- **Identity Domain URL:** `https://idcs-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.identity.oraclecloud.com`
- **NameID format:** Email Address
- **Expected NameID claim:** `user.mail`

Also share the **SAML endpoint URLs** they will need for manual configuration (if metadata import does not work):

| Parameter | Value |
|-----------|-------|
| **Entity ID (Identifier)** | `https://idcs-XXXXXXXX.identity.oraclecloud.com:443/fed` |
| **Reply URL (ACS)** | `https://idcs-XXXXXXXX.identity.oraclecloud.com:443/fed/v1/sp/sso` |
| **Sign-on URL** | `https://idcs-XXXXXXXX.identity.oraclecloud.com:443/fed/v1/sp/sso` |
| **Logout URL** | `https://idcs-XXXXXXXX.identity.oraclecloud.com:443/fed/v1/sp/slo` |

Replace `XXXXXXXX` with your actual CUSTOMER_IDENTIFIER (the alphanumeric string after `idcs-` in your domain URL).

---

## Phase 2: Tasks for the Entra ID Engineer (Share This Section)

> **EPM Resource Note:** Share this entire section with your Entra ID engineer. These steps must be performed in the Microsoft Entra admin center at [https://entra.microsoft.com](https://entra.microsoft.com).

### Step 4 — Create the Enterprise Application

1. Sign in to the **Microsoft Entra admin center**.
2. Navigate to **Identity** > **Applications** > **Enterprise applications**.
3. Click **New application**.
4. Search for **Oracle Cloud Infrastructure Console** in the gallery.
5. Select the **Oracle Cloud Infrastructure Console by Oracle Corporation** tile.
6. Enter a name for the application (e.g., `Oracle EPM Cloud SSO`).
7. Click **Create**.

### Step 5 — Configure SAML-Based SSO

1. In the enterprise application, navigate to **Manage** > **Single sign-on**.
2. Select **SAML** as the single sign-on method.
3. Click **Upload metadata file** and select the **OCIMetadata.xml** file received from the EPM resource.
4. In the **Sign on URL** field, enter:
   ```
   https://idcs-XXXXXXXX.identity.oraclecloud.com/ui/v1/myconsole
   ```
5. Click **Save**.

**If metadata upload is not available**, manually enter the values in the **Basic SAML Configuration** section:

| Field | Value |
|-------|-------|
| **Identifier (Entity ID)** | `https://idcs-XXXXXXXX.identity.oraclecloud.com:443/fed` |
| **Reply URL** | `https://idcs-XXXXXXXX.identity.oraclecloud.com:443/fed/v1/sp/sso` |
| **Sign on URL** | `https://idcs-XXXXXXXX.identity.oraclecloud.com:443/fed/v1/sp/sso` |
| **Logout URL** | `https://idcs-XXXXXXXX.identity.oraclecloud.com:443/fed/v1/sp/slo` |

Check the **Default** box next to the Entity ID. Click **Save**.

### Step 6 — Configure Attributes and Claims

1. In the **Attributes & Claims** section, click **Edit**.
2. Click on **Unique User Identifier (Name ID)**.
3. Change the **Source attribute** from `user.userprincipalname` to `user.mail`.
4. Ensure the **Name identifier format** is set to **Email address**.
5. Click **Save**.

This ensures Entra ID sends the user's email address as the SAML NameID, which Oracle IDCS uses to match users.

### Step 7 — Assign the EPMUSERS Group

1. In the enterprise application, navigate to **Manage** > **Users and groups**.
2. Click **Add user/group**.
3. Under **Users and groups**, click **None Selected**.
4. Search for and select the **EPMUSERS** group.
5. Click **Select**, then click **Assign**.

All members of the EPMUSERS group will now be authorized to authenticate via this enterprise application.

### Step 8 — Download the Entra ID Federation Metadata

1. Return to the **Single sign-on** page.
2. In the **SAML Signing Certificate** section, click **Download** next to **Federation Metadata XML**.
3. Save the file (e.g., `EntraID_Federation_Metadata.xml`).
4. **Send this file back to the EPM resource** to complete the IDCS configuration.

---

## Phase 3: Configure Entra ID as IdP in Oracle IDCS (EPM Resource)

Once you receive the **Federation Metadata XML** from the Entra ID engineer, proceed with the following steps.

### Step 9 — Add SAML Identity Provider

1. Sign in to the **OCI Console** and navigate to **Identity & Security** > **Domains**.
2. Click on your EPM identity domain.
3. Go to **Security** > **Identity providers**.
4. Click **Add IdP** > **Add SAML IdP**.

### Step 10 — Enter IdP Details

1. **Name:** Enter `Microsoft Entra ID` (or your preferred display name).
2. **Description:** (Optional) `SAML SSO integration with Microsoft Entra ID for EPM Cloud users`.
3. Click **Next**.

### Step 11 — Import Metadata

1. Select **Import identity provider metadata**.
2. Browse and select the **EntraID_Federation_Metadata.xml** file received from the Entra ID engineer.
3. The SAML endpoints and signing certificate will auto-populate.
4. Click **Next**.

### Step 12 — Map User Identity

Configure the following attribute mappings:

| Setting | Value |
|---------|-------|
| **Requested NameID format** | Email address |
| **Identity provider user attribute** | SAML assertion Name ID |
| **Identity domain user attribute** | Primary email address |

This tells IDCS to match the incoming SAML NameID (email) against the **Primary email address** of users in the identity domain.

Click **Next**.

### Step 13 — Review and Create

1. Review all the configuration details on the summary page.
2. Click **Create IdP**.

### Step 14 — Test the SSO Connection

Before activating for all users, test the connection:

1. Under **Identity Providers**, click on **Microsoft Entra ID**.
2. Click the **Actions** menu (three dots) > **Test Login**.
3. You will be redirected to the Microsoft login page.
4. Authenticate with a user account that exists in both Entra ID (assigned to the enterprise app) and the EPM identity domain.
5. On success, you will see: **"Your connection is successful."**

If the test fails, verify:
- The user exists in both systems with the same email address.
- The user is assigned to the enterprise application (or is a member of the EPMUSERS group).
- The NameID format matches (Email address on both sides).

### Step 15 — Activate the Identity Provider

1. On the Microsoft Entra ID details page, click **Actions** > **Activate IdP**.
2. The IdP status changes to **Active**.

### Step 16 — Configure IdP Policy Rule

You need to assign the newly activated IdP to a policy rule so that users see it as a sign-in option.

**Option A: Add to the Default Policy**

1. Navigate to **Security** > **Identity providers**.
2. Scroll to **Identity Provider Policies** section.
3. Click on **Default Identity Provider Policy**.
4. Click the **Actions** menu > **Edit IdP rule**.
5. Under **Assign identity providers**, select **Microsoft Entra ID**.
6. Click **Save Changes**.

**Option B: Create a Dedicated Policy (Recommended for Production)**

1. On the **Identity providers** page, scroll to **Identity Provider Policies**.
2. Click **Create IdP policy**.
3. Enter a name (e.g., `EPM SSO Policy`).
4. Click **Create identity provider policy**.
5. Navigate to the **Identity Provider Rules** tab, click **Add IdP rule**.
6. Enter a rule name (e.g., `Entra ID SSO Rule`).
7. Under **Assign identity providers**, select **Microsoft Entra ID**.
8. Configure conditions as needed (e.g., apply to all users or specific groups).
9. Click **Add IdP rule**.
10. Navigate to the **Applications** tab, click **Add apps**.
11. Search for and assign the EPM Cloud applications that should use this SSO policy.
12. Click **Add App**.

---

## Phase 4: Bulk User Provisioning in EPM Identity Domain (EPM Resource)

Users must exist in the EPM identity domain before they can authenticate via SSO. Use a CSV file to provision users in bulk.

### Step 17 — Prepare the User CSV File

Create a CSV file with the following columns. The **email address must match** what is in Entra ID:

```csv
First Name,Last Name,Email,User Login,Identity Domain Role
John,Smith,john.smith@clientdomain.com,john.smith@clientdomain.com,Identity Domain User
Sarah,Johnson,sarah.johnson@clientdomain.com,sarah.johnson@clientdomain.com,Identity Domain User
Michael,Chen,michael.chen@clientdomain.com,michael.chen@clientdomain.com,Identity Domain User
Lisa,Williams,lisa.williams@clientdomain.com,lisa.williams@clientdomain.com,Identity Domain User
David,Brown,david.brown@clientdomain.com,david.brown@clientdomain.com,Identity Domain User
```

**Important notes on the CSV:**

- The **User Login** and **Email** fields should both contain the user's corporate email address.
- This email must match the `user.mail` attribute in Entra ID (used as the SAML NameID).
- The **Identity Domain Role** column is for the IDCS role. EPM application roles (e.g., Planner, Viewer, Admin) are assigned separately within the EPM Cloud application.

### Step 18 — Import Users via OCI Console

1. In the OCI Console, navigate to **Identity & Security** > **Domains** > your identity domain.
2. Go to **Users**.
3. Click **Import users**.
4. Browse and select your CSV file.
5. Review the import summary and click **Import**.
6. Verify that all users appear in the user list with status **Active**.

### Step 19 — Assign EPM Application Roles

After importing users, assign them to the appropriate EPM predefined roles:

1. In the OCI Console, navigate to your identity domain.
2. Go to **Oracle Cloud Services**.
3. Click on the EPM Cloud application instance.
4. Navigate to **Application Roles**.
5. Assign users to the appropriate roles:
   - **Service Administrator** — Full administrative access
   - **Power User** — Create and manage artifacts
   - **User** — Standard user access (run forms, view reports)
   - **Viewer** — Read-only access

Alternatively, use **EPM Automate** for bulk role assignment:

```bash
epmautomate login admin@domain.com password https://epm-instance.epm.us-phoenix-1.ocs.oraclecloud.com

epmautomate assignRole "john.smith@clientdomain.com" "Power User"
epmautomate assignRole "sarah.johnson@clientdomain.com" "User"
```

---

## Phase 5: End-to-End Validation

### Step 20 — Test SP-Initiated SSO

1. Open a browser and navigate to your **EPM Cloud URL**.
2. On the sign-in page, you should see the **Microsoft Entra ID** option alongside the default IDCS login.
3. Click **Microsoft Entra ID**.
4. You will be redirected to the Microsoft login page.
5. Sign in with a test user account that is:
   - A member of the **EPMUSERS** group in Entra ID.
   - Provisioned in the EPM identity domain with a matching email.
   - Assigned an EPM application role.
6. After successful authentication, you should land on the **EPM Cloud home page**.

### Step 21 — Test IdP-Initiated SSO (Optional)

1. Sign in to [https://myapps.microsoft.com](https://myapps.microsoft.com).
2. Click the **Oracle EPM Cloud SSO** application tile.
3. You should be automatically redirected and signed into EPM Cloud.

---

## Troubleshooting Common Issues

**"AADSTS50105: User not assigned to application"**
The user is not assigned to the enterprise application in Entra ID. Ensure they are a member of the EPMUSERS group and the group is assigned to the application.

**"User not found" in IDCS after redirect**
The user exists in Entra ID but not in the EPM identity domain. Import the user via CSV and ensure the email address matches exactly.

**NameID mismatch**
Verify that Entra ID is sending `user.mail` (not `user.userprincipalname`) and that the IDCS mapping is set to **Primary email address**.

**Certificate expiry**
SAML signing certificates in Entra ID expire (typically after 3 years). Set a calendar reminder to rotate the certificate and re-import the updated metadata into IDCS before expiry.

**SSO works but EPM shows "No roles assigned"**
The user is authenticated but has no EPM application roles. Assign the appropriate predefined role (User, Power User, etc.) in the identity domain.

---

## Summary: Responsibility Matrix

| Task | Owner | Platform |
|------|-------|----------|
| Export SP metadata (OCIMetadata.xml) | EPM Resource | OCI Console |
| Create enterprise application | Entra ID Engineer | Microsoft Entra |
| Configure SAML SSO settings | Entra ID Engineer | Microsoft Entra |
| Set NameID to user.mail | Entra ID Engineer | Microsoft Entra |
| Assign EPMUSERS group | Entra ID Engineer | Microsoft Entra |
| Export IdP metadata (Federation XML) | Entra ID Engineer | Microsoft Entra |
| Add SAML IdP in IDCS | EPM Resource | OCI Console |
| Map user identity attributes | EPM Resource | OCI Console |
| Test and activate IdP | EPM Resource | OCI Console |
| Configure IdP policy rule | EPM Resource | OCI Console |
| Prepare and import user CSV | EPM Resource | OCI Console |
| Assign EPM application roles | EPM Resource | OCI Console |
| End-to-end SSO validation | Both Teams | Both Platforms |

---

## References

- [Oracle: Setting up SSO for EPM Cloud using Microsoft Entra ID](https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/cgsad/3_sso_config_chap_idcs_oci_azure.html)
- [Oracle: Steps to Complete in Microsoft Entra ID](https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/cgsad/3_sso_config_chap_idcs_oci_azure_config.html)
- [Oracle: Steps to Complete in Oracle Cloud Console](https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/cgsad/sso_steps_in_iam.html)
- [Oracle: SSO Between OCI and Microsoft Entra ID Tutorial](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/sso_azure/azure_sso.htm)
- [Microsoft: Configure Oracle Cloud Infrastructure Console SSO](https://learn.microsoft.com/en-us/entra/identity/saas-apps/oracle-cloud-tutorial)
