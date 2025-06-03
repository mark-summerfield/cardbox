#!/usr/bin/env python3
# Copyright © 2025 Mark Summerfield. All rights reserved.
# License: GPLv3

import os

from PySide2.QtGui import QIcon


def getIcon(svg):
    return QIcon(os.path.join(os.path.dirname(__file__), "images", svg))
