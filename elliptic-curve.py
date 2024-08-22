class EllipticCurve:
    def __init__(self, a, b, mod_p):
        self._a = a
        self._b = b
        self._p = mod_p
    
    def a(self):
        return self._a
    
    def b(self):
        return self._b
    
    def p(self):
        return self._p


class EllipticCurvePoint:
    def __init__(self, curve, x_coor, y_coor):
        self._curve = curve
        self._x = x_coor
        self._y = y_coor

    def x(self):
        return self._x
    
    def y(self):
        return self._y
    
    def __eq__(self, other):
        if (self.x() == other.x())  and (self.y() == other.y()):
            return True
        return False
    
    def isInf(self):
        return self._x == None

    def add(self, point2):
        if (self.isInf()):
            return point2
        
        if (point2.isInf()):
            return self

        if (self.y() == point2.y()) and ((self.y() != 0)):
            dx = (3*self._x*self._x) + self._curve.a()
            dy_inverse = pow(2*self._y, -1, self._curve.p())
            m = (dx*dy_inverse) % self._curve.p()

        elif (self.y() != point2.y()) and (self.y() + point2.y() != 0) and (point2.x() - self.x() != 0):
            dy = point2.y() - self.y()
            dx_inverse = pow(point2.x() - self.x(), -1, self._curve.p())
            m = (dy*dx_inverse) % self._curve.p()

        elif point2.x() - self.x() == 0:
            return EllipticCurvePoint(self._curve, None, None)
        
        elif (self.y() + point2.y() == 0):
            return EllipticCurvePoint(self._curve, None, None)
        
        x3 = (m*m - self.x() - point2.x()) % self._curve.p()
        y3 = (m*(self.x() - x3) - self.y()) % self._curve.p()

        return EllipticCurvePoint(self._curve, x3, y3)
    
    def multiply(self, n):
        result = self
        i = 1
        while i <= n:
            result = result.add(self)
            i += 1
        return result
    
    def __str__(self):
        return "(" + str(self._x) + ", " + str(self._y) + ")" + " on the curve: x^3 + " + str(self._curve.a()) + "x + " + str(self._curve.b())

def find_k(ec, ecp1, ecp2):
    result = ecp1
    k = 0
    while result != ecp2:
        result = result.add(ecp1)
        k+=1
    return k

def find_distinct_multiples(ec, ecp1):
    list = []
    result = ecp1
    while result not in list:
        list.append(result)
        result = ecp1.add(ecp1)
    return len(list)




def q1():
    ec1 = EllipticCurve(2, 3, 19) 
    p1 = EllipticCurvePoint(ec1, 1, 5)
    p2 = EllipticCurvePoint(ec1, 9, 3)

    print("a." + str(p1.add(p2)))

    p3 = EllipticCurvePoint(ec1, 9, -3)
    print("b. " + str(p2.add(p3)))

    print("c. " + str(p1.add(p3)))

    print("d. " + str(find_k(ec1, p1, p2)))

    print(find_distinct_multiples(ec1, p1))

q1()

def q2():
    ec2 = EllipticCurve(-10, 21, 557)
    p1 = EllipticCurvePoint(ec2, 2, 3)
    print("189 * (2, 3) = " + str(p1.multiply(188)))
    print("63 * (2, 3) = " + str(p1.multiply(63)))
    print("27 * (2, 3) = " + str(p1.multiply(27)))
 
q2()


