#!/usr/bin/env python3
# Copyright © 2025 Mark Summerfield. All rights reserved.
# License: GPLv3

import os
import re

from PySide2.QtGui import QIcon


def getIcon(svg):
    return QIcon(os.path.join(os.path.dirname(__file__), "images", svg))


def clamp(minimum, value, maximum):
    return (minimum if value < minimum else (maximum if value > maximum
            else value))


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
