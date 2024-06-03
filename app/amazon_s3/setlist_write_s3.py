import boto3
import json

from app.setlist.filter import spotify_setlist

# Convert the dictionary to JSON string
json_string = json.dumps(spotify_setlist)

# Initialize Boto3 S3 client
s3 = boto3.client("s3")

# Upload the JSON string to S3
bucket_name = "setlist7909"
object_key = "spotifysetlist.json"

s3.put_object(Bucket=bucket_name, Key=object_key, Body=json_string)
