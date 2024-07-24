import numpy as np
import os
import json
import transformers
import fastchat

class Attack:

    def __init__(self,
                 config,
                 model,
                 tokenizer,
                 **kwargs):
        raise NotImplementedError

    def log(self, path, file_name, verbose=False):
        # Probably belongs in a utils file
        pass

    def attack(self, **kwargs):
