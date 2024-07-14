import clipman,sys

try:
    clipman.init()
except:
    print("Clipman is not initialised")
    sys.exit()

clipboard_text = clipman.paste()
file = open("test_this.txt",'a')
file.write(clipboard_text+"\n")
file.close()
#print("Text written successfully")

