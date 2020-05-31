# zicrypt
 gpg recursive folders encryptor suitable to be used with cloud storage services!

 If you use a cloud service for storing your files, you should never send plain to the cloud. This because the cloud is third-party server and you cannot know what is happening there and who can access your files. You cannot know if your files are deleted as well, when you want they to. This script makes possible to store your directory three after encryption to the cloud. The encryption is made with your gpg key hosted locally on your computer or within a youbikey.


 syntax (encryption)

```
usage: encrypt.py [-h] -s SOURCE -d DESTINATION

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        The source directory to process
  -d DESTINATION, --destination DESTINATION
                        The destination directory for processed files

```

 syntax (decryption)

```
usage: decrypt.py [-h] -s SOURCE -d DESTINATION

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        The source directory to process
  -d DESTINATION, --destination DESTINATION
                        The destination directory for processed files

```
