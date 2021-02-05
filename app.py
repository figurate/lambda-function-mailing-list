import boto3


def handler(event, context):
    print(f'Received event: {event}')

    mailing_list = event['list']
    action = event['action'] # subscribe, unsubscribe, list..
    email_address = event['email']

    if action == 'subscribe':
        subscribe(mailing_list, email_address)
    elif action == 'unsubscribe':
        unsubscribe(mailing_list, email_address)
    elif action == 'list':
        list_addresses(mailing_list)
    else:
        print(f"Unsupported action: {action}")


def subscribe(mailing_list, email_address):
    ddb = boto3.client('dynamodb')


def unsubscribe(mailing_list, email_address):
    ddb = boto3.client('dynamodb')


def list_addresses(mailing_list):
    ddb = boto3.client('dynamodb')
