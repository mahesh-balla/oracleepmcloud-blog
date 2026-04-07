---
title: 'NR Bursting — Automating Report Distribution to Cost Center Owners'
description: 'Configure bursting in Narrative Reporting to automatically generate and distribute personalized reports to department and cost center owners.'
product: 'narrative-reporting'
subcategory: 'tips'
pubDate: '2026-04-03'
---

# NR Bursting — Automating Report Distribution to Cost Center Owners

Bursting is one of Narrative Reporting's most powerful features for enterprise-scale financial reporting. Rather than generating a single report for all users, bursting automatically creates personalized, filtered versions of a Book or Report Package and distributes them to hundreds or thousands of recipients. This guide covers the complete implementation of bursting for cost center management reporting.

## What is Bursting?

Bursting automates the generation and distribution of filtered report instances based on dimension members. For example:

- Single Book or Report Package → 50 separate bursts (one per cost center)
- Each burst contains only data relevant to that cost center
- Each burst is delivered automatically to the cost center manager
- Delivery occurs on a schedule (daily, weekly, monthly)
- Eliminates manual report generation and distribution errors

**Benefits**:
- **Personalization**: Each recipient sees only their data
- **Automation**: Eliminates manual report creation and emailing
- **Timeliness**: Reports generated and distributed on schedule
- **Auditability**: Track what was sent, when, and to whom
- **Scalability**: Handle thousands of reports in a single scheduled job
- **Security**: Enforce access controls; users only see authorized data

## Bursting Concepts

**Burst Dimension**: The dimension along which you split reports. Common choices:
- Entity
- Cost Center
- Department
- Division
- Business Unit
- Legal Entity

**Burst Members**: The specific members of the burst dimension that trigger separate report generation. For a 50-cost-center organization:
- Burst Dimension = Cost Center
- Burst Members = CC001, CC002, ..., CC050
- Result = 50 distinct reports generated

**Recipient Mapping**: Assignment of burst members to email addresses or distribution lists. Examples:
- CC001 → john.smith@company.com
- CC002 → mary.johnson@company.com
- CC003 → sales.team.west@company.com

**Output Format**: Format for each burst instance:
- PDF (print-ready, ideal for email)
- Excel (data-oriented, allows further analysis)
- HTML (web-viewable, interactive)
- ZIP archive (multiple formats bundled per recipient)

## Step 1: Prepare Your Book or Report Package

Before configuring bursting, ensure your Book/Package supports filtered output:

1. **POV Configuration**: Enable member selection on the burst dimension
   - Example: Cost Center selection must be available to end-users
   - All grids and charts must respect the Cost Center POV selection

2. **Test Single Instance**: Verify the Book/Package generates correctly when POV is set to a specific cost center
   - Select Cost Center = CC001, generate, and validate output
   - Repeat for another cost center (CC050) to ensure no cross-contamination

3. **Content Validation**: Ensure all content respects the burst dimension:
   - Grids filter correctly by cost center
   - Charts update dynamically
   - Text commentary includes cost center name (merge field: {{COST_CENTER_NAME}})
   - Summary tables exclude unrelated cost centers

4. **Performance Test**: Generate the book with your largest cost center dataset
   - If generation takes >2 minutes, apply optimization techniques (covered below)
   - Test with 3-5 different cost centers to confirm consistent performance

## Step 2: Configure Bursting in Narrative Reporting

Navigate to bursting configuration:

1. Open your Book or Report Package
2. Click **Settings** → **Bursting** (or **Configure Distribution**)
3. Click **Enable Bursting** and confirm

The bursting configuration form appears with these sections:

**Burst Dimension Selection**:
- Select the dimension for bursting (Cost Center, Entity, etc.)
- This must match the POV dimension available in your Book/Package

**Burst Member Selection**:
- Choose "All members" to generate reports for every cost center in your data
- Or select "Specific members" and choose a subset (useful for phased rollout)
- Or select "Members matching filter" and define a filter expression

Example Configurations:

**Configuration A: All Active Cost Centers**
- Burst Dimension: Cost Center
- Member Selection: All members where Entity = "North America" AND Status = "Active"
- Expected: 25 separate reports

