---
title: 'Planning Cloud Groovy Rules — Practical Examples for Administrators'
description: 'A hands-on guide to writing Groovy business rules in Planning Cloud, with working code examples for allocations, data copy, conditional logic, and runtime prompts.'
product: 'planning-cloud'
subcategory: 'tutorials'
pubDate: '2026-04-02'
---

# Planning Cloud Groovy Rules — Practical Examples for Administrators

Groovy scripting in Oracle Planning Cloud's Calculation Manager provides a powerful alternative to graphical rule builders when you need advanced business logic, complex conditional processing, or direct cube manipulation. This guide walks you through practical Groovy examples that solve real planning challenges.

## Why Groovy Rules Over Graphical Rules?

Planning Cloud's Calculation Manager provides two approaches to business rules: graphical (point-and-click) and script-based (Groovy). Graphical rules are excellent for straightforward calculations and allocations. Groovy rules are necessary when:

- **Complex conditional logic**: "If revenue > 1M, apply 5% growth; if revenue < 500K, apply 3% growth"
- **Multi-step data transformations**: Copy data, then apply formulas, then validate results in one cohesive script
- **Looping and iteration**: Process each member of a dimension in a loop
- **External data integration**: Call APIs or read files to fetch parameters for calculations
- **Email notifications**: Send stakeholders alerts based on data conditions
- **Dynamic calculations**: Build formulas based on runtime parameters

Groovy provides a programming language approach to business rules, giving you flexibility that graphical rules cannot match.

## Setting Up Groovy in Calculation Manager

### Enabling Groovy Rules

In Calculation Manager, create a new rule and select "Script" as the rule type. Then choose "Groovy" as the scripting language. You'll need to associate the rule with a plan type (Plan1, Plan2, or a custom plan type).

### Key Objects and APIs

When you write Groovy rules in Planning Cloud, you work with specific objects provided by the Calculation Manager framework:

**Rule object**: The primary interface representing the rule execution context
- `Rule.getDataGrid(String gridName)`: Retrieve a grid from the form (your data context)
- `Rule.startDataGridDefinition()`: Define a new grid programmatically
- `Rule.sendMessage(String message)`: Send feedback to the user
- `Rule.raiseException(String message)`: Halt execution with an error

**DataGridDefinition and DataGridBuilder**: Objects for programmatically building data grids
- `DataGridDefinition`: Describes which dimensions are rows, columns, and POV
- `DataGridBuilder`: Builds the actual grid with values

**GridIterator**: Iterates over cells in a grid
- `iterator.getValue()`: Get the cell's current value
- `iterator.setValue(Double value)`: Update the cell
- `iterator.skip()`: Skip to the next cell

**DataCell**: Represents a single cell
- `cell.getValue()`: Get value
- `cell.setValue(Double value)`: Set value
- `cell.getFormattedValue()`: Get formatted display value

## Example 1: Simple Allocation Rule

The most common business rule is allocation: distribute a parent total across child members based on a ratio or proportion.

**Scenario**: You have corporate overhead in the parent "Company" account. You want to allocate it to divisions (East, West, Midwest) based on their headcount proportions.

```groovy
// Allocation rule: Distribute Corporate Overhead to divisions by headcount

try {
    // Get the data grid containing headcount and overhead
    def grid = Rule.getDataGrid("AllocationGrid")

    if (grid == null) {
        Rule.raiseException("AllocationGrid not found in form")
    }

    // Define dimensions for our calculation
    String parentEntity = "Company"
    String overheadAccount = "CorporateOverhead"
    String headcountAccount = "Headcount"

    // Calculate total headcount across all divisions
    double totalHeadcount = 0.0

    // Divisions to process
    List<String> divisions = ["East", "West", "Midwest"]

    // First pass: sum total headcount
    for (String division in divisions) {
        // Simulate reading headcount for each division
        // In a real scenario, this would come from the grid or database
        double divisionHeadcount = grid.getCellValue(division, headcountAccount)
        totalHeadcount += divisionHeadcount
    }

    // Get the corporate overhead amount to allocate
    double totalOverhead = grid.getCellValue(parentEntity, overheadAccount)

    if (totalHeadcount == 0) {
        Rule.raiseException("Total headcount is zero; cannot allocate overhead")
    }

    // Second pass: allocate overhead proportionally
    for (String division in divisions) {
        double divisionHeadcount = grid.getCellValue(division, headcountAccount)
        double headcountProportion = divisionHeadcount / totalHeadcount
        double allocatedOverhead = totalOverhead * headcountProportion

        // Write allocated overhead back to the grid
        grid.setCellValue(division, overheadAccount, allocatedOverhead)

        // Send feedback to user
        Rule.sendMessage("Allocated ${allocatedOverhead} to ${division}")
    }

    Rule.sendMessage("Overhead allocation completed successfully")

} catch (Exception ex) {
    Rule.raiseException("Allocation rule failed: ${ex.message}")
}
```

