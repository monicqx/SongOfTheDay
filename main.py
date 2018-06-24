import json
import requests


def get_token():
    # File has to be in same folder as main.py.
    with open("token.txt", "r") as f:
        for line in f:
            return line.strip()


def get_content(url):
    response = requests.get(url, timeout=0.1)
    return response.content.decode("utf8")


def get_json_from_url(url):
    json_object = json.loads(get_content(url))
    return json_object


class Bot:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://api.telegram.org/bot{}/".format(self.token)
        self.updates_url = self.base_url + "getUpdates"

    def get_updates(self):
        print("Getting updates from: " + self.updates_url)
        json_object = get_json_from_url(self.updates_url)
        return json_object


def main():
    bot = Bot(get_token())
    updates = bot.get_updates()
    print(updates)


if __name__ == "__main__":
    main()
