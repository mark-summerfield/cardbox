#!/usr/bin/env python3
# Copyright © 2025 Mark Summerfield. All rights reserved.
# License: GPLv3

import RecentFiles
from Const import DEFAULT_CURSOR_BLINK


class Config:

    def __init__(self, filename=None):
        self.filename = filename
        self.cursorBlink = DEFAULT_CURSOR_BLINK
        self.windowGeometry = None
        self.windowState = None
        self.mostRecentFile = None
        self.recentFiles = RecentFiles.RecentFiles()