**Configuration B: Pilot Rollout**
- Burst Dimension: Cost Center
- Member Selection: Specific members [CC001, CC010, CC025, CC042]
- Expected: 4 separate reports (for testing)

**Configuration C: Phased Rollout by Region**
- Burst Dimension: Cost Center
- Member Selection: All members where Region = "EMEA"
- Expected: 15 separate reports (European cost centers only)

## Step 3: Configure Recipient Mapping

Each burst member (cost center) must map to one or more recipients (email addresses or distribution lists).

1. In the bursting configuration, click **Recipient Mapping** or **Distribution Settings**
2. Choose mapping method:

**Method 1: Automatic Mapping via User Attributes**
- NR automatically matches cost center to user attribute in Oracle EPM Cloud
- Requires: EPM user records include a "Cost Center Manager" attribute
- Implementation:
  1. In EPM Cloud Users, set "Cost Center Manager" = "CCXXX" for relevant users
  2. In NR bursting, select "Map via User Attribute"
  3. Choose attribute: "Cost Center Manager"
  4. NR finds all users with matching attribute and includes them as recipients

**Method 2: Manual Mapping Upload**
- Upload CSV file with cost center to email mappings
- CSV format:
  ```
  CostCenter,Email,Recipient Name
  CC001,john.smith@company.com,John Smith
  CC002,mary.johnson@company.com,Mary Johnson
  CC003,sales.team@company.com,Sales Team Distribution List
  ```
- Process:
  1. Prepare CSV file
  2. Click **Upload Recipient File** in bursting configuration
  3. NR validates email format and cost center members
  4. Confirm and save mappings

**Method 3: Dynamic SQL Query**
- For advanced scenarios, query EPM user database directly
- Example SQL:
  ```sql
  SELECT DISTINCT
    u.cost_center_code AS CostCenter,
    u.email_address AS Email,
    u.full_name AS RecipientName
  FROM users u
  WHERE u.system_access = 'Active'
    AND u.email_address IS NOT NULL
  ORDER BY u.cost_center_code
  ```

**Method 4: Directory Service Integration** (if configured)
- NR queries LDAP or Active Directory for cost center managers
- Returns: cost center → manager email mapping
- Advantage: Automatically updates when organizational structure changes
- Requires: EPM Cloud integration with company directory

## Step 4: Configure Output Format and File Naming

1. Click **Output Format** or **Publishing Options**
2. Select format:
   - **PDF**: Default for most reporting use cases
   - **Excel**: For data-intensive reports where recipients analyze further
   - **HTML**: For web viewing and digital-first organizations
   - **Multiple Formats**: Create both PDF and Excel (increases storage and processing time)

3. Configure file naming:
   - **Static Name**: "Monthly_Report.pdf" (all bursts have same name; recipients overwrite if re-downloaded)
   - **Dynamic Name with Cost Center**: "Monthly_Report_{{COST_CENTER}}.pdf" (recommended)
   - **Dynamic Name with Date**: "Monthly_Report_{{COST_CENTER}}_{{PERIOD}}.pdf"

4. Example file naming for cost center bursting:
   - Format: PDF
   - Naming Convention: "CC_Report_{{COST_CENTER_CODE}}_{{PERIOD}}_{{MONTH}}_{{YEAR}}.pdf"
   - Generated Examples:
     - CC_Report_CC001_2026Q1_April_2026.pdf
     - CC_Report_CC002_2026Q1_April_2026.pdf

5. Configure PDF options:
   - Paper size: A4 or Letter
   - Orientation: Portrait or Landscape
   - Margins: Top, bottom, left, right (in inches or mm)
   - Include headers/footers: Cost center name, report date, page numbers

## Step 5: Set Up Delivery Configuration

1. Click **Delivery Method** or **Distribution Channel**
2. Configure email delivery:

**Email Settings**:
- **From Address**: NR system email or your email
- **Subject Line Template**:
  ```
  Monthly Financial Report for {{COST_CENTER_NAME}} - {{PERIOD}}
  ```
- **Body Text**:
  ```
  Dear {{RECIPIENT_NAME}},

  Please find attached your monthly financial report for {{COST_CENTER_NAME}}.

  Report Period: {{PERIOD}}
  Generated: {{TODAY}}

  Contact Finance if you have questions.

  Best regards,
  Finance Team
  ```
