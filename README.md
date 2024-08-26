# SUBFINDER

![Version](https://img.shields.io/badge/version-1.0.0-green.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen.svg)

Subfinder is a cybersecurity software that is used to enumerate the subdomains of a domain


## requirements

- Python 3.8+


## setup

update your distro

- **Windows**: `winget update --all`

- **Debian**: `sudo apt update -y && sudo apt upgrade -y`

- **Arch**: `sudo pacman -Syu`

- **Red Hat**: `sudo yum update -y && sudo yum upgrade -y`

---

install python3

- **Windows**: `winget install python3`

- **Debian**: `sudo apt install python3`

- **Arch**: `sudo pacman -S python3`

- **Red Hat**: `sudo yum install python3`

---

clone the repo

```bash
git clone https://github.com/0lunar/subfinder.git
```

---

enter the directory

```bash
cd subfinder
```


## usage

```bash
python3 subfinder.py domain worlist threads
```