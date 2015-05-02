import os
import sys


def search(dir)
    for root, subdirs, files in os.walk(dir):
        print('Dir(%s)' % root)

        for filename in files:
            print('- File(%s)' % r)
