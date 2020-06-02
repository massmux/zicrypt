import os,shutil
from pathlib import Path,PurePath


ERR_NOTSUPPORTED="error: mode not supported or invalid"
ERR_SOURCE_NOTPRESENT="error: source dir invalid or not present"


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


def movedirs(Source,Dest):
    (abs_source,abs_dest,souceName,destName) = (    os.path.dirname(os.path.realpath(Source)),
                                                os.path.dirname(os.path.realpath(Dest)),
                                                PurePath(Source).name,
                                                PurePath(Dest).name
                                                )

    try:
        shutil.move( abs_dest+"/"+destName+"/"+Source, abs_dest+"/"+destName)
        if PurePath(Source).parts[0] in ['/','.','..']:
            shutil.rmtree((abs_dest+"/"+destName+"/"+PurePath(Source).parts[1] ))
            print ((abs_dest+"/"+destName+"/"+PurePath(Source).parts[1] ))
        else:
            shutil.rmtree((abs_dest+"/"+destName+"/"+PurePath(Source).parts[0] ))
            print ((abs_dest+"/"+destName+"/"+PurePath(Source).parts[0] ))
        return True
    except:
        return False


