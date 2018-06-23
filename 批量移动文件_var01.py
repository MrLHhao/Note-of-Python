import os
import shutil

def filemove(oldfile,newfile,fileformat):
    weblist = os.walk(oldfile)
    newpath = newfile
    for path,d,filelist in weblist:
        for filename in filelist:
            if fileformat in filename:
                full_path = os.path.join(path,filename)
                despath = newpath
                print(shutil.move(full_path,despath),'文件移动成功')
            else:
                print('文件不存在')
filemove('C:\\Users\\lh\\Desktop','F:\\工作\\Python\\视频','.mp4')
