---
title: 'Designing Management Reports with Narrative Reporting Books'
description: 'How to use NR Books to build dynamic management reports with grids, charts, text, and table of contents for executive board packs.'
product: 'narrative-reporting'
subcategory: 'tutorials'
pubDate: '2026-04-04'
---

# Designing Management Reports with Narrative Reporting Books

Oracle Narrative Reporting Books represent a powerful evolution beyond static PDF documents. Books enable Solution Architects to assemble dynamic, interactive reports that combine live data grids, visual analytics, narrative commentary, and executive dashboards into cohesive board-ready packages. This guide covers the full lifecycle of designing, building, and publishing professional management reports using NR Books.

## What Are Narrative Reporting Books?

Books are dynamic report containers that bind together multiple content elements:

- **Grids**: Live data tables pulling directly from EPM Management Reporting
- **Charts**: Visual analytics (bar, line, pie, waterfall) with drill-down capability
- **Text Blocks**: Narrative commentary, variance analysis, and management discussion
- **Images and Branding**: Logos, headers, and company styling
- **Table of Contents**: Auto-generated hierarchical TOC with navigation
- **Page Breaks and Sections**: Logical grouping for executive flow

Unlike static Word documents, Books update dynamically when underlying EPM data changes, ensuring reports always reflect current information without manual re-generation.

## Architecture and Components

**Book Structure**:
- **Book**: Top-level container (e.g., "Q4 2026 Financial Results")
- **Chapters**: Major logical sections (e.g., "Executive Summary", "Divisional Performance")
- **Topics**: Subsections within chapters (e.g., "Revenue Analysis", "Cost Management")
- **Content Items**: Individual grids, charts, or text blocks

**Content Types**:
1. **Management Reporting Grids**: Live POV-based data tables with formulas
2. **Charts**: Visual representations with dynamic member selection
3. **Text Blocks**: Rich text with variable substitution (merge fields)
4. **Aligned Grids**: Multiple grids sharing synchronized member selection
5. **Composite Charts**: Combining multiple data series in single visualization
6. **KPI Dashboards**: Scorecard-style metrics with conditional formatting

## Step 1: Create a New Book

In the Narrative Reporting web interface:

1. Click **Books** from the main menu
2. Select **Create New Book**
3. Enter book metadata:
   - **Book Name**: e.g., "Q4 2026 Board Financial Pack"
   - **Description**: Purpose and intended audience
   - **Owner/Administrator**: Responsibility assignment
   - **Default Template**: Select corporate branding template
   - **Visibility**: Public, Private, or Restricted to roles

## Step 2: Design the Book Structure

Plan your book architecture before building. A typical quarterly board pack follows this structure:

**Chapter 1: Executive Summary**
- Topic 1a: Key Highlights (text block with bullet points)
- Topic 1b: Financial Snapshot (consolidated P&L grid)
- Topic 1c: KPI Dashboard (scorecard with variance indicators)

**Chapter 2: Financial Performance**
- Topic 2a: Consolidated P&L (detailed revenue and expense analysis)
- Topic 2b: Balance Sheet Summary (assets, liabilities, equity)
- Topic 2c: Cash Flow Analysis (operating, investing, financing activities)

**Chapter 3: Divisional Performance**
- Topic 3a: Division A Results (grid + variance commentary)
- Topic 3b: Division B Results (grid + variance commentary)
- Topic 3c: Division C Results (grid + variance commentary)

**Chapter 4: KPI and Metrics Dashboard**
- Topic 4a: Operating Metrics (grid with trend charts)
- Topic 4b: Financial Ratios (efficiency, profitability, liquidity)
- Topic 4c: Headcount and Labor Analysis (FTE trends and costs)

**Chapter 5: Appendices**
- Topic 5a: Accounting Policies (static text)
- Topic 5b: Glossary of Terms (reference table)

To implement this structure:

