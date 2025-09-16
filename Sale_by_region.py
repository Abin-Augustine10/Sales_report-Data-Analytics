def sales_by_region(final_df):
    sales_by_region = final_df.groupby("region")['sales_amount'].sum().sort_values(ascending=False)
    print("Sales by Region:\n", sales_by_region)
