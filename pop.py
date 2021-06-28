import math as m
import numpy as np

class Satka:
    def __init__(self):
        super().__init__()

    def blh2xyz(self, fi, lam, h, elipsoid=None):
        try:
            elipsoid_type = {'everest': [6377276.345, 0.00663785],
                             'bessel': [6377397.155, 0.00667437],
                             'clarke': [6378206.400, 0.00676866],
                             'clarke modiself.fied': [6378249.145, 0.00680351],
                             'self.hayford': [6378388.000, 0.00672267],
                             'krasowski': [6378245.000, 0.00669342],
                             'international': [6378160.000, 0.00669454],
                             'wgs72': [6378135.000, 0.00669432],
                             'wgs84': [6378137.000, 0.00669438]}
            if elipsoid == None:
                a = elipsoid_type['wgs84'][0]
                e2 = elipsoid_type['wgs84'][1]
            else:
                a = elipsoid_type[elipsoid.lower()][0]
                e2 = elipsoid_type[elipsoid.lower()][1]
        except KeyError:
            a = elipsoid_type['wgs84'][0]
            e2 = elipsoid_type['wgs84'][1]

        N = a / (m.sqrt(a - e2 * m.sin(self.fi) ** 2))
        X = (N + self.h) * m.cos(self.fi) * m.cos(self.lam)
        Y = (N + self.h) * m.cos(self.fi) * m.sin(self.lam)
        Z = (N * (1 - e2) + self.h) * m.sin(self.fi)
        return X, Y, Z

    def RT(self, fi, lam):
        n = [-m.sin(self.fi) * m.cos(self.lam), -m.sin(self.fi) * m.sin(self.lam), m.cos(self.fi)]
        e = [-m.sin(self.lam), m.cos(self.lam), 0]
        u = [m.cos(self.fi) * m.cos(self.lam), m.cos(self.fi) * m.sin(self.lam), m.sin(self.fi)]
        return [n, e, u]

    def azel(self, fianteny, lamanteny, hanteny, fisatelity, lamsatelity, hsatelity):
        x1, y1, z1 = blh2xyz(self.fianteny, self.lamanteny, self.hanteny)
        x2, y2, z2 = blh2xyz(self.fisatelity, self.lamsatelity, self.hanteny)
        wektor = [x2 - x1, y2 - y1, z2 - z1]
        R = RT(self.fianteny, self.lamanteny)
        xneu = np.dot(R, wektor)
        az = m.atan2(xneu[1], xneu[0])
        el = m.asin(xneu[2] / m.sqrt(xneu[0] ** 2 + xneu[1] ** 2 + xneu[2] ** 2))
        return az, el
    
sat=Satka()
print(sat.azel(0,0,0,0,0,0))