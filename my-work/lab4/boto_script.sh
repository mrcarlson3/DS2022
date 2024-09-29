#!/Users/michaelcarlson/anaconda3/bin/python

import boto3

s3 = boto3.client('s3', region_name='us-east-1')

bucket = 'ds2022-mjy7nw'
local_file = 'lab4/perry.png'

resp = s3.put_object(
    Body = local_file,
    Bucket = bucket,
    Key = local_file,
    ACL = 'public-read'
)
