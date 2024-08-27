import socket
import sys
import random
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


banner_ascii = """\t                           |`-:_
\t  ,----....____            |    `+.
\t (             ````----....|___   |
\t  \     _                      ````----....____
\t   \    _)                                     ```---.._
\t    \                                                   \\
\t  )`.\  )`.   )`.   )`.   )`.   )`.   )`.   )`.   )`.   )`.   )`.
\t-'   `-'   `-'   `-'   `-'   `-'   `-'   `-'   `-'   `-'   `-'   `
"""


GREEN = "\x1b[1;32m"
RED = "\x1b[1;31m"
YELLOW = "\x1b[1;33m"
BLUE = "\x1b[1;34m"
MAGENTA = "\x1b[1;35m"
CYAN = "\x1b[1;36m"
RESET = "\x1b[0m"


OK = "\x1b[1;32m[\x1b[0m+\x1b[1;32m] "
ERROR = "\x1b[1;31m[\x1b[0m!\x1b[1;31m] "
WARNING = "\x1b[1;33m[\x1b[0m-\x1b[1;33m] "
INFO = "\x1b[1;34m[\x1b[0mI\x1b[1;34m] "


def checkArgs():
    if len(sys.argv) != 4:
        print("\n" + ERROR + "Usage: python3 subfinder.py domain wordlist threads\n\nif you want max threads, set 0 to threads arg")
        sys.exit()


def clean():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def banner():
    colors = [GREEN, RED, YELLOW, BLUE, MAGENTA, CYAN]
    print(random.choice(colors) + banner_ascii + RESET)


def check():
    if "://" in sys.argv[1]:
        print("\n" + ERROR + "The domain doesn't need the protocol (https://)")
        sys.exit()
    
    if "." not in sys.argv[1]:
        print("\n" + ERROR + "Invalid domain")
        sys.exit()
    
    if not os.path.isfile(sys.argv[2]):
        print("\n" + ERROR + "Can't find wordlist " + sys.argv[2])
        sys.exit()


def init():
    clean()
    banner()
    checkArgs()
    check()


def find(word, domain):
    s = (word.strip() + "." + domain).replace("\n", "")

    try:
        sub = socket.gethostbyname(s)

        if sub != "127.0.0.1":
            print(OK + s)
        
    except socket.gaierror:
        pass


def findSubs():
    domain = sys.argv[1]
    max_threads = int(sys.argv[3])

    start = time.time()

    with open(sys.argv[2], "rt") as wordlist, ThreadPoolExecutor(max_workers=max_threads or None) as executor:
        for word in wordlist:
            executor.submit(find, word.strip(), domain)

    print("\n\n" + INFO + "search time: " + str(int(time.time() - start)) + " sec")


if __name__ == "__main__":
    init()
    findSubs()
