#!/usr/bin/env python3
# Copyright © 2025 Mark Summerfield. All rights reserved.
# License: GPLv3

import base64
import binascii
import configparser
import os

import RecentFiles
import Util

ASCII = 'ascii'
GENERAL_SECT = 'General'
WINDOW_SECT = 'Window'
WINDOW_STATE = 'State'
WINDOW_GEOMETRY = 'Geometry'
CURSOR_BLINK = 'CursorBlink'
DEFAULT_CURSOR_BLINK = True
MOST_RECENT_FILE = 'MostRecentFile'
RECENT_FILES_SECT = 'RecentFiles'
RECENT_FILE = 'File'
MAX_RECENT_FILES = 'MaxRecentFiles'


class Config:

    def __init__(self, filename=None):
        self.filename = filename
        self.cursorBlink = DEFAULT_CURSOR_BLINK
        self.windowGeometry = None
        self.windowState = None
        self.mostRecentFile = ''
        self.recentFiles = RecentFiles.RecentFiles()
        if filename is not None:
            cfg = configparser.ConfigParser()
            cfg.read(filename)
            self.cursorBlink = cfg.getboolean(GENERAL_SECT, CURSOR_BLINK,
                                              fallback=self.cursorBlink)
            raw = cfg.get(WINDOW_SECT, WINDOW_GEOMETRY, fallback=None)
            if raw:
                try:
                    self.windowGeometry = base64.b64decode(bytes(raw,
                                                                 ASCII))
                except binascii.Error as err:
                    print(f'failed to read window geometry: {err}')
            raw = cfg.get(WINDOW_SECT, WINDOW_STATE, fallback=None)
            if raw:
                try:
                    self.windowState = base64.b64decode(bytes(raw, ASCII))
                except binascii.Error as err:
                    print(f'failed to read window state: {err}')
            self.mostRecentFile = cfg.get(GENERAL_SECT, MOST_RECENT_FILE,
                                          fallback='')
            maximum = Util.clamp(
                0, cfg.getint(GENERAL_SECT, MAX_RECENT_FILES,
                              fallback=RecentFiles.DEFAULT_MAX),
                RecentFiles.DEFAULT_MAX)
            self.recentFiles = RecentFiles.RecentFiles(maximum)
            for i in range(maximum, 1, -1):
                filename = cfg.get(RECENT_FILES_SECT,
                                   f'{MOST_RECENT_FILE}{i}', fallback=None)
                if filename:
                    self.recentFiles.add(filename)


    def save(self, filename=None):
        filename = filename or self.filename
        dirname = os.path.dirname(filename)
        if not os.path.isdir(dirname):
            os.makedirs(dirname)
        cfg = configparser.ConfigParser()
        cfg.add_section(GENERAL_SECT)
        cfg.set(GENERAL_SECT, CURSOR_BLINK, str(self.cursorBlink))
        cfg.set(GENERAL_SECT, MOST_RECENT_FILE, self.mostRecentFile)
        cfg.set(GENERAL_SECT, MAX_RECENT_FILES,
                str(self.recentFiles.maxlen))
        cfg.add_section(RECENT_FILES_SECT)
        for i, filename in enumerate(self.recentFiles.files(), 1):
            if os.path.isfile(filename):
                cfg.set(RECENT_FILES_SECT, f'{RECENT_FILE}{i}', filename)
        cfg.add_section(WINDOW_SECT)
        if self.windowGeometry:
            text = str(self.windowGeometry.toBase64())[2:-1]
            cfg.set(WINDOW_SECT, WINDOW_GEOMETRY, text)
        if self.windowState:
            text = str(self.windowState.toBase64())[2:-1]
            cfg.set(WINDOW_SECT, WINDOW_STATE, text)
        with open(filename, 'wt', encoding='utf-8') as file:
            cfg.write(file)


    def __str__(self):
        return (f'{self.filename=} {self.cursorBlink=} '
                f'{self.windowGeometry=} {self.windowState=} '
                f'{self.mostRecentFile=} '
                f'self.recentFiles={str(self.recentFiles)}')