1. Click **Edit Structure** or **Add Chapter**
2. Create each chapter by clicking **New Chapter**
3. Within each chapter, click **New Topic** to add subsections
4. Set display order and TOC inclusion preferences

## Step 3: Add Management Reporting Grids

Grids are the backbone of data-driven reports, pulling live information from EPM Management Reporting.

1. Open a topic where you want to add a grid
2. Click **Add Content Item** → **Grid**
3. Configure the grid properties:

**Data Source Configuration**:
- **Report**: Select pre-built Management Reporting report (e.g., "Consolidated P&L")
- **Rows**: Dimension for row headers (e.g., Account, Department)
- **Columns**: Dimension(s) for column headers (e.g., Period, Scenario, Entity)
- **Measures**: Metrics to display (e.g., Actuals, Budget, Variance, %)

**Formatting Options**:
- **Number Format**: Currency, percentage, decimal places
- **Conditional Formatting**: Color scales for variance highlighting
- **Subtotals**: Enable/disable automatic subtotal rows
- **Suppression**: Hide zero values, blank rows
- **Fonts**: Bold headers, alternating row colors

**POV (Point of View) Configuration**:
- **Locked Members**: Fixed selections (e.g., locked to Currency = USD)
- **Default Members**: Pre-selected but changeable (e.g., Period = Current Month)
- **Prompts**: Allow user to change specific dimensions at report run time

Example P&L Grid Configuration:
- **Report**: "Consolidated P&L"
- **Rows**: Account (nested: Category > Account)
- **Columns**: Scenario (Actuals | Budget)
- **Measures**: Amount, Variance, Variance %
- **POV**: Entity = All, Period = Current Year to Date
- **Conditional Format**: Red for negative variances > 10%, green for positive variances > 5%

## Step 4: Add Charts and Visual Analytics

Charts provide executive-friendly visualizations of complex data.

1. Click **Add Content Item** → **Chart**
2. Select chart type:
   - **Column/Bar Chart**: For comparative analysis across categories
   - **Line Chart**: For trend analysis over time
   - **Pie Chart**: For composition analysis (revenue by division)
   - **Waterfall Chart**: For variance bridge analysis
   - **Scatter Plot**: For correlation analysis

3. Configure chart properties:

**Data Binding**:
- **Data Source**: Management Reporting grid or exported dataset
- **X-Axis**: Category dimension (e.g., months, cost centers)
- **Y-Axis**: Numeric measure (e.g., revenue, margin)
- **Series**: Multiple data series for comparison (e.g., Actuals vs. Budget)

**Interactivity**:
- **Drill-Down**: Click data points to navigate to detailed grids
- **Member Selection**: Filter by entity, period, scenario
- **Tooltips**: Display detailed values on hover

**Formatting**:
- **Colors**: Align with corporate branding (can override per series)
- **Legends**: Placement and styling
- **Axis Labels**: Format and rotation
- **Title and Subtitle**: Dynamic text with member substitution

Example Variance Trend Chart:
- **Type**: Line chart with markers
- **X-Axis**: Month (Jan-Dec 2026)
- **Y-Axis**: Revenue Variance (Amount)
- **Series**: Division A, Division B, Division C
- **Drill-Down**: Click point to view detailed P&L for that division/month
- **POV Override**: Allow user to select division at report run time

## Step 5: Add Text Blocks and Commentary

Narrative text provides management context and variance explanations.

1. Click **Add Content Item** → **Text Block**
2. Enter content using the rich text editor:
   - Bold, italic, underline, strikethrough
   - Lists (bulleted and numbered)
   - Hyperlinks
   - Tables
   - Images

3. Add merge fields for dynamic substitution:
   - `{{ENTITY_NAME}}`: Current entity selection
   - `{{PERIOD}}`: Current period
   - `{{VARIANCE_PCT}}`: Calculated variance percentage
   - `{{GROWTH_TREND}}`: Text variable from data integration

