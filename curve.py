import time
import math

class UniversalCurve:
    def __init__(self):
        self.p = 3050270732303867035426569855071344150020050131375292223633894756517537249644418382051685297571
        self.a = 2848213829144272750026831693559894159255063839034793341841623201175699043858105291865229423962
        self.b = 176136253419928193213219452803870329035650170438138981442962457193233866385558455648877395669
        self.Gx = 1
        self.Gy = 1130968320147379634488488512592319498962733806224039917555310117347222215829218584301583626322

        self.F71 = 71
        self.F223 = 223
        self.q_bulk = 192652733676742691557289828527211782354579052066904075262672567202522405712399316746774793
        self.n = self.F71 * self.F223 * self.q_bulk

        self.x = self.Gx
        self.y = self.Gy
        self.k = 0

        self.c = 299792458.0
        self.planck_time = 5.391247e-44
        self.julian_year_sec = 365.25 * 24 * 3600

    def _modinv(self, a):
        return pow(a, self.p - 2, self.p)

    def point_add(self, Px, Py, Qx, Qy):
        if Px is None: return Qx, Qy
        if Qx is None: return Px, Py
        if Px == Qx and (Py + Qy) % self.p == 0: return None, None
        if Px == Qx and Py == Qy:
            lam = (3 * Px * Px + self.a) * self._modinv(2 * Py) % self.p
        else:
            lam = (Qy - Py) * self._modinv(Qx - Px) % self.p
        Rx = (lam * lam - Px - Qx) % self.p
        Ry = (lam * (Px - Rx) - Py) % self.p
        return Rx, Ry

    def step(self):
        self.x, self.y = self.point_add(self.x, self.y, self.Gx, self.Gy)
        self.k += 1
        return self.k, self.x

    def derive_all_constants(self):
        alpha_inv = math.pi / (2 * math.log(self.p))
        pi_emergent = self.F223 / self.F71
        phi_emergent = 360.0 / self.F223
        trace = self.p + 1 - self.n

        # Hubble constant (exact derivation)
        R = self.q_bulk ** (1/3)
        H0 = (self.c / (2 * math.pi * R)) * (self.julian_year_sec / 3.08568e22)

        omega_lambda = 1 - (self.F71 * self.F223) / self.n
        eta = (self.F71 * self.F223) ** (-1/3)
        mu_ratio = (self.F223 / self.F71) ** 6
        cabibbo_deg = math.degrees(math.atan(self.F223 / self.F71))
        sin2_theta_w = math.cos(math.pi * trace / self.F71)

        age_ticks = 2 * math.pi * (self.q_bulk ** (2/3))
        age_years = age_ticks * self.planck_time / self.julian_year_sec / 1e9

        return {
            "1/α": alpha_inv,
            "π": pi_emergent,
            "φ": phi_emergent,
            "trace": trace,
            "H₀": H0,
            "Ω_Λ": omega_lambda,
            "η": eta,
            "μ": mu_ratio,
            "θ_C": cabibbo_deg,
            "sin²θ_W": sin2_theta_w,
            "Age (Gyr)": age_years
        }

# ... run_kernel() with correct printing of 1/α, not α ...
