import socket
import sys
import random
import os
import time
from threading import Thread


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


threads = 0
max_threads = 0


def checkArgs():
    if len(sys.argv) != 4:
        print("\n" + ERROR + "Usage: python3 subfinder.py domain worlist threads")
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
        print("\n" + ERROR + "The domain don't need the protocol (https://)")
        sys.exit()
    
    if "." not in sys.argv[1]:
        print("\n" + ERROR + "Invalid domain")
        sys.exit()
    
    if os.path.isfile(sys.argv[2]) == False:
        print("\n" + ERROR + "Can't find wordlist " + sys.argv[2])
        sys.exit()


def init():
    global max_threads

    clean()
    banner()
    checkArgs()
    check()

    max_threads = int(sys.argv[3])


def findSubs():
    global threads, max_threads

    domain = sys.argv[1]
    wordlist = open(sys.argv[2], "rt")

    word = wordlist.readline()

    start = time.time()

    while word != "":

        while threads == max_threads:
            pass

        Thread(target=find, args=(word, domain,)).start()

        threads += 1

        word = wordlist.readline()
    
    while threads != 0:
        pass

    print("\n\n" + INFO + "search time: " + str(int(time.time() - start)) + " sec")


def find(word, domain):
    global threads

    s = (word + domain).replace("\n", "")

    try:
        sub = socket.gethostbyname(s)

        if sub != "127.0.0.1":
            print(OK + (word + "." + domain).replace("\n", ""))
        
    except:
        pass
    
    threads -= 1


if __name__ == "__main__":
    init()
    findSubs()
