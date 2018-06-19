
def get_token():
    # File has to be in same folder as main.py.
    with open("token.txt", "r") as f:
        for line in f:
            token = line
            break  # There should only be one line in this file anyway.
    return token


def main():
    token = get_token()
    print(token)


if __name__ == "__main__":
    main()
