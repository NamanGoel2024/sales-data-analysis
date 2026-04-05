import pandas as pd
import numpy as np

np.random.seed(42)
products = ['Laptop', 'Phone', 'Tablet', 'Headphones', 'Charger']
n = 200

df = pd.DataFrame({
    'Date': pd.date_range('2024-01-01', periods=n, freq='2D').astype(str),
    'Product': np.random.choice(products, n),
    'Units_Sold': np.random.randint(1, 50, n),
    'Unit_Price': np.random.choice([999, 499, 299, 79, 19], n),
    'Region': np.random.choice(['North', 'South', 'East', 'West', None], n),
    'Salesperson': np.random.choice(['Alice', 'Bob', 'Charlie', None], n)
})

# Inject missing values and inconsistencies
df.loc[df.sample(15).index, 'Units_Sold'] = None
df.loc[df.sample(5).index, 'Product'] = 'laptop'  # lowercase inconsistency
df.to_csv('data/raw_sales_data.csv', index=False)
