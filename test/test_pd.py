import pandas as pd
# from mysql import connector
# from sqlalchemy import create_engine


# db_connection = create_engine("mysql+mysqldb://admin:admin@localhost/adv_works")
# print("successfulllll.....")

df = pd.read_parquet("TABLE_X_PART_CLASS_VALUES.parquet", engine='fastparquet')
df.to_csv('TABLE_X_PART_CLASS_VALUES.csv')
# print(type(df))
# df1 = pd.DataFrame(data=df)
# print(type(df1))
# df.info()

print(df.columns)

# df1.to_sql(con=db_connection, name='testdata', if_exists='append')
# df.to_sql(con=db_connection, name='testdata2', if_exists="fail")
# print("Done....")

# query = "select * from testdata2"
# query = "select count(*) from testdata2"
# data = pd.read_sql(query, db_connection)
# print(data)
# print(data)

# db_connection = connector.connect(user='admin', password='admin', database='adv_works', host='localhost', port=3306)
# query = 'select * from customer'
# cursor = db_connection.cursor()
# cursor.execute(query)
# for data in cursor:
#     print(data)

# df1.to_sql(con=db_connection, name='pandas_data',if_exists='append', index=False)
# print("Successfully appended..........")