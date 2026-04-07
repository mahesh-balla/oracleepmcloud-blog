---
title: 'Task Manager Configuration for Month-End Close in EPM Cloud'
description: 'How to configure Task Manager in EPM Cloud to orchestrate the month-end close process with task dependencies, scheduling, alerts, and integration with consolidation and reporting.'
product: 'epm-cloud-updates'
subcategory: 'tutorials'
pubDate: '2026-03-30'
---

## What is Task Manager?

Task Manager is an orchestration engine in EPM Cloud that coordinates the month-end (or period-end) close process. Instead of manually tracking spreadsheets and email reminders, Task Manager provides a structured workflow where tasks have owners, due dates, dependencies, and automated escalations.

Task Manager works across EPM Cloud applications—Planning, Financial Consolidation and Close Suite (FCCS), Narrative Reporting—to coordinate the entire close cycle from GL data load through final reporting and sign-off.

## Core Concepts

### Close Template

A close template defines the structure of your close cycle. It's a reusable blueprint that you configure once and use every month.

**Example Template: 15-Day Month-End Close**

```
Day 1: GL Actuals Load (Automatic)
Days 1-3: GL Load Validation (Manual)
Days 2-5: Intercompany Elimination (Automatic)
Days 3-6: Management Review (Manual)
Days 6-10: Journal Entry Review and Approval (Manual)
Days 10-12: Consolidation Process (Automatic)
Days 11-15: Final Reporting and Sign-Off (Manual)
```

### Tasks

Tasks are the atomic units of work in the close process. Each task:

- Has an owner (e.g., "GL Accounting Manager").
- Has a due date (e.g., "Day 3 of the close").
- Can be manual (human intervention required) or automated (runs a business rule, data load, or pipeline).
- Can have predecessors/successors (depends on prior tasks, gates subsequent ones).
- Generates alerts when overdue.

### Task Types

Task Manager supports several task types:

| Task Type | Example | Triggered By |
|-----------|---------|---|
| **Manual Task** | "Review GL reconciliation" | User manually marks complete |
| **Automated Task** | "Run consolidation business rule" | Task Manager trigger |
| **Business Rule Task** | Execute EPM Cloud business rule | Scheduled via Task Manager |
| **Data Load Task** | Import GL actuals from ERP | EPM Automate or pipeline |
| **System Task** | Check data integrity, refresh cubes | Task Manager system jobs |
| **Data Export Task** | Generate variance report | Run Book execution |

## Creating a Close Template

### Step 1: Define the Close Cycle

1. Log into your EPM Cloud instance.
2. Navigate to **Task Manager > Close Templates**.
3. Click **Create Close Template**.
4. Name it (e.g., "Month-End Close 2026").
5. Specify the duration: "15 days" (or however many days your close takes).

### Step 2: Add Tasks to the Template

1. Click **Add Task**.
2. Fill in task details:

| Field | Example |
|-------|---------|
| **Task Name** | GL Actuals Load Validation |
| **Description** | Review GL details for accuracy and completeness |
| **Owner** | GL Accounting Manager |
| **Task Type** | Manual Task |
| **Scheduled Start** | Day 1 |
| **Scheduled End** | Day 3 |
| **Predecessor** | GL Actuals Load |
| **Successor** | Intercompany Elimination |

3. Click **Save Task**.

### Step 3: Define Task Dependencies

Task dependencies create a workflow sequence. In the template:

- **GL Actuals Load** (Day 1) is a predecessor of **GL Validation** (Day 1–3).
- **GL Validation** must be marked complete before **Intercompany Elimination** can start.
- **Intercompany Elimination** gates the **Consolidation Process**.

This prevents out-of-order work and ensures data quality at each stage.

### Step 4: Assign Automated Tasks

For tasks that run automatically (data loads, business rules, pipelines):

1. Click the task.
2. Click **Configure Automation**.
3. Choose the action type:
   - **Business Rule**: Select a business rule from Planning or FCCS.
   - **Pipeline**: Run a Data Exchange pipeline.
   - **Run Book**: Execute a Narrative Reporting book.
   - **Data Load**: Trigger a data load from an external system.

**Example: GL Load Automation**

- Task Name: "GL Actuals Load"
- Action Type: Pipeline
- Pipeline: "GL_Actuals_Load" (configured in Data Exchange)
- Trigger: Day 1 at 6:00 AM

