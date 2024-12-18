import math


def raise_un_sup(a, b):
    """Used for raising a TypeError when the operation is not supported, for e.g., when adding a Vec2 to a float."""
    raise TypeError(f'Unsupported operand type(s) for +: {type(a)} and {type(b)}')


class Vec2:
    """
    A 2D vector class.
    -----------------
    Attributes:
    ----------
    x -- The x component of the vector,
    y -- The y component of the vector,
    mag_Sq -- The magnitude squared of the vector,
    dir_x -- The direction of the vector w.r.t. the x-axis,
    dir_y -- The direction of the vector w.r.t. the y-axis

    Methods:
    -------
    mag -- Returns the magnitude of the vector,
    normalized -- Returns the normalized vector
    """

    def __init__(self, x: float, y: float):
        """
        Parameters:
        ----------
        x -- The x component of the vector,
        y -- The y component of the vector
        """
        self.x = x
        self.y = y
        self.mag_Sq = (x ** 2 + y ** 2)
        self.dir_x = math.atan2(y, x)
        self.dir_y = math.atan2(x, y)

    def __str__(self):
        """Overloads the 'str' function for a vector."""
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        """Overloads the '+' operator for two vectors such that 2D vectors may be added to both 2D and 3D vectors."""
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        elif isinstance(other, Vec3):
            return Vec3(self.x + other.x, self.y + other.y, other.z)
        else:
            raise_un_sup(self, other)

    def __sub__(self, other):
        """
        Overloads the '-' operator for two vectors such that 2D vectors may be subtracted from both 2D and 3D vectors.
        """
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)
        elif isinstance(other, Vec3):
            return Vec3(self.x - other.x, self.y - other.y, -other.z)
        else:
            raise_un_sup(self, other)

    def mag(self):
        """Returns the magnitude of the vector, accurate upto 2 decimal places."""
        return round(math.sqrt(self.mag_Sq), 2)

    def normalized(self):
        """Returns a normalized vector."""
        return Vec2(self.x / self.mag(), self.y / self.mag())

    def __eq__(self, other):
        """Overrides == operator for vectors"""
        if isinstance(other, Vec2):
            return self.x == other.x and self.y == other.y
        else:
            raise_un_sup(self, other)


#######################################################################################################


class Vec3:
    """
    A 3D vector class.
    -----------------
    Attributes:
    ----------
    x -- The x component of the vector,
    y -- The y component of the vector,
    z -- The z component of the vector,
    mag_Sq -- The magnitude squared of the vector,
    dir -- A tuple storing the direction cosines of the vector.

    Methods:
    -------
    mag -- Returns the magnitude of the vector,
    normalized -- Returns the normalized vector
    """

    def __init__(self, x: float, y: float, z: float):
        """
        Parameters:
        ----------
        x -- The x component of the vector,
        y -- The y component of the vector,
        z -- The z component of the vector
        """
        self.x = x
        self.y = y
        self.z = z
        self.mag_Sq = (x ** 2 + y ** 2 + z ** 2)

        self.dir = (math.acos(x / math.sqrt(self.mag_Sq)), math.acos(y / math.sqrt(self.mag_Sq)),
                    math.acos(z / math.sqrt(self.mag_Sq)))

    def __str__(self):
        """Overloads the 'str' function for a vector."""
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        """Overloads the '+' operator for two vectors such that 3D vectors may be added to both 2D and 3D vectors."""
        if isinstance(other, Vec3):
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, Vec2):
            return Vec3(self.x + other.x, self.y + other.y, self.z)
        else:
            raise_un_sup(self, other)

    def __sub__(self, other):
        """Overloads the '-' operator for two vectors such that 3D vectors may be subtracted from both 2D and 3D vectors."""
        if isinstance(other, Vec3):
            return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, Vec2):
            return Vec3(self.x - other.x, self.y - other.y, self.z)
        else:
            raise_un_sup(self, other)

    def mag(self):
        """Returns the magnitude of the vector, accurate upto 2 decimal places."""
        return round(math.sqrt(self.mag_Sq), 2)

    def normalized(self):
        """Returns a normalized vector."""
        return Vec3(self.x / self.mag(), self.y / self.mag(), self.z / self.mag())

    def __eq__(self, other):
        """Overrides == operator for vectors"""
        if isinstance(other, Vec3):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            raise_un_sup(self, other)
