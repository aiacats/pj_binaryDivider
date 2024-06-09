
import os
import binaryDevider

target = "sample.png"

if os.path.isfile(target):
    print(os.path.getsize(target))
    fileList = binaryDevider.divide_file(target, 50000)
else:
    print("target file don't exist.")


input()