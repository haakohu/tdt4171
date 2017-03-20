import numpy as np
from tools import *


transition = np.array([0.7,0.3])
sensor = np.array([0.9,0.2])
ev = [True,True,False, True, True]
n = len(ev)
mv = [None for i in range(n+1)]
mv[0] = np.array( normalize([0.5,0.5]*sensor))

def sensor_model(ev,i):
  if i == len(ev):
    return np.array([1,1])
  if ev[i]:
    return sensor
  return np.flip(sensor,0)

choices = [None for i in range(n)]
choices[0] = True

for i in range(1,n):
  max_true = max(transition * mv[i-1][0]) # for xt true
  max_false = max(np.flip(transition,0) * mv[i-1][1]) # for xt false
  if max_true > max_false:
    new_value = transition * mv[i-1][0]
    choices[i] = True
  else:
    new_value = np.flip(transition,0) * mv[i-1][1]
    choices[i] = False
  new_value  *= sensor_model(ev,i+1)
  mv[i] = normalize(new_value)

print(choices)
print(mv)

