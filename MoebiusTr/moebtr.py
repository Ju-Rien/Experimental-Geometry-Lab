"""Required data structures for Moebius transformation, homogeneous complex 2D coordinates and more."""

import numpy as np
#import sys

class MoebTr:

    def __init__(self, a, b, c, d):
        if abs(a*d - b*c) < np.sqrt(np.finfo(float).eps):
            raise ValueError("The created MoebTr is not invertible. ad - bc = {}".format(a*d - b*c))

        elif (abs(a) == float("inf") or
             abs(b) == float("inf") or
             abs(c) == float("inf") or
             abs(d) == float("inf")):
            raise ValueError("The created MoebTr has an infinite value: {}, {}, {}, {}".format(a,b,c,d))

        self._mat = np.array([[complex(a), complex(b)],
                              [complex(c), complex(d)]])
        self.normalize()


    def __mul__(self, othertr):
        """The same as .dot()."""
        res = self.dot(othertr)
        return res


    def __eq__(self, otr):
        return (otr._mat[0][0] == self._mat[0][0] and
                otr._mat[0][1] == self._mat[0][1] and
                otr._mat[1][0] == self._mat[1][0] and
                otr._mat[1][1] == self._mat[1][1])


    def __ne__(self, otr):
        return (otr._mat[0][0] != self._mat[0][0] or
                otr._mat[0][1] != self._mat[0][1] or
                otr._mat[1][0] != self._mat[1][0] or
                otr._mat[1][1] != self._mat[1][1])


    def __getitem__(self, key):
        return self._mat[key]


    def __repr__(self):
        return f'MoebTr({self._mat[0][0]}, {self._mat[0][1]}, {self._mat[1][0]}, {self._mat[1][1]})'


    @classmethod
    def fromTo(cls, α, β, γ, x, y, z):
        """Creates the Moebius transformation mapping 3 complex numbers (α, β, γ) to (x, y, z)

        Note:
            Is a class method, which can be called using: MoebTr.fromTo(...)

        Args:
            α, β, γ: The 3 points from the domain.
            x, y, z: The 3 points in the image on which to map α, β, γ, respectively.

        Returns:
            The Moebius Transformation to map points (α, β, γ) to (x, y, z).
        """

        if (isinstance(α, HComplex) or
            isinstance(β, HComplex) or
            isinstance(γ, HComplex) or
            isinstance(x, HComplex) or
            isinstance(y, HComplex) or
            isinstance(z, HComplex)):
            α, β, γ = α.toComplex(), β.toComplex(), γ.toComplex()
            x, y, z = x.toComplex(), y.toComplex(), z.toComplex()

        Mabc = MoebTr._toRef(α, β, γ)._mat
        Mxyz = MoebTr._toRef(x, y, z)._mat

        tr = MoebTr(1, 0, 0, 1)
        try:
            tr._mat = np.linalg.inv(Mxyz).dot(Mabc)
            np.linalg.inv(Mabc)
        except np.linalg.LinAlgError as e:
            # print(str(e), file=sys.stderr)
            raise ValueError("A point is duplicated in starting set:({},{},{}) or \
in end set: ({}, {}, {})".format(α, β, γ, x, y, z)) from None

        return tr


    @classmethod
    def _toRef(cls, α, β, γ):
        """ Returns a MoebTr for the Moebius transformation between complex numbers (α, β, γ) and (0, 1, ∞)"""
        return MoebTr(β - γ, -1 * α * (β - γ), β - α, -1 * γ * (β - α))


    def dot(self, z):
        """Apply the Moebius transform to a point, in homogeneous coordinates.

        Args:
            z: A HComplex point or complex number.

        Returns:
            The resulting HComplex number from the product: M.z, where M is the Moebius \
            transformation encoded in this object.

        Note:
            MoebTr(a,b,c,d) * MoebTr(e,f,g,h) == MoebTr(a,b,c,d).dot(MoebTr(e,f,g,h))
        """
        if isinstance(z, complex) or isinstance(z, float) or isinstance(z, int):
            z = HComplex(z)

        if isinstance(z, Circle):
            res = z.tr(self)
        elif isinstance(z, MoebTr):
            mult = self._mat.dot(z[:])
            res = MoebTr(mult[0][0], mult[0][1], mult[1][0], mult[1][1])
        else:
            mult = self._mat.dot(z[:])

            if mult[1] == 0:
                res = HComplex(complex(1), mult[1])
            else:
                res = HComplex(mult[0], mult[1])

        return res

    #def t(self):
    #    """Returns the transpose of the MoebTr."""
    #    tr = self._mat.transpose()
    #    return MoebTr(tr[0][0], tr[0][1], tr[1][0], tr[1][1])

    def inv(self):
        """Returns the inverse MoebTr."""
        inv = np.linalg.inv(self._mat)
        return MoebTr(inv[0][0], inv[0][1], inv[1][0], inv[1][1])

    def normalize(self):
        """Normalizes matrix by square root of determinant"""
        det = self._mat[0][0]*self._mat[1][1] - self._mat[0][1]*self._mat[1][0]
        for i in range(2):
            for j in range(2):
                self._mat[i][j] = (self._mat[i][j])/(np.sqrt(det))

    def trace(self):
        """Returns the trace (as complex number)"""
        self.normalize()
        return (self._mat[0][0] + self._mat[1][1])**2


