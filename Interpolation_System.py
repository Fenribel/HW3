from scipy.interpolate import interp1d
from numpy import *
from math import *
import random
import matplotlib as mpl
import matplotlib.pyplot as plt


def f(x):
    return sin(x)

xs = []
cos_vals = []
x = 0.0

for i in range (12):
    x = i*(1-0.5*random.random())
    cos_vals += [f(x)]
    xs += [x]

xs_real = []
cos_vals_real = []

for i in range (120):
    x = i/10
    cos_vals_real += [f(x)]
    xs_real += [x]



dpi = 80
fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
mpl.rcParams.update({'font.size': 10})

plt.axis([0, 12, -1.5, 1.5])

plt.title('Cos(x)')
plt.xlabel('x')
plt.ylabel('F(x)')




g = interp1d(xs, cos_vals, kind = 3)

xs_interpol = []
cos_vals_interpol = []
x = 0.0

for i in range (120):
    try:
        x = i/10
        cos_vals_interpol += [g(x)]
        xs_interpol += [x]
    except:
        print('')

plt.plot(xs, cos_vals, 'go')
plt.plot(xs_interpol, cos_vals_interpol, color='red', linestyle='solid',
         label='cos(x)')
plt.plot(xs_real, cos_vals_real, color='blue', linestyle='dashed',
         label='cos(x)')

plt.show()
error = 0
for i in range(ceil(max(xs) * 10)):
    error += (cos_vals_interpol[i] - cos_vals_real[i]) ** 2
error = sqrt(error / ceil(max(xs) * 10))
print(error)
