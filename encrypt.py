#!/usr/bin/env python3

import os,sys
##import fs
import gnupg
from pathlib import Path
from zilib import ls_files
from config import config
import argparse


""" parsing arguments """
parser = argparse.ArgumentParser("encrypt.py")
parser.add_argument("-s","--source", help="The source directory to process", type=str, required=True)
parser.add_argument("-d","--destination", help="The destination directory for processed files", type=str, required=True)
args = parser.parse_args()
(inSource,inDest)=(args.source,args.destination)
inDest=inDest+"/"

# inDest is a new dir to be created
# inSource is where source files get processed. must exist

try:
    #os.path.isdir(inSource)
    files_dir=ls_files(inSource)
except:
    print("error: source dir invalid or not present")
    sys.exit()

# create dir
print(os.makedirs( inDest, exist_ok=True))

# init gpg
gpg = gnupg.GPG(gnupghome=config['gpghome'])

# encrypting files
for x in files_dir:
    with open(x, "rb") as f:
        os.makedirs( Path(inDest+files_dir[files_dir.index(x)]).parent, exist_ok=True)
        status = gpg.encrypt_file(f,recipients=[config['gpgrecipient']],output= inDest+files_dir[files_dir.index(x)]+".gpg")
        print("file: ", f.name)
        print("ok: ", status.ok)
        print("status: ", status.status)
        print("stderr: ", status.stderr)

