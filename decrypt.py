#!/usr/bin/env python3

import os
import fs
import gnupg
from pathlib import Path


config={    "gpghome": "/home/massmux/.gnupg",
            "outdir": "decrypted/",
            "gpgrecipient":"go@massmux.com",
            "todecrypt":"./encrypted/"
            }

gpg = gnupg.GPG(gnupghome=config['gpghome'])

os.makedirs( config['outdir'], exist_ok=True)

def ls_files(dir):
    files = list()
    for item in os.listdir(dir):
        abspath = os.path.join(dir, item)
        try:
            if os.path.isdir(abspath):
                files = files + ls_files(abspath)
            else:
                files.append(abspath)
        except FileNotFoundError as err:
            print('invalid directory\n', 'Error: ', err)
    return files

files_dir=ls_files(config['todecrypt'])

for x in files_dir:
    with open(x, "rb") as f:
        os.makedirs( Path(config['outdir']+files_dir[files_dir.index(x)]).parent, exist_ok=True)
        status = gpg.decrypt_file(f, passphrase="123456",output=config['outdir']+files_dir[files_dir.index(x)]+".dec" )
        print("file: ", f.name)
        print("ok: ", status.ok)
        print("status: ", status.status)
        print("stderr: ", status.stderr)

