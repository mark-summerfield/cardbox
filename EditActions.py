#!/usr/bin/env python3
# Copyright © 2025 Mark Summerfield. All rights reserved.
# License: GPLv3

from PySide2.QtGui import QKeySequence

import Util
from Const import (
    SVG_EDIT_BOLD, SVG_EDIT_BULLET_LIST, SVG_EDIT_COPY, SVG_EDIT_CUT,
    SVG_EDIT_END_LIST, SVG_EDIT_INSERT_FILE_LINK, SVG_EDIT_INSERT_SYMBOL,
    SVG_EDIT_INSERT_WEB_LINK, SVG_EDIT_ITALIC, SVG_EDIT_MONOSPACE,
    SVG_EDIT_NUMBERED_LIST, SVG_EDIT_PASTE, SVG_EDIT_REDO, SVG_EDIT_UNDO)


class Mixin:

    def editActionsMake(self):
        print('editActionsMake') # TODO
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