This rule:
1. Retrieves the data grid from the form
2. Calculates total headcount across divisions
3. Retrieves the corporate overhead amount
4. Allocates overhead proportionally to each division
5. Writes results back and sends feedback

## Example 2: Data Copy Across Scenarios

Another common pattern is copying data from one scenario to another as a baseline for new plans.

**Scenario**: You want to copy Actuals from the Actual scenario to the Forecast scenario as a starting point. Then planners can modify the forecast.

```groovy
// Copy Actuals to Forecast scenario with optional growth factor

try {
    def grid = Rule.getDataGrid("CopyGrid")

    if (grid == null) {
        Rule.raiseException("CopyGrid not found in form")
    }

    String sourceScenario = "Actual"
    String targetScenario = "Forecast"
    String growthFactor = "1.02"  // 2% growth

    // Iterate through all cells in the grid
    def iterator = grid.getGridIterator()
    int cellCount = 0

    while (iterator.hasNext()) {
        iterator.next()

        // Get source cell value (Actuals)
        double sourceValue = iterator.getValue()

        // Skip empty or zero cells to preserve sparsity
        if (sourceValue == 0 || sourceValue == null) {
            iterator.skip()
            continue
        }

        // Apply growth factor and write to target
        double targetValue = sourceValue * Double.parseDouble(growthFactor)
        iterator.setValue(targetValue)

        cellCount++
    }

    Rule.sendMessage("Copied ${cellCount} cells from ${sourceScenario} to ${targetScenario}")

} catch (NumberFormatException ex) {
    Rule.raiseException("Invalid growth factor: must be numeric")
} catch (Exception ex) {
    Rule.raiseException("Copy rule failed: ${ex.message}")
}
```

This rule:
1. Iterates through all cells in the grid
2. Retrieves source (Actual) values
3. Applies a growth multiplier
4. Writes target (Forecast) values
5. Reports the number of cells updated

## Example 3: Conditional Logic and Tiered Growth

Many planning scenarios require different logic based on data values.

**Scenario**: Apply tiered growth rates based on revenue magnitude. Large divisions (>$10M revenue) get 3% growth, mid-market (>$1M) get 5%, and small (<$1M) get 7%.

```groovy
// Tiered growth rate application based on revenue thresholds

try {
    def grid = Rule.getDataGrid("GrowthGrid")

    if (grid == null) {
        Rule.raiseException("GrowthGrid not found in form")
    }

    // Define growth tiers
    def growthTiers = [
        [threshold: 10_000_000, growthRate: 0.03],  // >$10M: 3%
        [threshold: 1_000_000,  growthRate: 0.05],  // >$1M: 5%
        [threshold: 0,          growthRate: 0.07]   // >$0: 7%
    ]

    def iterator = grid.getGridIterator()
    int updatedCells = 0
    double totalGrowth = 0.0

    while (iterator.hasNext()) {
        iterator.next()

        double revenueValue = iterator.getValue()

        if (revenueValue <= 0) {
            iterator.skip()
            continue
        }

        // Determine applicable growth rate
        double applicableGrowth = 0.07  // Default to smallest tier

        for (def tier in growthTiers) {
            if (revenueValue > tier.threshold) {
                applicableGrowth = tier.growthRate
                break
            }
        }

        // Calculate new forecast value
        double forecastValue = revenueValue * (1 + applicableGrowth)
        double growthAmount = forecastValue - revenueValue

        // Write forecast value
        iterator.setValue(forecastValue)

        totalGrowth += growthAmount
        updatedCells++
    }

    Rule.sendMessage("Applied tiered growth to ${updatedCells} revenue items. Total growth: ${totalGrowth}")

} catch (Exception ex) {
    Rule.raiseException("Growth rule failed: ${ex.message}")
}
```

