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


for i in range(1,n+1):
  part_1 = transition  * fv[i-1][0]  # if x is true
  part_2 = np.flip(transition,0) * fv[i-1][1] # if x is false
  new_value = (part_1+part_2)*sensor_model(ev[i-1])
  fv[i] = normalize(new_value)

print(fv)



