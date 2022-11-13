#!/usr/bin/python3
import os
import shutil

count1 = 0
count2 = 0

dir1 = '~/orginal/Fire'
dir2 = '~/orginal/Smoke'
dir3 = '~/XMLonly/Fire'
dir4 = '~/XMLonly/Smoke'
dir5 = '~/DataSet/test'
dir6 = '~/train'

os.chdir(dir1)
os.system('cp *.jpg ~/XMLonly/Fire')
os.chdir(dir2)
os.system('cp *.jpg ~/XMLonly/Smoke')

os.chdir(dir3)
for path in os.scandir(dir3):
    if path.is_file():
        count1 += 1
        
os.chdir(dir4)
for path in os.scandir(dir3):
    if path.is_file():
        count2 += 1
        
trainfilefire = int(count1 * 0.7)
testfilefire = count1 - trainfilefire

trainfilesmoke = int(count2 * 0.7)
testfilesmoke = count2 - trainfilesmoke


files1 = os.listdir(dir3)
files1.sort()

os.chdir(dir3)
for f in range(0, trainfilefire):
	shutil.move(os.getcwd()+"/"+files1[f] , dir6) 

files3 = os.listdir(dir3)
files3.sort()

os.chdir(dir3)
for f in range(0, testfilefire):
	shutil.move(os.getcwd()+"/"+files3[f] , dir5)
	
	
files2 = os.listdir(dir4)
files2.sort()
	
os.chdir(dir4)
for f in range(0, trainfilesmoke):
	shutil.move(os.getcwd()+"/"+files2[f] , dir6) 

files4 = os.listdir(dir4)
files4.sort()

os.chdir(dir4)
for f in range(0, testfilesmoke):
	shutil.move(os.getcwd()+"/"+files4[f] , dir5)
