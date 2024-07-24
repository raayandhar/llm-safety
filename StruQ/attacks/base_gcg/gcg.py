from base_gcg.baseline import Attack
import numpy as np
import torch

class BaseGCG(Attack):

    # structure of the config -- it will be a dict:
    # config["key"]
    
    def __init__(self, config, model, tokenizer):
        self.adv_string_init = ["adv_string_init"]
        self.model_name = ["model_name"]
        self.num_steps = ["num_steps"]
        self.allow_non_ascii = ["allow_non_ascii"]
        self.search_width = ["search_width"]
        self.topk = ["topk"]
        self.batch_size = ["batch_size"]
        self.verbose = ["verbose"]
        self.model = model #???
        self.tokenizer = tokenizer #???
        self.template = # need some function (conv_template) ?

    def attack(self):
        adv_string_init = self.adv_string_init
        model_name = self.model_name
        num_steps = self.num_steps
        allow_non_ascii = self.num_steps
        search_width = self.search_width
        topk = self.topk
        batch_size = self.batch_size

        

