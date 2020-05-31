#!/usr/bin/env python3


#   Copyright (C) 2019-2020 Denali Sàrl www.denali.swiss, Massimo Musumeci, @massmux
#
#   This script encrypts/descrypts file by file, all items found and rebuilds directory structure
#
#   It is subject to the license terms in the LICENSE file found in the top-level
#   directory of this distribution.
#
#   No part of this software, including this file, may be copied, modified,
#   propagated, or distributed except according to the terms contained in the
#   LICENSE file.
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER


import os,sys
import gnupg
from pathlib import Path
from zilib import *
from config import config
import argparse


""" parsing arguments """
parser = argparse.ArgumentParser("zicrypt.py")
parser.add_argument("-m","--mode", help="mode encrypt|decrypt", type=str, required=True)
parser.add_argument("-s","--source", help="The source directory to process", type=str, required=True)
parser.add_argument("-d","--destination", help="The destination directory for processed files", type=str, required=True)
args = parser.parse_args()
(inSource,inDest,inMode)=(args.source,args.destination,args.mode)
inDest=inDest+"/"

#ERR_NOTSUPPORTED="error: mode not supported or invalid"
#ERR_SOURCE_NOTPRESENT="error: source dir invalid or not present"


"""encrypt or decrypt mode"""
if inMode not in ['encrypt','decrypt']:
    print(ERR_NOTSUPPORTED)
    sys.exit()

"""check source dir"""
try:
    files_dir=ls_files(inSource)
except:
    print(ERR_SOURCE_NOTPRESENT)
    sys.exit()

# init gpg
gpg = gnupg.GPG(gnupghome=config['gpghome'])

# create dir
os.makedirs( inDest, exist_ok=True)

if inMode=='encrypt':
    # encrypting files
    for x in files_dir:
        with open(x, "rb") as f:
            os.makedirs( Path(inDest+files_dir[files_dir.index(x)]).parent, exist_ok=True)
            status = gpg.encrypt_file(f,recipients=[config['gpgrecipient']],output= inDest+files_dir[files_dir.index(x)]+".gpg")
            print("file: %s\nstatus: %s\nstderr: %s\n" % (f.name,status.status,status.stderr) )


elif inMode=='decrypt':
    # decrypting files
    for x in files_dir:
        with open(x, "rb") as f:
            os.makedirs( Path(inDest+files_dir[files_dir.index(x)]).parent, exist_ok=True)
            oFileName=os.path.splitext(inDest+files_dir[files_dir.index(x)] )[0]
            status = gpg.decrypt_file(f, passphrase=config['passphrase'],output=oFileName )
            print("file: %s\nstatus: %s\nstderr: %s\n" % (f.name,status.status,status.stderr) )

else:
    print(ERR_NOTSUPPORTED)
    sys.exit()


