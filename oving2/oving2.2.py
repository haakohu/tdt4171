import numpy as np


ev = [None, True,True,False,True,True] #No evidence for t = 0
p_x_t_1_given_x_t = np.array((0.7,0.3)) # P(X(t) | x(t-1))
p_x_t_1_given_not_x_t = np.array((0.3,0.7)) # P(X(t) | !x(t-1))

def get_e_t_given_x(e): # P(e[t] | X[t])
  if e: 
    return np.array([0.9,0.2])
  else:
    return np.array([0.2,0.9])

def get_sum(fv,ev,t): # Sum of P(X[t+1] | x[t]) * P (x[t] | e[1:t])
  last_prob = forward(fv,ev,t-1)[t-1]
  return p_x_t_1_given_x_t * last_prob[0] + p_x_t_1_given_not_x_t * last_prob[1]

def forward(fv,ev,t):
  print("RUNE")
  if t == 0:
    fv += [np.array([0.5,0.5])]
    return fv
  if t < len(fv):
    return fv
  new_value = get_e_t_given_x(ev[t]) * get_sum(fv,ev,t)
  fv += [new_value]
  normalize(fv)
  return fv


def normalize(vector):
  const = sum(vector)
  vector = vector / const



fv = []
t = 5
forward(fv,ev,t)
