---
title: 'Migrating from Financial Reporting (FR) to Narrative Reporting'
description: 'A practical guide for migrating from the de-supported Financial Reporting (FR Studio) to Narrative Reporting and Reports, including what maps over and recommended strategies.'
product: 'narrative-reporting'
subcategory: 'use-cases'
pubDate: '2026-04-02'
---

# Migrating from Financial Reporting (FR) to Narrative Reporting

As of June 2025 (EPM Cloud version 25.06), Oracle de-supported Financial Reporting (FR/FR Studio), marking the end of an era for traditional grid-based financial reporting. Organizations relying on FR must migrate to Oracle's modern reporting solutions: Narrative Reporting and Reports. This guide provides a pragmatic, step-by-step migration strategy covering what maps over, what doesn't, and how to plan a smooth transition.

## Understanding the FR Sunset

**Timeline**:
- June 2025 (25.06): Financial Reporting de-supported; no new features
- December 2025: FR instances will be shut down; access removed
- January 2026 onward: FR applications will not be available

**What This Means**:
- Your existing FR reports stop working January 2026
- New reports cannot be created in FR
- Support and maintenance for FR ends
- You must migrate to Reports or Narrative Reporting by year-end 2025

## Migration Path Options

Oracle provides two primary migration paths:

**Path 1: FR to Reports (Simple Grids)**
- Best for: Simple row/column grids without complex formatting
- Minimal effort, leverages existing Management Reporting data sources
- Output: PDF, Excel, scheduled distribution
- Limitations: Limited formatting, no complex page layouts, no narrative capabilities

**Path 2: FR to Narrative Reporting (Complex Books)**
- Best for: Multi-page reports, book layouts, mixed content (grids + text + charts)
- More effort, but unlocks advanced narrative capabilities
- Output: Professional PDFs, interactive web views, dynamic content
- Advantages: Future-proof, more flexible, supports modern reporting trends

**Recommendation**: Mixed approach
- Migrate simple FR reports to Reports (faster, simpler)
- Migrate complex FR reports to Narrative Reporting (richer output, narrative commentary)
- Pilot approach: Start with 3-5 key reports, validate mapping, then scale

## What Maps from FR to NR

### Features That Fully Map Over

**Data Source and Member Selection**:
- FR member selections → NR POV (Point of View)
- Dynamic member prompts → NR member selectors
- Account/Cost Center/Entity filters → NR filters and suppressions
- Hierarchical row/column selections → NR grid row/column definitions
- Zero suppression → NR suppression rules

**Formatting**:
- Grid formatting (colors, fonts, bold, italic) → NR grid styling
- Currency/percentage number formats → NR number formatting
- Conditional formatting (e.g., red for negative) → NR conditional formatting rules
- Indentation and subtotals → NR subtotal row/column structure
- Border styles → NR border definitions

**Calculations and Formulas**:
- FR account formulas (e.g., Assets = Current Assets + Fixed Assets) → Remain in Management Reporting
- User-defined calculations → Map to NR calculated measures
- Variance calculations (Actual - Budget) → NR formula grids

**Metadata and Governance**:
- Report descriptions and categories → NR report metadata
- User access permissions → NR security roles and access lists
- Audit logs and version history → NR version control

### Features That Partially Map Over

**Complex Formatting**:
- Nested grids with different hierarchies → Must recreate in NR (more flexible but requires redesign)
- Custom fonts and sizes → NR has standard fonts; custom fonts via PDF template only
- Merged cells and complex layouts → NR supports better layout options; may simplify design
- Image embedding → Full support in NR Books; partial in grid-based reports

**Advanced Functions**:
- FR-specific functions (some are proprietary) → Most map to Management Reporting functions or calculated measures
- Cross-grid calculations → Can reference multiple NR grids but with some limitations
- Dynamic text based on data values → NR supports text blocks with variable substitution

**Scheduling and Distribution**:
- FR scheduled reports → NR scheduled reports (similar functionality)
- Email delivery with attachments → Fully supported
- FTP delivery → Supported via file system export
- Printer output → Limited in cloud (PDF recommended)
- Bursting (report per entity) → Full support in NR with enhanced capabilities

