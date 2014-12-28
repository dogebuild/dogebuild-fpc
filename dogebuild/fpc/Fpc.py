__author__ = 'kir'

import os
import subprocess

class Fpc:
    def __init__(self):
        self.dir = str()

    def build(self):
        if self.dir is not None:
            subprocess.call(["fpc", str(self.dir)])

