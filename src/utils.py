def upload_files_to_s3(s3_client, s3_bucket, files_or_urls):
    """ Uploads a local image or url to an s3 bucket 
    
    Inputs:
        s3_client (boto.client.S3)
        s3_bucket (str)
        files_or_urls ([str]):                   Either a path to a local file or url prepended with http
    Outputs:
        file_names ([str]):                     Name of the uploaded file
    """
    if not s3_bucket_exists(s3_client, s3_bucket):
        s3_client.create_bucket(Bucket=s3_bucket)

    if type(files_or_urls) is not list:
        files_or_urls = [files_or_urls]

    file_names = []
    for file_or_url in files_or_urls:
        file_path = file_or_url
        file_name = file_or_url.split("/")[-1]
        
        if not s3_file_exists(s3_client, s3_bucket, file_name):
            s3_client.upload_file(file_path, s3_bucket, file_name)
        file_names.append(file_name)
    return file_names


def get_s3_file_names(s3_client, s3_bucket: str):
    """ Returns file names from s3 bucket 

    Inputs:
        s3_client (boto.client.S3)
        s3_bucket (str)
    Outputs:
        file_names (list):           List of file names from the bucket
    """
    s3_objects = s3_client.list_objects(Bucket=s3_bucket)
    s3_contents = s3_objects["Contents"]
    s3_files = [content["Key"] for content in s3_contents]
    return s3_files
    
def delete_from_s3(s3_client, s3_bucket, file_names):
    """ Deletes a file from an s3 bucket """
    if type(file_names) is not list:
        file_names = [file_names]
    
    for file_name in file_names:
        s3_client.delete_object(Bucket=s3_bucket, Key=file_name)
    return file_names

def s3_bucket_exists(s3_client, s3_bucket) -> bool:
    """ Returns whether a bucket exists 

    Inputs:
        s3_client (boto.client.S3)
        s3_bucket (str)
    Outputs:
        file_exists (bool)
    """
    return s3_bucket in [b.get("Key") for b in s3_client.list_buckets().get("Buckets")]

def s3_file_exists(s3_client, s3_bucket, file_name) -> bool:
    """ Returns whether a file exists in a bucket 
    Inputs:
        s3_client (boto.client.S3)
        s3_bucket (str)
        file_name (str)
    Outputs:
        file_exists (bool)
    """
    try:
        s3_client.get_object(Bucket=s3_bucket, Key=file_name)
        return True
    except:
        return False