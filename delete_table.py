import boto3

client = boto3.client('dynamodb', region_name='us-west-2', endpoint_url='http://localhost:8000')

try:
    resp = client.delete_table(
        TableName="Books",
    )
    print("Table deleted successfully!")
except Exception as e:
    print("Error deleting table:")
    print(e)
