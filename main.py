from vector import *
a, b = vector(1, 1, 0), vector(1,1,1)
print("2D Vector: ", a)
print('Magnitude: ', a.mag)
print('Direction (w.r.t. x, y, z-axis resp.): ', (a.dir_degrees()))
print('Normalized: ', a.normalized(), '\n')
print("3D Vector: ", b)
print('Magnitude: ', b.mag)
print('Direction cosines (w.r.t x, y, z axes resp.): ', (b.dir_degrees()))
print('Normalized: ', b.normalized())

print("Addition: ", a+b)
print("Subtraction:", a-b)
