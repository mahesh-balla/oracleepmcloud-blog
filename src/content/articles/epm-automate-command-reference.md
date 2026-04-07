---
title: 'EPM Automate Command Reference for Daily Operations'
description: 'A practical reference guide covering the most essential EPM Automate commands for daily administration, data operations, and automation scripting.'
product: 'epm-cloud-updates'
subcategory: 'epm-cloud-platform'
pubDate: '2026-04-04'
---

## What is EPM Automate?

EPM Automate is a command-line interface (CLI) tool that allows you to automate routine EPM Cloud tasks, schedule recurring operations, and integrate EPM Cloud with external systems. Instead of manually clicking through the EPM Cloud user interface, you write scripts that run data loads, execute business rules, manage users, and export/import data.

EPM Automate is essential for operational excellence—it eliminates manual steps, reduces human error, and enables 24/7 unattended automation.

## Installation and Prerequisites

### System Requirements

- **Java**: Java 17 (minimum) is required as of version 25.08. Earlier versions required Java 8 or 11, so verify your current EPM Automate version.
- **Operating System**: Windows, Linux, or macOS.
- **Network**: Your machine must have outbound HTTPS connectivity to your EPM Cloud instance.
- **Disk Space**: At least 500 MB for EPM Automate installation; more if you're handling large data exports.

### Installation Steps

1. Download EPM Automate from your EPM Cloud instance's **Help > Downloads** menu.
2. Extract the ZIP archive to a stable location (e.g., `C:\EPMAutomate` on Windows or `/opt/epmautomate` on Linux).
3. Verify Java is installed: `java -version`
4. Test connectivity: `epmautomate login -URL https://your-epm-instance.us1.oraclecloudapps.com -User admin -Password yourpassword`

## Authentication: The Login Command

Before any EPM Automate command executes, you must authenticate.

### Interactive Login

```
epmautomate login -URL https://your-instance.us1.oraclecloudapps.com -User yourusername -Password yourpassword
```

### Encrypted Password File (Recommended for Scripts)

Hardcoding passwords in scripts is a security risk. Use encrypted password files:

```
epmautomate encryptPassword -User yourusername -Password yourpassword -File encrypted.txt
```

Then reference it in your scripts:

```
epmautomate login -URL https://your-instance.us1.oraclecloudapps.com -User yourusername -PasswordFile encrypted.txt
```

### Best Practice

Store encrypted password files in a secure location with restricted file permissions. Rotate credentials regularly.

## Data Operations

### importData

Load data into EPM Cloud applications from external systems (GL, HR, sales systems, etc.).

```
epmautomate importData -File mydata.txt -Application Planning
```

**Key Parameters**:
- `-File`: Path to your data file (TXT, CSV, or Excel).
- `-Application`: Target application (Planning, FCCS, NR, ARCS).
- `-DataFile`: Alternative syntax for older versions.

**Common Use Cases**:
1. Monthly GL actuals load into Planning.
2. Headcount data load into workforce planning applications.
3. Product hierarchy refresh from a master data system.

**Pro Tip**: Validate your data file format against the EPM Cloud application's expected layout before automating. Test in your test environment first.

### exportData

Extract data from EPM Cloud for external reporting, archive, or analysis.

```
epmautomate exportData -Application Planning -File exporteddata.txt
```

**Key Parameters**:
- `-Application`: Source application.
- `-File`: Output file path.
- `-OutputType`: Format (txt, csv, xls, xlsx).

**Common Use Cases**:
1. Monthly export of actual results for external audit review.
2. Snapshot of forecast data for benchmarking.
3. Extract trial balance from a consolidation application for GL reconciliation.

## Calculation and Business Rules

### runBusinessRule

Execute a business rule within an EPM Cloud application.

```
epmautomate runBusinessRule -Application Planning -Name "Calculate Commission" -POV Entity:US,Scenario:Actual,Year:2026
```

**Key Parameters**:
- `-Application`: Target application.
- `-Name`: Business rule name.
- `-POV`: Point of view (dimensions and members) the rule operates on.

