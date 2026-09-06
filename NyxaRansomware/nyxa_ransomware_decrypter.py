import os
from cryptography.fernet import Fernet 

files = []

for file in os.listdir():
    if file.endswith(".py") or file == "ransom.key":
        continue

    if os.path.isdir(file):
        continue

    files.append(file)


with open("ransom.key", "rb") as ransom_key:
    secure_key = ransom_key.read()

for file in files:
    with open(file, "rb") as ransom_file_read:
        contents = ransom_file_read.read()

    contents_decrypted = Fernet(secure_key).decrypt(contents)

    with open(file, "wb") as ransom_file_write:
        ransom_file_write.write(contents_decrypted)
