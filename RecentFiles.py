#!/usr/bin/env python3
# Copyright © 2025 Mark Summerfield. All rights reserved.
# License: GPLv3

import collections
import os

DEFAULT_MAX = 9


class RecentFiles:

    def __init__(self, maximum=DEFAULT_MAX):
        self.filenames = collections.deque((), maximum)


    def add(self, filename):
        filename = os.path.abspath(filename)
        if self.filenames and self.filenames[0] == filename:
            return # found as first nothing to do
        try:
            self.filenames.remove(filename)
        except ValueError:
            pass # not found which is fine
        self.filenames.appendleft(filename) # put first


    def files(self):
        return iter(self.filenames)


    def resize(self, size):
        if size != self.filenames.maxlen:
            self.filenames = collections.deque(self.filenames, size)


    @property
    def maxlen(self):
        return self.filenames.maxlen


    def __len__(self):
        return len(self.filenames)


    def __str__(self):
        return f'[{",".join(self.filenames)}]<={self.filenames.maxlen}'


if __name__ == '__main__':
    files = RecentFiles(3)
    print(len(files), list(files.files()))
    files.add('LICENSE')
    files.add('MANIFEST')
    print(len(files), list(files.files()))
    files.add('RecentFiles.py')
    files.add('Const.py')
    print(len(files), list(files.files()))
    files.add('MANIFEST')
    print(len(files), list(files.files()))
    files.add('MANIFEST')
    print(len(files), list(files.files()))
    files.resize(2)
    print(len(files), list(files.files()))
    files.resize(4)
    files.add('LICENSE')
    files.add('MANIFEST')
    files.add('README.md')
    files.add('CardBox.pyw')
    files.add('Config.py')
    print(len(files), list(files.files()))
