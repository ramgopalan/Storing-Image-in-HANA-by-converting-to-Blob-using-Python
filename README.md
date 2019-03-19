# Storing-Image-in-HANA-by-converting-to-Blob-using-Python
Store the images in HANA (by converting it to BLOB file) through Python

Thanks for using this python script!

Before Executing the imagetoblob.py Program:

Ensure
    *** You have python installed along with the pyhdb library in your system
	*** You have all the images that needs to be converted in the same directory as the imagetoblob.py 
	*** Also you have placed the systemdetails.txt in the same directory as the imagetoblob.py
	*** Fill in the details of the host, port, username, password, schemaname and tablename in the systemdetails.txt
	*** You already have the table created in your destination HANA System if not you can create it with this SQL
	  CREATE COLUMN TABLE <SCHEMA_NAME>.<TABLE_NAME> (IMAGE_NAME NVARCHAR(200) PRIMARY KEY,IMAGE_CONTENT BLOB ST_MEMORY_LOB);

If any issues do comment/get back to me(ram.gopalan@live.com)