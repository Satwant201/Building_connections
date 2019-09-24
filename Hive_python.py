
################# Hive connection in Python using pyhive package 

import pandas as pd
from pyhive import hive
import time

statement = '''SELECT * from dbo.tablename limit 10'''


#print( "Setting up connection")
conn = hive.connect(host='<server name>',port=<port number>,auth='LDAP',username='<id>',password="<password?>")
#print "Connection successful"



#print( "fetching stars data")

start1=time.time()
start=time.ctime()
#print( "started at:"),start
cur = conn.cursor()
cur.execute('set mapreduce.job.queuename=araadh_q1.arapi_sq1')
cur.execute(statement)
df = cur.fetchall()
cur.execute("show columns in dbo.tablename")
df1 = cur.fetchall()
col_names=[w[0] for w in df1]
#print( "Data fetch completed at:"),time.ctime()
#print(  "Time taken: "),time.time()-start1


#### output saved as a pandas df 

df_final=pd.DataFrame(df,columns=col_names)

