---
title: 'Building Your First Planning Application — Dimensions, Forms, and Business Rules'
description: 'A foundational tutorial for new Planning Cloud administrators covering application creation, dimension setup, form design, and basic business rule configuration.'
product: 'planning-cloud'
subcategory: 'tutorials'
pubDate: '2026-04-05'
---

# Building Your First Planning Application — Dimensions, Forms, and Business Rules

Creating your first Oracle Planning Cloud application is an exciting milestone for any EPM administrator. This comprehensive guide walks you through the entire process, from application creation through testing with real data.

## Understanding Application Types

Before you create an application, you need to understand the two fundamental application types available in Planning Cloud:

### Standard Planning
Standard Planning is the traditional approach, built on the Planning framework with predefined structures and features. It includes built-in support for Task Lists, Allocations, Transfers, Workforce Planning, CapEx Planning, and other Planning-specific modules. When you choose Standard Planning, you get the full Planning framework out of the box, which means you inherit all the standard dimensions (Entity, Account, Period, Scenario, Version, Year, Currency) and access to Planning-specific business logic tools like the Allocation Engine and Workforce module.

Standard Planning is ideal when you want to leverage Planning Cloud's built-in features and don't need complete flexibility over the underlying dimensional structure. It's particularly suited for financial planning scenarios where you'll be using Task Lists for approval workflows or leveraging pre-built modules like Workforce or CapEx Planning.

### FreeForm Planning
FreeForm Planning, by contrast, gives you complete flexibility to define your dimensions and cube structure without the Planning framework constraints. With FreeForm, you work directly with Essbase multidimensional structures, enabling ad-hoc analysis and custom dimension hierarchies that don't fit the standard Planning mold. FreeForm is excellent for organizations migrating from on-premises Essbase or those who need cube-centric workloads where Planning's built-in features aren't critical.

For this tutorial, we'll focus on creating a Standard Planning application, as this is the most common starting point for new planning initiatives.

## Step 1: Creating Your Application

Navigate to the Planning Cloud home page and select the option to create a new application. You'll be prompted to:

1. **Choose your application type**: Select "Standard Planning"
2. **Name your application**: Use a meaningful name like "FY2026_FinancialPlan" (avoid spaces; use underscores)
3. **Add a description**: Document the purpose, data owner, and expected data refresh frequency
4. **Select application type**: Choose "Standard" to enable Planning features
5. **Choose your cube type**: Select either BSO (Block Storage Option) for planning scenarios or ASO (Aggregate Storage Option) for reporting-heavy, read-only cubes. For your first application, BSO is recommended as it supports write-back and business rule execution

The application provisioning process takes several minutes. You'll receive a notification when your application is ready. During this time, Planning Cloud is creating:
- The underlying Essbase cube infrastructure
- The Planning application structure with default dimensions
- The Task List module and workflow framework
- Integration with Data Management for data loads
- Smart View connectivity configuration

## Step 2: Defining Your Dimensions

Dimensions are the foundation of your multidimensional model. Planning Cloud provides seven standard dimensions that you configure to match your organization:

### Entity Dimension
The Entity dimension represents your organizational hierarchy. In a financial planning context, this typically includes divisions, departments, cost centers, or business units. You'll structure this as a parent-child hierarchy where:
- Parents (rollups) contain formulas that aggregate child values
- Children are leaf nodes where actual data entry occurs
- Example structure: Company > Region > District > Store

Create your entity list by uploading a CSV file or manually entering members. For each member, specify:
- Member name (code)
- Member description
- Parent (for rollup members)
- Account type (Asset, Liability, Equity for balance sheet items; Revenue, Expense for income statement items)

### Account Dimension
The Account dimension maps to your chart of accounts. This might include revenue line items, operating expense categories, capital expenditures, or balance sheet accounts. Structure this dimension to match your GL (General Ledger) system. A typical structure includes:
- Revenue (with sub-accounts for each revenue line)
- Cost of Sales
- Operating Expenses
- Capital Expenditures
- Balance Sheet accounts

Use the Account type field to mark items as either "Income" or "Expense" so that Planning Cloud can properly calculate variances and totals. You can also enable the "Expense" marker to support the Workforce Planning module, which automatically calculates headcount and compensation costs.

