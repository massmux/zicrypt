# zicrypt
 gpg recursive folders encryptor suitable to be used with cloud storage services!

 If you use a cloud service for storing your files, you should never send plain files to any cloud. This because the cloud is third-party server or servers and you cannot know what is happening there and who can access your files. You cannot know if your files are deleted as well, when you remove them. This script makes possible to store your directory tree after encryption to the cloud. The encryption is made with your gpg key hosted either locally on your computer or within a youbikey usb-connected.

 Source and destination dirs are expressed as relative to local path. The destination dir is created and all the files are placed there with the same tree structure they had in the source directory. No file is ever deleted.

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