This rule:
1. Defines tiered growth rates by threshold
2. Iterates through each cell
3. Determines the applicable growth tier based on value
4. Applies tier-specific growth and updates cells
5. Tracks statistics for user feedback

## Example 4: Runtime Prompts for Parameterized Rules

Groovy rules can accept runtime parameters—users select values when executing the rule.

**Scenario**: Create a rule that allows users to select a source scenario and target scenario at runtime, plus a growth factor to apply during the copy.

```groovy
// Dynamic copy rule with runtime parameters

try {
    def grid = Rule.getDataGrid("ParameterizedGrid")

    if (grid == null) {
        Rule.raiseException("ParameterizedGrid not found in form")
    }

    // Runtime parameters (user selects these when executing the rule)
    String sourceScenario = Rule.getParameter("SourceScenario", "Actual")
    String targetScenario = Rule.getParameter("TargetScenario", "Forecast")
    String growthFactorStr = Rule.getParameter("GrowthFactor", "1.00")

    // Validate parameters
    double growthFactor = 1.0
    try {
        growthFactor = Double.parseDouble(growthFactorStr)
    } catch (Exception e) {
        Rule.raiseException("Growth factor must be numeric (e.g., 1.05 for 5% growth)")
    }

    if (growthFactor < 0.5 || growthFactor > 2.0) {
        Rule.raiseException("Growth factor must be between 0.5 and 2.0")
    }

    def iterator = grid.getGridIterator()
    int updatedCells = 0
    double totalValue = 0.0

    while (iterator.hasNext()) {
        iterator.next()

        double sourceValue = iterator.getValue()

        if (sourceValue == 0 || sourceValue == null) {
            iterator.skip()
            continue
        }

        double targetValue = sourceValue * growthFactor
        iterator.setValue(targetValue)

        totalValue += targetValue
        updatedCells++
    }

    Rule.sendMessage("Copied ${updatedCells} cells from ${sourceScenario} to ${targetScenario} with ${(growthFactor - 1) * 100}% growth. Total: ${totalValue}")

} catch (Exception ex) {
    Rule.raiseException("Parameterized copy rule failed: ${ex.message}")
}
```

When this rule is added to a form, users see prompts at execution time:
- SourceScenario: Dropdown to select source
- TargetScenario: Dropdown to select target
- GrowthFactor: Text input (validates as numeric)

## Example 5: Email Notification on Completion

Groovy rules can trigger email notifications based on conditions.

**Scenario**: After running an allocation rule, email the finance manager to review the results.

```groovy
// Allocation rule with email notification

try {
    def grid = Rule.getDataGrid("AllocationGrid")

    if (grid == null) {
        Rule.raiseException("AllocationGrid not found")
    }

    // Run allocation logic
    double totalOverhead = 0.0
    int allocatedDivisions = 0

    List<String> divisions = ["East", "West", "Midwest"]

    for (String division in divisions) {
        // Allocation calculation
        double allocatedAmount = 100_000  // Placeholder
        totalOverhead += allocatedAmount
        allocatedDivisions++
    }

    // Prepare email
    String recipient = "finance.manager@company.com"
    String subject = "Planning Cloud Allocation Rule Executed"
    String body = """
        The corporate overhead allocation rule has completed.

        Summary:
        - Divisions processed: ${allocatedDivisions}
        - Total overhead allocated: ${totalOverhead}
        - Execution time: ${System.currentTimeMillis()}

        Please review the results in Planning Cloud.

        This is an automated message from Planning Cloud.
    """

    // Send email (if email service is available)
    try {
        Rule.sendEmail(recipient, subject, body)
        Rule.sendMessage("Email notification sent to ${recipient}")
    } catch (Exception emailEx) {
        Rule.sendMessage("Warning: Email notification failed - ${emailEx.message}")
        // Continue processing even if email fails
    }

    Rule.sendMessage("Allocation rule completed successfully")

} catch (Exception ex) {
    Rule.raiseException("Allocation rule failed: ${ex.message}")
}
```

This approach:
1. Performs the core allocation calculation
2. Prepares an email with results summary
3. Sends the email to relevant stakeholders
4. Continues processing even if email fails (graceful degradation)

## Example 6: Excel Output and Inbox Export (25.06)

Planning Cloud 25.06 introduced the ability to generate Excel files and write them to the user's Inbox/Outbox.

