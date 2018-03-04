from math import *
import random
import matplotlib as mpl
import matplotlib.pyplot as plt


xs = []
cos_vals = []

x = 0.0

def f(x):
    return cos(x)

for i in range (12):
    x = i*(1-0.5*random.random())
    cos_vals += [f(x)]
    xs += [x]


x_list = xs
y_list = cos_vals
N = len(x_list)

def c_k(x, N, k, x_list):
    c = 1.0
    for i in range (N):
        if i != k:
            c *= (x - float(x_list[i]))/(float(x_list[k]) - float(x_list[i]))
    return c

def L(x, N, x_list, y_list):
    l = 0
    for i in range (N):
        l += float(c_k(x, N, i, x_list))*float(y_list[i])
    return l

xs_interpol = []
cos_vals_interpol = []

x = 0.0

for i in range (120):
    x = i/10
    cos_vals_interpol += [L(x, N, x_list, y_list)]
    xs_interpol += [x]


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

plt.xlim(0, max(xs_interpol))

plt.plot(xs_interpol, cos_vals_interpol, color='red', linestyle='solid',
         label='cos(x)')
plt.plot(xs_real, cos_vals_real, color='blue', linestyle='dashed',
         label='cos(x)')
plt.plot(xs, cos_vals, 'go')
plt.show()


error = 0
for i in range (ceil(max(xs)*10)):
    error += (cos_vals_interpol[i]-cos_vals_real[i])**2
error = sqrt(error/ceil(max(xs)*10))
print(error)