### Period Dimension
The Period dimension typically includes months (Jan, Feb, Mar, etc.) and quarters (Q1, Q2, Q3, Q4). You can also include a "Total" member that aggregates all periods. The Period dimension is critical for rolling forecasts, as you'll use substitution variables to dynamically shift which periods are locked for actual data versus open for forecasting.

### Scenario Dimension
Scenario allows you to model multiple planning versions: Actual (read-only actuals from your GL), Budget (your annual budget), Forecast (rolling forecast), Forecast_High (best-case scenario), Forecast_Low (worst-case scenario). Each scenario can have different business rules applied.

### Version Dimension
Version allows you to track evolution over time. You might have Version1 (first submission), Version2 (revised after review), Final (approved version). This enables what-if analysis and scenario management.

### Year Dimension
Year contains your fiscal years: 2024, 2025, 2026, etc. Planning Cloud typically works with fiscal years rather than calendar years, matching your accounting period.

### Currency Dimension (Optional)
If your organization operates in multiple currencies, add a Currency dimension with entries for each currency code (USD, EUR, GBP) and a conversion method. Planning Cloud can automatically calculate exchange rates if you configure external rate sources.

### Custom Dimensions
Beyond the standard dimensions, you can add custom dimensions to address specific planning needs. Examples include:
- Product Dimension: Product lines, SKUs, or categories
- Channel Dimension: Direct, Distributor, E-commerce
- Department Dimension: Sales, Marketing, Operations
- Function Dimension: Headcount, Salary, Benefits (for Workforce Planning)

For each custom dimension, define the member hierarchy, which members can receive data, and any calculation rules.

## Step 3: Understanding Plan Types

Plan types determine which dimensions are included in a cube and which business rules apply. Planning Cloud provides three preconfigured plan types:

**Plan1**: Contains all seven standard dimensions (Entity, Account, Period, Scenario, Version, Year, Currency). Use this for general financial planning.

**Plan2**: A simplified version focused on Entity, Account, Period, and Scenario. Useful when you don't need Version or Currency tracking.

**Plan3**: An even simpler structure for specific use cases like workforce or capital expenditure planning.

If none of these fit your needs, you can create a custom plan type with just the dimensions you need. When defining a custom plan type:
- Select which standard dimensions to include
- Determine which custom dimensions to add
- Specify the dense/sparse configuration (dense dimensions are precalculated for fast retrieval; sparse dimensions are calculated on demand)
- Configure the cube type (BSO or ASO)

## Step 4: Designing Your Forms

Forms are the user interface for data entry. They provide a structured, audited way for planners to input data rather than giving them direct access to the cube. A well-designed form increases data quality, enforces validation rules, and provides context through supporting information.

### Creating Your First Form

Navigate to the Form Designer and select "Create New Form". You'll specify:

**Form Name**: Use a descriptive name like "EntityActualRevenue" so users understand the form's purpose

