import hashlib
import tkinter
import tkinter.messagebox
import tkinter.filedialog
from tkinter import *
import os
from sys import argv
import re


def readFile(argv):
    path = argv
    for curDir, dirs, files in os.walk(argv):
        for file in files:
            position = re.sub(r"\\", "/", os.path.join(curDir, file))
            md5_1 = hashlib.md5()
            with open(position, "r", encoding='utf-8', errors='ignore') as f:
                data = f.read()
                if data:
                    md5_1.update(data.encode('utf-8'))
                else:
                    break
            md5_2 = md5_1.hexdigest()
            print(position)
            print(md5_2)


if __name__ == '__main__':
    input1 = input('Please input the path which you want to get the hash:\n')
    argv = re.sub(r"\\", "/", input1)
    readFile(argv)