### Features That Don't Map

**Java-Based Extensions**:
- Custom Java functions in FR → Cannot be automatically converted
- Java-based plugins and extensions → No equivalent in NR
- Workaround: Implement via data integration (pre-calculate in Management Reporting) or custom API integration

**Proprietary FR Objects**:
- FR-specific Smart Lists → Use EPM Architect dimension/member lists instead
- FR-only functions (CROSSDIM, FR.ACCOUNT_NAME, etc.) → Implement in Management Reporting formulas or NR text blocks
- Graph objects (FR graph objects) → Recreate as NR Charts with superior capabilities

**Complex Interactivity**:
- FR drill-down hyperlinks → NR supports drill-down but requires configuration
- FR hyperlinks to external systems → Implement via NR API integration or hyperlinks in text blocks
- FR custom actions → Workaround: Event-driven automation or Task Manager integration

**Backwards Compatibility**:
- FR versions for multiple cloud instances → NR is cloud-native; migration may consolidate instances
- Custom metadata extensions → May need to be adapted to NR schema

## Step 1: Assess Your FR Reporting Portfolio

Before beginning migration, inventory all FR reports:

1. **Export FR Report List**:
   - Access FR Studio administration
   - Generate report inventory (name, owner, last modified date, users accessing)
   - Export to spreadsheet

2. **Categorize by Complexity**:

| Complexity | Characteristics | Count | Examples |
|-----------|-----------------|-------|----------|
| Low | Simple grid, <5 rows, <4 columns, basic formatting | 15 | Summary P&L, Cash Position |
| Medium | 10-20 rows, 5-10 columns, nested hierarchy, variance calc | 25 | Detailed P&L, BS by Cost Center |
| High | 20+ rows, complex formulas, custom functions, multi-page layout | 8 | Consolidated Financial Statements |
| Very High | Multi-grid layout, custom Java, complex interactivity | 2 | Executive dashboards, custom tools |

3. **Assess Data Dependencies**:
   - Which Management Reporting reports feed each FR report?
   - Are member selections dynamic or hard-coded?
   - Are there consolidation considerations?
   - Are there external data sources (Excel, SQL)?

4. **Identify User Base**:
   - Who uses each report? (Finance team size, cost centers, departments)
   - How frequently accessed? (daily, weekly, monthly, ad-hoc)
   - Critical vs. nice-to-have?

5. **Calculate Migration Effort**:

| Complexity | Hours to Migrate to Reports | Hours to Migrate to NR |
|-----------|---------------------------|----------------------|
| Low | 2-4 hours | 4-8 hours |
| Medium | 4-8 hours | 8-16 hours |
| High | 8-16 hours | 16-32 hours |
| Very High | 16+ hours | 32+ hours |

**Example Portfolio**:
- 15 Low complexity: 30-60 hours to Reports, 60-120 hours to NR
- 25 Medium complexity: 100-200 hours to Reports, 200-400 hours to NR
- 8 High complexity: 64-128 hours to Reports, 128-256 hours to NR
- 2 Very High complexity: Evaluate ROI; consider retiring or custom solution

**Total Effort**: ~250-550 hours (depending on path chosen)
**Recommended Timeline**: 4-6 months with 2-3 FTE EPM administrators

## Step 2: Plan Migration Priorities

Prioritize migration in waves:

**Wave 1 (Month 1): Quick Wins** (2-3 weeks)
- Migrate 10 lowest-complexity reports to Reports
- Choose reports used by >20 employees
- Validate data mapping, member selections, formatting
- Gather user feedback; adjust approach based on findings
- Success Criteria: Reports generate correctly; users can access; formatting acceptable

**Wave 2 (Month 2-3): Core Financial Reports** (4 weeks)
- Migrate 15 medium-complexity reports to Reports or NR
- Include monthly/quarterly reporting requirements
- Prioritize month-end close requirements
- Develop templates/patterns for consistent approach
- Success Criteria: Core financial reporting runs on schedule without FR dependency

