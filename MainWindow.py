#!/usr/bin/env python3
# Copyright © 2025 Mark Summerfield. All rights reserved.
# License: GPLv3

import os

from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QMainWindow, QMessageBox

import BoxActions
import CardActions
import EditActions
import FileActions
import HelpActions
import MainWindowMake
import MainWindowModel
import SearchActions
import Util
import WindowActions
from Const import APPNAME


class Window(QMainWindow, MainWindowMake.Mixin, MainWindowModel.Mixin,
             FileActions.Mixin, EditActions.Mixin, CardActions.Mixin,
             BoxActions.Mixin, SearchActions.Mixin, WindowActions.Mixin,
             HelpActions.Mixin):

    def __init__(self, config, parent=None):
        super().__init__(parent)
        self.config = config
        self.model = None
        self.mdiArea = None
        self.statusIndicator = None
        self.makeActions()
        self.makeMainMenu()
        self.makeToolbars()
        self.makeMainWindow()
        self.makeConnections()


    def show(self):
        self.restoreGeometry(self.config.windowGeometry)
        self.restoreState(self.config.windowState)
        self.fileMenuUpdate()
        self.windowMenuUpdate()
        super().show()
        if self.config.mostRecentFile:
            QTimer.singleShot(
                0, lambda: self.openModel(self.config.mostRecentFile))


    def closeEvent(self, _event):
        self.saveSettings()
        self.closeModel()


    def warn(self, message):
        QMessageBox.warning(self, 'Error — ' + APPNAME, message,
                            QMessageBox.Close)


    def saveSettings(self):
        self.config.windowGeometry = self.saveGeometry()
        self.config.windowState = self.saveState()
        if self.model:
            self.config.mostRecentFile = self.model.filename
        self.config.save()
