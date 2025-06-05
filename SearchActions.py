#!/usr/bin/env python3
# Copyright © 2025 Mark Summerfield. All rights reserved.
# License: GPLv3

from PySide2.QtGui import QKeySequence

import Util
from Images import SVG_SEARCH_DELETE, SVG_SEARCH_NEW, SVG_VIEW_SEARCHES


class Mixin:

    def searchActionsMake(self):
        print('searchActionsMake') # TODO
        self.searchNewAction = None
        self.searchViewAction = None
        self.searchDeleteAction = None
