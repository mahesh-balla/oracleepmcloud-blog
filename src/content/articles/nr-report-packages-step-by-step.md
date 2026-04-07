---
title: 'Setting Up Report Packages in Narrative Reporting — A Step-by-Step Guide'
description: 'A comprehensive tutorial on creating report packages in Oracle Narrative Reporting, from initial setup through doclet assignment, review workflows, and final publishing.'
product: 'narrative-reporting'
subcategory: 'tutorials'
pubDate: '2026-04-05'
---

# Setting Up Report Packages in Narrative Reporting — A Step-by-Step Guide

Report Packages in Oracle Narrative Reporting (NR) provide a structured framework for organizing content, managing authorship responsibilities, and controlling review workflows. This guide walks EPM Administrators and NR Solution Architects through the complete lifecycle of creating, configuring, and publishing a report package.

## Understanding Report Packages

A Report Package is a container that bundles multiple doclets (content pieces) together with defined metadata, author assignments, approval workflows, and publishing rules. Report Packages enable large organizations to:

- Assign authorship and accountability across teams
- Enforce multi-stage review and approval workflows
- Maintain consistent branding and formatting
- Publish final content to standardized output formats (PDF, Excel, HTML)
- Track version history and audit trails

## Prerequisites

Before creating a Report Package, ensure you have:

- Access to Narrative Reporting web interface with Administrator or Solution Architect role
- Understanding of your organizational structure (cost centers, departments, entities)
- Planning document outlining package structure, content sections, and approval hierarchy
- Identified authors, reviewers, and sign-off approvers
- Knowledge of the content types you'll include (Word doclets, Excel reference doclets, Management Reporting doclets)

## Step 1: Navigate to Report Packages

In the Narrative Reporting web interface:

1. Log in with your Oracle EPM Cloud credentials
2. Select **Narrative Reporting** from the application menu
3. Click **Administration** or **Manage**
4. Navigate to **Report Packages**
5. Click **Create New Package** or the plus (+) icon

## Step 2: Define Package Metadata

In the package creation form, enter:

- **Package Name**: Use a clear, descriptive name (e.g., "FY2026 Annual Report Package")
- **Description**: Briefly describe the package's purpose and scope
- **Template**: Select a pre-built template if available, or start from blank
- **Default Content Type**: Specify the primary content type (Word, Excel, Management Reporting)
- **Default Output Format**: Choose PDF, Excel, HTML, or multiple formats
- **Package Owner**: Assign the administrator responsible for the package
- **Effective Date**: Set when the package becomes active

Click **Save** to create the base package.

## Step 3: Define Package Structure and Sections

Report Packages are organized into sections, which logically group related doclets. Sections appear in the table of contents and control the document flow.

1. Open your newly created package
2. Click **Add Section** or **Edit Structure**
3. For each section, define:
   - **Section Title**: e.g., "Executive Summary", "Financial Performance", "Risk Assessment"
   - **Display Order**: Numeric priority (1, 2, 3, etc.)
   - **Include in TOC**: Toggle to show/hide in table of contents
   - **Page Break**: Set whether a new page starts at this section
   - **Section Description**: Optional notes for authors

Example structure for a quarterly board pack:
- Section 1: Executive Summary
- Section 2: Financial Overview
- Section 3: Cost Center Analysis
- Section 4: KPI Dashboard
- Section 5: Appendices

## Step 4: Add and Configure Doclets

Doclets are the individual content pieces within a section. Each doclet has an author, content type, and review requirements.

1. Within each section, click **Add Doclet**
2. Configure doclet properties:
   - **Doclet Name**: Descriptive title (e.g., "P&L Summary", "Balance Sheet Analysis")
   - **Doclet Type**: Word, Excel Reference, Management Reporting Grid, Chart, Text Block, or Table
   - **Merge Area**: If using Word doclets, specify the merge area placeholder (e.g., {{PL_SUMMARY}})
   - **Content Source**: Link to the source data or template
   - **Default Author**: Assign the person responsible for this content
   - **Required**: Toggle whether this doclet is mandatory
   - **Sequence**: Order within the section

### Content Type Configuration

**Word Doclets**: Upload or link Word templates with merge fields. Narrative Reporting substitutes data at generation time.

**Excel Reference Doclets**: Reference external Excel files. Data updates when the file changes.

**Management Reporting Doclets**: Pull live data from EPM Management Reporting. Specify the report name, dimension selections, and member filters.

**Chart Doclets**: Create embedded charts from data sources. Configure chart type (bar, line, pie), data mapping, and formatting.

**Text Blocks**: Static or template-driven narrative text sections for commentary and explanations.

## Step 5: Assign Authors and Approvers

Narrative Reporting uses role-based assignments to distribute content ownership and approval responsibility.

1. Open the package's **User Assignments** section
2. Click **Add Assignment** to assign users to roles

Configure the following roles:

- **Package Author**: User(s) who can edit package metadata and manage structure
- **Section Author**: Assigned per section; responsible for editing all doclets in that section
- **Doclet Author**: Assigned to specific doclets; edits only that content
- **Reviewer**: Reviews content during review phase; can comment but not approve
- **Approver**: Reviews and approves content; required for sign-off phase
- **Sign-Off Authority**: Final approval; can publish the package

For large organizations (50+ cost centers), consider:
- Central team for executive summary and consolidated views
- Cost center managers as doclet authors for their specific data
- Regional finance teams as reviewers
- Controller or CFO as final sign-off authority

## Step 6: Configure Review Workflow

Review workflows define the multi-stage approval process. Narrative Reporting supports three phases:

**Phase 1: Author Phase**
- Duration: Number of days authors have to draft content
- Notification: Automatic email reminders at start and end
- Content Lock: Authors can edit; reviewers cannot view

