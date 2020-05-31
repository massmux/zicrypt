#!/usr/bin/env python3

import os
import fs
import gnupg
from pathlib import Path
from zilib import ls_files
from config import config


# create dir
os.makedirs( config['decrypted'], exist_ok=True)

# init gpg
gpg = gnupg.GPG(gnupghome=config['gpghome'])

# decrypting procedure
files_dir=ls_files(config['todecrypt'])
for x in files_dir:
    with open(x, "rb") as f:
        os.makedirs( Path(config['decrypted']+files_dir[files_dir.index(x)]).parent, exist_ok=True)
        oFileName=os.path.splitext(config['decrypted']+files_dir[files_dir.index(x)] )[0]
        status = gpg.decrypt_file(f, passphrase="123456",output=oFileName )
        print("processing: ", f.name)
        print("ok: ", status.ok)
        print("status: ", status.status)
        print("stderr: ", status.stderr)

