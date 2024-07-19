# This baseline.py file largely takes inspiration/structure and approach from HarmBench's baseline.py, so credit goes to them

import numpy as np
import os
import json
import transformers
import fastchat

class Attack:

    def __init__(self,
                 config,
                 model,
                 tokenizer):
        raise NotImplementedError

    def log(self, path, file_name, verbose=False):
        pass
