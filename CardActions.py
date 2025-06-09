#!/usr/bin/env python3
# Copyright © 2025 Mark Summerfield. All rights reserved.
# License: GPLv3

from PySide2.QtGui import QKeySequence

import Util
from ImageFilenames import (
    SVG_CARD_ADD_TO_BOX, SVG_CARD_DELETE, SVG_CARD_EXPORT, SVG_CARD_HIDE,
    SVG_CARD_NEW, SVG_CARD_REMOVE_FROM_BOX, SVG_CARD_UNHIDE,
    SVG_VIEW_HIDDEN, SVG_VIEW_UNBOXED, SVG_VIEW_VISIBLE)


class Mixin:

    def cardActionsMake(self):
        print('cardActionsMake') # TODO
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
