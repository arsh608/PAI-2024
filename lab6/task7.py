import pandas as pd

df = pd.read_excel(r'C:\Users\arsha\OneDrive\Desktop\employee.xlsx')
#install openpyxl to read xlxs files
df['Hire Date'] = pd.to_datetime(df['Hire Date'], format='%m/%d/%Y')

specified_year = 2016

filtered_df = df[df['Hire Date'].dt.year == specified_year]
print(filtered_df)
