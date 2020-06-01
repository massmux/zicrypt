# zicrypt
 gpg recursive folders encryptor suitable to be used with cloud storage services!

 If you use a cloud service for storing your files, you should never send plain files. This is because the cloud is third-party server (or servers) and you cannot know what is happening on that machine and who can really access your files. Moreover you cannot know if your files get really deleted when you remove them. This script makes possible to encrypt a whole directory tree (file by file) on your local computer in order to be suitable for secure upload to any cloud. The encryption is made with your gpg key hosted either locally on your computer or within a youbikey usb-connected.

 Source and destination dirs are expressed as relative to local path. The destination dir is created and all the files are placed there with the same tree structure they had in the source directory. No file is ever deleted.

 Os requirement. GPG installed on the computer. It is also obvious that a rsa key must be created in order to work with this script. To install gnupg, just run the command


```
 apt-get install gnupg2 
```


 python lib requirements

```
pip3 install gnupg
pip3 install pathlib
pip3 install argparse
```


 syntax

```
usage: zicrypt.py [-h] -m MODE -s SOURCE -d DESTINATION

optional arguments:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  mode encrypt|decrypt
  -s SOURCE, --source SOURCE
                        The source directory to process
  -d DESTINATION, --destination DESTINATION
                        The destination directory for processed files

```


 My youtube channel: http://www.youtube.com/c/MassimoSMusumeci and also at the telegram group with discussions about privacy and security: https://t.me/BitcoinSecPriv

