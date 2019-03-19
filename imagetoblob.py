import pyhdb
import os

imagefilenames = []
blobimage = []

# Checking for the files in Current Directory
for root, dirs, files in os.walk("."):  
    for filename in files:
        if filename.endswith(".png") or filename.endswith(".jpg"):
            imagefilenames.append(filename)

for filenames in imagefilenames:
    with open(filenames,'rb') as file:
        binaryData = file.read()
        blobimage.append(binaryData)


with open("systemdetails.txt") as f:
    d = dict(line.strip().split('=') for line in f)

# This default connection connects to HANA Sandbox System, if needed change the host and port 
# to connect in respective system(s)
connection = pyhdb.connect(
    host=d['host'],
    port=d['port'],
    user=d['username'],
    password=d['password']
)

# Preparing various SQL Statements for inserting into table
selectsqlstatement = 'select * from "'+d['schemaname']+'"."'+d['tablename']+'"'
deletesqlstatement = 'delete from "'+d['schemaname']+'"."'+d['tablename']+'"'
insertsqlstatement = 'insert into "'+d['schemaname']+'"."'+d['tablename']+'" values(:1,:2)'

cursor = connection.cursor()
c = cursor.execute(selectsqlstatement)
d = cursor.fetchone()

# We are checking if value already exist in table, then we delete it
if d is not None:
    c = cursor.execute(deletesqlstatement)
    connection.commit()

# We insert all the images related with png extension into this table
for i,imagenames in enumerate(imagefilenames):
    c = cursor.execute(insertsqlstatement,[imagenames,blobimage[i]])
connection.commit() 
print("Successfully inserted into the table")
