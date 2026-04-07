---
title: 'Configuring EPM Cloud Backup and Recovery'
description: 'Best practices for backing up EPM Cloud applications, managing migration snapshots, and implementing a disaster recovery strategy with daily automated backups.'
product: 'epm-cloud-updates'
subcategory: 'tutorials'
pubDate: '2026-03-28'
---

## Oracle's Built-In Daily Backup

EPM Cloud is backed up automatically every day. You don't need to request this; it happens during your instance's maintenance window.

### What's Included in the Daily Backup

- **Application Data**: All cell values, user-submitted data, forecasts.
- **Metadata**: Dimensions, members, member properties, hierarchies.
- **Artifacts**: Business rules, calculation scripts, reports, dashboards, data load rules.
- **Security**: User assignments, roles, access controls.
- **System Files**: EPM Cloud configuration, integration settings.

Essentially, a complete snapshot of your application state.

### Backup Retention Period

Oracle retains the daily backup for a configurable period, typically **30 days**. This means you can restore from any day in the past month.

If you need to recover from a failure that occurred more than 30 days ago, you'll need a manual backup (more on that below).

### Backup Timing and Your Maintenance Window

The daily backup runs during your instance's maintenance window (typically a 4-hour window, e.g., 2:00 AM–6:00 AM PST). The maintenance window is configured when you provision your EPM Cloud instance.

**Important**: Schedule critical batch jobs, integrations, and data loads outside your maintenance window. If a load is running when the backup starts, the backup may fail or the load may be interrupted.

### Accessing Daily Backup Information

To view backup status:

1. Log into the Oracle Cloud Console (OCI).
2. Navigate to **EPM Cloud > Instances**.
3. Click your instance.
4. View the **Backup Status** and **Last Backup Date**.

EPM Automate also provides backup status:

```
epmautomate getServerProperties | grep -i backup
```

## Manual Backups: exportSnapshot

While the daily backup is automatic and transparent, you may want to manually export a snapshot for specific purposes:

- **Pre-change backup**: Before applying a major configuration change, export a snapshot.
- **Long-term archive**: Keep weekly/monthly snapshots in cloud storage for multi-year retention.
- **Migration**: Export from one instance, import to another.

### Exporting a Snapshot via EPM Automate

```bash
epmautomate exportSnapshot -Application Planning
```

This command creates a snapshot file (ZIP archive) containing all Planning data and metadata.

**Parameters**:
- `-Application`: Target application (Planning, FCCS, NR, ARCS).
- `-File`: Output filename (default: `snapshot_<timestamp>.zip`).

**Example**:

```bash
epmautomate exportSnapshot -Application Planning -File snapshot_pre_update_25.06.zip
```

### Snapshot File Format and Contents

The exported snapshot is a ZIP archive. When extracted, it contains:

```
snapshot/
├── data/
│   ├── actuals.txt
│   └── forecast.txt
├── metadata/
│   ├── dimensions.xml
│   ├── members.xml
│   └── properties.xml
├── artifacts/
│   ├── business_rules/
│   └── reports/
└── security/
    ├── users.xml
    └── roles.xml
```

### Snapshot File Size

Snapshot size varies by application volume:

- **Small Planning app** (< 1 GB of data): 100–500 MB snapshot.
- **Large Planning app** (> 10 GB of data): Several GB snapshot.

Factor this into your storage and network bandwidth planning.

## Downloading Snapshots to On-Premises Storage

By default, exported snapshots are stored on the EPM Cloud instance's file system. To retain them long-term, download them to your on-premises storage.

### Download via Oracle Cloud Console

1. Log into Oracle Cloud Console.
2. Navigate to **EPM Cloud > Instances > [Your Instance] > File Storage**.
3. Locate your snapshot file.
4. Click **Download**.

The snapshot downloads to your local machine.

### Download via EPM Automate

EPM Automate doesn't have a direct download command, but you can scripted retrieve snapshots:

```bash
# Export a snapshot
epmautomate exportSnapshot -Application Planning -File snapshot_20260407.zip

# Then use your OS's file copy mechanism
# On Windows:
copy C:\EPMAutomate\snapshots\snapshot_20260407.zip \\nas\backups\epm\

# On Linux:
scp C:\EPMAutomate\snapshots\snapshot_20260407.zip backup-server:/mnt/backups/epm/
```

## Automating Backups with EPM Automate

### Daily Automated Snapshot Script

Create a scheduled script that exports snapshots weekly:

**Linux Shell Script** (`/opt/epm-scripts/weekly_backup.sh`):

