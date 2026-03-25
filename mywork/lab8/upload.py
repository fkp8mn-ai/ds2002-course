import boto3

s3 = boto3.client('s3', region_name='us-east-1')

s3.upload_file(
    'cloud.jpg',
    'ds2002-fkp8mn',
    'cloud_public.jpg',
    ExtraArgs={'ACL': 'public-read'}
)

print("Public upload successful")
