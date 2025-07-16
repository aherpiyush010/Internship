
import pandas as pd


## 💾 **9️⃣ Reading and Writing Files**

# Read a CSV
df = pd.read_csv('sales_data_sample.csv', encoding = 'latin8')
print(df)

# Read an Excel file
df = pd.read_excel('filename.xlsx',engine='openpyxl')
print(df)

# # Export to CSV
df.to_csv('sales_data_sample.csv', index=False)

# Export to Excel
df.to_excel('filename.xlsx', index=False)
