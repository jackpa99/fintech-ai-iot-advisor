import boto3
from botocore.exceptions import ClientError
from fastapi import HTTPException
from app.models import User

cognito_client = boto3.client('cognito-idp')
USER_POOL_ID = 'your-user-pool-id'
CLIENT_ID = 'your-client-id'

def auth_user_facebook(access_token: str) -> User:
    try:
        response = cognito_client.initiate_auth(
            AuthFlow='CUSTOM_AUTH',
            AuthParameters={
                'TOKEN': access_token
            },
            ClientId=CLIENT_ID
        )
        id_token = response['AuthenticationResult']['IdToken']
        user_info = get_user_info(id_token)
        return User(username=user_info['email'])
    except ClientError as e:
        raise HTTPException(status_code=401, detail="Invalid Facebook token")

def get_user_info(id_token: str) -> dict:
    try:
        response = cognito_client.get_user(
            AccessToken=id_token
        )
        user_attributes = {attr['Name']: attr['Value'] for attr in response['UserAttributes']}
        return user_attributes
    except ClientError as e:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_user(token: str) -> User:
    try:
        user_info = get_user_info(token)
        return User(username=user_info['email'])
    except:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")