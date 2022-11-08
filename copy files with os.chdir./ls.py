import os
dir1 = '~/TestCode/dir1'
dir2 = '~/TestCode/dir2'
os.chdir(dir1)
print(os.getcwd())
os.system('cp *.jpg ~/TestCode/dir2/')
os.chdir(dir2)
print(os.getcwd())
print(os.listdir(dir2))
