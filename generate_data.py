import pandas as pd
import random
from datetime import datetime, timedelta
import os

def generate_sales_data(n=1000):
    products = {
        'Laptop Gaming': 15000000,
        'Laptop Office': 8000000,
        'Mouse Wireless': 150000,
        'Keyboard Mechanical': 500000,
        'Monitor 24 inch': 2000000,
        'Headset Bluetooth': 350000,
        'Smartphone Flagship': 12000000,
        'Smartphone Mid-range': 4000000
    }
    
    cities = ['Jakarta', 'Surabaya', 'Bandung', 'Medan', 'Makassar']
    payment_methods = ['Credit Card', 'E-Wallet', 'Bank Transfer', 'COD']
    
    data = []
    
    # Generate data setahun terakhir
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    
    for i in range(n):
        prod_name = random.choice(list(products.keys()))
        price = products[prod_name]
        qty = random.randint(1, 3)
        total = price * qty
        
        # Random date
        date_random = start_date + timedelta(days=random.randint(0, 365))
        
        data.append({
            'Order ID': f"ORD-{1000+i}",
            'Date': date_random,
            'Customer ID': random.randint(101, 150), # 50 Customer unik
            'City': random.choice(cities),
            'Product': prod_name,
            'Price': price,
            'Quantity': qty,
            'Total Sales': total,
            'Payment': random.choice(payment_methods)
        })
        
    df = pd.DataFrame(data)
    
    # Pastikan folder data ada
    if not os.path.exists('data'):
        os.makedirs('data')
        
    df.to_csv('data/sales_data.csv', index=False)
    print(f"Berhasil! Data penjualan ({n} transaksi) disimpan di data/sales_data.csv")

if __name__ == "__main__":
    generate_sales_data()