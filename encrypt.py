#!/usr/bin/env python3

import os
import fs
import gnupg
from pathlib import Path


config={    "gpghome": "/home/massmux/.gnupg",
            "outdir": "encrypted/",
            "gpgrecipient":"go@massmux.com",
            "toencrypt":"./startfiles/"
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

files_dir=ls_files(config['toencrypt'])

for x in files_dir:
    with open(x, "rb") as f:
        os.makedirs( Path(config['outdir']+files_dir[files_dir.index(x)]).parent, exist_ok=True)
        status = gpg.encrypt_file(f,recipients=[config['gpgrecipient']],output= config['outdir']+files_dir[files_dir.index(x)]+".gpg")
        print("file: ", f.name)
        print("ok: ", status.ok)
        print("status: ", status.status)
        print("stderr: ", status.stderr)

