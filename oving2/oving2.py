# PART A
# Xt is the fact if it is raining or not 
# Et is the set of variables that describes wether or not we observed the director coming in with an umbrella


# P(X(t) | x(t-1)) = (0.7,0.3)
# P(E(t) | X(t)) = (0.9,0.2)
# The assumptions in this model is that the current state only depend on the previous state as we are using an first-order markov process

# PART B

# P(X(t+1) | E(1: t+1)) =  * P(e(t+1) | X(t+1)) sum( P(X(t+1) | x(t)) P(X(t) | E(1:t)))

import numpy as np


p_x_t_given_x_t_1 = np.array((0.7,0.3)) # P(X(t) | x(t-1))
not_p_x_t_given_x_t_1 = np.array((0.3,0.7)) # P(X(t) | !x(t-1))

ev = [True, True, False, True, True]
fv = []

def get_e_t_given_x(t): # P(e[t] | X[t])
  if ev[t-1]: # e starts at t = 1, but index starts at 0.
    return np.array([0.9,0.2])
  else:
    return np.array([0.2,0.9])

def get_sum(t): # Sum of P(X[t+1] | x[t]) * P (x[t] | e[1:t])
  last_prob = forward(t-1)
  return p_x_t_given_x_t_1 * last_prob[0] + not_p_x_t_given_x_t_1 * last_prob[1]


def forward(t): # P(x[t+1] | e[1:t+1])
  if t == 0:
    return np.array([0.5,0.5])
  global fv
  if len(fv) > t:
    return fv[t]
  value = get_e_t_given_x(t) * get_sum(t)
  value = normalize(value)
  fv.append(value)
  return value

def backward(t,k): # P(e(k+1:t) | Xk)
  print(1)
def backward_sum(t,k):
  if k+1 >= t:
    return 1
  return 0.9 * backward_sum(t,k+1) * np.array([0.7,0.3]) + 0.2*backward_sum(t,k+1) *  np.array([0.3,0.7])




def forward_backward(t):
  forward(len(ev))
  b = np.ones(len(ev))
  sv = np.zeros(len(ev))
  global fv
  fv[0] = prior
  for i in range(len(ev)-1,-1,-1):
    sv[i] = normalize(fv[i] * b)
    b = backward(b,ev[i])
  return sv
  

def normalize(vector):
  const = sum(vector)
  return vector / const



print(forward(5))
print(fv)


