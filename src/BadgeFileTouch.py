import os
import time
import datetime
from datetime import datetime
from stat import *

#returns a list of all the files on the current directory
path='\\\\pdatfile01\\ProdData\\HRMS_Payroll_Exchange\\PEBS\\Badge_Photos\\Archived'
files = os.listdir(path)
os.chdir(path)
basedate = "2018-10-31"

#print(time.localtime()
      
for f in files:
  #my folder has some jpegs and raw images
    if f.lower().endswith('jpg') or f.lower().endswith('crw'):
        st = os.stat(f)
        #atime = st[ST_ATIME] #access time
        mtime = st[ST_MTIME] #modification time
        mtimedt = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
#if f.startswith('00004'):
        if mtimedt > basedate:
            print(f, end=' ')
            #print(datetime.fromtimestamp(time.localtime())
            print(mtimedt)
            os.utime(f,None)