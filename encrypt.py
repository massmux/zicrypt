#!/usr/bin/env python3

import os
import fs
import gnupg
from pathlib import Path
from zilib import ls_files
from config import config


gpg = gnupg.GPG(gnupghome=config['gpghome'])

os.makedirs( config['encrypted'], exist_ok=True)

files_dir=ls_files(config['toencrypt'])

for x in files_dir:
    with open(x, "rb") as f:
        os.makedirs( Path(config['encrypted']+files_dir[files_dir.index(x)]).parent, exist_ok=True)
        status = gpg.encrypt_file(f,recipients=[config['gpgrecipient']],output= config['encrypted']+files_dir[files_dir.index(x)]+".gpg")
        print("file: ", f.name)
        print("ok: ", status.ok)
        print("status: ", status.status)
        print("stderr: ", status.stderr)

