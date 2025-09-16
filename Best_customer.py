def best_customer(final_df):
    # Top 5 Customers
    top_customers = final_df.groupby("customer_name")['sales_amount'].sum().sort_values(ascending=False).head(5)
    print("Top Customers:\n", top_customers)

    # Top 5 Sales Reps
    top_reps = final_df.groupby("rep_name")['sales_amount'].sum().sort_values(ascending=False).head(5)
    print("Top Sales Reps:\n", top_reps)
