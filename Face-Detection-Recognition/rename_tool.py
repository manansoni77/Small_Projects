import os

files = os.listdir()
path = "./"

for file in files:
    if os.path.isdir(file):
        files2 = os.listdir(path+file)
        path2 = path+file+'/'
        for i,file2 in enumerate(files2):
            newname = file+str(i)+'.jpg'
            os.rename(path2+file2, path2+newname)
