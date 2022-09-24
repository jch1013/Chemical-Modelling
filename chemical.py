from scipy.optimize import root


class Chemical:
    def __init__(self, name, params):
        self.name = name
        self.A = params[0]
        self.B = params[1]
        self.C = params[2]

    def vapor_pressure(self, temperature):
        exponent = self.A - (self.B / (temperature + self.C))
        return 10 ** exponent

    def boiling_point(self, p=1.01):
        def f(temperature):
            return p - 10 ** (self.A - (self.B / (temperature + self.C)))

        bp = root(f, 300)
        return bp.x[0]

    def __str__(self):
        return "Chemical: " + self.name