```bash
#!/bin/bash

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/mnt/backups/epm/"
LOG_FILE="/var/log/epm_backup_$TIMESTAMP.log"

cd /opt/epmautomate/bin

echo "Starting EPM Cloud backup at $(date)" > $LOG_FILE

# Login
./epmautomate login \
  -URL https://your-instance.us1.oraclecloudapps.com \
  -User admin \
  -PasswordFile encrypted.txt >> $LOG_FILE 2>&1

# Export snapshots for all applications
for app in Planning FCCS Narrative; do
    echo "Exporting $app..." >> $LOG_FILE
    ./epmautomate exportSnapshot \
      -Application $app \
      -File snapshot_${app}_$TIMESTAMP.zip >> $LOG_FILE 2>&1
done

# Download snapshots to NAS
cp *.zip $BACKUP_DIR >> $LOG_FILE 2>&1

# Verify backup size
BACKUP_SIZE=$(du -sh $BACKUP_DIR | awk '{print $1}')
echo "Total backup size: $BACKUP_SIZE" >> $LOG_FILE

# Cleanup old backups (keep last 12 weeks)
find $BACKUP_DIR -name "snapshot_*" -mtime +84 -exec rm {} \; >> $LOG_FILE 2>&1

./epmautomate logout >> $LOG_FILE 2>&1

echo "Backup completed at $(date)" >> $LOG_FILE
```

**Windows Batch Script** (`C:\EPMAutomate\scripts\weekly_backup.bat`):

```batch
@echo off
REM Weekly EPM Cloud backup script
REM Run via Windows Task Scheduler every Sunday at 2:00 AM

set TIMESTAMP=%date:~10,4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%
set BACKUP_DIR=\\nas\backups\epm
set LOG_FILE=C:\Logs\epm_backup_%TIMESTAMP%.log

cd C:\EPMAutomate\bin

echo Starting EPM Cloud backup at %date% %time% > %LOG_FILE%

epmautomate login -URL https://your-instance.us1.oraclecloudapps.com -User admin -PasswordFile encrypted.txt >> %LOG_FILE% 2>&1

REM Export snapshots
epmautomate exportSnapshot -Application Planning -File snapshot_Planning_%TIMESTAMP%.zip >> %LOG_FILE% 2>&1
epmautomate exportSnapshot -Application FCCS -File snapshot_FCCS_%TIMESTAMP%.zip >> %LOG_FILE% 2>&1

REM Copy to NAS
copy snapshot_*.zip %BACKUP_DIR% >> %LOG_FILE% 2>&1

epmautomate logout >> %LOG_FILE% 2>&1

echo Backup completed at %date% %time% >> %LOG_FILE%
```

### Scheduling the Script

**Linux (Crontab)**:

```bash
crontab -e
# Run weekly backup every Sunday at 2:00 AM
0 2 * * 0 /opt/epm-scripts/weekly_backup.sh
```

**Windows (Task Scheduler)**:

1. Open Task Scheduler.
2. Create a new task.
3. **Trigger**: Weekly, Sunday, 2:00 AM.
4. **Action**: Start program `C:\EPMAutomate\scripts\weekly_backup.bat`.
5. **Settings**: Run with highest privileges, run whether user is logged on or not.

## Disaster Recovery: Restoring from Backup

### Scenario 1: Restore from Daily Backup (< 30 Days Ago)

If data loss occurred within the last 30 days:

1. Contact Oracle Support.
2. Provide:
   - Instance name.
   - Target recovery date (e.g., "restore to March 25, 2026, 5:00 AM").
3. Oracle initiates a restore from the daily backup.
4. The restore runs during the maintenance window (typically takes 1–4 hours depending on data volume).

Your instance is temporarily unavailable during restore.

### Scenario 2: Restore from Exported Snapshot

If you have an exported snapshot (from days/weeks/months ago):

1. Use EPM Automate to import the snapshot:

```bash
epmautomate importSnapshot -Application Planning -File snapshot_pre_incident.zip
```

2. The snapshot is imported into the current application, merging with existing data or overwriting (depending on your merge strategy).

**Caution**: Importing a snapshot overwrites current state. Backup your current state first if you might need it.

### Scenario 3: Full Environment Recreation

If your environment is corrupted and unrecoverable:

1. Oracle provisions a new EPM Cloud instance with the same configuration.
2. You import your latest snapshot:

```bash
epmautomate importSnapshot -Application Planning -File latest_snapshot.zip
```

3. Validate that the import succeeded: check cube balances, verify member counts, test business rules.

## Testing Recovery Procedures

**Never assume backups work until you've tested them.**

### Recovery Test Procedure

1. **Export a snapshot** from your production instance.
2. **Import into your test environment** (or a temporary sandbox instance).
3. **Validate the import**:
   - Check cube balances: Do totals match what you expect?
   - Run a test query: Can you retrieve data correctly?
   - Validate member counts: Are all dimensions and members present?
   - Test a business rule: Does it execute correctly on restored data?
4. **Document results**: How long did import take? Were there any warnings?