**Common Scenarios**:
1. Run allocation rules after loading actuals.
2. Execute consolidation logic at month-end.
3. Trigger automated calculations on-demand instead of waiting for scheduled runs.

### runDataRule

Execute a data rule (often used in Financial Consolidation and Close Suite).

```
epmautomate runDataRule -Application FCCS -Name "Intercompany Elimination"
```

### runBatchRule

Execute a batch rule that operates on multiple POV combinations.

```
epmautomate runBatchRule -Application Planning -Name "Monthly Consolidation"
```

Batch rules are more efficient than looping single-POV business rules, especially for large data volumes.

### clearCube

Clear all data from a cube (careful—this is irreversible without a backup).

```
epmautomate clearCube -Application Planning -Cube Actuals
```

**Warning**: Always back up your data before clearing. Use `exportData` or `exportSnapshot` first.

## Application Management

### refreshCube

Refresh aggregations and optimize cube storage after large data loads.

```
epmautomate refreshCube -Application Planning -Cube Actuals
```

Run this after loading large volumes of data to ensure query performance remains optimal.

### runPlanTypeMap

Map dimension members from one planning type to another (advanced Planning feature).

```
epmautomate runPlanTypeMap -Application Planning -PlanType "DetailedBudget"
```

### recreate

Recreate an application (metadata and structure) from scratch—useful for data archival or disaster recovery.

```
epmautomate recreate -Application Planning
```

This is a destructive operation. Use only in disaster recovery scenarios or after exporting data.

## Environment and Snapshot Management

### exportSnapshot

Export a complete snapshot of your application for backup or migration.

```
epmautomate exportSnapshot -Application Planning -File snapshot_20260405.zip
```

**What's Included**:
- Metadata (dimensions, members, member properties).
- Data (all cell values).
- Business rules and calculation scripts.
- Artifacts (reports, data rules, etc.).
- Security settings (if enabled).

**Typical Use**: Weekly or pre-update backups, disaster recovery preparation.

### importSnapshot

Import a previously exported snapshot.

```
epmautomate importSnapshot -Application Planning -File snapshot_20260405.zip
```

### exportUpdate

Export pending or applied updates.

```
epmautomate exportUpdate
```

### skipUpdate

Defer the next monthly update by one cycle.

```
epmautomate skipUpdate
```

Use cautiously and only when necessary. See the environment management article for detailed guidance.

### resetService

Reset a service or application to its initial state (very destructive).

```
epmautomate resetService -Application Planning
```

## User Management

### addUsers

Bulk add users to your EPM Cloud instance.

```
epmautomate addUsers -File users.txt
```

The file format is tab-delimited:
```
username email firstname lastname directoryid groupname role
```

### removeUsers

Remove users from the instance.

```
epmautomate removeUsers -User user1,user2,user3
```

### assignRole

Assign a role to a user.

```
epmautomate assignRole -User jsmith -Role ServiceAdministrator
```

Available roles: Viewer, User, PowerUser, ServiceAdministrator, IdentityDomainAdministrator.

### unassignRole

Remove a role from a user.

```
epmautomate unassignRole -User jsmith -Role ServiceAdministrator
```

## Reporting and Artifacts

### runBook

Execute an EPM Cloud book (report or dashboard) and trigger cascading exports.

```
epmautomate runBook -Book "Monthly Variance Report" -Application Planning
```

### downloadFile

Download a file (report output, export) from your EPM Cloud instance.

```
epmautomate downloadFile -File "variance_report.pdf" -LocalFile ./reports/variance.pdf
```

## Pipelines (25.02+)

### runPipeline

Execute a data pipeline (Data Exchange or custom integration pipeline).

```
epmautomate runPipeline -Name "GL_Actuals_Load" -Mode "SYNCHRONOUS"
```

**Parameters**:
- `-Name`: Pipeline name.
- `-Mode`: SYNCHRONOUS (wait for completion) or ASYNCHRONOUS (fire and forget).

Pipelines are the modern approach to data integration, replacing legacy Data Management (FDMEE).

## Scripting Patterns

### Windows Batch Script Example

