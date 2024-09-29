#!/Users/michaelcarlson/anaconda3/bin/python

import boto3

s3 = boto3.client('s3', region_name="us-east-1")

bucket = 'ds2022-mjy7nw'

import urllib.request

url = 'https://i.redd.it/t09mg0nuf84c1.jpeg'
local_file = 'pug.jpeg'
urllib.request.urlretrieve(url, local_file)
resp = s3.put_object(
    Body = local_file,
    Bucket = bucket,
    ACL = 'public-read',
    Key = local_file
)

# vars needed
bucket_name = 'ds2022-mjy7nw'
object_name = 'pug.jpeg'
expires_in = 604800

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
    )
print(response)
