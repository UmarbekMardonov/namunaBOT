import requests

from data.config import BOT_TOKEN, ADMINS


def countUsers():
    # Replace <bot_token> and <chat_id> with your actual bot token and chat ID
    bot_token = BOT_TOKEN
    chat_id = ADMINS

    # Send a request to the Telegram Bot API to get the number of users in the chat
    response = requests.get(f'https://api.telegram.org/bot{bot_token}/getChatMembersCount?chat_id={chat_id}')

    # Get the number of users from the response
    num_users = response.json()['result']

    # Print the number of users
    return f'There are {num_users} users in the chat.'
