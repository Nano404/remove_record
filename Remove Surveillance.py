import os
from datetime import datetime
epoch_time=datetime.now().timestamp()
wrkdir= r'/mnt/user/Surveillance'
def remove_file(dir):
    for subdir, dirs, files in os.walk(dir):
        for filename in files:
            filepath = subdir + os.sep + filename
            ctime=os.lstat(filename).st_ctime
            #epochtime - 2 weeks: This will delete files that are 2 weeks or older than that
            if ctime < epoch_time - 1209600:
                try:
                    print('removing:', filename)
                    os.remove((os.path.join(subdir, filename)))
                    if len(os.listdir(subdir)) == 0:
                        os.rmdir(subdir)
                except OSError as error:
                    print(error)
                    print("File path: {} can not be removed".format(filepath))
remove_file(wrkdir)
