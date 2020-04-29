import os
import shutil


def all_path(dirname):
    result = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            result.append(apath)
    return result


def GetExtNamesList(fileslist, ext):
    filenames = []
    for file in fileslist:
        fileinfo = os.path.splitext(file)
        if fileinfo[1] == ext:
            filenames.append(file)
    return filenames


sourcefolder = r'c:\Users\Admin\Desktop\a'
desfolder = r'c:\Users\Admin\Desktop\b'
filelist = GetExtNamesList(all_path(sourcefolder), '.xlsx')  # 此处例子是htm，可以改为其他类型
for file in filelist:
    print(file)
    desfilename = file.replace(sourcefolder, desfolder)
    desfilename = desfilename.replace('\\', '/')
    print(desfilename)
    if not os.path.exists(os.path.dirname(desfilename)):
        os.makedirs(os.path.dirname(desfilename))
    if not os.path.exists(desfilename):
        shutil.copy(file, desfilename)  # 如果要改为移动，而不是拷贝，可以将copy改为move
