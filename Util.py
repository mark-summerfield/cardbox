#!/usr/bin/env python3
# Copyright © 2025 Mark Summerfield. All rights reserved.
# License: GPLv3

import os
import re

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QAction


def getIcon(svg):
    return QIcon(os.path.join(os.path.dirname(__file__), "images", svg))


def makeAction(iconname, text, tooltip=None, shortcut=None):
    action = QAction(getIcon(iconname), text)
    if tooltip is not None:
        action.setToolTip(tooltip)
    if shortcut is not None:
        action.setShortcut(shortcut)
    return action


def clamp(minimum, value, maximum):
    return (minimum if value < minimum else (maximum if value > maximum
            else value))


def getDefaultDir(self, filename=None): # e.g., model.filename
    dirname = os.path.dirname(filename) if filename else None
    if dirname is None:
        dirname = os.path.dirname(os.path.expanduser('~'))
    return os.path.abspath(dirname)


def getConfigFilename(domain, appname, ext='.ini'):
    name = re.sub(r'\W+', '_', appname) + ext
    home = os.path.expanduser('~')
    configpath = os.path.join(home, '.config', domain)
    normal = os.path.join(configpath, name)
    fallback = os.path.join(home, f'.{name}')
    if os.path.isfile(normal):
        return normal, True # exists in normal place
    if os.path.isfile(fallback):
        return fallback, True # exists in fallback place
    if os.path.isdir(configpath):
        return normal, False # doesn't exist but normal place does
    return fallback, False # doesn't exist and normal place doesn't either
