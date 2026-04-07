---
title: 'FreeForm Planning — When to Use It and How to Configure It'
description: 'Understand when FreeForm Planning is the right choice over standard Planning, and learn how to configure FreeForm applications with BSO and ASO considerations.'
product: 'planning-cloud'
subcategory: 'tutorials'
pubDate: '2026-04-04'
---

# FreeForm Planning — When to Use It and How to Configure It

Oracle Planning Cloud provides two fundamentally different approaches to building planning applications: Standard Planning, which leverages the Planning framework with predefined features, and FreeForm Planning, which offers complete dimensional flexibility for organizations with unique analytical needs. This guide helps you understand when FreeForm is the right choice and how to configure it successfully.

## FreeForm vs Standard Planning: The Core Difference

### Standard Planning Architecture
Standard Planning enforces a specific dimensional model and framework. You get seven standard dimensions (Entity, Account, Period, Scenario, Version, Year, Currency), built-in Task Lists for approval workflows, predefined modules like Workforce and CapEx Planning, and tight integration with Planning-specific features like the Allocation Engine and Transfers.

The tradeoff is rigidity. If your planning needs don't fit the standard model—if you need custom dimensions in non-standard configurations, or if you want to work at a lower level directly with Essbase—Standard Planning can feel constraining.

### FreeForm Planning Architecture
FreeForm Planning removes the Planning framework entirely. Instead, you work directly with Essbase multidimensional cube technology. You define exactly the dimensions you need, in any configuration you want. There are no predefined Task Lists, no built-in Workforce module, and no Planning-specific features. What you get instead is complete freedom to design a cube that matches your analytical domain.

FreeForm is Essbase-centric. You design dense and sparse dimensions, optimize aggregate tables (for ASO cubes), and handle all calculation logic through Essbase calculation scripts or Groovy code.

## When to Choose FreeForm Planning

### 1. Migrating from On-Premises Essbase
If you're moving from an on-premises Essbase system to the cloud, FreeForm Planning is the natural migration path. Your existing Essbase cubes—with their custom dimensions and calculations—can be more easily adapted to FreeForm than forced into Standard Planning's framework.

**Migration scenario**: You have a global supply chain optimization cube with dimensions for Product, Plant, Distribution Center, and Customer Segment. The non-standard dimensional structure doesn't fit Planning's Entity-Account-Period model. FreeForm allows you to preserve this structure while gaining cloud benefits.

### 2. Ad-Hoc Analysis and Exploration
When your primary use case is exploratory analysis rather than structured, guided planning, FreeForm shines. Users with Essbase knowledge can build custom views, modify calculations, and experiment without hitting Planning framework constraints.

**Analysis scenario**: Your data science team wants to analyze sales patterns across product, region, customer segment, and time period with custom calculations for seasonal adjustment and trend analysis. FreeForm's dimensional flexibility supports this without workaround.

### 3. Complex Dimensional Hierarchies
If your organization has non-standard hierarchies or requires multiple parallel hierarchies within a single dimension (e.g., organizational hierarchy, cost center hierarchy, and management hierarchy for the same entities), FreeForm handles this more elegantly than Standard Planning.

**Hierarchy scenario**: Your company has entities that report in three different hierarchies simultaneously: by geography, by business unit, and by P&L responsibility. FreeForm accommodates these overlapping structures directly.

### 4. No Need for Planning Framework Features
If you don't use Task Lists, approval workflows, Workforce Planning, CapEx Planning, or Transfers, there's no benefit to Standard Planning's framework. FreeForm is simpler and more lightweight.

**Lightweight scenario**: You need a reporting cube for KPI analysis and variance reporting, but you don't need data submission workflows or multi-version what-if capabilities. FreeForm's simpler model is a better fit.

### 5. Essbase-Native Cube Operations
If your team has deep Essbase expertise and wants to leverage Essbase-specific features like sparse optimization, aggregate tables, or native calc scripts, FreeForm gives you direct access.

**Advanced scenario**: Your team maintains a large ASO (Aggregate Storage Option) cube for financial reporting that requires careful optimization of aggregate generation. FreeForm's exposure of these Essbase details is valuable.

