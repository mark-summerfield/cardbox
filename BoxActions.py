#!/usr/bin/env python3
# Copyright © 2025 Mark Summerfield. All rights reserved.
# License: GPLv3

from PySide2.QtGui import QKeySequence

import Util
from ImageFilenames import (
    SVG_BOX_ADD_FROM_BOX, SVG_BOX_ADD_FROM_SEARCH, SVG_BOX_DELETE,
    SVG_BOX_NEW, SVG_VIEW_BOXES)


class Mixin:

    def boxActionsMake(self):
        print('boxActionsMake') # TODO
        self.boxNewAction = None
        self.boxViewAction = None
        self.boxAddFromSearchAction = None
        self.boxAddFromBoxAction = None
        self.boxDeleteAction = None