class HComplex:

    def __init__(self, z, w=1):
        self._vector = np.array([complex(z), complex(w)])

        if abs(w) == float("inf") and abs(z) == float("inf"):
            raise ValueError("Both arguments can't be infinity.")
        elif abs(z) == float("inf") or w == 0:
            self._vector[0] = complex(1)
            self._vector[1] = complex(0)
        elif abs(w) == float("inf"):
            self._vector[0] = complex(0)
            self._vector[1] = complex(1)


    def __eq__(self, ohc):
        if self._vector[1] == 0:
            return ohc._vector[1] == 0
        elif ohc._vector[1] == 0:
            return False
        else:
            return self.homogenize()._vector[0] == ohc.homogenize()._vector[0]

    def __ne__(self, ohc):
        if self._vector[1] == 0:
            return ohc._vector[1] != 0
        elif ohc._vector[1] == 0:
            return True
        else:
            return self._vector[0]/self._vector[1] != ohc._vector[0]/ohc._vector[1]


    def __str__(self):
        if self._vector[1] == 0:
            return "∞"
        else:
            return str(self._vector[0] / self._vector[1])

    def __getitem__(self, key):
        return self._vector[key]

    def __repr__(self):
        return f'HComplex({self._vector[0]}, {self._vector[1]})'

    def __bool__(self):
        return self._vector[0] == 0

    def homogenize(self):
        """Homogenizes the HComplex number to its canonic form ()."""
        if abs(self._vector[1]) < np.finfo(float).eps:
            self._vector[0] = 1
        else:
            self._vector[0] = self._vector[0] / self._vector[1]
            self._vector[1] = 1
        return self

    def isInf(self):
        self.homogenize()
        return self._vector[1] == 0

    def toComplex(self):
        """Returns the complex number associated with the HComplex value. Identical with .value().

        WARNING:
            If HComplex is ∞ (infinity), it will return float("inf"). Use .isInf to verify if the value is ∞ (infinity).
        """
        if self.isInf():
            return complex(float("inf"))
        self.homogenize()
        return self._vector[0]

    def value(self):
        """Returns the complex number associated with the HComplex value. Identical with .toComplex().

        WARNING:
            If HComplex is ∞ (infinity), it will return complex(float("inf")). Use .isInf to verify if the value is ∞ (infinity).
        """
        return self.toComplex()

    def _values(self):
        return self._vector[0], self._vector[1]

    def real(self):
        return self.toComplex().real

    def imag(self):
        return self.toComplex().imag


# TODO - La classe Circle devrait être développé en prenant en compte l'affichage.
class Circle:

    def __init__(self, p1, p2, p3):
        if isinstance(p1, HComplex) and isinstance(p2, HComplex) and isinstance(p3, HComplex):
            self._points = [p1, p2, p3]

        else:
            try:
                self._points = [HComplex(p1), HComplex(p2), HComplex(p3)]
            except:
                raise ValueError("Circle requires three points castable to complex numbers or HComplex points. \
Received: {},{} and {}".format(type(p1), type(p2), type(p3))) from None

        if p1 == p2 or p2 == p3 or p1 == p3:
            raise ValueError("Circle requires distinct points. Given: {},{} and {}".format(p1, p2, p3))


    def __str__(self):
        st = "Circle("
        for i in range(3):
            st += str(self._points[i])
            if i != 2:
                st += ", "
        st += ")"
        return st


    def __getitem__(self, key):
        return self._points[key]


    def __repr__(self):
        return f'Circle({self._points[0]}, {self._points[1]}, {self._points[2]})'


    def toComplex(self):
        """Returns the three complex points parametrizing the circle."""
        return (self._points[0].value(),
                self._points[1].value(),
                self._points[2].value())


    def center(self):
        α, β, γ = self.toComplex()

        if abs(α) == float("inf") or abs(β) == float("inf") or abs(γ) == float("inf"):
            return HComplex(1,0)

        α1, α2 = α.real, α.imag
        β1, β2 = β.real, β.imag
        γ1, γ2 = γ.real, γ.imag

        a = 2 * (α1 - β1)
        b = 2 * (α2 - β2)
        c = 2 * (α1 - γ1)
        d = 2 * (α2 - γ2)
        f = abs(β) ** 2 - abs(α) ** 2
        g = abs(γ) ** 2 - abs(α) ** 2

        tmp = b*c - a*d

        if abs(tmp) > np.finfo(float).eps:
            R = -(b * g - d * f)/tmp
            I = (g*a - f*c)/tmp
            res = HComplex(complex(R, I))
        else:
            res = HComplex(1, 0)

        return res.toComplex()


    def radius(self):
        # Ne fonctionnera pas, car j'ai retirer la soustraction de HComplex
        return abs((self._points[0].value() - self.center()))


    def tr(self, tr):
        return Circle(tr.dot(self._points[0]),
                      tr.dot(self._points[1]),
                      tr.dot(self._points[2]))
#initialize the 4 circles
def initialise(p1, p2, p3, p4):
    return

def cross_ratio(z1, z2, z3, z4):
    """Returns the cross ration of 4 complex numbers"""
    return ((z1-z4)*(z3-z2))/((z1-z2)*(z3-z4))

def inv_cross_ration(z1, z2, z3, a):
    """Returns the 4th complex number given 3 complex numbers and a cross-ratio"""
    return ((1-a)*z1*z3 + a*z2*z3 - z1*z2)/((a-1)*z2 - a*z1 + z3)

if __name__ == "__main__":
    print("Coming soon.")
