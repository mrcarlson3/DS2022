#!/Users/michaelcarlson/anaconda3/bin/python

import boto3
import urllib.request

s3 = boto3.client('s3', region_name="us-east-1")

bucket = 'ds2022-mjy7nw'

url = 'https://i.pinimg.com/736x/de/71/bb/de71bb8a57ff473cc58ebc6af58c4858.jpg'
local_file = 'pug.jpg'

urllib.request.urlretrieve(url, local_file)

s3.put_object(
    Body = local_file,
    Bucket = bucket,
    ACL = 'public-read',
    Key = local_file
)

# vars needed
bucket_name = 'ds2022-mjy7nw'
object_name = 'pug.jpg'
expires_in = 604800

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
    )
print(response)
