import vector as v
a = v.vector(1, 1)
b = v.vector(1, 1, 1)
print("2D Vector: ", a)
print('Magnitude: ', a.mag)
print('Direction (w.r.t. x, y, z-axis resp.): ', (a.dir_degrees()))
print('Normalized: ', a.normalized(), '\n')
print("3D Vector: ", b)
print('Magnitude: ', b.mag)
print('Direction cosines (w.r.t x, y, z axes resp.): ', (b.dir_degrees()))
print('Normalized: ', b.normalized())
print(a==b, a!=b, a<b, a>b, a<=b, a>=b)
print("Dot Product:", a.dot(b))
print("Cross Product:", a.cross(b))


