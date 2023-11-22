import os
import pandas as pd
import openpyxl

data_file_folder= 'D:\Final'

df=[]
for file in os.listdir(data_file_folder):
    if file.endswith('.xlsx'):
        df.append(pd.read_excel(os.path.join(data_file_folder,file),sheet_name='in'))

print(len(df))
df_master = pd.concat(df,axis=0)
df_master.to_excel('merged.xlsx',index=False)