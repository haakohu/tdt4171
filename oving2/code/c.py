import numpy as np
from tools import *


transition = np.array([0.7,0.3])
sensor = np.array([0.9,0.2])
ev = [True,True,False, True, True]
n = len(ev)
fv = [None for i in range(n+1)]
fv[0] = np.array([0.5,0.5])

def sensor_model(value):
  if value:
    return sensor
  return np.flip(sensor,0)

#Forward part
for i in range(1,n+1):
  part_1 = transition  * fv[i-1][0]  # if X is true
  part_2 = np.flip(transition,0) * fv[i-1][1]
  new_value = (part_1+part_2)*sensor_model(ev[i-1])
  fv[i] = normalize(new_value)

print(fv)

bv = [None for i in range(n+1)]
bv[n] = np.array([1,1])
#Backwards part
for i in range(n-1,0,-1):
  part_1 = sensor[0] * bv[i+1][0] * transition # X is false
  part_2 = sensor[1] * bv[i+1][1] * np.flip(transition,0)
  new_value = (part_1+part_2) * fv[i]
  bv[i] = normalize(new_value)

print(bv)