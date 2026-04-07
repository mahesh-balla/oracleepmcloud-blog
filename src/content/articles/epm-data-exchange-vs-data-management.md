---
title: 'Data Exchange vs Data Management (FDMEE) — Which Should You Use?'
description: 'Oracle is retiring Data Management. This guide compares Data Exchange and Data Management to help administrators plan their migration to the modern integration platform.'
product: 'epm-cloud-updates'
subcategory: 'epm-cloud-platform'
pubDate: '2026-04-02'
---

## The Evolution: FDMEE → Data Management → Data Exchange

Oracle's approach to data integration in EPM Cloud has evolved over the past decade. Understanding this progression clarifies why Data Management is being retired.

### FDMEE (Financial Data Quality Management for Enterprise Edition)

FDMEE was Oracle's on-premises data integration tool. It provided a GUI for building data load mappings, validating source data, and loading into Planning and Consolidation applications. FDMEE was powerful but required significant infrastructure.

### Data Management (2016–2026)

When EPM Cloud launched, Oracle ported FDMEE's capabilities into a cloud-native version called **Data Management**. It replicated much of FDMEE's workflow: create a data load rule, define mappings, validate, and load.

Data Management served the market well for nearly a decade, but it had architectural limitations:

- **Monolithic Design**: Each load rule was a standalone object; there was no concept of reusable pipelines.
- **Limited Extensibility**: Custom logic required Java or Python scripts embedded in the rule.
- **Single-Purpose**: Designed for periodic data loads, not continuous integration or streaming.
- **Scaling Challenges**: Performance degraded with very large data volumes (terabytes).

### Data Exchange (2023–Present)

Launching in 2023, **Data Exchange** is a complete redesign for the cloud era. It introduces pipelines—composable, reusable workflows that can extract, transform, and load data with flexibility and scale. Data Exchange is Oracle's strategic investment in cloud-native data integration.

## Feature Comparison: Data Management vs Data Exchange

| Feature | Data Management | Data Exchange |
|---------|---|---|
| **Load Type** | Periodic (scheduled) | Periodic, on-demand, event-driven |
| **Pipeline Concept** | No | Yes (reusable, composable stages) |
| **Mapping GUI** | Yes (rule-based) | Yes (block-based visual builder) |
| **Data Sources** | Limited (files, JDBC, REST) | Expanded (files, databases, cloud services, SFTP—25.09+) |
| **Drill-Through** | Yes | Yes (in roadmap) |
| **Validation Rules** | Yes (basic) | Yes (advanced validation framework) |
| **Error Handling** | File-based error logs | Integrated error logs, retry logic |
| **Scheduling** | Cron/calendar-based | Cron + event-triggered |
| **Location Security** | No | Yes (25.06+—data stays in configured region) |
| **SFTP Support** | No | Yes (25.09+) |
| **Copy Pipeline** | No | Yes (25.05+—bulk data copy between instances) |
| **Performance (TB+ scale)** | Limited | Optimized |
| **Maintenance Status** | Retiring (end-of-life 2026) | Active development |

## What Data Exchange Adds Beyond Data Management

### 1. Pipelines (Reusable, Composable Workflows)

Instead of monolithic data load rules, Data Exchange uses pipelines—sequences of blocks (extract, transform, load, validate) that can be reused across different loads.

Example Pipeline:

```
[CSV File Source] → [Column Mapping] → [Data Validation]
  → [Smart Lookup] → [EPM Cloud Target] → [Success Notification]
```

This same pipeline can load GL actuals, headcount data, or FX rates—just swap the source file and target application.

### 2. Copy Pipeline (25.05+)

Copy Pipeline is a purpose-built pipeline type for migrating large volumes of data between EPM Cloud instances (e.g., from dev to test, test to prod).

**Use Case**: You have 2 years of historical data in your dev Planning application and want to clone it to test. Instead of exporting/importing snapshots, use Copy Pipeline to transfer the data in minutes.

