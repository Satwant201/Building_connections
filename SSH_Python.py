################ Serial connection in Python 

import paramiko

ssh_client =paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname="<server location>",username="<id>",password="<passwordhere>")

handle = ssh_client.open_sftp()

######### Reading file from HDFS location into python session

file_path =handle.file("<remote server location to be read>")

data_read= pd.read_csv(file_path)

data_read.to_csv("testinfile.csv")

#### Writing back file from domino location to HDFS location 

handle.put("testinfile.csv","<remote server location where we want to write back")
