#!/usr/bin/env python3
# Copyright © 2025 Mark Summerfield. All rights reserved.
# License: GPLv3

from PySide2.QtGui import QKeySequence

import Util
from ImageFilenames import SVG_HELP_ABOUT, SVG_HELP_HELP


class Mixin:

    def helpActionsMake(self):
        print('helpActionsMake') # TODO
        self.helpHelpAction = None
        self.helpAboutAction = None
