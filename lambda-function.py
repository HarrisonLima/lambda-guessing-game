import json
import random


def lambda_handler(event, context):
    secret_number = random.randint(1, 10)
    user_number = event['user_number']

    result = game_result(user_number, secret_number)

    return {'secret_number': secret_number, 'user_number': user_number, 'result': result}


def game_result(user_number, secret_number):
    if user_number == secret_number:
        return 'Parábens, você descobriu o número secreto.'
    else:
        return 'Número incorreto!'