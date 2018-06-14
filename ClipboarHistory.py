import win32clipboard
import time
old = ""
new = ""
while 1:
    win32clipboard.OpenClipboard()
    new = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    while old != new:
        win32clipboard.OpenClipboard()
        new = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        file = open('data.log', 'a+')
        file.write("### PASTE ###\r\n")
        file.write(new+"\r\n")
        file.close()
        old = new
        
    time.sleep(1)
