
def monthly_growth(final_df):
    
    monthly_sales = final_df.groupby(final_df['order_date'].dt.to_period("M"))['sales_amount'].sum()

    print("Monthly Sales:\n", monthly_sales)
