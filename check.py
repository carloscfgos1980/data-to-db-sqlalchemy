import pandas as pd
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, BOOLEAN


engine = create_engine("sqlite:///amet.db", echo=True)

df = pd.read_excel('Amet_data.xlsx')
print(df)


dfs = pd.read_excel('Amet_data.xlsx', sheet_name=None)
for table, df in dfs.items():
    df.to_sql(table, con=engine, if_exists='append', index=False)
    print(f'{df} inserted successfully')


wb = pd.ExcelFile('Amet_data.xlsx')
for sheet in wb.sheet_names:
    df = pd.read_excel('Amet_data.xlsx', sheet_name=sheet)
    df.to_sql(sheet, con=engine, index=False, if_exists="append")
