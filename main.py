from argparse import ArgumentParser
import random
import requests


def register_new_account(useremail: str, username: str):
    pwchars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    password = ''.join(random.choices(pwchars, k=8))
    fingerprint = requests.post('https://discord.com/api/v6/auth/fingerprint').json()['fingerprint']

    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 "
                      "Safari/605.1.15",
        "referer": "https://www.google.com/"
    }

    data = {
        "captcha_key": None,
        "consent": True,
        "date_of_birth": "1992-03-03",
        "email": useremail,
        "fingerprint": fingerprint,
        "gift_code_sku_id": None,
        "invite": None,
        "password": password,
        "username": username,
    }

    response = requests.post("https://discord.com/api/v9/auth/register", headers=headers, json=data)
    return response.text


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-u', help='username', type=str, required=True, dest='username')
    parser.add_argument('-e', help='useremail', type=str, required=True, dest='useremail')

    try:
        print(
            register_new_account(**vars(parser.parse_args()))
        )
    except KeyError as e:
        print(e)