## Configuring FreeForm Planning: Step by Step

### Creating a FreeForm Application

Navigate to Planning Cloud and select "Create Application". When prompted for application type, choose "FreeForm Planning" instead of "Standard Planning".

Provide:
- **Application name**: Use a clear, descriptive name (e.g., "SupplyChain_Analytics")
- **Description**: Document the purpose and expected users
- **Cube type**: Choose between BSO (Block Storage Option) or ASO (Aggregate Storage Option)

### Understanding Cube Types: BSO vs ASO

**Block Storage Option (BSO)**
BSO cubes store data in dense blocks. They're optimized for write-back scenarios where users frequently update values. BSO automatically aggregates parent values from child data, so you don't need to explicitly calculate rollups. BSO cubes support all calculation functions and are ideal for planning scenarios where users modify data.

Characteristics:
- Fast write performance
- Automatic aggregation from children to parents
- Support for all calculation features
- Efficient for smaller to medium-sized cubes
- Dense dimensions aggregate quickly

**Aggregate Storage Option (ASO)**
ASO cubes pre-calculate aggregations and store them in separate aggregate tables. This makes reads extremely fast (ideal for dashboards and reporting) but requires explicit cube rebuild when source data changes. ASO cubes don't support write-back operations on aggregated cells.

Characteristics:
- Extremely fast query performance
- Read-optimized for reporting
- No write-back support on aggregated members
- Requires manual aggregate generation after data loads
- Better for large, reporting-heavy cubes

**Choosing between BSO and ASO**:
- Choose BSO if your users will frequently enter or modify data
- Choose ASO if your cube is primarily for reporting and read-only analysis
- Consider Hybrid mode (BSO for detailed level, ASO for reporting) if you need both

### Defining Dimensions for FreeForm

Unlike Standard Planning, which gives you predefined dimensions, FreeForm requires you to define each dimension explicitly. For each dimension, specify:

**Dimension Name**: Use a clear name like "Product", "Region", "Account", "Time"

**Members and Hierarchy**: Define the parent-child structure
- Create parent (consolidation) members that roll up child data
- Specify which members accept data entry (leaf level)
- Which members are calculations (parents derived from children)

**Properties**: For each dimension:
- **Type**: Time (for period/year dimensions), Account (for account dimensions), Standard (for everything else)
- **Dense vs Sparse**: Dense dimensions are pre-aggregated for fast retrieval; sparse dimensions calculate on demand
  - Time is typically dense
  - Account is often dense
  - Custom dimensions (Product, Region) are usually sparse

For BSO cubes, optimize by making frequently analyzed dimensions dense. For ASO cubes, all aggregations are pre-calculated, so the dense/sparse designation matters less, but you'll explicitly manage aggregate generation.

**Dimension Ordering**: In FreeForm, you'll specify how dimensions relate to each other and whether they form the data measures:
- One dimension typically contains your metrics (revenue, cost, quantity, etc.)—this is often called the "Account" or "Measures" dimension
- Other dimensions provide context (time, product, region, scenario)

### Handling Cube Refresh and Aggregation

After defining dimensions, you need to initialize the cube. This process:
- Creates the multidimensional database structure
- Aggregates parent values from children (for BSO)
- Pre-calculates all aggregations (for ASO)
- Makes the cube available for data load

For ASO cubes, you'll also perform "aggregate generation" after loading data. This recalculates all the pre-computed aggregations to reflect the latest data.

### Data Entry and Reporting in FreeForm

Unlike Standard Planning with its predefined forms and Task Lists, FreeForm requires either:

**Smart View**: Users connect via Excel using Smart View, create ad-hoc grids, and write data directly to the cube. This requires Essbase knowledge but is highly flexible.

