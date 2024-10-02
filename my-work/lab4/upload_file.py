#!/Users/michaelcarlson/anaconda3/bin/python

import boto3
import urllib.request

s3 = boto3.client('s3', region_name="us-east-1")

bucket = 'ds2022-mjy7nw'

url = 'https://helloartsy.com/wp-content/uploads/kids/halloween/how-to-draw-a-halloween-pumpkin/how-to-draw-a-halloween-pumpkin-step-6-1024x1024.jpg'
local_file = 'pumpkin.jpg'

urllib.request.urlretrieve(url, local_file)

s3.put_object(
    Body = local_file,
    Bucket = bucket,
    ACL = 'public-read',
    ContentType='image/jpg',
    Key = local_file  
)

# vars needed
bucket_name = 'ds2022-mjy7nw'
object_name = 'pumpkin.jpg'
expires_in = 604800

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
    )

print(response)

# https://ds2022-mjy7nw.s3.amazonaws.com/pumpkin.jpg?AWSAccessKeyId=AKIA6IY36ALUF7HDEIRC&Signature=nzVXyswU1nE4qGN75%2B0JHg2lUx0%3D&Expires=1728504043
