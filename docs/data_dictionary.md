# Data Dictionary - Sales Pattern Analysis

**Dataset:** dataregina/datasets-para-proyecto-bi
**Source:** Kaggle
**Downloaded:** November 21, 2025
**Total Tables:** 5
**Total Records:** 3,797 rows across all tables

---

## Table of Contents

1. [Overview](#overview)
2. [Data Model](#data-model)
3. [Table Definitions](#table-definitions)
   - [categorias](#1-categorias-product-categories)
   - [clientes](#2-clientes-customers)
   - [metodos_pago](#3-metodos_pago-payment-methods)
   - [productos](#4-productos-products)
   - [ventas](#5-ventas-sales-transactions)
4. [Relationships](#relationships)
5. [Business Rules](#business-rules)
6. [Data Quality Notes](#data-quality-notes)

---

## Overview

This dataset represents sales transactions from a retail business in Argentina, covering multiple product categories, customer regions, and payment methods. The data spans from April 2023 (customer registrations) through September 2024 (sales transactions).

### Key Statistics
- **Time Range (Sales):** February 1, 2024 - September 9, 2024 (~7 months)
- **Time Range (Customers):** April 1, 2023 - October 31, 2023 (~7 months)
- **Total Customers:** 326 unique customers
- **Total Products:** 38 unique products across 8 categories
- **Total Sales:** 3,029 transactions
- **Geographic Coverage:** 6 regions of Argentina

---

## Data Model

```
┌─────────────────┐
│   categorias    │
│  (8 categories) │
└────────┬────────┘
         │
         │ ID_Categoria
         │
         ↓
┌─────────────────┐        ┌──────────────────┐
│    productos    │←──────→│      ventas      │
│  (38 products)  │        │  (3,029 sales)   │
└─────────────────┘        └────────┬─────────┘
   Categoría                        │
                                    │ ID_Cliente
                                    │ ID_Producto
                                    │ Método_Pago
                                    ↓
                          ┌──────────────────┐
                          │     clientes     │
                          │  (326 customers) │
                          └──────────────────┘

                          ┌──────────────────┐
                          │  metodos_pago    │
                          │  (5 methods)     │
                          └──────────────────┘
```

---

## Table Definitions

### 1. `categorias` (Product Categories)

**Purpose:** Catalog of product categories available in the store.

**Granularity:** One row per category

**Row Count:** 8 rows

| Column | Data Type | Description | Example | Constraints |
|--------|-----------|-------------|---------|-------------|
| **ID_Categoria** | Integer | Unique identifier for category (PRIMARY KEY) | 1 | NOT NULL, UNIQUE |
| **Categoría** | String | Category name | "Lácteos" | NOT NULL, UNIQUE |
| **Descripción** | String | Detailed description of category | "Productos lácteos frescos y procesados..." | NOT NULL |

**Categories List:**
1. Lácteos (Dairy products)
2. Carnicería (Butchery/Meats)
3. Panadería (Bakery)
4. Frutas y Verduras (Fruits and Vegetables)
5. Bebidas (Beverages)
6. Congelados (Frozen foods)
7. Galletitas y Snacks (Cookies and Snacks)
8. Conservas (Canned goods)

**Data Quality:**
- ✅ No null values
- ✅ No duplicates
- ✅ All IDs sequential (1-8)

---

### 2. `clientes` (Customers)

**Purpose:** Customer master data including contact information and regional assignment.

**Granularity:** One row per customer

**Row Count:** 326 rows

| Column | Data Type | Description | Example | Constraints |
|--------|-----------|-------------|---------|-------------|
| **ID_Cliente** | Integer | Unique customer identifier (PRIMARY KEY) | 1 | NOT NULL, UNIQUE, Range: 1-326 |
| **Nombre** | String | Customer first name | "Karisa" | NOT NULL |
| **Apellido** | String | Customer last name | "Cromett" | NOT NULL |
| **Email** | String | Customer email address | "kcromett0@imageshack.us" | NOT NULL, UNIQUE |
| **Fecha_Resgistro** | String (Date) | Registration date (DD/MM/YYYY) | "19/11/2023" | NOT NULL, Format: DD/MM/YYYY |
| **Región** | String | Geographic region | "Patagonia" | NOT NULL, 6 distinct values |

**Regional Distribution:**
| Region | Count | Percentage |
|--------|-------|------------|
| Buenos Aires | 111 | 34.0% |
| Patagonia | 64 | 19.6% |
| Centro | 63 | 19.3% |
| Cuyo | 44 | 13.5% |
| NEA (Northeast) | 37 | 11.3% |
| NOA (Northwest) | 7 | 2.1% |

**Date Range:**
- First Registration: April 1, 2023
- Last Registration: October 31, 2023
- Span: 214 days (~7 months)
- Unique Registration Dates: 198

**Data Quality:**
- ✅ No null values
- ✅ All emails unique
- ✅ All ID_Cliente values used in ventas table
- ⚠️ Date format is string (needs parsing)
- ⚠️ "Fecha_Resgistro" has typo (should be "Fecha_Registro")

---

### 3. `metodos_pago` (Payment Methods)

**Purpose:** Catalog of available payment methods.

**Granularity:** One row per payment method

**Row Count:** 5 rows

| Column | Data Type | Description | Example | Constraints |
|--------|-----------|-------------|---------|-------------|
| **ID_Metodo** | Integer | Unique payment method ID (PRIMARY KEY) | 1 | NOT NULL, UNIQUE, Range: 1-5 |
| **Método** | String | Payment method name | "Efectivo" | NOT NULL, UNIQUE |
| **Descripción** | String | Detailed description | "Pago en dinero en efectivo..." | NOT NULL |

**Payment Methods List:**
1. Efectivo (Cash)
2. Tarjeta de Crédito (Credit Card)
3. Tarjeta de Débito (Debit Card)
4. Billetera Virtual (Digital Wallet)
5. Transferencia Bancaria (Bank Transfer)

**Usage in Sales (from ventas table):**
| Method | ID | Transaction Count | Percentage |
|--------|----|--------------------|------------|
| Billetera Virtual | 4 | 872 | 28.8% |
| Transferencia Bancaria | 5 | 796 | 26.3% |
| Efectivo | 1 | 557 | 18.4% |
| Tarjeta de Débito | 3 | 542 | 17.9% |
| Tarjeta de Crédito | 2 | 262 | 8.6% |

**Data Quality:**
- ✅ No null values
- ✅ No duplicates
- ✅ All IDs sequential (1-5)

---

### 4. `productos` (Products)

**Purpose:** Product master data including pricing and inventory information.

**Granularity:** One row per product

**Row Count:** 38 rows

| Column | Data Type | Description | Example | Constraints |
|--------|-----------|-------------|---------|-------------|
| **ID_Producto** | Integer | Unique product identifier (PRIMARY KEY) | 1 | NOT NULL, UNIQUE, Range: 1-38 |
| **Nombre_producto** | String | Product name | "Leche" | NOT NULL, UNIQUE |
| **Categoría** | String | Category name (FOREIGN KEY to categorias.Categoría) | "Lácteos" | NOT NULL, 8 distinct values |
| **Precio_Unitario** | String (Decimal) | Unit price with comma as decimal separator | "12,24" | NOT NULL, Format: "##,##" |
| **Stock** | Integer | Current stock level (units) | 3327 | NOT NULL, Positive integer |

**Price Statistics:**
- Minimum Price: $3.25
- Maximum Price: $28.56
- Average Price: $9.84
- Unique Prices: 33

**Stock Statistics:**
- Minimum Stock: 1,363 units
- Maximum Stock: 5,137 units
- Average Stock: 3,137 units

**Products per Category:**
| Category | Product Count |
|----------|---------------|
| Carnicería | 6 |
| Frutas y Verduras | 6 |
| Lácteos | 5 |
| Panadería | 5 |
| Bebidas | 4 |
| Congelados | 4 |
| Galletitas y Snacks | 4 |
| Conservas | 4 |

**Data Quality:**
- ✅ No null values
- ✅ All products have unique names
- ✅ All ID_Producto values used in ventas table
- ✅ All categories exist in categorias table
- ⚠️ Precio_Unitario stored as string with comma separator (needs conversion)
- ⚠️ No unit of measure specified for stock

---

### 5. `ventas` (Sales Transactions)

**Purpose:** Transactional data recording all sales events.

**Granularity:** One row per sale transaction

**Row Count:** 3,029 rows

| Column | Data Type | Description | Example | Constraints |
|--------|-----------|-------------|---------|-------------|
| **ID_Venta** | Integer | Unique sale transaction ID (PRIMARY KEY) | 919 | NOT NULL, UNIQUE, Range: 1-3000 |
| **Fecha** | String (Date) | Transaction date | "31/01/2024" | NOT NULL, Format varies |
| **ID_Cliente** | Integer | Customer ID (FOREIGN KEY to clientes.ID_Cliente) | 10 | NOT NULL, Range: 1-326 |
| **ID_Producto** | Integer | Product ID (FOREIGN KEY to productos.ID_Producto) | 25 | NOT NULL, Range: 1-38 |
| **Cantidad** | Integer | Quantity purchased | 5 | NOT NULL, Range: 1-6 |
| **Método_Pago** | Integer | Payment method ID (FOREIGN KEY to metodos_pago.ID_Metodo) | 1 | NOT NULL, Range: 1-5 |
| **Estado** | String | Transaction status | "Completa" | NOT NULL, 3 distinct values |

**Date Range:**
- First Transaction: February 1, 2024
- Last Transaction: September 9, 2024
- Span: 221 days (~7.3 months)
- Unique Transaction Dates: 595

**Transaction Status Distribution:**
| Status | Count | Percentage |
|--------|-------|------------|
| Completa (Complete) | 2,548 | 84.1% |
| Pendiente (Pending) | 471 | 15.5% |
| Cancelada (Cancelled) | 10 | 0.3% |

**Quantity Distribution:**
| Quantity | Transactions | Percentage |
|----------|--------------|------------|
| 1 | 501 | 16.5% |
| 2 | 528 | 17.4% |
| 3 | 516 | 17.0% |
| 4 | 494 | 16.3% |
| 5 | 494 | 16.3% |
| 6 | 496 | 16.4% |

**Transaction Metrics:**
- Average Quantity: 3.48 units per transaction
- Total Quantity Sold: 10,529 units
- Unique Customers: 326 (100% of customer base)
- Unique Products: 38 (100% of product catalog)

**Data Quality:**
- ✅ No null values
- ✅ All foreign keys valid (match parent tables)
- ⚠️ Date format inconsistent ("31/01/2024" vs "31/1/2024")
- ⚠️ 29 duplicate ID_Venta values (3,000 unique IDs for 3,029 rows)
- ⚠️ Date stored as string (needs parsing)

---

## Relationships

### Foreign Key Constraints

1. **ventas.ID_Cliente → clientes.ID_Cliente**
   - Cardinality: Many-to-One
   - Referential Integrity: ✅ All customer IDs exist
   - Coverage: 100% of customers have at least one transaction

2. **ventas.ID_Producto → productos.ID_Producto**
   - Cardinality: Many-to-One
   - Referential Integrity: ✅ All product IDs exist
   - Coverage: 100% of products have been sold

3. **ventas.Método_Pago → metodos_pago.ID_Metodo**
   - Cardinality: Many-to-One
   - Referential Integrity: ✅ All payment method IDs exist
   - Coverage: All 5 payment methods used

4. **productos.Categoría → categorias.Categoría**
   - Cardinality: Many-to-One
   - Referential Integrity: ✅ All categories exist
   - Coverage: All 8 categories have products

### Entity Relationship Summary

```sql
-- Conceptual schema
clientes (326 rows)
  ├── ID_Cliente (PK)
  └── has many → ventas

categorias (8 rows)
  ├── Categoría (PK)
  └── has many → productos

productos (38 rows)
  ├── ID_Producto (PK)
  ├── Categoría (FK → categorias)
  └── has many → ventas

metodos_pago (5 rows)
  ├── ID_Metodo (PK)
  └── has many → ventas

ventas (3,029 rows)
  ├── ID_Venta (PK, with 29 duplicates)
  ├── ID_Cliente (FK → clientes)
  ├── ID_Producto (FK → productos)
  └── Método_Pago (FK → metodos_pago)
```

---

## Business Rules

### Transactions
1. **Quantity Range:** Customers can purchase 1-6 units per transaction
2. **Transaction States:**
   - "Completa": Successfully completed sale
   - "Pendiente": Pending/in-progress sale
   - "Cancelada": Cancelled sale
3. **Complete Transactions:** 84.1% completion rate

### Customers
1. **Registration Period:** Customers registered 3-12 months before sales period
2. **Activity Rate:** 100% of registered customers have made at least one purchase
3. **Regional Coverage:** All 6 Argentine regions represented

### Products
1. **Category Distribution:** Fairly balanced across 8 categories (4-6 products each)
2. **Price Range:** Products range from $3.25 to $28.56
3. **Stock Levels:** All products maintain inventory between 1,363 and 5,137 units
4. **Sales Coverage:** Every product in catalog has been sold

### Payment Methods
1. **Digital Preference:** 55.1% of transactions use digital methods (Billetera Virtual + Transferencia)
2. **Card Usage:** 26.5% use cards (credit + debit)
3. **Cash Usage:** 18.4% still use cash

---

## Data Quality Notes

### Data Type Issues

1. **Date Fields as Strings:**
   - `clientes.Fecha_Resgistro`: String format "DD/MM/YYYY"
   - `ventas.Fecha`: String format inconsistent ("DD/MM/YYYY" and "DD/M/YYYY")
   - **Action Required:** Parse to datetime format

2. **Decimal as String:**
   - `productos.Precio_Unitario`: String with comma separator ("12,24")
   - **Action Required:** Convert to float, replace comma with period

3. **Encoding Issues:**
   - Column names with special characters may display incorrectly (á, é, í, ó, ú, ñ)
   - **Action Required:** Ensure UTF-8 encoding throughout pipeline

### Data Integrity Issues

1. **Duplicate IDs:**
   - `ventas.ID_Venta`: 29 duplicate IDs (3,000 unique for 3,029 rows)
   - **Impact:** Cannot use as true primary key
   - **Action Required:** Investigate duplicates, potentially create new unique ID

2. **Column Name Typo:**
   - `clientes.Fecha_Resgistro`: Typo in "Registro"
   - **Action Required:** Rename for consistency

3. **Date Format Inconsistency:**
   - `ventas.Fecha`: Mixed formats ("31/01/2024" vs "31/1/2024")
   - **Action Required:** Standardize format during parsing

### Missing Data

- ✅ **No null values** in any table
- ✅ **Complete referential integrity** across all foreign keys

### Potential Data Anomalies to Investigate

1. **Customer Registration vs Sales Timeline:**
   - Customers registered: April-October 2023
   - Sales period: February-September 2024
   - Gap of 3-12 months between registration and sales data
   - **Question:** Is there missing sales data from late 2023/early 2024?

2. **Uniform Quantity Distribution:**
   - Nearly equal distribution across quantities 1-6
   - **Question:** Is this natural or synthetic data?

3. **High Completion Rate:**
   - 84.1% completion rate seems high
   - Only 0.3% cancellations
   - **Question:** Typical for this business or data filtering?

---

## Derived Metrics & Calculations

### Recommended Calculated Fields

1. **Total Sale Amount:**
   ```sql
   ventas.Cantidad * productos.Precio_Unitario
   ```

2. **Sale Date (Parsed):**
   ```python
   pd.to_datetime(ventas.Fecha, format='%d/%m/%Y', errors='coerce')
   ```

3. **Registration Date (Parsed):**
   ```python
   pd.to_datetime(clientes.Fecha_Resgistro, format='%d/%m/%Y')
   ```

4. **Customer Lifetime Value (CLV):**
   ```sql
   SUM(ventas.Cantidad * productos.Precio_Unitario)
   GROUP BY ventas.ID_Cliente
   ```

5. **Product Revenue:**
   ```sql
   SUM(ventas.Cantidad * productos.Precio_Unitario)
   WHERE ventas.Estado = 'Completa'
   GROUP BY productos.ID_Producto
   ```

6. **Inventory Turnover:**
   ```sql
   SUM(ventas.Cantidad WHERE Estado = 'Completa') / productos.Stock
   ```

7. **RFM Features:**
   - **Recency:** Days since last purchase
   - **Frequency:** Count of purchases per customer
   - **Monetary:** Total spent per customer

---

## Usage Guidelines

### For Data Cleaning:
1. Parse all date strings to datetime
2. Convert Precio_Unitario to float
3. Standardize date formats
4. Handle duplicate ID_Venta records
5. Validate all foreign key relationships

### For Feature Engineering:
1. Extract temporal features (day, month, quarter, day of week)
2. Calculate derived monetary values
3. Create customer segments based on region
4. Aggregate sales by time periods
5. Calculate rolling statistics

### For Analysis:
1. Filter by Estado = 'Completa' for completed sales
2. Join tables on appropriate foreign keys
3. Consider regional stratification
4. Account for seasonal patterns (7-month period)
5. Analyze payment method trends

---

**Document Version:** 1.0
**Last Updated:** November 21, 2025
**Author:** Sales Pattern Analysis Team
**Status:** Complete

---

## Appendix: Sample Queries

### Total Revenue
```sql
SELECT
    SUM(CAST(REPLACE(p.Precio_Unitario, ',', '.') AS DECIMAL) * v.Cantidad) AS Total_Revenue
FROM ventas v
JOIN productos p ON v.ID_Producto = p.ID_Producto
WHERE v.Estado = 'Completa'
```

### Sales by Region
```sql
SELECT
    c.Región,
    COUNT(v.ID_Venta) AS Num_Transactions,
    SUM(v.Cantidad) AS Total_Units
FROM ventas v
JOIN clientes c ON v.ID_Cliente = c.ID_Cliente
WHERE v.Estado = 'Completa'
GROUP BY c.Región
ORDER BY Num_Transactions DESC
```

### Top Products
```sql
SELECT
    p.Nombre_producto,
    p.Categoría,
    COUNT(v.ID_Venta) AS Num_Sales,
    SUM(v.Cantidad) AS Total_Units_Sold
FROM ventas v
JOIN productos p ON v.ID_Producto = p.ID_Producto
WHERE v.Estado = 'Completa'
GROUP BY p.ID_Producto, p.Nombre_producto, p.Categoría
ORDER BY Total_Units_Sold DESC
LIMIT 10
```
