import pandas as pd
import numpy as np
import re

df = pd.read_excel('../data/products_temp.xls', sheetname='Sheet1').reset_index().drop('index',axis = 1)
df2 = pd.read_excel('../data/products_temp.xls', sheetname='Data').reset_index().drop('index',axis = 1)
ID = ['PA_' + "%05d" % (i,) for i in range(df.shape[0])]
active = [True if i == 'Active' else False for i in df['Active Status']]
Product_Type = ['Stockable Product' if i == 'Inventory Part' else 'Consumable' if i == 'Non-inventory Part' else 'Service' for i in df['Type']]
Name = list(df['Item'])
Sale_Description = list(df['Description'])
Description = [None for i in range(df.shape[0])]
Sale_Price = list(df['Price'])
Cost = list(df['Cost'])
Barcode = ["%05d" % (i,) + '_' +str(datetime.date.today()).replace('-','') for i in range(df.shape[0])]
Vendor_Vendor = list(df['Preferred Vendor'])
Account = df['Account']
df_p = pd.DataFrame(np.array([ID, Name, active, Product_Type, Sale_Price, Cost, Barcode, Description, Sale_Description]).T) 
df_p.columns = ['ID', "Name", "active", "Product Type", "Sale Price", "Cost", "Barcode",  'Description',"Sale Description"]
df_p.to_csv('data/product.csv', encoding = 'utf8')
