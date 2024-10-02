#!/Users/michaelcarlson/anaconda3/bin/python

import boto3
import urllib.request

s3 = boto3.client('s3', region_name="us-east-1")

bucket = 'ds2022-mjy7nw'

url = 'https://media.tenor.com/Ucg45NFV8XkAAAAM/ducks-funny-ducks.gif'
local_file = 'duck.gif'

urllib.request.urlretrieve(url, local_file)

resp = s3.put_object(
    Body = local_file,
    Bucket = bucket,
    ACL = 'public-read',
    Key = local_file
)

# vars needed
bucket_name = 'ds2022-mjy7nw'
object_name = 'duck.gif'
expires_in = 604800

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
    )

print(response)
