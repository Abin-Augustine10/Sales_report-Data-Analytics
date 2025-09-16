import matplotlib.pyplot as plt
import seaborn as sns
def dashboard(final_df):


    # --- Revenue Trend (Monthly) ---
    monthly_revenue = final_df.groupby(final_df['order_date'].dt.to_period("M"))['sales_amount'].sum()
    monthly_revenue.index = monthly_revenue.index.to_timestamp()

    # --- Top 5 Customers ---
    top_customers = final_df.groupby("customer_name")['sales_amount'].sum().nlargest(5)

    # --- Top 5 Sales Reps ---
    top_reps = final_df.groupby("rep_name")['sales_amount'].sum().nlargest(5)

    # --- Region Sales ---
    region_sales = final_df.groupby("region")['sales_amount'].sum()

    # Create a 2x2 dashboard
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))

    # 1. Monthly Revenue Trend
    sns.lineplot(x=monthly_revenue.index, y=monthly_revenue.values, marker="o", ax=axs[0,0])
    axs[0,0].set_title("Monthly Revenue Trend")
    axs[0,0].set_xlabel("Month")
    axs[0,0].set_ylabel("Revenue")
    axs[0,0].grid(True)

    # 2. Top Customers
    sns.barplot(x=top_customers.values, y=top_customers.index, palette="Blues_d", ax=axs[0,1])
    axs[0,1].set_title("Top 5 Customers by Revenue")
    axs[0,1].set_xlabel("Revenue")
    axs[0,1].set_ylabel("Customer")

    # 3. Top Sales Reps
    sns.barplot(x=top_reps.values, y=top_reps.index, palette="Greens_d", ax=axs[1,0])
    axs[1,0].set_title("Top 5 Sales Reps by Revenue")
    axs[1,0].set_xlabel("Revenue")
    axs[1,0].set_ylabel("Sales Rep")

    # 4. Region Sales (Pie Chart)
    axs[1,1].pie(region_sales.values, labels=region_sales.index, autopct="%1.1f%%", startangle=90)
    axs[1,1].set_title("Revenue by Region")

    # Adjust layout
    plt.tight_layout()
    plt.savefig("charts/dashboard.png")
    plt.show()
