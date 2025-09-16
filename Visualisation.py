import matplotlib.pyplot as plt
import seaborn as sns
import os

def visualisation(final_df):


# --- Revenue Trend (Monthly) ---
    os.makedirs("charts", exist_ok=True)

# --- Revenue Trend (Monthly) ---
    monthly_revenue = final_df.groupby(final_df['order_date'].dt.to_period("M"))['sales_amount'].sum()
    monthly_revenue.index = monthly_revenue.index.to_timestamp()

    plt.figure(figsize=(10, 5))
    sns.lineplot(x=monthly_revenue.index, y=monthly_revenue.values, marker="o")
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("charts/monthly_revenue.png")
    plt.show()

    # --- Top 5 Customers by Revenue ---
    top_customers = final_df.groupby("customer_name")['sales_amount'].sum().nlargest(5)

    plt.figure(figsize=(8, 5))
    sns.barplot(x=top_customers.values, y=top_customers.index, palette="Blues_d")
    plt.title("Top 5 Customers by Revenue")
    plt.xlabel("Revenue")
    plt.ylabel("Customer")
    plt.tight_layout()
    plt.savefig("charts/top_customers.png")
    plt.show()

    # --- Top 5 Sales Reps by Revenue ---
    top_reps = final_df.groupby("rep_name")['sales_amount'].sum().nlargest(5)

    plt.figure(figsize=(8, 5))
    sns.barplot(x=top_reps.values, y=top_reps.index, palette="Greens_d")
    plt.title("Top 5 Sales Reps by Revenue")
    plt.xlabel("Revenue")
    plt.ylabel("Sales Rep")
    plt.tight_layout()
    plt.savefig("charts/top_sales_reps.png")
    plt.show()

    # --- Revenue by Region ---
    region_sales = final_df.groupby("region")['sales_amount'].sum()

    plt.figure(figsize=(6, 6))
    plt.pie(region_sales.values, labels=region_sales.index, autopct="%1.1f%%", startangle=90)
    plt.title("Revenue by Region")
    plt.tight_layout()
    plt.savefig("charts/revenue_by_region.png")
    plt.show()