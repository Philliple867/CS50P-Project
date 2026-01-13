import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Regex to find YouTube embed URLs in iframe tags
    # It accounts for http, https, with or without www, and youtube.com/embed/
    if match := re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([\w-]+)"', s):
        # Extract the video ID (group 1) and return the shortened link
        return f"https://youtu.be/{match.group(1)}"
    else:
        return None

if __name__ == "__main__":
    main()
