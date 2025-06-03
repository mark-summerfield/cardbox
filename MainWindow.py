#!/usr/bin/env python3
# Copyright © 2025 Mark Summerfield. All rights reserved.
# License: GPLv3

from PySide2.QtWidgets import QMainWindow


class Window(QMainWindow):

    def __init__(self, config, parent=None):
        super().__init__(parent)
        self.config = config
        self.model = None
        self.mdiArea = None
        self.statusIndicator = None
        self.makeActions()
        self.makeGui()
        self.loadSettings()


    def show(self):
        super().show()
        # TODO
        # if me.config.MostRecentFile != "" {
        # 	me.openModel(me.config.MostRecentFile)
        # }
        # me.fileMenuUpdate()
        # me.windowMenuUpdate()


    def makeActions(self): # TODO
        self.fileMenu = None
        self.fileNewAction = None
        self.fileOpenAction = None
        self.fileSaveAction = None
        self.fileSaveAsAction = None
        self.fileExportAction = None
        self.fileConfigureAction = None
        self.fileQuitAction = None
        self.editMenu = None
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
        self.cardMenu = None
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
        self.boxMenu = None
        self.boxNewAction = None
        self.boxViewAction = None
        self.boxAddFromSearchAction = None
        self.boxAddFromBoxAction = None
        self.boxDeleteAction = None
        self.searchMenu = None
        self.searchNewAction = None
        self.searchViewAction = None
        self.searchDeleteAction = None
        self.windowMenu = None
        self.windowNextAction = None
        self.windowPrevAction = None
        self.windowCascadeAction = None
        self.windowTileAction = None
        self.windowCloseAction = None
        self.helpMenu = None
        self.helpHelpAction = None
        self.helpAboutAction = None


    def makeGui(self):
        print('makeGui') # TODO


    def loadSettings(self):
        print('loadSettings') # TODO
