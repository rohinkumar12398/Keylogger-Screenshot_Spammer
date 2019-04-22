# Keylogger-Screenshot_Spammer

This project has 4 files
  - keylogger.py
  -screenshotCapture.py
  -serverFileTransfer.py
  -clientFileTransfer.py

This project is designed for Mac OS

## keylogger.py
  This file contains the code for the keylogger. The keylogger logs every keystroke by the victim and stores this information       in a text file called 'keylog.txt'. The format in which this log is organized reveals the date, time, and key that was pressed.

## screenshotCapture.py
  This file contains the code for taking a screenshot everytime the victim clicks on the mouse. The problem with this is that the frequency is screenshots becomes too much due to its reliance on clicks. As a result, the purpose of this is to serve more of "screenshot spammer" where the victim will be constantly spammed with screenshots on his/her Mac everytime he/she clicks.

## serverFileTransfer.py
  This file contains the code for transferring the 'keylog.txt' to a server (Currently configured to be Local but can easily be changed). In conjunction with 'clientFileTransfer.py', the data from the 'keylog.txt' file is transferred to a server IP address and into a new file called 'keylogReceived.txt' on the server side.
  
## clientFileTransfer.py
  This file contains the code for transferring the 'keylog.txt' to a server. In conjunction with 'serverFileTransfer.py', the data from the 'keylog.txt' file is transferred to a server IP address and into a new file called 'keylogReceived.txt' on the server side.
  
## keylog.txt
  This file is the output file from the 'keylogger.py' program. This contains all the keys logged by the victim.
  
## keylogReceived.txt
  This file is the output file from the 'serverFileTransfer.py' and 'clientFileTransfer.py' program. This contains the data from the original 'keylog.txt' file.
  
## FacebookForm.png & GmailForm.png
  These images contain example screenshots taken by the 'screenshotCapture.py' program.
  
