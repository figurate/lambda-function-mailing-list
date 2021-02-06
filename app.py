import boto3


def handler(event, context):
    print(f'Received event: {event}')

    subscriber_list = event['list']
    action = event['action'] # subscribe, unsubscribe, list..
    subscriber_id = event['subscriber']

    if action == 'subscribe':
        subscribe(subscriber_list, subscriber_id)
    elif action == 'unsubscribe':
        unsubscribe(subscriber_list, subscriber_id)
    elif action == 'list':
        list_addresses(subscriber_list)
    else:
        print(f"Unsupported action: {action}")


def subscribe(subscriber_list, subscriber_id):
    ddb = boto3.client('dynamodb')


def unsubscribe(subscriber_list, subscriber_id):
    ddb = boto3.client('dynamodb')


def suspend(subscriber_list, subscriber_id):
    ddb = boto3.client('dynamodb')


def activate(subscriber_list, subscriber_id):
    ddb = boto3.client('dynamodb')


def list_addresses(subscriber_list):
    ddb = boto3.client('dynamodb')
