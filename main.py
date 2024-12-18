from vector import *
a, b = Vec2(1, 1), Vec3(1,1,1)
print("2D Vector: ", a)
print('Magnitude: ', a.mag())
print('Direction w.r.t. x-axis: ', a.dir_x)
print('Normalized: ', a.normalized(), '\n')
print("3D Vector: ", b)
print('Magnitude: ', b.mag())
print('Direction cosines (w.r.t x, y, z axes resp.): ', b.dir)
print('Normalized: ', b.normalized())

print("Addition: ", a+b)
print("Subtraction:", a-b)
