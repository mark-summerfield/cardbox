#!/usr/bin/env python3
# Copyright © 2025 Mark Summerfield. All rights reserved.
# License: GPLv3

from PySide2.QtGui import QKeySequence


class Mixin:

    def makeActions(self):
        self.fileActionsMake()
        self.editActionsMake()
        self.cardActionsMake()
        self.boxActionsMake()
        self.searchActionsMake()
        self.windowActionsMake()
        self.helpActionsMake()


    def makeMainMenu(self):
        print('makeMainMenu') # TODO
        menubar = self.menuBar()
        self.fileMenuMake(menubar)
        self.editMenu = None
        self.cardMenu = None
        self.boxMenu = None
        self.searchMenu = None
        self.windowMenu = None
        self.helpMenu = None


    def makeToolbars(self):
        print('makeToolbars') # TODO


    def makeMainWindow(self):
        print('makeMainWindow') # TODO


    def makeConnections(self):
        print('makeConnections') # TODO
