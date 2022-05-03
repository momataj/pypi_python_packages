import s3_last_modified_objects

from datetime import datetime,timedelta
import boto3

bucket='contact-dataplatform-test-trusted'
path='contract_products'
last_modified_date =(datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')  
s3client = boto3.client('s3')
object_dict= s3_last_modified_objects.latest_objects(
                s3client=s3client,
                bucket=bucket,
                prefix=path,
                last_modified_date='2019-01-01')
for obj in object_dict:
   print(obj)