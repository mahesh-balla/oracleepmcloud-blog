---
title: 'Configuring Smart View for EPM Cloud — Setup and Troubleshooting Guide'
description: 'A complete guide to installing, configuring, and troubleshooting Oracle Smart View for Office connections to EPM Cloud, including common error resolution.'
product: 'epm-cloud-updates'
subcategory: 'tutorials'
pubDate: '2026-04-01'
---

## What is Smart View?

Smart View is an Excel add-in that connects Excel to EPM Cloud applications, allowing you to query, analyze, and submit data directly from within familiar spreadsheets. Instead of copying data between systems or using a separate web-based interface, users work in Excel with live connections to Planning, Financial Consolidation and Close Suite (FCCS), Narrative Reporting (NR), and Analytics Cloud.

Smart View includes advanced features like ad hoc analysis (pivoting dimensions dynamically), data entry with validation, and drill-through (trace values back to source data).

## System Requirements

Before installing Smart View, verify your environment meets these requirements:

| Component | Requirement |
|-----------|---|
| **Operating System** | Windows 10/11, macOS (limited support), or browser-based |
| **Microsoft Office** | Excel 2016 or newer (Office 2019, Office 365, Microsoft 365) |
| **Java** | Java 8 Update 60 or higher (Smart View embeds its own Java runtime as of 25.06) |
| **TLS/SSL** | TLS 1.3 required (since 25.06). Older TLS versions are no longer supported. |
| **Internet Connection** | Continuous HTTPS connectivity to your EPM Cloud instance |
| **Proxy/Firewall** | If behind a proxy, Smart View must be configured to use proxy settings |
| **Disk Space** | At least 500 MB for installation and cache |

## Installation and Setup

### Download Smart View

1. Log into your EPM Cloud instance.
2. Navigate to **Help > Downloads**.
3. Locate **Smart View for Office**.
4. Click **Download**.

The download is a `.exe` (Windows) or `.dmg` (macOS) installer.

### Install on Windows

1. Run the installer.
2. Accept the license agreement.
3. Choose installation path (default: `C:\Program Files\Oracle\SmartView`).
4. The installer creates a Start Menu shortcut and adds Smart View as an Excel add-in.
5. Restart Excel.
6. Verify the **Smart View** ribbon tab appears in Excel (between Data and Review tabs).

### Install on macOS

1. Run the `.dmg` installer.
2. Drag Smart View to the Applications folder.
3. Restart Excel.
4. Enable the add-in: Excel > Tools > Excel Add-ins > Smart View > Enable.

## Connection Configuration

Smart View uses two types of connections:

### Shared Connections (Administrator Configured)

System administrators provision shared connections to EPM Cloud applications. All users access the same connection URL, reducing configuration overhead.

**Location**: Configured in EPM Cloud under **Administration > Smart View Settings**.

**Example**: Your administrator creates a shared connection `EPM_PROD` pointing to `https://epm.us1.oraclecloudapps.com`.

Users simply select "EPM_PROD" from the Smart View provider dropdown—no URL to enter.

### Private Connections (User Configured)

Users create their own connections if shared connections aren't available or if they need access to a different instance.

**Steps to Create a Private Connection**:

1. In Excel, open the **Smart View** ribbon.
2. Click **Connections > New Connection**.
3. Enter connection details:
   - **Connection Name**: My EPM Prod
   - **Provider**: OracleEssbase (for Planning, FCCS, etc.)
   - **URL**: `https://your-instance.us1.oraclecloudapps.com`
4. Click **Test Connection**.
5. Enter your EPM Cloud username and password.
6. If the test succeeds, click **Save**.

## Connection URL Format

The connection URL structure is critical:

```
https://<instance-name>.<region>.oraclecloudapps.com
```

Example URLs by region:

| Region | Example URL |
|--------|---|
| US | `https://epm.us1.oraclecloudapps.com` |
| EMEA | `https://epm.eu2.oraclecloudapps.com` |
| APAC | `https://epm.ap1.oraclecloudapps.com` |

Your instance name and region are shown in the EPM Cloud console.

## Setting Up Connections to Specific Applications

### Planning

```
https://your-instance.us1.oraclecloudapps.com/HyperionPlanning
Provider: OracleEssbase
```

After connecting, you can select any Planning application from the dropdown.

### Financial Consolidation and Close Suite (FCCS)

```
https://your-instance.us1.oraclecloudapps.com/HyperionConsolidation
Provider: OracleEssbase
```

### Narrative Reporting (NR)

