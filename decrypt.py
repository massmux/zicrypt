#!/usr/bin/env python3

import os,sys
import gnupg
from pathlib import Path
from zilib import ls_files
from config import config
import argparse


""" parsing arguments """
parser = argparse.ArgumentParser("decrypt.py")
parser.add_argument("-s","--source", help="The source directory to process", type=str, required=True)
parser.add_argument("-d","--destination", help="The destination directory for processed files", type=str, required=True)
args = parser.parse_args()
(inSource,inDest)=(args.source,args.destination)
inDest=inDest+"/"

try:
    files_dir=ls_files(inSource)
except:
    print("error: source dir invalid or not present")
    sys.exit()


# create dir
os.makedirs( inDest, exist_ok=True)

# init gpg
gpg = gnupg.GPG(gnupghome=config['gpghome'])

# decrypting procedure
for x in files_dir:
    with open(x, "rb") as f:
        os.makedirs( Path(inDest+files_dir[files_dir.index(x)]).parent, exist_ok=True)
        oFileName=os.path.splitext(inDest+files_dir[files_dir.index(x)] )[0]
        status = gpg.decrypt_file(f, passphrase=config['passphrase'],output=oFileName )
        print("processing: ", f.name)
        print("ok: ", status.ok)
        print("status: ", status.status)
        print("stderr: ", status.stderr)

