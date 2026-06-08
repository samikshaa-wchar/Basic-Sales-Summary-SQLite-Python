
# Basic Sales Summary Using SQLite and Python

## Objective
Use SQL queries inside Python to analyze sales data and create a simple visualization.

## Tools Used
- Python
- SQLite
- Pandas
- Matplotlib

## SQL Query Used

```sql
SELECT
    product,
    SUM(quantity) AS total_qty,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product;
