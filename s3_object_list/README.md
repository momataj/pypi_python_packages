# s3_last_modified_objects with bucket, path and last_modified_date

Utilities for latest files from s3 bucket

### Parameters:
        Args:
                s3client:
                boto3 S3 client
                bucket:
                Name of the S3 bucket.
                prefix:
                Only fetch objects whose key starts with this prefix (optional).
                suffix:
                Only fetch objects whose keys end with this suffix (optional).
                last_modified_date: Only yield objects with LastModified dates greater or equal to this value (optional).

        Returns:
                Dictionary objects for each qualifying S3 object through a generator. The dict includes:
                key
                        the object key (name)
                size
                        the size of the object in bytes (integer)
                last_modified
                        the datetime object of which has modified based on parameter last_modified_date or by defualt 1 day before current date

Example Usage
.. code-block:: python

        import s3-last-modified-objects
        from datetime import datetime,timedelta
        import boto3

        bucket='bucket_customer'
        path='products'
        last_modified_date =(datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')  
        s3client = boto3.client('s3')
        object_dict= s3-last-modified-objects.latest_objects(
                s3client=s3client,
                bucket=bucket,
                prefix=path,
                last_modified_date=last_modified_date)
        for obj in object_dict:
            print(obj)