**Custom Web Forms**: You can build custom web forms (using Planning Cloud's form builder or external UI frameworks) that write to FreeForm cubes via REST APIs or data load processes.

**Direct Data Loads**: For bulk data entry, use Data Exchange, Data Management, or Data Integration to load data files into the cube.

### New in Planning Cloud 25.11: Parent-Level Data Entry in FreeForm

Planning Cloud 25.11 introduced a significant enhancement for FreeForm Planning: the ability to enter data at the parent (consolidation) level in grids. Previously, FreeForm cubes enforced data entry only at leaf (detail) levels, consistent with Essbase's traditional behavior.

With this enhancement:
- Users can now enter data directly into parent members in Smart View grids
- The system automatically distributes (or "pushes down") parent-level entries across children
- Useful for top-down planning scenarios where a manager enters a total and wants Planning to distribute it

**How it works**:
1. Create a Smart View grid that includes parent members in rows
2. Enable the "Allow Parent Entry" option in the grid settings
3. Users enter a total at the parent level
4. A distribution algorithm (weighted by existing proportions or equally) pushes the value to children
5. Child-level details automatically update to match the new parent total

This feature bridges the gap between Standard Planning's top-down capability and FreeForm's detailed modeling, making FreeForm more suitable for blended planning processes.

### Calculation and Business Rules in FreeForm

FreeForm doesn't include Calculation Manager (Planning's graphical rule builder). Instead, you use:

**Groovy Scripts**: Write business logic in Groovy directly against the Essbase cube. You have full access to the Essbase Java API, allowing complex calculations, data movements, and validations.

**Essbase Calculation Scripts**: For traditional Essbase administrators, you can write native calc script syntax (if your cube uses the traditional calculation engine).

**Data Movement via Groovy**: Because there are no built-in copy or allocation rules, you implement these via Groovy scripts that read from source cells and write to target cells.

## Hybrid Mode: BSO + ASO in One Application

For large, complex FreeForm applications, consider Hybrid mode:
- **Detailed level**: BSO cube with detailed dimensions where users enter data
- **Reporting level**: ASO cube with aggregated dimensions for fast reporting

Data flows from the BSO (detail) to the ASO (reporting) via scheduled data synchronization. Users enter at detailed level; analysts and executives query the ASO for performance.

This architecture is common in large-scale planning implementations where detail-level data entry must be lightning-fast, but reporting queries often aggregate across millions of cells.

## Comparison: FreeForm vs Standard Planning Quick Reference

| Feature | FreeForm | Standard |
|---------|----------|----------|
| Dimensional flexibility | Complete | Fixed framework |
| Task Lists/Workflows | No | Yes |
| Workforce Planning module | No | Yes |
| CapEx Planning module | No | Yes |
| Allocation Engine | No | Yes |
| Predefined forms | No | Yes |
| Direct Essbase access | Yes | Limited |
| Cube types (BSO/ASO) | Both | Primarily BSO |
| Graphical rule builder | No | Yes (Calculation Manager) |
| Business rule approach | Groovy/Calc scripts | Calculation Manager or Groovy |
| Migration from on-prem Essbase | Natural fit | Requires redesign |

## Configuration Checklist for FreeForm

When setting up a new FreeForm Planning application:

- [ ] Define all dimensions (name, members, hierarchy)
- [ ] Specify dense vs sparse for each dimension
- [ ] Configure dimension ordering
- [ ] Choose cube type (BSO, ASO, or Hybrid)
- [ ] Plan dense aggregation settings (for BSO)
- [ ] Plan aggregate generation strategy (for ASO)
- [ ] Build initial data load process (Data Exchange, Data Management, or direct load)
- [ ] Create Smart View templates or custom web forms for data entry
- [ ] Develop Groovy scripts for business rules and calculations
- [ ] Test data loads and aggregations
- [ ] Document dimension structure and calculation logic
- [ ] Train users on Smart View or custom form interfaces
- [ ] Plan refresh and optimization schedule

## Conclusion

FreeForm Planning is the right choice when you need Essbase-level control and dimensional flexibility that Standard Planning's framework constrains. It's ideal for organizations migrating from on-premises Essbase, building exploratory analytics cubes, or handling non-standard dimensional models.

The tradeoff is that you lose Planning Cloud's built-in features like Task Lists, Workforce Planning, and graphical rule builders. You gain direct Essbase control and dimensional freedom, along with new capabilities like parent-level data entry (available in 25.11).

If your team has Essbase expertise and your requirements don't depend on Planning-specific modules, FreeForm is worth serious consideration. You'll build a leaner, more flexible application that aligns directly with your analytical domain.