- **Recipient Field**: To, Cc, or Bcc (use To for cost center owners)
- **Attachment**: Filename and format (PDF recommended)
- **Track Delivery**: Log successful/failed email sends in audit trail

**Alternative: File System Delivery**
- Save bursted files to EPM Cloud file storage instead of emailing
- Path structure: `/reports/monthly/{{PERIOD}}/{{COST_CENTER}}/`
- Recipients access reports via EPM Cloud UI or SharePoint integration
- Advantage: Reduces email volume for large organizations

**Alternative: SharePoint Integration**
- Upload bursted PDFs to SharePoint document library
- Folder structure: Site → /Reports → /Monthly → /Period202604 → files
- Configure permissions: Cost center owners can only access their cost center folder
- Recipients receive notification email with SharePoint link

## Step 6: Schedule Bursting

1. Click **Schedule** or **Bursting Schedule**
2. Configure timing:

**Frequency Options**:
- **Monthly**: Trigger on specific day of month (e.g., 5th business day after month-end close)
- **Weekly**: Trigger on specific day (e.g., every Monday at 8:00 AM)
- **Daily**: Trigger at specific time (e.g., 6:00 AM daily)
- **On-Demand**: Manually initiated (useful for one-time bursts or testing)

**Example Schedule for Monthly Cost Center Bursting**:
- Frequency: Monthly
- Trigger Date: 3rd business day of the following month (allows time for close)
- Trigger Time: 8:00 AM
- Time Zone: America/New_York
- Repeat: First business day of month if initial job fails
- Output: PDF
- Delivery: Email to cost center managers
- Recipients: Mapped via EPM User Cost Center attribute

3. Set up notifications:
   - **Success Notification**: Send email to Finance team confirming burst completion and count
   - **Failure Notification**: Alert administrator if any burst fails
   - **Recipient Notification**: Each recipient receives email with attached report

## Step 7: Handle Large Member Counts

Organizations with 100+ cost centers face performance challenges. Optimize:

**Phased Bursting**:
- Don't generate all 200 cost centers in one job
- Split into 4 parallel jobs (50 cost centers each):
  - Job 1: CC001-CC050 (Regions: Americas)
  - Job 2: CC051-CC100 (Regions: EMEA)
  - Job 3: CC101-CC150 (Regions: APAC)
  - Job 4: CC151-CC200 (Regions: Other)
- Schedule staggered (start 15 minutes apart to spread load)

**Performance Tuning**:
- Reduce number of grids per Book (aim for <8 for bursting)
- Apply row suppression to eliminate zero/null rows
- Use summary accounts instead of detail accounts where possible
- Pre-filter data in Management Reporting to burst-relevant dimensions only
- Consider splitting Books by functional area (P&L, Balance Sheet, Cash Flow) rather than bursting one large Book

**Job Monitoring**:
- Enable logging for each burst job
- Configure alerts for slow bursts (>5 minutes per member)
- Monitor email queue for delivery failures
- Set up daily reconciliation: Expected count = Successful + Failed + Skipped

## Step 8: Security and Access Control

Bursting must respect data security and access controls:

**Recipient Verification**:
- Verify cost center managers can access only their cost center data in standard reporting
- If a user cannot run a report for CC001, they should not receive a burst for CC001
- Implementation: Link bursting recipients to EPM user dimension and cost center access list

**Content Filtering**:
- Books used for bursting must apply cost center filters at all levels
- Check all grids, charts, and text blocks respect POV
- Avoid global consolidation data leaking into cost center bursts

**Audit Trail**:
- Log all burst generations: date, time, members processed, delivery status
- Log failed recipients: timestamp, reason (invalid email, user deleted, etc.)
- Enable recipient verification: Did john.smith@company.com receive the April report?

## Step 9: Testing and Pilot Rollout

Before full production:

1. **Test with Small Subset**:
   - Create bursting definition for 3-5 cost centers only
   - Generate manually and review each output
   - Verify cost center filtering, recipient mapping, file naming

2. **Validate Recipient Mapping**:
   - Review recipient list; ensure no cost centers missing recipients
   - Check for duplicate recipients (same email for multiple cost centers?)
   - Confirm all email addresses are valid and current