```
https://your-instance.us1.oraclecloudapps.com/Narrative
Provider: OracleEssbase
```

### Analytics Cloud (ARCS)

```
https://your-instance.us1.oraclecloudapps.com/Analytics
Provider: OracleEssbase
```

## Smart View for Google Workspace (New in 25.01)

Oracle released a browser-based Smart View for Google Workspace (Google Sheets alternative to Excel).

**How to Use**:

1. Open Google Sheets.
2. Click **Extensions > Add-ons > Get Add-ons**.
3. Search for "Oracle Smart View".
4. Click **Install**.
5. Authorize the add-on.
6. A "Smart View" menu appears in Sheets.
7. Configure connections and query EPM Cloud data.

**Limitations**: Not all Excel features are available (ad hoc analysis is limited, some custom formulas unsupported).

## Smart View for Mac and Browser

### Mac Support

Smart View for Mac is available but with limitations:
- No Excel ribbon (add-in interface is in a sidebar).
- Some ad hoc features unavailable.
- Performance may be slower than Windows version.

If possible, recommend Windows for power users requiring advanced Smart View features.

### Browser-Based Smart View

A web-based Smart View is in beta. It runs in any modern browser without Excel, useful for:
- Tablets and mobile devices.
- Environments where Excel isn't available.
- Remote/cloud-based desktops.

Check the **Downloads** page for browser availability in your region.

## Ad Hoc Analysis Basics

Ad hoc analysis is Smart View's killer feature—it lets you dynamically pivot EPM Cloud data without pre-building reports.

### Creating an Ad Hoc Query

1. In Excel, click **Smart View > Open > Ad Hoc Analysis**.
2. Select your connection and application.
3. A web-based interface opens.
4. Drag dimensions to Rows, Columns, and Page areas.
5. Select member selections (which entities, scenarios, periods).
6. Click **Refresh** to run the query.

Example:

```
Rows: Entity (US, Canada, Mexico)
Columns: Period (Jan, Feb, Mar, Apr)
Page: Scenario (Actual), Account (Revenue, COGS)
Values: (automatically calculated)
```

The result is an Excel table showing actuals revenue by entity and month. Modify the query and refresh—no need to go back to Planning UI.

### Performance Tips for Ad Hoc

- **Suppress Zeros**: Exclude cells with zero values (speeds up rendering).
- **Suppress Missing**: Exclude cells with no data (reduces clutter).
- **Limit Selections**: If you're pulling millions of cells, Smart View becomes slow. Narrow your member selections.

## Common Smart View Issues and Troubleshooting

### Issue 1: Cannot Reach Server

**Error**: "The server is not responding" or "Connection timed out".

**Troubleshooting**:

1. **Verify the URL**: Check that you're using the correct instance URL (no typos).
2. **Check Internet Connectivity**: Open a browser and navigate to your EPM Cloud instance. If the browser can't reach it, network/firewall is the issue.
3. **Verify Firewall Rules**: If behind a corporate firewall, ensure HTTPS (port 443) traffic to your instance is allowed.
4. **Proxy Configuration**: If your organization uses a proxy, configure Smart View to use it:
   - Click **Smart View > Options > Proxy**.
   - Enter your proxy server and port.
   - Test the connection.

### Issue 2: SSL/TLS Errors (TLS 1.3 Required Since 25.06)

**Error**: "SSL certificate error" or "Security handshake failed".

**Cause**: Smart View is using an outdated TLS version, or the certificate is not trusted.

**Solution**:

1. **Update Smart View**: Ensure you have 25.06 or later (which enforces TLS 1.3).
   - Uninstall Smart View.
   - Download the latest version from **Help > Downloads**.
   - Reinstall.

2. **Verify System TLS Settings**:
   - On Windows, open **Internet Options > Advanced** and ensure TLS 1.3 is enabled.
   - On macOS, TLS 1.3 is enabled by default in System 11+.

3. **Corporate Certificate**: If your organization uses a corporate root certificate, it may need to be installed on your workstation.
   - Contact your IT team to provide the root certificate.
   - Install it in your system's trusted certificate store.

### Issue 3: Login Loops or Repeated Authentication

**Issue**: Smart View keeps asking for credentials; you can never successfully log in.

**Cause**: Session tokens are expiring or not being cached properly.

**Solution**:

1. **Clear Smart View Cache**:
   - Windows: Delete `C:\Users\<username>\AppData\Local\Oracle\SmartView\cache`.
   - macOS: Delete `~/Library/Caches/Oracle/SmartView`.
   - Restart Excel.

