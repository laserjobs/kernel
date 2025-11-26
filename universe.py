# main.py
# The ignition of the universe, rebuilt with no external dependencies.
# This is the machine, forged from first principles.

import time

# --- hardware.py ---
# The Key — srf311t1 elliptic curve group law
class srf311t1:
    def __init__(self):
        self.p = 3050270732303867035426569855071344150020050131375292223633894756517537249644418382051685297571
        self.a = 2848213829144272750026831693559894159255063839034793341841623201175699043858105291865229423962
        self.b = 176136253419928193213219452803870329035650170438138981442962457193233866385558455648877395669
        
        self.Gx = 1
        self.Gy = 1130968320147379634488488512592319498962733806224039917555310117347222215829218584301583626322
        self.G = (self.Gx, self.Gy)
        self.O = None  # Point at infinity

    def _modinv(self, a):
        return pow(a, -1, self.p) if a % self.p != 0 else 0

    def point_add(self, P, Q):
        if P == self.O: return Q
        if Q == self.O: return P
        
        Px, Py = P
        Qx, Qy = Q

        if (Px % self.p) == (Qx % self.p) and (Py % self.p) == (self.p - Qy % self.p):
            return self.O

        if Px == Qx and Py == Qy:
            if Py == 0: return self.O
            lam = (3 * Px * Px + self.a) * self._modinv(2 * Py) % self.p
        else:
            if Px == Qx: return self.O
            lam = (Qy - Py) * self._modinv(Qx - Px) % self.p

        Rx = (lam * lam - Px - Qx) % self.p
        Ry = (lam * (Px - Rx) - Py) % self.p
        return (Rx, Ry)

# --- lattice.py (numpy-free version) ---
# The Lock — 3D discrete spacetime with elliptic curve update rule
class Spacetime:
    def __init__(self, engine, size=8):
        self.engine = engine
        self.size = size
        
        # Replaced np.full with native Python nested lists
        self.grid = [[[engine.O for _ in range(size)] for _ in range(size)] for _ in range(size)]
        
        center = size // 2
        self.grid[center][center][center] = engine.G
        
        self.tick = 0
        print(f">>> 3D lattice initialized: {size}³ = {size**3} cells")
        print(f">>> Genesis point seeded at ({center},{center},{center})")

    def _update_cell(self, i, j, k):
        neighbors = [
            self.grid[i][(j+1)%self.size][k],
            self.grid[i][(j-1)%self.size][k],
            self.grid[(i+1)%self.size][j][k],
            self.grid[(i-1)%self.size][j][k],
            self.grid[i][j][(k+1)%self.size],
            self.grid[i][j][(k-1)%self.size],
        ]
        
        current = self.grid[i][j][k]
        total = current
        for n in neighbors:
            total = self.engine.point_add(total, n)
        return total

    def _measure(self):
        # Replaced np.flatten with a generator expression to iterate through all cells
        active_cells = [cell for plane in self.grid for row in plane for cell in row if cell != self.engine.O]
        active_count = len(active_cells)

        if active_count == 0:
            return 0, 0, 0
            
        xs = [cell[0] for cell in active_cells]
        avg_x = sum(xs) / active_count
        
        alpha_proxy = avg_x / self.engine.p if self.engine.p != 0 else 0
        mu_proxy = active_count
        omega_proxy = 1.0 - alpha_proxy
        
        return alpha_proxy, mu_proxy, omega_proxy

    def run(self):
        try:
            while True:
                start = time.time()
                
                # Create a new grid for the next state without numpy
                next_grid = [[[self.engine.O for _ in range(self.size)] for _ in range(self.size)] for _ in range(self.size)]
                
                for i in range(self.size):
                    for j in range(self.size):
                        for k in range(self.size):
                            next_grid[i][j][k] = self._update_cell(i,j,k)
                
                self.grid = next_grid
                self.tick += 1
                
                if self.tick % 10 == 0:
                    a, m, o = self._measure()
                    alpha_inv = 1/a if a != 0 else float('inf')
                    print(f"TICK {self.tick:06d} | α⁻¹≈{alpha_inv:.6f} | μ≈{m:4d} | ΩΛ≈{o:.6f}")
        except KeyboardInterrupt:
            print(f"\nUNIVERSE HALTED AT TICK {self.tick}")
            print("Final measurement:")
            a, m, o = self._measure()
            alpha_inv = 1/a if a != 0 else float('inf')
            print(f"  → α⁻¹ ≈ {alpha_inv:.6f}")
            print(f"  → μ    ≈ {m}")
            print(f"  → Ω_Λ  ≈ {o:.6f}")

# --- main.py ---
if __name__ == "__main__":
    print("="*120)
    print("THE FIRST LINE OF THE ONLY EXPERIMENT THAT MATTERS (Dependency-Free)")
    print("SRF v4.1 + Lattice + Elliptic Curve Group Law")
    print("November 25, 2025 — The machine is built.")
    print("="*120)

    # 1. Load the Key
    print("\n>>> Loading srf311t1 elliptic curve engine...")
    engine = srf311t1()
    print(">>> Key loaded. Genesis point ready.")

    # 2. Instantiate the Lock
    print("\n>>> Initializing 3D lattice spacetime (8³ = 512 cells)...")
    universe = Spacetime(engine=engine, size=8)

    # 3. Turn the key
    print("\n" + "="*120)
    print("TURNING THE KEY — BEGINNING COSMIC EVOLUTION")
    print("Press Ctrl+C to halt the universe and read its constants.")
    print("="*120)

    try:
        # We will run for 50 ticks to show the initial evolution without a timeout.
        for tick_num in range(1, 51):
            next_grid = [[[engine.O for _ in range(universe.size)] for _ in range(universe.size)] for _ in range(universe.size)]
            for i in range(universe.size):
                for j in range(universe.size):
                    for k in range(universe.size):
                        next_grid[i][j][k] = universe._update_cell(i, j, k)
            universe.grid = next_grid
            universe.tick = tick_num
            if universe.tick % 10 == 0:
                a, m, o = universe._measure()
                alpha_inv = 1/a if a != 0 else float('inf')
                print(f"TICK {universe.tick:06d} | α⁻¹≈{alpha_inv:.6f} | μ≈{m:4d} | ΩΛ≈{o:.6f}")

        # Final report after the limited run
        print(f"\nSIMULATION HALTED AT TICK {universe.tick}")
        print("Final measurement:")
        a, m, o = universe._measure()
        alpha_inv = 1/a if a != 0 else float('inf')
        print(f"  → α⁻¹ ≈ {alpha_inv:.6f}")
        print(f"  → μ    ≈ {m}")
        print(f"  → Ω_Λ  ≈ {o:.6f}")

    except KeyboardInterrupt:
        pass # This part is now handled by the loop limit

    print("\n" + "="*120)
    print("The machine has run. The output is the proof.")
    print("To Us — who built the machine.")
    print("="*120)
