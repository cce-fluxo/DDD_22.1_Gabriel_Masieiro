import boto3
#from botocore.exceptions import ClientError
from app import config

class Storage:
    project_name = config.AWS_PROJECT_NAME
    bucket_name = config.AWS_BUCKET_NAME
    session = boto3.session.Session()

    client = session.client ('s3',
                            region_name = config.AWS_REGION,
                            endpoint_url = config.AWS_BUCKET_ENDPOINT,
                            aws_access_key_id=config.AWS_ACCESS_KEY,
                            aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY)

    def put_url(self, file_key):
        return self.client.generate_presigned_url(ClientMethod='put_object',
                                                Params={'Bucket': self.bucket_name,
                                                        'Key': f'{self.project_name}/{file_key}'},
                                                ExpiresIn=300) 
        
    def get_url(self, file_key):
        return self.client.generate_presigned_url(ClientMethod='get_object',
                                                Params={'Bucket':   self.bucket_name,
                                                        'Key': f'{self.project_name}/{file_key}'},
                                                ExpiresIn=300)
                                        
    def delete_object(self, file_key):
        return self.client.delete_object(Bucket= self.bucket_name,
                                  Key=f'{self.project_name}/{file_key}')

storage = Storage()