import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r'^<iframe.+src="https?://(?:www\.)?youtube\.com/embed/(.+?)".+</iframe>', s):
        link = f"https://youtu.be/{match.group(1)}"
        return link
    else:
        return None



if __name__ == "__main__":
    main()