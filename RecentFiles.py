#!/usr/bin/env python3
# Copyright © 2025 Mark Summerfield. All rights reserved.
# License: GPLv3

from Const import DEFAULT_MAX_RECENT_FILES


class RecentFiles: # TODO replace list with size-limited deque

    def __init__(self):
        self.filenames = []
        self.maximum = DEFAULT_MAX_RECENT_FILES


    def add(self, filename):
        filename = os.path.abspath(filename)
        if self.filenames and self.filenames[0] == filename:
            return # found as first nothing to do
        try:
            self.filenames.remove(filename)
        except ValueError:
            pass # not found which is fine
        self.filenames.insert(0, filename) # put first
        self.filenames = self.filenames[:self.maximum] 

