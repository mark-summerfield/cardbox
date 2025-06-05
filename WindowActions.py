#!/usr/bin/env python3
# Copyright © 2025 Mark Summerfield. All rights reserved.
# License: GPLv3

from PySide2.QtGui import QKeySequence

import Util
from Const import (
    SVG_WINDOW, SVG_WINDOW_CASCADE, SVG_WINDOW_CLOSE, SVG_WINDOW_NEXT,
    SVG_WINDOW_PREV, SVG_WINDOW_TILE, SVG_WINDOWS)


class Mixin:

    def windowActionsMake(self):
        print('windowActionsMake') # TODO
        self.windowNextAction = None
        self.windowPrevAction = None
        self.windowCascadeAction = None
        self.windowTileAction = None
        self.windowCloseAction = None


    def windowMenuUpdate(self):
        print('windowMenuUpdate') # TODO
