# s3_upload_download with subfolders

Utilities for s3 download and upload file.

## Function for s3 download to the local path including s3 sub folder path

from  s3_upload_download import s3_transfers_utlits

s3_transfers_utlits.download_s3_file(bucket_name, s3_folder,file_extension, destination_path)

### Parameters:

        bucket_name: The name of the s3 bucket 
        s3_folder: The folder path in the s3 bucket including subfolders 
        file_extension: extension of file such as .parquet or .csv 
        destination_path: a relative or absolute directory path in the local file system 

Example Usage
.. code-block:: python

        from  s3_upload_download import s3_transfers_file

        bucket_name='test_bucket'
        s3_folder='test_folder'
        file_extension='.parquet'
        destination_path=f'home/momataj/test_folder/'
        s3_transfers_file.download_s3_file(bucket_name, s3_folder, file_extension, destination_path)





## Function for s3 upload from the local path including s3 sub folder path and file extension

from  s3_upload_download import s3_transfers_utlits

s3_transfers_utlits.upload_s3_file(bucket_name,source_path,base_dir,file_extension)

### Parameters:
        bucket_name: the name of the s3 bucket 
        source_path: local dirctory where file is located such as /home/{username}/{foldername} 
        base_dir: a relative or absolute directory path in the local file system such as /home/{username}/ 
        file_extension: extension of file such as .parquet or .csv 

Example Usage
.. code-block:: python
        from  s3_upload_download import s3_transfers_file

        bucket_name='test_bucket'
        s3_folder='test_folder'
        file_extension='.parquet'
        base_dir='home/momataj/'
        sourceDir=f'home/momataj/test_folder/'
        s3_transfers_file.upload_s3_file(bucket_name,sourceDir,base_dir,file_extension)
