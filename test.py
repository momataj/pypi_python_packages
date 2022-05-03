from s3_last_modified_objects import s3_objects

from datetime import datetime,timedelta
import boto3

bucket='bucket_test'
path='products'
last_modified_date =(datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')  
s3client = boto3.client('s3')
object_dict= s3_objects.latest_files(
                s3client=s3client,
                bucket=bucket,
                prefix=path,
                last_modified_date='2019-01-01')
for obj in object_dict:
   print(obj)