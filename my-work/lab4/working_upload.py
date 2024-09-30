#!/Users/michaelcarlson/anaconda3/bin/python

import boto3
import urllib.request

s3 = boto3.client('s3', region_name="us-east-1")

bucket = 'ds2022-mjy7nw'
object_name = 'pug.jpeg'

url = 'https://i.redd.it/t09mg0nuf84c1.jpeg'
local_file = 'pug.jpeg'
urllib.request.urlretrieve(url, local_file)

# Upload the file to S3 (open the file in binary mode)
with open(local_file, 'rb') as file_data:
    s3.put_object(
        Body=file_data,
        Bucket=bucket,
        ACL='public-read',
        Key=object_name
    )

# Variables needed for presigned URL
expires_in = 604800  

# Generate presigned URL
response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket, 'Key': object_name},
    ExpiresIn=expires_in
)

# Print the presigned URL
print(response)

