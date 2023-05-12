import boto3

#using Amazon S3

""" s3 = boto3.resource("s3") """

#print bucket names

""" for bucket in s3.buckets.all():
    print(bucket.name) """

bucket_name='reddit-data-jb'
file_path='/Users/josephbrown/Desktop/MyApps/reddit_api_pipeline/dataengineering_posts.csv'
#creating an S3 access object
s3 = boto3.client("s3")

s3.upload_file(file_path,bucket_name,file_path.split('/')[-1])

