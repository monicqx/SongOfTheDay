import json
import requests


def get_token():
    # File has to be in same folder as main.py.
    with open("token.txt", "r") as f:
        for line in f:
            return line.strip()


BASE_URL = "https://api.telegram.org/bot{}/".format(get_token())


def get_content(url):
    response = requests.get(url, timeout=0.1)
    return response.content.decode("utf8")


def get_json_from_url(url):
    json_object = json.loads(get_content(url))
    return json_object


def compute_updates_url():
    return BASE_URL + "getUpdates"


def get_updates():
    updates_url = compute_updates_url()
    print("Getting updates from: " + updates_url)
    json_object = get_json_from_url(updates_url)
    return json_object


def main():
    print(get_updates())


if __name__ == "__main__":
    main()
