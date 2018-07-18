import json
import requests
import time


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
        self.send_message_url_format=self.base_url+"sendMessage?text={}&chat_id={}"

    def get_updates(self):
        print("Getting updates from: " + self.updates_url)
        json_object = get_json_from_url(self.updates_url)
        return json_object

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


def main():
    bot = Bot(get_token())

    last_update_info = (None, None, None)
    while True:
        chat_id, message_id, message_text = bot.get_last_update_info(bot.get_updates())
        if (chat_id, message_id, message_text) != last_update_info:
            bot.send_message(message_text, chat_id)
            last_update_info = (chat_id, message_id, message_text)
        time.sleep(0.5)

    # updates = bot.get_updates()
    # chat_id, text = bot.get_last_chat_id_and_text(updates)
    # print(text, chat_id)
    # bot.send_message("Mwahhh", chat_id)


if __name__ == "__main__":
    main()