**Wave 3 (Month 4-5): Advanced Reports** (4-6 weeks)
- Migrate 8 high-complexity reports to NR Books
- Implement narrative commentary and advanced formatting
- Enhance with charts and dashboards
- Success Criteria: Deliver enhanced user experience with NR capabilities

**Wave 4 (Month 6): Sunset FR** (1 week)
- Migrate 2 very-high-complexity reports or retire
- Final validation and user training
- Decommission FR completely
- Success Criteria: Zero dependencies on FR; users trained on NR

## Step 3: Set Up Technical Foundation

Before migrating reports:

1. **Verify Narrative Reporting is Configured**:
   - NR service is active in your EPM Cloud instance
   - Security roles are assigned (Administrator, Architect, Author)
   - Management Reporting integration is working

2. **Verify Reports Module (if using)**:
   - Reports service is active
   - Access to reporting templates

3. **Plan POV Strategy**:
   - Define which dimensions allow user selection (Entity, Period, Scenario, Cost Center)
   - Lock vs. prompt: What can users change?
   - Defaults: What pre-selects when report opens?

4. **Establish Naming Conventions**:
   - FR reports often have cryptic names (FIN_RPT_001); adopt clear NR names
   - Example: "Monthly P&L by Cost Center" instead of "RPT_0024_V3"

5. **Review Security**:
   - FR access controls → Map to NR user assignments and roles
   - Dimension-level security (hide sensitive accounts) → Implement in NR
   - Cost center restrictions → Apply at POV filter level

## Step 4: Migrate Individual Reports — Reports Path

**Workflow for Simple Reports to Reports Module**:

1. **Export FR Report Definition**:
   - Open report in FR Studio
   - Document: Row dimension, Column dimension, Measures, Filters
   - Screenshot formatting (colors, fonts, number formats)
   - Document member selections and prompt logic

2. **Create New Report in Reports Module**:
   - Name: Use clear, descriptive naming
   - Choose data source: Management Reporting report
   - Define structure:
     - Rows: Account dimension with hierarchy
     - Columns: Period and/or Scenario
     - Suppress: Zeros and blank rows
   - Apply formatting:
     - Currency for amounts, percentage for ratios
     - Bold for subtotals and totals
     - Alternating row colors for readability

3. **Configure Member Selection**:
   - Default members: Current entity, current period, Actual scenario
   - Prompts: Allow Cost Center selection
   - Filters: Restrict to active members

4. **Test and Validate**:
   - Generate report with sample members
   - Compare output vs. FR version
   - Verify calculations (totals, subtotals, variances)
   - Check number formatting and alignment

5. **Schedule and Distribute**:
   - Set publication schedule (if monthly/quarterly)
   - Configure email delivery
   - Test email delivery to sample recipient list

**Example: Migrate Monthly P&L Summary**

FR Report Details:
- Name: "Monthly P&L Summary"
- Rows: GL Account hierarchy (P&L accounts only)
- Columns: Current month, Prior month, YTD
- Measures: Actual amount and %
- Filters: Exclude zero-balance accounts

Reports Configuration:
- Report Name: "Monthly P&L Summary"
- Data Source: Management Reporting "P&L Actuals"
- Rows: Account (nested by category)
- Columns: Period (Jan, Feb, Mar, ..., Dec)
- Filters: Account Type = "P&L"; Amount != 0
- Number Format: Currency (2 decimals); Percentage (1 decimal)
- Conditional Format: Red for negative amounts
- Schedule: Monthly on 2nd business day
- Delivery: Email to Finance, CFO distribution list

## Step 5: Migrate Complex Reports — Narrative Reporting Path

**Workflow for Complex Reports to Narrative Reporting**:

1. **Plan Book Architecture**:
   - Sketch expected structure (chapters, topics, content items)
   - Identify data sources (which Management Reporting reports needed?)
   - Plan layout: How many pages? How many grids, charts, text?

2. **Create Book in Narrative Reporting**:
   - Book name, description, owner
   - Select template (corporate branding)
   - Define structure (chapters and topics)