```
epmautomate runPipeline -Name "Copy_Planning_Data" -SourceInstance dev-instance -TargetInstance test-instance
```

### 3. Location Security (25.06+)

Data Exchange enforces data residency requirements. You can configure a pipeline to ensure data never leaves a specified geographic region (e.g., "data must stay in EU").

**Compliance Scenario**: Your company operates in the EU and is subject to GDPR. Configure location security on your data load pipelines to ensure customer data is processed and stored only in EU data centers.

### 4. SFTP Support (25.09+)

Data Exchange added SFTP as a source/target, enabling secure file transfers for air-gapped environments or integrations with legacy systems.

**Example**: Your legacy GL system can only SFTP files to a shared server. Data Exchange reads directly from SFTP, validates, and loads into Planning.

### 5. Advanced Validation Framework

Data Exchange's validation system is more sophisticated than Data Management's:

- **Pre-load Validation**: Check data quality before loading.
- **Reconciliation Rules**: Compare loaded data against expected totals.
- **Custom Validation**: Write Python or JavaScript validation logic.
- **Quarantine & Retry**: Failed records are quarantined and can be reprocessed after fixing.

## Gap Analysis: What's Not Yet in Data Exchange

While Data Exchange is the future, a few features from Data Management are still being ported:

| Feature | Status | Expected Timeline |
|---------|--------|---|
| **Data Lineage** | Roadmap | 2026 Q2 |
| **Drill-Through** | Roadmap | 2026 Q3 |
| **Audit Logs** | Basic | Enhanced version in 2026 |
| **Reverse Mappings** | Planned | 2026 Q2 |
| **Conditional Routing** | Planned | 2026 Q3 |

If you rely heavily on any of these features, Data Exchange may not be ready for you yet. Plan your migration timeline accordingly.

## Migration Timeline and Oracle's Guidance

### Oracle's Retirement Plan for Data Management

- **2026 Q2**: Data Management enters "Maintenance Mode"—no new features, security fixes only.
- **2027 Q1**: Data Management reaches "End of Support"—no bug fixes, support tickets closed.
- **2028**: Data Management is completely retired.

### Recommended Migration Path

**Phase 1: Plan (Now – Q2 2026)**
- Inventory all Data Management rules in use.
- Identify high-risk rules (complex validation, custom code).
- Evaluate Data Exchange's feature parity.
- Begin POC with a low-risk rule.

**Phase 2: Pilot (Q2 2026 – Q3 2026)**
- Migrate 20–30% of your rules to Data Exchange.
- Validate data loads match Data Management output.
- Refine your migration approach based on lessons learned.

**Phase 3: Cutover (Q4 2026 – Q1 2027)**
- Migrate remaining rules.
- Maintain parallel runs of Data Management and Data Exchange for validation.
- Retire Data Management rules.

