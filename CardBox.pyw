#!/usr/bin/env python3
# Copyright © 2025 Mark Summerfield. All rights reserved.
# License: GPLv3

import os
import sys

from PySide2.QtWidgets import QApplication

import Config
import MainWindow
import Util
from Const import APPNAME, DOMAIN
from ImageFilenames import SVG_ICON


def main():
    app = QApplication(sys.argv)
    app.setApplicationName(APPNAME)
    app.setWindowIcon(Util.getIcon(SVG_ICON))
    config = Config.Config(Util.getConfigFilename(DOMAIN, APPNAME)[0])
    if not config.cursorBlink:
        app.setCursorFlashTime(0)
    window = MainWindow.Window(config)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