3. **Recreate Grids as NR Grids**:
   - Use Management Reporting grids as data source
   - Configure rows, columns, measures (as in Reports module)
   - Apply formatting (colors, conditional formats, number formats)
   - Set POV and prompts

4. **Add Narrative Content**:
   - Identify text blocks needed:
     - Executive summary paragraph
     - Variance commentary for significant changes
     - Key assumptions and estimates
   - Create text blocks with merge fields ({{ENTITY_NAME}}, {{PERIOD}}, etc.)
   - Add hyperlinks to supporting detail reports

5. **Add Visual Content**:
   - Identify charts needed (revenue trend, margin analysis, etc.)
   - Create charts in NR pointing to Management Reporting data
   - Configure drill-down from chart to detailed grid
   - Add company logos and branding elements

6. **Configure Table of Contents and Navigation**:
   - Define chapter and topic structure
   - Enable PDF bookmarks
   - Set up interactive navigation for web view

7. **Test and Validate**:
   - Generate Book with sample POV selections
   - Verify all grids, charts, and text display correctly
   - Check PDF formatting (page breaks, headers/footers)
   - Validate with actual end-users

8. **Schedule and Publish**:
   - Set publication schedule
   - Configure bursting (if needed for cost center distribution)
   - Set up email delivery
   - Archive reports for audit trail

**Example: Migrate Executive Board Pack**

FR State:
- 3 separate FR reports (Summary, Details, Appendix)
- Each generated manually, assembled in Word, printed, distributed
- 2 days of work per month to produce

NR Design:
- Single Narrative Reporting Book: "Monthly Board Financial Results"

Structure:
- Chapter 1: Executive Dashboard (2 pages)
  - Topic 1a: Key Highlights (text)
  - Topic 1b: Consolidated P&L (grid)
  - Topic 1c: KPI Scorecard (grid with conditional formatting)
- Chapter 2: Financial Detail (5 pages)
  - Topic 2a: Revenue Analysis (grid + chart)
  - Topic 2b: Cost Analysis (grid + variance commentary)
  - Topic 2c: Balance Sheet (grid)
- Chapter 3: Appendices (2 pages)
  - Topic 3a: Accounting Policies (text)
  - Topic 3b: Data Definitions (table)

Content:
- 4 management reporting grids
- 3 charts
- 5 text blocks with variance commentary
- Dynamic member selection (Entity selection)

Result:
- 9-page professional PDF
- Scheduled monthly on 5th business day
- Distributed automatically to board members
- Requires <4 hours/month maintenance (vs. 2 days previously)

## Step 6: Handle Special Migration Cases

**Case 1: Reports with Custom Java Functions**

Problem: FR report uses custom Java function to calculate KPI.

Solution Options:
1. **Migrate Function to Management Reporting**: Pre-calculate KPI in Management Reporting formula; pull into NR
2. **Implement in NR Calculated Measure**: Use NR formula syntax to replicate logic
3. **Integrate via API**: Call external service via NR REST API at report generation time
4. **Retire if Obsolete**: Evaluate if KPI is still needed; may be outdated

**Case 2: Reports with External Data Sources**

Problem: FR report links to Excel file or SQL database for external data.

Solution Options:
1. **Integrate into Management Reporting**: Import data into EPM Planning/Consolidation; use as additional dimension
2. **Use Data Connectors**: Configure NR to pull from external source (if connector available)
3. **Manual Data Entry**: If external data is static, enter into NR text blocks or calculated measures
4. **Pre-process**: Automate ETL to load external data into EPM before NR report generation

**Case 3: Reports with Complex Drill-Down Interactivity**

Problem: FR has custom drill-down menus linked to other reports.

Solution Options:
1. **Implement NR Drill-Down**: Configure in NR to drill from chart/grid to detailed report
2. **Hyperlinks in Text**: Add hyperlinks in narrative text blocks to other NR Books or Reports
3. **Parameterized Reports**: Use member selector to allow user to navigate to different views
4. **Custom Application**: Develop web application using NR APIs to provide advanced navigation

