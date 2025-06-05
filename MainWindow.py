#!/usr/bin/env python3
# Copyright © 2025 Mark Summerfield. All rights reserved.
# License: GPLv3

import os

from PySide2.QtCore import QTimer
from PySide2.QtGui import QKeySequence
from PySide2.QtWidgets import QMainWindow, QMessageBox

import Util
from Const import (
    APPNAME, SVG_BOX_ADD_FROM_BOX, SVG_BOX_ADD_FROM_SEARCH, SVG_BOX_DELETE,
    SVG_BOX_NEW, SVG_CARD_ADD_TO_BOX, SVG_CARD_DELETE, SVG_CARD_EXPORT,
    SVG_CARD_HIDE, SVG_CARD_NEW, SVG_CARD_REMOVE_FROM_BOX, SVG_CARD_UNHIDE,
    SVG_EDIT_BOLD, SVG_EDIT_BULLET_LIST, SVG_EDIT_COPY, SVG_EDIT_CUT,
    SVG_EDIT_END_LIST, SVG_EDIT_INSERT_FILE_LINK, SVG_EDIT_INSERT_SYMBOL,
    SVG_EDIT_INSERT_WEB_LINK, SVG_EDIT_ITALIC, SVG_EDIT_MONOSPACE,
    SVG_EDIT_NUMBERED_LIST, SVG_EDIT_PASTE, SVG_EDIT_REDO, SVG_EDIT_UNDO,
    SVG_FILE_CONFIGURE, SVG_FILE_EXPORT, SVG_FILE_NEW, SVG_FILE_OPEN,
    SVG_FILE_QUIT, SVG_FILE_SAVE, SVG_FILE_SAVE_AS, SVG_HELP_ABOUT,
    SVG_HELP_HELP, SVG_SEARCH_DELETE, SVG_SEARCH_NEW, SVG_VIEW_BOXES,
    SVG_VIEW_HIDDEN, SVG_VIEW_SEARCHES, SVG_VIEW_UNBOXED, SVG_VIEW_VISIBLE,
    SVG_WINDOW, SVG_WINDOW_CASCADE, SVG_WINDOW_CLOSE, SVG_WINDOW_NEXT,
    SVG_WINDOW_PREV, SVG_WINDOW_TILE, SVG_WINDOWS)


class Window(QMainWindow):

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


    def warn(self, message):
        QMessageBox.warning(self, 'Error — ' + APPNAME, message,
                            QMessageBox.Close)


    def getDefaultDir(self):
        dirname = None
        if self.model:
            dirname = os.path.dirname(self.model.filename)
        if dirname is None:
            dirname = os.path.dirname(os.path.expanduser('~'))
        return os.path.abspath(dirname)


    def makeActions(self):
        self.makeFileActions()
        self.makeEditActions()
        self.makeCardActions()
        self.makeBoxActions()
        self.makeSearchActions()
        self.makeWindowActions()
        self.makeHelpActions()


    def makeFileActions(self):
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


    def makeEditActions(self):
        print('makeEditActions') # TODO
        self.editUndoAction = None
        self.editRedoAction = None
        self.editCopyAction = None
        self.editCutAction = None
        self.editPasteAction = None
        self.editBoldAction = None
        self.editItalicAction = None
        self.editMonospaceAction = None
        self.editBulletListAction = None
        self.editNumberedListAction = None
        self.editEndListAction = None
        self.editInsertWebLinkAction = None
        self.editInsertFileLinkAction = None
        self.editInsertSymbolAction = None


    def makeCardActions(self):
        print('makeCardActions') # TODO
        self.cardNewAction = None
        self.cardViewVisibleAction = None
        self.cardViewUnboxedAction = None
        self.cardViewHiddenAction = None
        self.cardAddToBoxAction = None
        self.cardRemoveFromBoxAction = None
        self.cardExportAction = None
        self.cardUnhideAction = None
        self.cardHideAction = None
        self.cardDeleteAction = None


    def makeBoxActions(self):
        print('makeBoxActions') # TODO
        self.boxNewAction = None
        self.boxViewAction = None
        self.boxAddFromSearchAction = None
        self.boxAddFromBoxAction = None
        self.boxDeleteAction = None


    def makeSearchActions(self):
        print('makeSearchActions') # TODO
        self.searchNewAction = None
        self.searchViewAction = None
        self.searchDeleteAction = None


    def makeWindowActions(self):
        print('makeWindowActions') # TODO
        self.windowNextAction = None
        self.windowPrevAction = None
        self.windowCascadeAction = None
        self.windowTileAction = None
        self.windowCloseAction = None


    def makeHelpActions(self):
        print('makeHelpActions') # TODO
        self.helpHelpAction = None
        self.helpAboutAction = None


    def makeMainMenu(self):
        print('makeMainMenu') # TODO
        menubar = self.menuBar()
        self.makeFileMenu(menubar)
        self.editMenu = None
        self.cardMenu = None
        self.boxMenu = None
        self.searchMenu = None
        self.windowMenu = None
        self.helpMenu = None


    def makeFileMenu(self, menubar):
        self.fileMenu = menubar.addMenu('&File')
        self.fileMenuUpdate()


    def makeToolbars(self):
        print('makeToolbars') # TODO


    def makeMainWindow(self):
        print('makeMainWindow') # TODO


    def makeConnections(self):
        print('makeConnections') # TODO


    def fileMenuUpdate(self):
        print('fileMenuUpdate') # TODO
        self.fileMenu.clear()
        self.fileMenuAddActions()
        self.fileMenuMakeConnections()
        # TODO recent files


    def fileMenuAddActions(self):
        print('fileMenuAddActions') # TODO
        self.fileMenu.addAction(self.fileQuitAction)


    def fileMenuMakeConnections(self):
        print('fileMenuMakeConnections') # TODO
        self.fileQuitAction.triggered.connect(self.close)


    def windowMenuUpdate(self):
        print('windowMenuUpdate') # TODO


    def saveSettings(self):
        self.config.windowGeometry = self.saveGeometry()
        self.config.windowState = self.saveState()
        if self.model:
            self.config.mostRecentFile = self.model.filename
        self.config.save()


    def closeEvent(self, _event):
        self.saveSettings()
        self.closeModel()


    def openModel(self, filename):
        print('openModel', filename) # TODO


    def closeModel(self):
        print('closeModel') # TODO
        if self.model is not None:
            self.model.close()
            self.model = None
