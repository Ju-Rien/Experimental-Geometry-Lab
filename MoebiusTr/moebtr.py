"""Required data structures for Moebius transformation, homogeneous complex 2D coordinates and more."""

import numpy as np
import sys

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


# Je ne pense pas que ça aie du sens de définir l'addition d'une transformation de Moebius
#    def __add__(self, othertr):
#        res = self._mat + othertr._mat
#        return MoebTr(res[0][0], res[0][1], res[1][0], res[1][1])
#    def __sub__(self, othertr):
#        res = self._mat + othertr._mat
#        return MoebTr(res[0][0], res[0][1], res[1][0], res[1][1])


    def __mul__(self, othertr):
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

        # if isinstance(pt, HComplex):
        # VÉRIFIER si les points sont complexes ou HComplexes

        Mabc = MoebTr._toRef(α, β, γ)._mat
        Mxyz = MoebTr._toRef(x, y, z)._mat

        tr = MoebTr(1, 0, 0, 1)
        try:
            tr._mat = np.linalg.inv(Mxyz).dot(Mabc)
            np.linalg.inv(Mabc)
        except np.linalg.LinAlgError as e:
            #print(str(e), file=sys.stderr)
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
        elif isinstance(z, Circle):
            pass
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

    def inv(self):
        """Returns the inverse MoebTr."""
        inv = np.linalg.inv(self._mat)
        return MoebTr(inv[0][0], inv[0][1], inv[1][0], inv[1][1])


class HComplex:

    def __init__(self, z, w=1):
        self._vector = np.array([complex(0), complex(1)])
        self._vector[1] = complex(w)

        if w == 0:
            self._vector[0] = complex(1)
        else:
            self._vector[0] = complex(z)


    def __add__(self, otherhc):
        res = self._vector[0] + self._vector[1] * otherhc._vector[0] / otherhc._vector[1]
        return HComplex(res, self._vector[1])


    def __sub__(self, otherhc):
        res = self._vector[0] - self._vector[1] * otherhc._vector[0] / otherhc._vector[1]
        return HComplex(res, self._vector[1])


    def __mul__(self, otherhc):
        res = self._vector * otherhc._vector
        return HComplex(res[0], res[1])


    def __eq__(self, ohc):
        if self._vector[1] == 0:
            return ohc._vector[1] == 0
        elif ohc._vector[1] == 0:
            return False
        else:
            return self._vector[0]/self._vector[1] == ohc._vector[0]/ohc._vector[1]

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
        if self._vector[1] == 0:
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



        res = HComplex((b * g - a * f)/(b*c - a*d), (f*c - g*a)/(d*a - b*c))

        return res


    def radius(self):
        return abs((self._points[0] - self.center()).value())


if __name__ == "__main__":
    print("Coming soon.")
