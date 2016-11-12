import pandas as pd
import numpy as np
import re

df = pd.read_excel('../data/vendor list.xlsx', sheetname='Sheet1').reset_index().drop('index',axis = 1)
df2 = pd.read_csv('../data/customers_temp.csv')
ID = ['PA_0000' + str(i) for i in range(df.shape[0])]
Name = list(df.Vendor.values)
Job_Position = [None for i in range(df.shape[0])]
Is_Company = [True for i in range(df.shape[0])]
Email = [None for i in range(df.shape[0])]
reg = re.compile("[-+]?\d+[\.]?\d*[eE]?[-+]?\d*")
Phone = ['-'.join([i.lstrip('-') for i in reg.findall(j)]) if not pd.isnull(j) else j for j in df['Main Phone']]
Mobile = [None for i in range(df.shape[0])]
Street = list(df['Bill from 1'])
Street2 = list(df['Bill from 2'])
Zip = [i[-5:] for i in df['Bill from 3']]
City = [' '.join(i.split(' ')[:-2]).replace(',', '') for i in df['Bill from 3']]
State = [i.split(' ')[-2] for i in df['Bill from 3']]
Country = ['United States' for i in range(df.shape[0])]
Website = [np.nan for i in range(df.shape[0])]
address_type =['Invoice address' for i in range(df.shape[0])]
related_company_id = [None for i in range(df.shape[0])]
df_v = pd.DataFrame(np.array([ID, Name, address_type, Job_Position, Is_Company, related_company_id,Email,Phone,Mobile,Street,Street2,Zip,City, State,Country]).T)
df_v.columns = df2.columns.values[:-7]
sub_ID = ['VA_0000' + str(df.shape[0]+i) for i in range(df.shape[0])]
sub_Name = [re.sub('[^A-Za-z ]+', '', j).lstrip() if not pd.isnull(j) else j for j in df['Main Phone']]
sub_address_type = ['Shipping address' for i in range(df.shape[0])]
sub_Is_Company = [False for i in range(df.shape[0])]
sub_related_company_id = list(df_v.ID)
sub_Email = [None for i in range(df.shape[0])]
sub_Street = list(df['Ship from 1'])
sub_Street2 = list(df['Ship from 2'])
sub_Zip = [i[-5:] for i in df['Ship from 3']]
sub_City = [' '.join(i.split(' ')[:-2]).replace(',', '') for i in df['Ship from 3']]
sub_State = [i.split(' ')[-2] for i in df['Ship from 3']]
sub_Country = ['United States' for i in range(df.shape[0])]
df_v2 = pd.DataFrame(np.array([sub_ID, sub_Name, sub_address_type, Job_Position, sub_Is_Company, sub_related_company_id,Email,Phone,Mobile,sub_Street,sub_Street2,sub_Zip,sub_City, sub_State,sub_Country]).T)
df_v2.columns = df2.columns.values[:-7]
df_new = pd.concat([df_v,df_v2])
df_new.reset_index(inplace=True)
df_new.to_csv('../data/test.csv')
