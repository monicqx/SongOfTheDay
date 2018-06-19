TOKEN = ""


def main():
    # File has to be in same folder as main.py.
    with open("token.txt", "r") as f:
        for line in f:
            TOKEN = line
            break  # There should only be one line in this file anyway.
    print(TOKEN)


if __name__ == "__main__":
    main()