**Scenario**: After running a complex allocation, generate an Excel report showing the allocation breakdown and write it to the user's Planning Inbox for download.

```groovy
// Generate Excel report and write to Inbox

try {
    def grid = Rule.getDataGrid("AllocationGrid")

    if (grid == null) {
        Rule.raiseException("AllocationGrid not found")
    }

    // Collect allocation results
    List<Map> allocationResults = []

    List<String> divisions = ["East", "West", "Midwest"]
    double totalOverhead = 1_000_000

    for (String division in divisions) {
        double allocatedAmount = totalOverhead / divisions.size()

        allocationResults.add([
            division: division,
            allocatedAmount: allocatedAmount,
            percentage: (allocatedAmount / totalOverhead * 100).round(2)
        ])
    }

    // Build Excel file content
    StringBuilder excelContent = new StringBuilder()
    excelContent.append("Division,Allocated Amount,Percentage\n")

    for (Map result in allocationResults) {
        excelContent.append("${result.division},${result.allocatedAmount},${result.percentage}%\n")
    }

    // Write to Inbox (new in 25.06)
    String fileName = "AllocationBreakdown_${System.currentTimeMillis()}.xlsx"

    try {
        Rule.writeToInbox(fileName, excelContent.toString())
        Rule.sendMessage("Allocation report written to your Inbox: ${fileName}")
    } catch (Exception inboxEx) {
        Rule.sendMessage("Warning: Could not write to Inbox - ${inboxEx.message}")
    }

    Rule.sendMessage("Allocation rule completed successfully")

} catch (Exception ex) {
    Rule.raiseException("Allocation rule with export failed: ${ex.message}")
}
```

This feature (available in 25.06+) enables:
1. Generate calculation results in Excel format
2. Write the file to the Planning Inbox
3. Users download directly from Planning UI
4. Useful for audit trails and distribution

## Debugging Groovy Rules

### Using println for Logging

Groovy's `println` statements appear in the Planning Cloud job console. Add debug output strategically:

```groovy
println("DEBUG: Starting allocation rule")
println("DEBUG: Total overhead = ${totalOverhead}")
println("DEBUG: Division iteration starting")

for (String division in divisions) {
    println("DEBUG: Processing division ${division}")
    // ... processing ...
    println("DEBUG: Allocated ${amount} to ${division}")
}
```

### Checking Job Console

After executing a rule, navigate to the job console to view println output and any exceptions. This is invaluable for diagnosing issues.

### Using Rule.sendMessage for User Feedback

Unlike println, `Rule.sendMessage` shows feedback in the Planning UI and is visible to end users. Use this for normal operation summaries:

```groovy
Rule.sendMessage("Processing 1,000 cells...")
Rule.sendMessage("Allocation completed. Total: ${total}")
```

### Groovy Script Validator (25.08)

Planning Cloud 25.08 introduced a Groovy Script Validator that:
- Checks syntax before execution
- Identifies undefined variables
- Validates object method calls
- Provides error messages before runtime

Use the validator to catch errors before deploying rules to production.

## Common Pitfalls and How to Avoid Them

**1. Null Pointer Exceptions**
Always check for null before accessing objects:
```groovy
def grid = Rule.getDataGrid("MyGrid")
if (grid == null) {
    Rule.raiseException("Grid not found")
}
```

**2. Division by Zero**
Check denominators before division:
```groovy
if (denominator == 0) {
    Rule.raiseException("Cannot divide by zero")
}
double result = numerator / denominator
```

**3. Infinite Loops**
Add iteration limits:
```groovy
int maxIterations = 10_000
int iterations = 0

while (iterator.hasNext() && iterations < maxIterations) {
    iterations++
    // process
}

if (iterations >= maxIterations) {
    Rule.raiseException("Max iterations exceeded")
}
```

**4. Floating-Point Precision**
Use proper rounding for financial calculations:
```groovy
double rounded = Math.round(value * 100.0) / 100.0
```

## Conclusion

Groovy rules in Planning Cloud provide powerful extensibility for complex business logic. Start with the examples above and adapt them to your specific scenarios. The key patterns—allocation, data copy, conditional logic, runtime parameters, and notifications—solve the vast majority of planning automation needs.

As you become more comfortable, you'll discover advanced patterns like parallel processing, external API integration, and sophisticated error handling. Groovy's full programming language capabilities are at your disposal.
