#!/usr/bin/env python3
# Copyright © 2025 Mark Summerfield. All rights reserved.
# License: GPLv3

from PySide2.QtGui import QKeySequence

import Util
from ImageFilenames import (
    SVG_FILE_CONFIGURE, SVG_FILE_EXPORT, SVG_FILE_NEW, SVG_FILE_OPEN,
    SVG_FILE_QUIT, SVG_FILE_SAVE, SVG_FILE_SAVE_AS, SVG_HELP_ABOUT)


class Mixin:

    def fileActionsMake(self):
        self.fileNewAction = Util.makeAction(
            SVG_FILE_NEW, '&New…', 'Create a new card index',
            QKeySequence.New)
        self.fileOpenAction = Util.makeAction(
            SVG_FILE_OPEN, '&Open…', 'Open an existing card index',
            QKeySequence.Open)
        self.fileSaveAction = Util.makeAction(
            SVG_FILE_SAVE, '&Save', 'Save unsaved changes',
            QKeySequence.Save)
        self.fileSaveAsAction = Util.makeAction(
            SVG_FILE_SAVE_AS, 'Save &As…',
            'Save a copy of the card index and switch to using the copy')
        self.fileExportAction = Util.makeAction(
            SVG_FILE_EXPORT, '&Export…', 'Export the card index')
        self.fileConfigureAction = Util.makeAction(
            SVG_FILE_CONFIGURE, '&Configure…',
            'Configure the card index application')
        self.fileQuitAction = Util.makeAction(
            SVG_FILE_QUIT, '&Quit',
            'Save unsaved changed and quit the card index application',
            QKeySequence.Quit)


    def fileMenuMake(self, menubar):
        self.fileMenu = menubar.addMenu('&File')
        self.fileMenuUpdate()


    def fileMenuUpdate(self):
        print('fileMenuUpdate') # TODO
        self.fileMenu.clear()
        for action in (self.fileQuitAction,):
            if action.receivers('triggered'):
                action.triggered.disconnect()
        self.fileMenuAddActions()
        self.fileMenuMakeConnections()
        # TODO recent files


    def fileMenuAddActions(self):
        print('fileMenuAddActions') # TODO
        self.fileMenu.addAction(self.fileQuitAction)


    def fileMenuMakeConnections(self):
        print('fileMenuMakeConnections') # TODO
        self.fileQuitAction.triggered.connect(self.close)
