# Filename: backup_ver1.py

import os
import time

# 1. The files and directories to be backed up are specified in a list.
source = r'D:\pythonfile\test'

# 2. The backup must be stored in a main backup directory
target_dir = r'D:\pythonfile'  # Remember to change this to what you will be using

# 3. The files are backed up into a rar file.
# 4. The name of the rar archive is the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.rar'
# 5. We use the rar command in windows to put the files in a zip archive,you must to be sure  you have installed WinRARA and that in your path
rar_command = "WinRAR A %s %s -r" % (target, source)

# Run the backup
if os.system(rar_command) == 0:
    print ('Successful backup to', target)
else:
    print('Backup FAILED')