3. **Performance Test**:
   - Generate sample bursts for largest and smallest cost centers
   - Measure generation time per burst
   - Calculate total time for all 50 cost centers
   - If total > 30 minutes, implement phased approach

4. **Pilot Rollout Phase 1**:
   - Enable bursting for Finance team only (CC500 - Finance department)
   - Gather feedback on timing, content, file naming
   - Make adjustments based on feedback

5. **Pilot Rollout Phase 2**:
   - Enable for top 10 cost centers (highest spend/revenue)
   - Monitor for 1-2 months
   - Resolve any issues with recipient mapping or delivery

6. **Production Rollout**:
   - Enable for all cost centers
   - Communicate to organization: what is bursting, when reports arrive, how to access

## Step 10: Ongoing Maintenance

**Monthly Tasks**:
- Monitor burst job completion logs; investigate failures
- Review recipient list for organizational changes (new cost centers, manager changes)
- Update recipient mapping if cost center managers change

**Quarterly Tasks**:
- Analyze which bursts are being accessed (track downloads if using SharePoint)
- Gather feedback from cost center managers on report usefulness
- Validate that Books still generate within acceptable time
- Optimize if response time has degraded

**Annual Tasks**:
- Audit security: Verify no cross-cost-center data leakage
- Review Business case: Is bursting reducing manual reporting effort as intended?
- Evaluate expansion: Can additional dimensions be burst (division, product line)?
- Training: Ensure new employees understand bursting and how to access their reports

## Example: Bursting P&L Reports to 50 Cost Center Managers

**Scenario**:
- Organization has 50 cost centers across 3 regions (Americas, EMEA, APAC)
- Monthly close occurs on the 1st business day of following month
- Reports needed by 10:00 AM on the 3rd business day of month
- 45 cost center managers need individual P&L reports
- 5 regional controllers need consolidated regional P&Ls

**Implementation**:

| Component | Configuration |
|-----------|---------------|
| Book Name | "Monthly Cost Center P&L" |
| Burst Dimension | Cost Center |
| Burst Members | All active cost centers (50 total) |
| Recipient Mapping | EPM User attribute: CC_Manager |
| Output Format | PDF (1.5 MB avg) |
| File Naming | CC_PL_{{COST_CENTER}}_{{PERIOD}}.pdf |
| Delivery | Email + SharePoint archive |
| Schedule | 3rd business day at 7:30 AM EST |
| Total Generation Time | ~40 seconds (0.8 sec per cost center) |
| Total Emails Sent | 50 (one per manager) |
| Storage Required | 75 MB per month |

**Expected Benefits**:
- Eliminates 50 hours/month of manual report generation
- Reduces data errors (no copy/paste mistakes)
- Ensures consistent, timely reporting
- Provides audit trail of distribution
- Frees Finance team for analysis vs. reporting mechanics

## Troubleshooting Common Issues

**Issue: Burst Generation is Slow (>2 min per member)**
- Cause: Too many complex grids in Book
- Solution: Reduce grids to <5; move detailed analysis to appendix Book

**Issue: Some Bursts Fail; Others Succeed**
- Cause: Recipient mapping issue (invalid email) or data issue (missing cost center in GL)
- Solution: Review error log; update recipient mapping; validate cost centers exist in Management Reporting

**Issue: Cost Center Managers Receive Wrong Data (cross-contamination)**
- Cause: POV not properly applied to grids
- Solution: Verify all grids filter on Cost Center; test single instance with specific cost center

**Issue: Email Recipients Not Recognized (undeliverable mail)**
- Cause: Recipient mapping has typos or inactive email addresses
- Solution: Validate recipient CSV; cross-reference with active directory; update email addresses

## Conclusion

Bursting transforms cost center reporting from a manual, labor-intensive process into an automated, scalable distribution system. By carefully planning your burst dimension, mapping recipients, configuring output, and implementing a phased rollout, you can reliably deliver personalized financial reports to hundreds of managers. Start small with a pilot, gather feedback, and expand to full organizational implementation. The result is more timely, accurate, and actionable financial reporting across your enterprise.

For advanced bursting scenarios (cascading bursts, conditional recipients, integration with Task Manager), consult the Oracle Narrative Reporting Administration Guide.
