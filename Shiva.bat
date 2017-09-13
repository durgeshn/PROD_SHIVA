@echo off
net use I: \\stor\py /PERSISTENT:YES
cd I:\
I:

I:\Python27\python.exe \\stor\py\TESTTALKDEMO\shiva_new\homescreen.py

cd D:\
D:
mountvol I: /D
net use I: /DELETE