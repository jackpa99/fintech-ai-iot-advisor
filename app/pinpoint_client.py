import boto3

class PinpointClient:
    def __init__(self):
        self.client = boto3.client('pinpoint')
        self.application_id = 'your-pinpoint-application-id'

    def send_notification(self, user_id, message):
        response = self.client.send_messages(
            ApplicationId=self.application_id,
            MessageRequest={
                'Addresses': {
                    user_id: {'ChannelType': 'EMAIL'}
                },
                'MessageConfiguration': {
                    'EmailMessage': {
                        'Body': message,
                        'Subject': 'Fintech Advisor Notification'
                    }
                }
            }
        )
        return response