Example variance commentary template:
```
Revenue for {{ENTITY_NAME}} decreased {{VARIANCE_PCT}}% to
{{REVENUE_ACTUAL}} in {{PERIOD}}, primarily driven by:
- Decline in Product A sales due to market saturation
- Reduction in Service contract renewals
- Unfavorable product mix shift toward lower-margin offerings

Management Actions Underway:
1. Launch new Product B marketing campaign (Q2 2026)
2. Renegotiate key supplier contracts (Q2-Q3 2026)
3. Implement pricing optimization initiative (Q3 2026)

Expected Impact: Recovery to plan by Q4 2026
```

## Step 6: Implement Aligned Grids

Aligned grids synchronize member selection across multiple tables, enabling side-by-side comparisons.

1. Click **Add Content Item** → **Aligned Grids**
2. Add multiple grids that share the same POV:
   - Grid 1: Current Year Actual P&L
   - Grid 2: Prior Year Actual P&L
   - Grid 3: Variance (Current - Prior)

3. Set synchronization rules:
   - **Shared Dimensions**: Entity, Period (synchronized)
   - **Independent Dimensions**: Scenario (can vary per grid)
   - **Auto-Recalc**: Variance grid updates when other grids change

This approach is superior to separate grids because:
- User selects Entity/Period once; all three grids update together
- Reduces confusion from mismatched selections
- Improves visual comparison and analysis flow

## Step 7: Configure Table of Contents and Navigation

Books automatically generate table of contents based on structure.

1. Click **TOC Settings**
2. Configure:
   - **Include Chapters/Topics**: Toggle visibility
   - **Numbering Style**: None, Chapter.Number, or custom format
   - **Depth**: Show all levels or collapse after Chapter level
   - **Auto-Bookmarks**: Enable PDF bookmarks for navigation
   - **TOC Page**: Insert at beginning, end, or omit

Example TOC for board pack:
```
Table of Contents

1. Executive Summary                                      1
   1.1 Key Highlights                                    1
   1.2 Financial Snapshot                                2
   1.3 KPI Dashboard                                     3

2. Financial Performance                                  5
   2.1 Consolidated P&L                                 5
   2.2 Balance Sheet Summary                            7
   2.3 Cash Flow Analysis                               9

3. Divisional Performance                                11
   3.1 Division A Results                              11
   3.2 Division B Results                              13
   3.3 Division C Results                              15

4. KPI and Metrics Dashboard                            17
```

## Step 8: Configure POV for Dynamic Member Selection

POV allows report consumers to customize views by selecting entities, periods, and scenarios.

1. Click **Book Settings** → **POV Configuration**
2. Define available dimensions:
   - **Entity**: Allow selection of specific entities or "All Entities"
   - **Period**: Allow selection of individual periods or "Year to Date"
   - **Scenario**: Lock to Actual scenario or allow Actual/Budget comparison
   - **Version**: If applicable, allow version selection

3. Set default values:
   - **Default Entity**: Current user's entity
   - **Default Period**: Latest available period
   - **Default Scenario**: Actuals

4. Define filters per dimension:
   - **Entity Filter**: Restrict to entities in user's permission list
   - **Period Filter**: Show only periods in current fiscal year
   - **Scenario Filter**: Hide archived or non-reporting scenarios

5. Enable/disable:
   - **User Override**: Can users change defaults?
   - **Cascading Selection**: Does changing Entity filter Period options?
   - **Persist Selection**: Remember user's selections between sessions?

Example POV Configuration:
- **Entity**: Default = User's home entity; editable from approved list
- **Period**: Default = Latest month; editable; showing only last 24 months
- **Scenario**: Locked to "Actual Reporting Scenario"
- **User Override**: Enabled for Entity; disabled for Period and Scenario

## Step 9: Schedule Book Output

Books can be automatically generated and distributed on a schedule.

1. Click **Schedule** or **Publishing Schedule**
2. Configure:
   - **Frequency**: Daily, weekly, monthly, quarterly, annually
   - **Trigger Date/Time**: When book should generate (e.g., 3 days after month-end)
   - **Output Format**: PDF, Excel, HTML
   - **POV**: Which entity selections to generate (all entities, specific list, or parametric)
   - **Delivery Method**: Email, file system, SharePoint, archive

