#!/usr/bin/env python3
# Copyright © 2025 Mark Summerfield. All rights reserved.
# License: GPLv3

class Mixin:

    def openModel(self, filename):
        print('openModel', filename) # TODO


    def closeModel(self):
        print('closeModel') # TODO
        if self.model is not None:
            self.model.close()
            self.model = None
