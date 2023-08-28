
import pyodbc
import pandas as pd
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = r'usqespw6h5i.sd01.unicreditgroup.eu,8066' 
database = r'QES_ELSA2DB_P01' 
username = r'HD00\P852706' # It only took Puser / Windows authentication 
password = r'!Shuru@5012' # Password not required  / Windows authentication 
conn =  ';Trusted_Connection=yes'
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password+ conn)
cursor = cnxn.cursor()
# select 26 rows from SQL table to insert in dataframe.
query = "SELECT TOP (10) [PkRequestId],[FkPayloadTemplateId],[CreationDate] FROM [QES_ELSA2DB_P01].[Instance].[Request] order by creationdate desc;"
df = pd.read_sql(query, cnxn)


print(df.head(26))