**Dimension Selection**:
- Rows: Usually Account (your P&L or balance sheet items)
- Columns: Usually Period (months or quarters)
- Page (POV): Entity, Scenario, Year, Version (these don't repeat across the form)

### Form Layout Best Practices

1. **Keep forms focused**: Create separate forms for different data domains (Revenue form, Expense form, Headcount form). Wide forms with many row and column dimensions become difficult to navigate.

2. **Add row and column subtotals**: Include calculated rows that show subtotals (e.g., "Total Revenue", "Total Expenses"). This helps users verify data entry completeness.

3. **Use color coding**: Highlight data entry cells in white, locked cells in gray, and calculated cells in blue. This visual distinction immediately tells users where data entry is permitted.

4. **Add supporting information**: Include columns that show:
   - Prior year actuals (for comparison)
   - Budget values (to show variance)
   - Growth rate formulas (to drive planning assumptions)

### Adding Data Validation Rules

Data validation occurs at the cell level. You can define rules such as:
- **Range validation**: Revenue must be between minimum and maximum thresholds
- **Decimal places**: Ensure all entries are to the nearest dollar (no cents)
- **Required fields**: Certain cells must be populated before the form can be submitted
- **Comparison validation**: Ensure a derived value (e.g., Total = Sum of components) is satisfied

When a user violates a validation rule, they see a clear error message and cannot save their entry until corrected.

### Configuring Point of View (POV)

The POV section of your form allows users to select which Entity, Scenario, Year, and Version they want to view or edit. You can configure the POV to:
- Restrict users to specific entities (security)
- Pre-select a default entity for convenience
- Force the selection of certain dimensions (required POV)

### Right-Click Menus

Right-click menus (context menus) provide quick access to common actions without cluttering the form interface. You can configure:
- **Data Explorer**: Opens the Essbase cube analyzer to examine related data
- **Drill Down**: Navigate to child entities or accounts for detailed inspection
- **Submit Data**: Trigger a business rule or data submission workflow
- **Email Notification**: Send notifications to data owners
- **Smart View Export**: Download form data to Excel for offline analysis

## Step 5: Creating Business Rules

Business rules automate calculations and data movements, reducing manual work and ensuring consistency. Planning Cloud supports two approaches: Calculation Manager (graphical rules) and Groovy scripting (for complex logic).

### Calculation Manager Basics

Calculation Manager provides a visual interface for building rules without coding. A rule consists of a series of steps, each performing an operation:

1. **Allocation rule**: Distribute a total across child members proportionally
   - Parent Account total is split across Entity children based on a ratio (e.g., headcount or revenue)
   - Example: Allocate corporate overhead to departments based on employee count

2. **Copy rule**: Duplicate data from one area to another
   - Copy prior year actuals to current year forecast as a baseline
   - Copy approved budget to planning form for comparison

3. **Calculate rule**: Apply a formula to cells
   - Revenue Growth Forecast = Last Year Actuals × (1 + Growth Rate)
   - Gross Margin = Revenue - Cost of Sales

### Rule Execution Modes

**Graphical Mode**: Ideal for straightforward rules. You drag and drop operation blocks, specify source and target members, and the system generates the underlying calculation syntax.

**Script Mode**: For complex logic, you can switch to script mode and write the calculation directly using Planning's calculation language or Groovy.

### Practical Example: A Simple Allocation Rule

Let's create a rule that allocates Corporate Overhead to divisions based on headcount:

1. Define the source: Corporate Overhead account under the parent Entity
2. Define the targets: Individual division accounts
3. Specify the allocation method: Divide the total overhead by total headcount, then multiply each division's headcount by this per-head cost
4. Set the rule to execute automatically when users submit data, or allow manual execution from a form button

### Launching Rules from Forms

Once you've created business rules, you can add them to forms as buttons or automated submissions. Users can then click "Run Allocation" on the form, and the rule executes immediately, updating calculated cells.

## Step 6: The Cube Refresh Process

After you've structured dimensions, created forms, and built business rules, you need to refresh (or "save") your cube to activate all changes. A cube refresh:
- Restructures the multidimensional database with your updated dimensions
- Applies new business rule definitions
- Recompiles forms to reflect layout changes
- Optimizes the cube for performance

This process can take several minutes for large applications. During a refresh, users cannot access the application, so plan refreshes during maintenance windows.

## Step 7: Testing with Sample Data

Before rolling out to your planning community, test your application with sample data:

1. **Load sample data**: Create a simple CSV file with a few accounts, entities, and periods
2. **Load via Data Management**: Use Data Management (or the newer Data Exchange) to import this data
3. **Review in Smart View**: Open Excel and connect to your Planning application via Smart View to verify data loaded correctly
4. **Test forms**: Open your forms, verify that users can see the sample data, and that calculations work as expected
5. **Test business rules**: Run your allocation or copy rule on sample data and verify results
6. **Validate submissions**: If you've configured Task Lists, submit data as a user and verify the workflow progresses correctly

### Sample Data Checklist
- At least 10 accounts across different categories
- At least 3 entities at different hierarchy levels
- All 12 months of data for at least one year
- At least 2 scenarios (Actual and Budget)
- Enough data to verify parent calculations (ensure child totals equal parent)

## Conclusion

You've now walked through the complete process of creating a Planning Cloud application from scratch. The key steps are:

1. Choose your application type (Standard or FreeForm)
2. Define your dimensions to match your organizational structure
3. Create forms that guide users through data entry
4. Add validation rules to ensure data quality
5. Build business rules for calculations and data movements
6. Test thoroughly with sample data

From here, you can expand by adding more dimensions, creating advanced business rules, configuring Task Lists for approval workflows, or integrating with external data sources. The foundation you've built here is solid and ready to scale.

Happy planning!