**Phase 2: Review Phase**
- Duration: Days reviewers have to review and comment
- Comment Permission: Reviewers can add comments; authors cannot edit during this phase
- Escalation: Optionally escalate unreviewed items to approvers

**Phase 3: Sign-Off Phase**
- Duration: Days approvers have to review and approve
- Requirement: Approval required before publishing
- Change Lock: Usually locked; no changes permitted during sign-off
- Notification: Status updates to stakeholders

To configure:

1. Click **Review Workflow** or **Configure Phases**
2. Set dates for each phase:
   - Start Date: When the review window opens
   - End Date: When the window closes and next phase begins
   - Notification Schedule: Days before deadline (e.g., notify at -3 days, -1 day)
3. Assign role restrictions per phase
4. Enable/disable comments and changes per phase

Example timeline for a monthly report:
- Author Phase: Days 1-5 (content creation)
- Review Phase: Days 6-8 (internal review)
- Sign-Off Phase: Days 9-10 (final approval)
- Publication: Day 11 (automated PDF generation)

## Step 7: Set Up Merge Areas and Data Bindings

Merge areas are placeholders in Word doclets that Narrative Reporting replaces with live data at generation time.

1. In your Word template, insert merge field markers: `{{FIELD_NAME}}`
2. In the doclet configuration, map merge areas to data sources:
   - **Static Text**: Pre-defined text strings
   - **Management Reporting Data**: POV-based dynamic selectors
   - **Data Integration**: External data sources via APIs
   - **Calculated Fields**: Formulas to compute values

Example merge areas for a P&L doclet:
- `{{ENTITY_NAME}}`: Current entity selection
- `{{REVENUE_TOTAL}}`: Sum of revenue from Management Reporting
- `{{EXPENSE_RATIO}}`: Calculated as (Expenses / Revenue) * 100
- `{{YOY_GROWTH}}`: (Current Year - Prior Year) / Prior Year

## Step 8: Configure Point of View (POV) Selection

Point of View (POV) allows dynamic member selection for personalized reports. This is critical for bursting (sending customized reports to multiple recipients).

1. Click **POV Configuration**
2. Define dimensions available for selection:
   - **Primary Dimension**: Usually Entity or Cost Center
   - **Secondary Dimensions**: Period, Scenario, Currency (optional)
   - **Member Sets**: Restrict available members per user role
3. Set defaults for each dimension
4. Enable/disable user override capability

Example POV for cost center reports:
- **Entity**: Locked to user's assigned entity
- **Cost Center**: Editable; users select their own cost center
- **Period**: Default to current month; users can select any month
- **Scenario**: Locked to Actual scenario

## Step 9: Configure Publishing and Output Options

Publishing rules control how the report package is generated and delivered.

1. Navigate to **Publishing Settings**
2. Configure output formats:
   - **PDF**: Select template, page orientation, margins, branding
   - **Excel**: Specify worksheet structure, freeze panes, protection
   - **HTML**: Enable for web viewing
3. Set publishing triggers:
   - **Manual**: Initiated by user
   - **Scheduled**: Daily, weekly, monthly automation
   - **Event-Based**: Triggered by workflow completion
4. Configure delivery:
   - **File System**: Save to EPM Cloud file storage
   - **Email**: Attach PDF/Excel to automated email with recipient list
   - **SharePoint/OneDrive**: Integrate with Microsoft 365
   - **Printer**: Direct print output (requires on-premises setup)

## Step 10: Validate and Publish the Package

Before going live:

1. Click **Validate Package** to check for configuration errors
2. Review the validation report for warnings and errors:
   - Missing required doclets
   - Unassigned authors/approvers
   - Invalid merge area mappings
3. Resolve any critical issues
4. Click **Publish Package** to make it active

## Best Practices for Large Organizations

**Managing 50+ Cost Centers:**
- Use templated doclets to reduce manual duplication
- Assign cost center managers as section authors
- Implement hierarchical approval (team lead → manager → controller)
- Schedule reviews in phases to avoid bottlenecks
- Set realistic review windows (5-7 days per phase minimum)

**Performance Optimization:**
- Limit Management Reporting doclets per package (aim for <10 complex grids)
- Use filters to reduce dataset sizes in charts and tables
- Cache static content (branding, templates) at package level
- Break large books into separate packages for concurrent authoring

**Audit and Compliance:**
- Enable version history tracking
- Configure audit logs for approval sign-off
- Require sign-off authority comments for rejected content
- Archive completed packages for regulatory retention

**User Adoption:**
- Provide role-specific training (authors, reviewers, approvers)
- Create quick-start guides for common tasks
- Monitor review cycle times; escalate delays
- Gather feedback post-publication and iterate

## Troubleshooting Common Issues

**Merge Fields Not Updating**: Verify field names match exactly (case-sensitive); ensure data source is connected.

**Slow Document Generation**: Check for complex calculations in merged data; consider splitting across multiple doclets.

**Missing Author Notifications**: Confirm email addresses in user assignments; check spam filters; verify SMTP configuration.

**Review Phase Bottleneck**: Escalate unreviewed content automatically; reduce number of reviewers; extend phase duration.

## Conclusion

Report Packages provide the foundation for enterprise-scale narrative reporting. By carefully structuring your package, assigning clear roles and responsibilities, and implementing efficient review workflows, you enable your organization to produce consistent, high-quality financial reports and board packs. Start with a pilot package for a single department, gather lessons learned, and scale to organization-wide implementation.

For additional resources, consult the Oracle Narrative Reporting Administration Guide and attend EPM Cloud training sessions focused on advanced package configuration.