Perform this test quarterly. If recovery takes 4 hours and you haven't tested it, you might discover in a real incident that it takes 6 hours—unacceptable if your SLA is 4 hours.

## Comprehensive Backup Strategy: Three-Tier Approach

A robust backup strategy combines daily, weekly, and pre-change snapshots:

### Tier 1: Daily Automatic Backups (Oracle)

- **Frequency**: Daily (runs during maintenance window).
- **Retention**: 30 days.
- **RPO** (Recovery Point Objective): 1 day (worst case, you lose 1 day of data).
- **RTO** (Recovery Time Objective): 4 hours (time for Oracle to restore).
- **Cost**: Included in EPM Cloud subscription.
- **Your Responsibility**: None (completely automatic).

### Tier 2: Weekly Manual Snapshots

- **Frequency**: Weekly (e.g., Sunday nights via automated script).
- **Retention**: 12 weeks (3 months).
- **Storage Location**: On-premises NAS or cloud storage (S3, Azure Blob).
- **RPO**: 7 days.
- **RTO**: 2–4 hours (you initiate the import).
- **Cost**: Storage only.
- **Your Responsibility**: Automate script, monitor execution, test quarterly.

### Tier 3: Pre-Change Snapshots

- **Frequency**: Before major changes (configuration updates, customization rollouts, version upgrades).
- **Retention**: Until change is validated (usually 1–2 weeks), then delete.
- **Storage Location**: EPM Cloud file system + downloaded to NAS.
- **RPO**: Zero (snapshot taken immediately before change).
- **RTO**: 1–2 hours (quick rollback if needed).
- **Cost**: Minimal (temporary storage).
- **Your Responsibility**: Remember to take the snapshot before major changes.

### Example Backup Timeline

```
Monday:   Automatic daily backup (Oracle, 30-day window)
         Weekly manual snapshot (exported, stored on NAS)

Tuesday:  Automatic daily backup

Thursday: Major configuration change planned
         Pre-change snapshot exported and verified
         Configuration change applied

Friday:   Change validation tests pass
         Pre-change snapshot deleted (no longer needed)

Monday:   Automatic daily backup
         Weekly manual snapshot (includes last week's data)
```

## Monitoring and Validation

### Backup Health Checks

Regularly verify backups are working:

```bash
# Check last backup timestamp
epmautomate getServerProperties | grep -i "last backup"

# Expected output: Last backup date = 2026-04-06 02:15:00

# If backup is more than 1 day old, investigate
if [ $(date -d "2026-04-06" +%s) -lt $(date -d "1 day ago" +%s) ]; then
    echo "WARNING: Last backup is older than 1 day"
    # Send alert email
fi
```

### Snapshot Integrity Checks

After exporting a snapshot, verify its integrity:

```bash
# Check file size (should be non-zero)
ls -lh snapshot_*.zip

# Extract and verify contents
unzip -t snapshot_*.zip
# Output: testing: data/actuals.txt OK...
```

### Set Alerts

If you have monitoring tools (Splunk, DataDog, Prometheus), set alerts:

- Alert if last backup is > 1 day old.
- Alert if backup file size is unusually small (potential data loss indicator).
- Alert if backup process fails (exit code non-zero).

## Folder Naming Fix (25.09+)

**Important Bug Fix**: As of 25.09, Oracle fixed an issue where folder names containing "/" characters caused backup failures.

If you're on 25.08 or earlier and your instance has "/" in folder names:

1. Rename affected folders before upgrading to 25.09.
2. Use valid folder names (alphanumeric, hyphens, underscores).

Example:

```
Bad: My-Planning/Q1-Budget
Good: My-Planning_Q1-Budget
```

After upgrading to 25.09, the "/" character is allowed in folder names without causing issues.

## Key Takeaways

1. **Oracle's Daily Backup is Automatic**: Don't rely on it alone; it's only retained 30 days.

2. **Export Weekly Snapshots**: Provide a second layer of backup beyond the 30-day window.

3. **Test Recovery Quarterly**: A backup is only useful if you know how to restore it. Test in your test environment.

4. **Pre-Change Snapshots are Insurance**: Before major updates or customizations, export a snapshot so you can quickly rollback if needed.

5. **Automate Everything**: Use scripts to export and download snapshots consistently. Manual backups are forgotten backups.

6. **Document Your Strategy**: Your runbook should clearly state:
   - Daily backups (automatic, 30-day retention).
   - Weekly snapshots (automated export, 12-week retention).
   - Pre-change snapshots (manual, variable retention).
   - Recovery procedures (who calls Oracle, how long it takes).

7. **Monitor Backup Health**: Set up alerts so you're notified if backups fail.

With a well-implemented three-tier backup strategy, you'll sleep soundly knowing your EPM Cloud data is protected against accidental deletion, corruption, or infrastructure failures.
