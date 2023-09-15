import boto3
import json

region = 'sa-east-1'
instances = [] # ['i-0618c3e7ce9046da7', 'i-0d4769e2567c867bc']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    return {
        "status": "OK",
        "message": "Instances will shutdown in some minutes."
    }
