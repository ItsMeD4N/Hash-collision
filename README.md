# MD5 Hash Cracker

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

A simple Python script to find the pre-image of an MD5 hash using a dictionary attack. The program compares a given hash against the MD5 hash of every word in a specified wordlist.

This project was created for educational purposes to demonstrate how a dictionary attack against hashes works.

## ✨ Features

* **Simple**: Easy-to-use command-line interface.
* **Fast**: Written in standard Python for efficient performance.
* **Customizable**: Use any wordlist file of your choice.

## ⚙️ Requirements

* [Python 3.x](https://www.python.org/downloads/)

No external libraries are required as this script only uses standard Python modules (`hashlib` and `os`).

## 🚀 How to Use

1.  **Clone this repository:**
    ```bash
    git clone [https://github.com/ItsMeD4N/Hash-collision.git](https://github.com/ItsMeD4N/Hash-collision.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd Hash-collision
    ```

3.  **Run the script:**
    ```bash
    python main.py
    ```

4.  **Enter the requested inputs:**
    * The program will prompt you to enter the **MD5 hash** you want to crack.
    * Next, enter the **path to your wordlist file** (e.g., `wordlist.txt`).

## 📋 Example Session

For example, let's find the original text for the MD5 hash `21232f297a57a5a743894a0e4a801fc3`, where the word `admin` exists in `wordlist.txt`.

```
$ python main.py

============================================
|         [+] MD5 HASH CRACKER [+]         |
|           Author: ItsMeD4N               |
============================================

=> ENTER MD5 HASH: 21232f297a57a5a743894a0e4a801fc3
=> ENTER WORDLIST: wordlist.txt

[+] CALCULATING HASHES...

[+] HASH FOUND: admin
```

If the hash is not found in the wordlist, the program will display this message:
```
[-] HASH NOT FOUND
```

## 📂 Project Structure

```
Hash-collision/
├── main.py        # The main script to run the program
└── wordlist.txt   # An example wordlist file
```

## ⚠️ Disclaimer

This tool is intended for **educational purposes only**. The author is not responsible for any misuse of the information or the tool provided in this repository. Use it wisely and at your own risk.

---
## Contributing

Feel like something could be improved? Feel free to create a Pull Request or open an Issue. Contributions are welcome!
