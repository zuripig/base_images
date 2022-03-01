message = 'hello yall'

def lambda_handler(event, context):
  for x in message:
    print(message)