The pipeline runs automatically at the specified time, loading actuals from your GL system into Planning.

## Real-World Example: 15-Day Close Schedule

Here's a fully configured close template for a typical mid-sized organization:

### Week 1: Data Collection and Validation

| Day | Task | Owner | Task Type | Automation |
|-----|------|-------|-----------|---|
| 1 | GL Actuals Load | System | Automated | Pipeline: GL_Load |
| 1–2 | GL Reconciliation | GL Manager | Manual | — |
| 2 | Load Journal Entries | GL Admin | Automated | Pipeline: JE_Load |
| 2–3 | Journal Entry Review | Controller | Manual | — |
| 3 | Run Tax Calculations | Tax Accountant | Automated | Business Rule: TaxCalc |

### Week 2: Consolidation and Adjustments

| Day | Task | Owner | Task Type | Automation |
|-----|------|-------|-----------|---|
| 4–5 | Intercompany Elimination | Consolidation Analyst | Automated | Business Rule: IC_Elim |
| 5 | Management Review | Finance Director | Manual | — |
| 6 | FX Revaluation | Treasury | Automated | Business Rule: FXReval |
| 6–7 | Consolidation Approval | CFO | Manual | — |

### Week 3: Reporting and Sign-Off

| Day | Task | Owner | Task Type | Automation |
|-----|------|-------|-----------|---|
| 8 | Run Consolidation | System | Automated | FCCS Job: Consolidate |
| 8–10 | Report Generation | Reporting Team | Automated | Run Book: Monthly Variance |
| 10–12 | Variance Analysis | FPA Analyst | Manual | — |
| 13–14 | Board Package Assembly | Reporting Manager | Manual | — |
| 15 | Final Sign-Off | CFO | Manual | — |

## Integration Points with Other EPM Cloud Applications

Task Manager doesn't work in isolation. It orchestrates across multiple applications:

### Planning Integration

- **Task**: "Forecast Validation"
- **Action**: Run a Planning business rule that calculates forecast reconciliation.
- **Link**: Task Manager invokes the business rule; results populate Planning cubes.

### Financial Consolidation Integration

- **Task**: "Consolidation Process"
- **Action**: Run FCCS consolidation job.
- **Link**: Task Manager triggers FCCS consolidation; intercompany eliminations, consolidation logic, and currency revaluation execute.

### Narrative Reporting Integration

- **Task**: "Variance Report Generation"
- **Action**: Run a Narrative Reporting book.
- **Link**: Task Manager executes the book; report PDF is generated and distributed to stakeholders.

### Data Exchange Integration

- **Task**: "GL Load"
- **Action**: Run a Data Exchange pipeline.
- **Link**: Task Manager triggers the pipeline; GL data flows from ERP → validation → Planning.

## Alert Configuration and Escalation

Task Manager can automatically alert task owners when deadlines approach or are missed.

### Setting Up Alerts

1. In the close template, click **Alert Configuration**.
2. Define alert rules:

| Trigger | Action |
|---------|--------|
| Task is overdue (0 days) | Email task owner, notify Finance Director |
| Task is due tomorrow | Email task owner |
| Task is 2 days past due | Email owner, Finance Director, and VP of Finance |

3. Optionally, escalate to a manager if the task owner doesn't acknowledge the alert.

### Example Alert Workflow

- **Day 3**: GL Validation task is due.
- **Day 3, 5 PM**: If still incomplete, email sent to "GL Accounting Manager".
- **Day 4, 9 AM**: Email sent to GL Manager's supervisor (Finance Director).
- **Day 5, 9 AM**: Task escalated to VP of Finance; a new alert is created with the VP as the owner.

This escalation ensures nothing falls through the cracks.

## Task Manager Dashboard

The Task Manager dashboard gives you visibility into close progress:

### Dashboard Features

- **Current Task Status**: Which tasks are in progress, completed, overdue.
- **Timeline View**: Gantt-style visualization of task timing and dependencies.
- **Critical Path**: Highlights tasks that, if delayed, will push the entire close date.
- **Resource Utilization**: Shows which team members are overloaded (multiple high-priority tasks).

Example dashboard:

```
Close Cycle: Month of March 2026
Target Completion: March 15

✓ GL Load (Complete, Day 1)
✓ GL Validation (Complete, Day 3)
⏳ Intercompany Elimination (In Progress, Due Day 5)
⚠ Management Review (Overdue as of Day 6)
— Consolidation (Pending, Scheduled Day 8)
— Final Reporting (Pending, Scheduled Day 10–12)

Critical Path: Management Review → Consolidation → Final Reporting
(If Management Review completes late, final reporting will be delayed)
```

Stakeholders can view this dashboard to understand close status at a glance.

## Scheduling Close Cycles

### Creating a Close Cycle Instance

Once you've built the template, create instances (actual close runs):

1. Click **Task Manager > Close Cycles**.
2. Click **Create Close Cycle**.
3. Select the template: "Month-End Close 2026".
4. Set the cycle month: "April 2026".
5. Click **Create**.

The system generates all tasks with:
- Scheduled dates (Day 1 = April 1, Day 15 = April 15).
- Owners (carried forward from the template).
- Dependencies and automations.

### Automation: Recurring Cycles

Instead of manually creating a cycle each month:

1. In the template, click **Recurring Schedule**.
2. Set **Frequency**: Monthly, first business day.
3. Click **Enable**.

Now, every month on the first business day, a new close cycle is automatically created based on this template.

## Practical Tips for Success

### Tip 1: Start Simple, Iterate

Don't try to model your entire close process perfectly from day one. Start with key tasks (GL load, consolidation, reporting), run a cycle, learn, and refine.

### Tip 2: Set Realistic Due Dates

If your actual close takes 18 days, don't force it into a 15-day template. Use realistic dates so alerts are meaningful (not false positives).

### Tip 3: Align Task Dependencies with Reality

Map your actual close workflow, including:
- Which tasks truly depend on others (GL load must precede consolidation).
- Which tasks can run in parallel (multiple JE reviews happening simultaneously).

### Tip 4: Integrate with Communication

- When a close cycle starts, email the team with the link to the dashboard.
- Include links to runbooks (who does what) and contact info for blockers.

### Tip 5: Monitor Cycle-to-Cycle Improvements

Track metrics:
- Average close time (target: reduce from 18 to 15 days).
- Tasks completed on time (target: 95%+).
- Escalations (target: reduce month-over-month).

Use this data to justify improvements (automating a manual task, parallelizing sequential tasks).

### Tip 6: Test Automations in Dev/Test First

Before running a close cycle with automated business rules or pipelines in production:

1. Test the automation in your test environment.
2. Verify the expected output (reconcile balances, check member hierarchies).
3. Then enable it in the production template.

Automated tasks failing during a live close are disruptive. Testing prevents this.

## Performance Considerations

### Scaling to Large Closes

If your close involves hundreds of tasks or multiple applications:

- **Distribute Work**: Use parallel task paths where possible (multiple teams working on different applications).
- **Automate Heavily**: Reduce manual tasks. Automation is faster, consistent, and doesn't require human oversight.
- **Monitor EPM Cloud Health**: Ensure the platform (Planning, FCCS) can handle the load (large business rule runs, concurrent data loads). Coordinate with EPM Cloud operations.

### Storage and Retention

Task Manager stores historical close cycles. Over time, this can consume storage:

- **Archive Old Cycles**: After a year, move completed close cycles to an archive (reduces active storage).
- **Purge Logs**: Delete detailed logs older than 6 months (keep summary metrics).

## Key Takeaways

1. **Task Manager Orchestrates the Close**: It's the nerve center of your month-end process, coordinating teams, systems, and deadlines.

2. **Templates are Reusable**: Build once, use monthly. Reduces configuration overhead and ensures consistency.

3. **Automate Where Possible**: GL loads, consolidation, and reporting can all be automated. Free your team for analysis, not data processing.

4. **Dependencies Prevent Chaos**: Define task dependencies to ensure work happens in the right order and data is validated at each stage.

5. **Alerts Drive Accountability**: Escalation rules ensure nothing is forgotten.

6. **Dashboard Visibility**: Real-time status view reduces emails and status meetings.

7. **Iterate and Improve**: Use close metrics to continuously shorten the cycle and improve quality.

With Task Manager, you'll transform your month-end close from a chaotic scramble into a coordinated, predictable process. Your team will spend less time tracking who did what, and more time analyzing the numbers.