**Case 4: Consolidated Reporting Across Multiple Entities**

Problem: FR produces consolidated report aggregating multiple consolidation entities.

Solution Options:
1. **Management Reporting Consolidation Grid**: Use NR to display consolidated grid
2. **Ledger-Based Reporting**: Use GL data instead of consolidation; apply netting/elimination at reporting level
3. **Data Integration**: Import consolidated results from consolidation system into NR
4. **Narrative Calculation**: Calculate consolidated amounts in text blocks using summation formulas

## Step 7: Execute Migration and Testing

**Pre-Migration Checklist**:
- [ ] FR report inventory completed and prioritized
- [ ] Migration templates/examples created
- [ ] NR and Reports environments configured
- [ ] Security and POV strategy defined
- [ ] Management Reporting reports verified and tested
- [ ] User communication plan ready
- [ ] Training materials prepared

**Migration Execution**:
- [ ] Create new Reports/Books in NR for each FR report
- [ ] Map data sources and member selections
- [ ] Validate output matches FR version
- [ ] Configure scheduling and distribution
- [ ] Conduct UAT with end-users
- [ ] Gather feedback and adjust as needed

**Testing Protocol for Each Migrated Report**:
1. **Functional Testing**: Does report generate? Are all grids, charts, text present?
2. **Data Validation**: Do numbers match FR? Check totals, subtotals, variances
3. **Formatting Review**: Do colors, fonts, number formats match expectations?
4. **POV Testing**: Do member selections work? Do filters apply correctly?
5. **Output Format**: Does PDF look professional? Are page breaks correct?
6. **Performance**: Does report generate in acceptable time (<2 minutes)?
7. **Distribution**: Does email delivery work? Do files appear in file storage?
8. **User Acceptance**: Do end-users approve? Any requests for changes?

## Step 8: Decommission FR

Once migration complete:

1. **Verify All Reports Migrated**:
   - All FR reports have NR/Reports equivalents
   - All users transitioned to new reports
   - No critical reports still using FR

2. **Archive FR Definitions**:
   - Export FR report definitions for audit trail
   - Store in secure location (archive storage)
   - Document any unmigrated reports and reason

3. **Disable FR Access**:
   - Remove FR from user menus
   - Disable FR service in EPM Cloud
   - Update documentation and help systems

4. **Conduct Post-Migration Review**:
   - Gather feedback from users
   - Document lessons learned
   - Identify improvements for future reporting projects
   - Communicate success metrics

## Timeline and Resource Planning

**Small Organization (10 FR reports, <50 users)**:
- Timeline: 2-3 months
- Resources: 1 FTE EPM Admin, 0.5 FTE Finance Business Analyst
- Effort: ~80 hours
- Approach: Migrate most to Reports; enhance top 3 with NR Books

**Medium Organization (40 FR reports, 50-200 users)**:
- Timeline: 4-6 months
- Resources: 2 FTE EPM Admins, 1 FTE Finance Analyst, 0.5 FTE Training
- Effort: ~250 hours
- Approach: Mixed migration; wave-based rollout

**Large Organization (100+ FR reports, 200+ users)**:
- Timeline: 6-12 months
- Resources: 3-4 FTE EPM Admins, 2 FTE Finance Analysts, 1 FTE Training Manager
- Effort: ~500+ hours
- Approach: Phased migration; multiple teams in parallel; parallel operation of FR and NR

## Conclusion

Migrating from Financial Reporting to Narrative Reporting is not simply a tool replacement—it's an opportunity to modernize your reporting infrastructure and enhance user experience. By carefully planning your migration, prioritizing high-value reports, and leveraging NR's advanced capabilities (narrative commentary, professional formatting, dynamic content), you can create reporting solutions that are more maintainable, scalable, and user-friendly than FR ever was.

The key to success is structured planning, phased implementation, and continuous user feedback. Start small, learn from early waves, and scale confidently to complete FR sunset by December 2025.

For detailed migration assistance, engage Oracle EPM Cloud Professional Services or certified implementation partners who specialize in FR to NR migrations.
