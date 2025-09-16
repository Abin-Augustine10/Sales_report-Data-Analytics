import pandas as pd
from Monthly_revenue_growth import monthly_growth
from Best_customer import best_customer
from Sale_by_region import sales_by_region
from Visualisation import visualisation
from Dashboard import dashboard

# Load the datasets
orders = pd.read_excel("orders.xlsx")
customers = pd.read_excel("customers.xlsx")
salesreps = pd.read_excel("salesreps.xlsx")

# Show first 5 rows of each
print("Orders Sample:\n", orders.head(), "\n")
print("Customers Sample:\n", customers.head(), "\n")
print("Sales Reps Sample:\n", salesreps.head(), "\n")

# Check structure
print("Orders Info:")
print(orders.info())

# Check missing values in all datasets
print("Missing values in Orders:\n", orders.isnull().sum(), "\n")
print("Missing values in Customers:\n", customers.isnull().sum(), "\n")
print("Missing values in Sales Reps:\n", salesreps.isnull().sum(), "\n")

# --- Clean column names (snake_case) ---
orders.columns = orders.columns.str.strip().str.lower().str.replace(" ", "_")
customers.columns = customers.columns.str.strip().str.lower().str.replace(" ", "_")
salesreps.columns = salesreps.columns.str.strip().str.lower().str.replace(" ", "_")

print("Cleaned Orders Columns:", orders.columns)
print("Cleaned Customers Columns:", customers.columns)
print("Cleaned SalesReps Columns:", salesreps.columns)

# --- Fix mismatched column names ---
# Rename orders.sales_rep -> sales_rep_id for consistency
orders = orders.rename(columns={"sales_rep": "sales_rep_id"})

# Rename customer & sales rep name columns to avoid duplicate 'name'
customers = customers.rename(columns={"name": "customer_name"})
salesreps = salesreps.rename(columns={"name": "rep_name"})

# --- Convert data types ---
orders['order_date'] = pd.to_datetime(orders['order_date'], errors='coerce')
orders['sales_amount'] = pd.to_numeric(orders['total_amount'], errors='coerce')

# --- Merge datasets ---
orders_customers = pd.merge(orders, customers, on="customer_id", how="left")
final_df = pd.merge(orders_customers, salesreps, on="sales_rep_id", how="left")

# --- Final dataset ---
print("Final Dataset Sample:\n", final_df.head())
print("Final Shape:", final_df.shape)


print("Final Dataset Info:")
print(final_df.describe(include="all"))


# Total Revenue
total_revenue = final_df['sales_amount'].sum()

# Average Order Value
avg_order_value = final_df['sales_amount'].mean()

# Total Orders
total_orders = final_df['order_id'].nunique()

# Total Customers
total_customers = final_df['customer_id'].nunique()

# Total Sales Reps
total_reps = final_df['sales_rep_id'].nunique()

print(f"Total Revenue: {total_revenue}")
print(f"Average Order Value: {avg_order_value}")
print(f"Total Orders: {total_orders}")
print(f"Total Customers: {total_customers}")
print(f"Total Sales Reps: {total_reps}")

# monthly growth
monthly_growth(final_df)
# best customers 
best_customer(final_df)
# sales by region
sales_by_region(final_df)

final_df.to_csv("cleaned_sales_data.csv", index=False)

visualisation(final_df)
dashboard(final_df)