3. Set notification rules:
   - **Email Recipients**: Individual users or distribution lists
   - **Subject Line**: Template with dynamic text (e.g., "{{PERIOD}} Financial Results")
   - **Body Text**: Custom message for email

Example Schedule for Monthly Board Pack:
- **Trigger**: 8:00 AM on the 3rd business day of each month
- **Format**: PDF
- **POV**: Generate for all entities (separate files per entity)
- **Recipients**: CFO, Controllers, Board Members
- **Subject**: "{{ENTITY}} Financial Results for {{PERIOD}}"
- **Archive**: Store copies in EPM Cloud file storage for audit trail

## Step 10: Performance Optimization for Large Books

Books with many grids can slow down generation and rendering. Optimize:

**Grid Optimization**:
- Limit Management Reporting grids to <10 per book
- Use row suppression to hide zero/null values
- Apply appropriate filters to reduce dataset sizes
- Use account hierarchies to balance detail vs. summary

**Chart Optimization**:
- Limit to <5 complex charts per book
- Use simpler chart types (bar, line) over waterfall/scatter
- Cache frequently-used data at book level
- Pre-aggregate data in Management Reporting rather than at book level

**Content Item Strategy**:
- Break very large books (50+ pages) into separate books
- Use chapter-level page breaks for cleaner PDFs
- Defer heavy graphics to appendices
- Consider splitting "for each entity" into separate publications

**Caching and Refresh**:
- Cache static content (headers, TOC, company policies)
- Schedule heavy book generation during off-peak hours
- Set appropriate data refresh windows (e.g., refresh data every 1 hour, not every 5 minutes)

## Example: Building a Quarterly Board Financial Pack

Here's a complete walkthrough:

**Book**: "Q1 2026 Board Financial Results"

**Chapter 1: Executive Dashboard (Pages 1-3)**
- Text block with quarterly highlights
- Consolidated P&L grid (Entity hierarchy, Actual amounts and %)
- Key metrics chart (Revenue trend, Margin %)
- KPI scorecard (EPS, ROE, Days Cash On Hand with variance indicators)

**Chapter 2: Financial Deep Dive (Pages 4-10)**
- P&L Analysis (3-month rolling actual, aligned with prior year)
- Balance Sheet (with liquidity ratios)
- Cash Flow Waterfall (operating, investing, financing bridges)
- Commentary text block with management's variance analysis

**Chapter 3: Divisional Performance (Pages 11-20)**
- Separate topic per division with:
  - Divisional P&L grid
  - Performance vs. plan chart
  - Key metrics grid (margins, headcount, utilization)
  - Variance commentary (text)

**Chapter 4: Strategic Metrics Dashboard (Pages 21-25)**
- Operating metrics (production volume, units sold, market share)
- Headcount and labor cost analysis
- Efficiency metrics (revenue per employee, margins)
- Growth trend charts

**Chapter 5: Appendices (Pages 26-30)**
- Accounting policies (static text)
- Glossary of key terms
- Contact information for finance team

**Total Book Size**: 30 pages, 12 grids, 8 charts, 15 text blocks
**Generation Time**: ~45 seconds
**Output**: PDF, scheduled for 8 AM on 3rd business day of month
**Distribution**: Email to CFO, board members, investor relations

## Conclusion

Narrative Reporting Books transform financial reporting from static, error-prone documents into dynamic, responsive management tools. By combining live data grids with narrative commentary, visual analytics, and executive dashboards, Books enable your organization to communicate complex financial information clearly and compellingly. Start with a pilot quarterly board pack, refine based on feedback, and expand to monthly operational reporting and investor communications.

For advanced topics like parameterized Books, data integration with external systems, and mobile-optimized publishing, consult the Oracle Narrative Reporting Advanced User Guide.
