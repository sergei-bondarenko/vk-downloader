#!/usr/bin/python3
# Project page: https://github.com/grez911/vk-downloader

import sys
import re
from urllib.request import urlopen, urlretrieve

def main():
    if len(sys.argv) != 2:
        print("Please, pass video url as an argument. "\
              "Example: https://vk.com/video-12345678_987654321")
        sys.exit(1)

    f = urlopen(sys.argv[1])
    source = f.read().decode("windows-1251")
    reg = re.compile('<source src=\\\\"([^"]*)\\\\"')
    urls = reg.findall(source)

    for i in ['1080.mp4', '720.mp4', '360.mp4', '240.mp4']:
        for url in urls:
            if i in url:
                source = url.replace('\\/', '/')
                reg = re.compile('/([^/]*\.mp4)')
                name = reg.findall(source)[0]
                print("Downloading...")
                urlretrieve(source, name)
                print("Saved as " + name)
                sys.exit(0)

    print("Can't find video.")
    sys.exit(2)

if __name__ == '__main__':
    main()