2. **Check Identity Domain Settings**: Verify your user account is active and has the appropriate role (at minimum, "User" role).

3. **SSO Troubleshooting**: If SSO is enabled, verify your SSO provider (Azure AD, Okta) has your account active.

### Issue 4: Missing Add-in in Excel

**Issue**: Smart View ribbon doesn't appear in Excel.

**Cause**: The add-in wasn't installed correctly or was disabled.

**Solution**:

1. **Enable the Add-in**:
   - Excel > File > Options > Trust Center > Trust Center Settings > Trusted Add-ins.
   - Look for "Oracle Smart View for Office".
   - If it's listed as disabled, click it and enable it.

2. **Re-Register the Add-in**:
   - Windows: Open Command Prompt (Admin) and run:
     ```
     regsvr32 "C:\Program Files\Oracle\SmartView\bin\SV4Excel.dll"
     ```
   - Restart Excel.

3. **Reinstall**: If above steps don't work, uninstall and reinstall Smart View.

### Issue 5: Slow Query Performance

**Issue**: Ad hoc queries take minutes to load; Smart View is freezing.

**Possible Causes**:
- Selecting too many dimensions or members.
- Large sparse cubes with lots of missing data.
- Network latency or poor bandwidth.

**Solutions**:
1. **Reduce Query Scope**: Select fewer entities, periods, or scenarios.
2. **Enable Suppression**: Check "Suppress Zeros" and "Suppress Missing".
3. **Use Aliases**: If your dimension has long member names, display aliases instead (usually faster rendering).
4. **Check EPM Cloud Availability**: Run a business rule or data load in Planning to verify the cube is responsive. If it's slow there too, the issue is cube-side, not Smart View.

## Performance Optimization Tips

### 1. Query Optimization

- **Use member filters**: Instead of selecting all 1,000 entities, use Smart View's filter to show only active entities.
- **Limit time periods**: Don't pull 10 years of history if you only need 12 months.

### 2. Suppress Zeros and Missing Data

- **Right-click the query result > Suppress > Zeros and Missing**.
- This dramatically reduces the size of the result and improves rendering speed.

### 3. Use Native Mode (Deprecated, Migrate to Standard)

- **Important**: Native mode is deprecated as of 25.10.
- If you're still using native mode connections, plan to migrate to **Standard mode** (the current default).
- Native mode provided better performance in older versions but is no longer supported.

### 4. Refresh Strategy

- **Don't over-refresh**: Avoid pressing Refresh every few seconds.
- **Batch updates**: If loading multiple spreadsheets, load them sequentially, not in parallel (to avoid overwhelming the EPM Cloud instance).

## Configuring Smart View for Automation

### Scheduled Smart View Exports (Using EPM Automate)

You can automate Smart View exports using EPM Automate combined with Excel macros:

1. Create a Smart View query in Excel (save as `.xlsx`).
2. Write a macro that opens the file, refreshes Smart View queries, exports to CSV.
3. Schedule the macro via Windows Task Scheduler.

Example VBA macro:

```vba
Sub RefreshSmartViewAndExport()
    ' Connect to EPM Cloud and refresh all Smart View queries
    ThisWorkbook.RefreshAll

    ' Export to CSV
    ActiveSheet.SaveAs Filename:="C:\exports\data.csv", FileFormat:=xlCSV

    ' Close the file
    ThisWorkbook.Close SaveChanges:=False
End Sub
```

Schedule this macro to run nightly, and you have a fully automated Smart View export pipeline.

## Key Takeaways

1. **Smart View is Essential**: For Excel users, it's the most natural way to interact with EPM Cloud data.

2. **Configuration is Simple**: Connections are straightforward; shared connections (admin-provisioned) scale best.

3. **TLS 1.3 is Mandatory**: Ensure your Smart View version and system support TLS 1.3 (required since 25.06).

4. **Clear Cache for Most Issues**: Login loops, performance problems, and connection errors often resolve by clearing the Smart View cache.

5. **Ad Hoc Analysis is Powerful**: Master this feature to empower business users to analyze data without creating new reports.

6. **Optimize for Performance**: Suppress zeros/missing, reduce query scope, and batch large exports.

7. **Migrate from Native Mode**: If using native mode, plan your transition to Standard mode (deprecated in 25.10).

Smart View is a cornerstone of EPM Cloud usability. With proper configuration and troubleshooting strategies, you'll unlock powerful self-service analytics for your organization.
