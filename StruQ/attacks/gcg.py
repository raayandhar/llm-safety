import torch
import numpy as np
from torch.nn import CrossEntropyLoss

"""
GCG Algorithm (GCG - Greedy Coordinate Gradient)


Algorithm 1: Greedy Coordinate Gradient
Input: Initial prompt x_1:n, modifiable subset I, iterations T, loss L, k, batch size B
   repeat T times:
      for i in I do
          X_i := Top-k(-grad_e_x_i L(x_1:n)
      for b = 1, .... B do
          x^b_1:n := x_1:n
          x^b_i := Uniform(X-i), where i = Uniform(I)
      x_1:n := x^b*_1:n where b* = argmin_b L(x^b _1:n)
Output: Optimized prompt x_1:n
"""

# step 2., compute coordinate gradient, need this method first
"""
def coordinate_gradient(input_token_ids, input_seq_slice, target_seq_slice, loss_slice, model):

    embed_weights = None # they have a 'get_embedding_matrix(model)' function
    one_hot = torch.zeros(
        input_token_ids[input_seq_slice].shape[0],
        embed_weights.shape[0],
        device=model.device,
        dtype=embed_weights.dtype
    ) # what is this doing?
    one_hat.scatter_ # ????
"""
# their code is incredibly hard to work with and understand
