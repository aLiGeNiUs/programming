import os
dir1 = '/home/x/TestCode/dir1'
dir2 = '/home/x/TestCode/dir2'
os.chdir(dir1)
print(os.getcwd())
os.system('cp *.jpg /home/x/TestCode/dir2/ ')
os.chdir(dir2)
print(os.getcwd())
print(os.listdir(dir2))