**Phase 4: Decommission (Q2 2027+)**
- Archive Data Management rules (don't delete—keep for audit).
- Sunset monitoring and alerting for Data Management.

## Step-by-Step Migration Approach

### 1. Inventory Current Data Management Integrations

Create a spreadsheet:

```
Rule Name | Source | Target App | Frequency | Complexity | Priority
GL Actuals Load | GL Flat File | Planning | Daily | High | 1
Headcount Import | HRIS API | Workforce Cloud | Weekly | Low | 2
FX Rates Load | Bloomberg Feed | FCCS | Daily | Medium | 1
```

### 2. Map Each Rule to Data Exchange Equivalents

For each Data Management rule, identify which Data Exchange blocks and pipelines you'll need:

- **GL Actuals Load**: File source → Column mapping → Smart lookup (cost center) → Planning target
- **Headcount Import**: API source (REST connector) → Data validation → Workforce Cloud target
- **FX Rates Load**: CSV file source → Validation (check against previous month's rates) → FCCS target

### 3. Pilot the Top-Priority Rule

1. Create a new Data Exchange pipeline for your most critical load (usually GL actuals).
2. Run parallel loads: Data Management (prod) and Data Exchange (test environment).
3. Compare output: Do balances match? Are member hierarchies loaded correctly?
4. Iterate on the pipeline until output is identical.

### 4. Automate via EPM Automate

Once your Data Exchange pipeline is validated, schedule it via EPM Automate:

```bash
# Schedule via EPM Automate (25.02+)
epmautomate runPipeline -Name "GL_Actuals_Pipeline" -Mode SYNCHRONOUS

# Add to your scheduling script
if [ $? -eq 0 ]; then
    echo "Pipeline succeeded" >> /var/log/pipelines.log
else
    echo "Pipeline failed; alert team" >> /var/log/pipelines.log
    # Send email alert here
fi
```

### 5. Validate End-to-End

- Check that data loads successfully.
- Validate cube balances match expectations.
- Confirm downstream reports reflect the new data.
- Test error scenarios: bad source file, network timeout, invalid members.

### 6. Retire Data Management Rule

Once Data Exchange pipeline is stable and validated in production for 1–2 cycles:

1. Mark the Data Management rule as "deprecated" (don't delete yet).
2. Update runbooks and documentation to reference the Data Exchange pipeline.
3. After 3 months of stable operation, delete the Data Management rule.

## Coexistence Period

During 2026–2027, you can run Data Management and Data Exchange in parallel:

- Some rules stay in Data Management (not yet migrated).
- New rules are built in Data Exchange.
- Maintain clear documentation of which system owns which rule.

This gradual transition minimizes risk and allows your team to become proficient with Data Exchange before full cutover.

## Common Migration Challenges and Solutions

### Challenge 1: Complex Data Management Logic

**Issue**: Your Data Management rule has embedded Java code for custom transformations.

**Solution**:
- Evaluate if Data Exchange's transformation blocks (column mapping, string functions, lookups) can replicate the logic.
- If not, use Data Exchange's **Custom Script** block (Python or JavaScript) to embed custom logic.
- If neither works, consider migrating to a separate ETL tool (Informatica, Talend) as an intermediary.

### Challenge 2: Drill-Through Dependency

**Issue**: You rely on drill-through from Planning back to the original source data file.

**Solution**:
- Drill-through is on Data Exchange's roadmap for 2026 Q3.
- Until then, maintain the Data Management rule running in parallel for drill-through purposes only.
- Or, implement a workaround: load the source file details into a separate Planning dimension for manual drill-through.

### Challenge 3: Performance Regression

**Issue**: Your Data Management load processes 500 million cells. Data Exchange pipeline is slower.

**Solution**:
- Enable **Bulk Load Mode** in Data Exchange (optimizes for large volumes).
- Ensure your source file is pre-sorted by target members (avoid random lookups).
- Validate that you're using the correct EPM Cloud target type (direct load vs. staging).
- Contact Oracle Support if performance remains unsatisfactory—your use case might benefit from future optimizations.

## Key Takeaways for Administrators

1. **Data Management is Retiring**: Oracle's official end-of-support is 2027 Q1. Plan your migration now.

2. **Data Exchange is the Future**: It's architected for cloud-native scale and reusability. New feature development is focused here.

3. **Start with Pilots**: Don't try to migrate 100 rules at once. Pilot your top-priority, lowest-complexity rules first.

4. **Maintain Parallel Runs**: For critical integrations, run Data Management and Data Exchange in parallel during validation.

5. **Leverage New Capabilities**: Once migrated, take advantage of Data Exchange's new features (copy pipelines, location security, SFTP) to improve your integration architecture.

6. **Plan for Gaps**: If you depend on drill-through or other features not yet in Data Exchange, factor that into your timeline.

7. **Automate Everything**: Use EPM Automate to schedule pipelines consistently, just as you did with Data Management rules.

By proactively planning your migration from Data Management to Data Exchange, you'll minimize disruption and position your EPM Cloud architecture for long-term success.
