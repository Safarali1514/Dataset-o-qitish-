import pandas as pd

df = pd.read_csv('sales.csv')

print("Datasetning birinchi 5 qatori:")
print(df.head()) 

print("\nStatistikalar:")
print(df.describe())  
avg_unit_price = df['unit_price'].mean()
print(f"O‘rtacha narx: {avg_unit_price}")

df['total_sales'] = df['unit_price'] * df['quantity'] 
total_sales = df['total_sales'].sum()
print(f"Jami savdo hajmi: {total_sales}")


top_selling_products = df.groupby('product_name')['quantity'].sum().sort_values(ascending=False).head(5)
print("\nEng ko‘p sotilgan 5 mahsulot:")
print(top_selling_products)
