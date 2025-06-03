#!/usr/bin/env python3
# Copyright © 2025 Mark Summerfield. All rights reserved.
# License: GPLv3

import os
import sys

from PySide2.QtWidgets import (
    QApplication, QDialog, QLineEdit, QTextBrowser, QVBoxLayout)

import MainWindow
import Util
from Const import APPNAME, SVG_ICON


def main():
    app = QApplication(sys.argv)
    app.setApplicationName(APPNAME)
    app.setWindowIcon(Util.getIcon(SVG_ICON))
    config = None # TODO read config
    # TODO app.setCursorFlashTime(0) # read config
    window = MainWindow.Window(config)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