```batch
@echo off
REM Weekly backup script for Planning application
REM Run Saturdays at 2:00 AM via Windows Task Scheduler

cd C:\EPMAutomate\bin
set TIMESTAMP=%date:~10,4%%date:~4,2%%date:~7,2%

echo Starting EPM Cloud backup at %date% %time%

epmautomate login -URL https://your-instance.us1.oraclecloudapps.com -User admin -PasswordFile encrypted.txt
epmautomate exportSnapshot -Application Planning -File "C:\Backups\Planning_Backup_%TIMESTAMP%.zip"

if %ERRORLEVEL% EQU 0 (
    echo Backup completed successfully
) else (
    echo Backup failed with error code %ERRORLEVEL%
)

epmautomate logout
```

### Linux Shell Script Example

```bash
#!/bin/bash
# Monthly data load for Planning application
# Run first day of month at 3:00 AM via crontab

EPM_HOME=/opt/epmautomate
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_FILE="/var/log/epm_automate_$TIMESTAMP.log"

cd $EPM_HOME/bin

echo "Starting EPM data load at $(date)" >> $LOG_FILE

./epmautomate login \
  -URL https://your-instance.us1.oraclecloudapps.com \
  -User admin \
  -PasswordFile encrypted.txt >> $LOG_FILE 2>&1

./epmautomate importData \
  -Application Planning \
  -File /data/actuals_$(date +%Y%m).txt >> $LOG_FILE 2>&1

EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo "Data load completed successfully" >> $LOG_FILE
else
    echo "Data load failed with error code $EXIT_CODE" >> $LOG_FILE
    # Send alert email here if critical
fi

./epmautomate logout >> $LOG_FILE 2>&1
```

## Scheduling with Task Scheduler (Windows) or Cron (Linux)

### Windows Task Scheduler

1. Open **Task Scheduler**.
2. Create a new task: **New Task**.
3. Set **Trigger**: Recurrence (daily, weekly, monthly).
4. Set **Action**: Start a program pointing to your batch script.
5. Set **Settings**: Run whether user is logged on or not, run with highest privileges.
6. Test by running the task manually.

### Linux Cron

Edit your crontab:

```
crontab -e
```

Add an entry (format: minute hour day month weekday command):

```
# Run data load at 3:00 AM on the 1st of each month
0 3 1 * * /opt/epmautomate/scripts/monthly_load.sh
```

Common cron frequencies:
- `0 2 * * *` — Every day at 2:00 AM
- `0 2 * * 1-5` — Weekdays at 2:00 AM
- `0 2 1 * *` — 1st of each month at 2:00 AM
- `*/15 * * * *` — Every 15 minutes

## Error Handling and Logging

### Capture Exit Codes

EPM Automate returns exit codes indicating success or failure:

```bash
epmautomate importData -Application Planning -File mydata.txt
if [ $? -eq 0 ]; then
    echo "Success"
else
    echo "Failed"
fi
```

Exit code 0 = success, non-zero = failure.

### Redirect Output to Log Files

```bash
epmautomate runBusinessRule -Application Planning -Name "MyRule" >> /var/log/rule_execution.log 2>&1
```

This captures both standard output and error messages.

### Add Timestamps to Logs

```bash
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting data load..." >> $LOG_FILE
```

## Key Takeaways for Administrators

1. **Automate Repetitive Tasks**: Data loads, business rule executions, and exports are perfect candidates for automation.

2. **Secure Your Credentials**: Use encrypted password files, never hardcode passwords in scripts.

3. **Test Before Scheduling**: Always test scripts in your test environment and on a small data subset.

4. **Monitor Execution**: Capture logs, exit codes, and errors. Alert on failures so you know if something breaks.

5. **Version Your Scripts**: Keep EPM Automate scripts in version control (Git) to track changes and enable rollback.

6. **Document Assumptions**: Comment your scripts with business logic (e.g., "This load expects GL data in column C").

7. **Consider Timing**: Schedule automation outside maintenance windows and peak business hours.

EPM Automate is the backbone of operational efficiency in EPM Cloud. Master these commands and you'll unlock the platform's full potential.
