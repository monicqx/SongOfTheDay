import json
import requests
import time


def get_token():
    # File has to be in same folder as main.py.
    with open("token.txt", "r") as f:
        for line in f:
            return line.strip()


def get_content(url):
    response = requests.get(url, timeout=5)
    return response.content.decode("utf8")


def get_json_from_url(url):
    json_object = json.loads(get_content(url))
    return json_object


def get_max_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


class Bot:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://api.telegram.org/bot{}/".format(self.token)
        self.updates_url = self.base_url + "getUpdates?timeout=4"
        self.send_message_url_format = self.base_url + "sendMessage?text={}&chat_id={}"

    def get_updates(self, offset=None):
        url = self.updates_url
        if offset:
            url += "&offset={}".format(offset)
        return get_json_from_url(url)

    def get_last_update_info(self, updates):
        updates_num = len(updates["result"])
        last_update = updates_num - 1
        chat_id = updates["result"][last_update]["message"]["chat"]["id"]
        message_id = updates["result"][last_update]["message"]["message_id"]
        message_text = updates["result"][last_update]["message"]["text"]
        return chat_id, message_id, message_text

    def send_message(self, text, chat_id):
        print("Sending message " + text + " to chat_id:" + str(chat_id))
        url = self.send_message_url_format.format(text, chat_id)
        get_content(url)

    def echo_all(self, updates):
        for update in updates["result"]:
            try:
                text = update["message"]["text"]
                chat = update["message"]["chat"]["id"]
                self.send_message(text, chat)
            except Exception as e:
                print(e)


def main():
    bot = Bot(get_token())

    last_update_id = 713828276
    while True:
        updates = bot.get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_max_id(updates) + 1
            bot.echo_all(updates)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
