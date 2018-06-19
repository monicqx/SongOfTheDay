
def get_token():
    # File has to be in same folder as main.py.
    with open("token.txt", "r") as f:
        for line in f:
            return line


def main():
    token = get_token()
    print(token)


if __name__ == "__main__":
    main()
