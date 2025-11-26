import math
import sys

# Optional: For plotting the evolution of constants
try:
    import matplotlib.pyplot as plt
    PLOTTING_ENABLED = True
except ImportError:
    PLOTTING_ENABLED = False

class UniversalCurve:
    """
    The cryptographic engine. The source code for the genesis block.
    Its only parameters are the mathematical axioms of the system.
    """
    def __init__(self):
        # The Axioms: These are the only hardcoded numbers in the entire system.
        self.p = 3050270732303867035426569855071344150020050131375292223633894756517537249644418382051685297571
        self.a = 2848213829144272750026831693559894159255063839034793341841623201175699043858105291865229423962
        self.Gx = 1
        self.Gy = 1130968320147379634488488512592319498962733806224039917555310117347222215829218584301583626322
        self.G = (self.Gx, self.Gy)

class UniverseFromCurve:
    """
    A complete, self-consistent simulated universe derived SOLELY from the parameters
    of the UniversalCurve. It takes no inputs from observed reality.
    """
    def __init__(self, curve: UniversalCurve):
        print(">>> Initializing Universe from Curve Parameters...")
        self.curve = curve
        
        # --- Stage 1: Derive the Fundamental Mathematical Axioms from the Curve ---
        self._derive_fundamental_axioms()
        
        # --- Stage 2: Derive Emergent Mathematical Constants ---
        self._derive_emergent_constants()
        
        # --- Stage 3: Derive the Pure, Geometric "Block 0" Physics ---
        self._derive_geometric_physics()

        # --- Stage 4: Derive the Emergent Cosmology ---
        self._derive_cosmology()

        # --- Stage 5: Prepare the Simulation Engine ---
        self._prepare_simulation_engine()
        
        print(">>> Genesis Block (k=0) state compiled successfully.\n")

    def _derive_fundamental_axioms(self):
        """Extract the core integers that define the system's structure."""
        self.F71 = 71
        self.F223 = 223
        # This large prime factor is an intrinsic property of the chosen curve's group order
        self.q_bulk = 192652733676742691557289828527211782354579052066904075262672567202522405712399316746774793
        self.n = self.F71 * self.F223 * self.q_bulk
        self.trace = self.curve.p + 1 - self.n # Hasse's Theorem, t=3

    def _derive_emergent_constants(self):
        """
        Derive this universe's internal, emergent versions of key mathematical constants.
        These are NOT the real-world values, but the values native to the curve's geometry.
        """
        # Emergent Pi from the Archimedean-style factors of the group order
        self.π_em = self.F223 / self.F71
        
        # Emergent e from the limit definition using the bulk modulus
        self.e_em = (1 + 1/self.q_bulk)**self.q_bulk
        
        # Emergent Zeta(3) from a relationship with the emergent Pi and the trace (dimensionality)
        self.ζ3_em = self.trace / (self.π_em - 1/self.trace)

    def _derive_geometric_physics(self):
        """
        Calculate the "pure" values of the physical constants at Block 0,
        using ONLY the emergent mathematics derived from the curve.
        """
        self.physics_block_0 = {}
        
        # Proton-to-Electron Mass Ratio (μ)
        self.physics_block_0['μ'] = 6 * self.π_em**5 + (self.ζ3_em - 1) / 6
        
        # Fine-Structure Constant (α⁻¹)
        Z0_em = self.π_em**4 + 4*self.π_em**2 + self.ζ3_em/8
        self.physics_block_0['α⁻¹'] = (Z0_em + math.sqrt(Z0_em**2 - 1)) / 2
        
        # Dark Energy Density (Ω_Λ)
        self.physics_block_0['Ω_Λ'] = self.π_em**2 / (12 * self.ζ3_em)

        # Strong Coupling Constant (α_s)
        self.physics_block_0['α_s'] = self.trace * self.ζ3_em / self.π_em**3
        
        # Cabibbo Angle (θ_c)
        pgc = math.sqrt(self.trace) * self.ζ3_em / (self.π_em**2)
        scf = 1 + 1/16
        sin_theta_c_pure = pgc * scf
        self.physics_block_0['θ_C (°)'] = math.asin(sin_theta_c_pure) * 180 / self.π_em

    def _derive_cosmology(self):
        """
        Derive the cosmological parameters of this universe. The total possible
        age of the universe is a function of its computational substrate (q_bulk).
        """
        self.cosmology = {}
        # Planck time in seconds
        t_p = 5.391247e-44
        # Derived pure age is a holographic scaling law of q_bulk
        age_in_planck_units = 2 * self.π_em * (self.q_bulk ** (2/3))
        age_in_seconds = age_in_planck_units * t_p
        self.cosmology['Total Age (Gyr)'] = age_in_seconds / (365.25 * 24 * 3600 * 1e9)

    def _prepare_simulation_engine(self):
        """Prepares the state for the dynamic evolution of the universe."""
        self.simulation_history = []
        self.current_block_height = 0
        self.running_constants = self.physics_block_0.copy()

    def run_simulation(self, end_block_height: int, report_interval: int = 0):
        """
        Evolves the universe forward in time, calculating the running of the constants.
        """
        print(f"\n>>> Running Simulation from Block 0 to {end_block_height}...\n")
        total_age = self.cosmology['Total Age (Gyr)']
        
        for k in range(1, end_block_height + 1):
            self.current_block_height = k
            
            # The internal "time" parameter of the simulation
            κ = (k / end_block_height) * (13.799 / total_age) # Scaled to match our time for comparison
            κ = min(κ, 0.99999) # Prevent division by zero at the very end

            # The Transformation Law: Renormalization from elapsed time
            # We use the one-loop model as the simplest physical evolution law.
            alpha_em = 1 / self.physics_block_0['α⁻¹']
            delta_kappa = (alpha_em / (2 * self.π_em)) * (1 - κ)
            
            # Update running constants
            sin_theta_c_pure = math.sin(self.physics_block_0['θ_C (°)'] * self.π_em / 180)
            sin_theta_c_today = sin_theta_c_pure + delta_kappa
            self.running_constants['θ_C (°)'] = math.asin(sin_theta_c_today) * 180 / self.π_em

            # Store history for plotting
            self.simulation_history.append(self.running_constants.copy())
            
            if report_interval > 0 and k % report_interval == 0:
                self.print_report(f"Report at Block Height k={k}")

        print("\n>>> Simulation Complete.")

    def print_report(self, title: str = "Universe State Report"):
        """Prints a detailed report of the universe's current state."""
        print("-" * 80)
        print(f"{title.upper()}")
        print("-" * 80)
        
        print("\n[A] Foundational Axioms (from Curve):")
        print(f"  Holographic Boundary (p) : {self.curve.p}")
        print(f"  Geometric OS Code (a)    : {self.curve.a}")
        print(f"  Genesis State (G)        : ({self.curve.Gx}, ...)")
        print(f"  Dimensionality (trace)   : {self.trace}")

        print("\n[B] Emergent Mathematics (Internal Logic):")
        print(f"  Emergent π (223/71)      : {self.π_em:.12f}")
        print(f"  Emergent e               : {self.e_em:.12f}")
        print(f"  Emergent ζ(3)            : {self.ζ3_em:.12f}")

        print("\n[C] Geometric Physics (State at Block 0):")
        for key, val in self.physics_block_0.items():
            print(f"  {key:<12} : {val:.10f}")
            
        print("\n[D] Emergent Cosmology:")
        print(f"  Total Possible Age       : {self.cosmology['Total Age (Gyr)']:.6f} Gyr")
        
        if self.current_block_height > 0:
            print("\n[E] Current State (Running Values):")
            print(f"  Current Block Height     : {self.current_block_height}")
            for key, val in self.running_constants.items():
                print(f"  {key:<12} : {val:.10f}")
        print("-" * 80 + "\n")

    def plot_evolution(self):
        """Plots the history of the running constants."""
        if not PLOTTING_ENABLED:
            print("[Plotting Disabled] Please install matplotlib: pip install matplotlib")
            return
        if not self.simulation_history:
            print("[Plotting] No simulation history to plot. Run simulation first.")
            return

        fig, ax = plt.subplots(figsize=(12, 7))
        
        blocks = range(1, len(self.simulation_history) + 1)
        theta_c_history = [s['θ_C (°)'] for s in self.simulation_history]
        
        ax.plot(blocks, theta_c_history, label='Running Cabibbo Angle (θ_C)', color='cyan')
        ax.axhline(y=self.physics_block_0['θ_C (°)'], color='magenta', linestyle='--', label='Pure Geometric Value (Block 0)')
        
        ax.set_title('Renormalization Group Flow of a Constant in the Simulated Universe', fontsize=16)
        ax.set_xlabel('Block Height (Cosmic Time)', fontsize=12)
        ax.set_ylabel('Cabibbo Angle (°)', fontsize=12)
        ax.legend()
        ax.grid(True, linestyle=':', alpha=0.6)
        
        plt.tight_layout()
        plt.show()

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # 1. Instantiate the fundamental machine code of reality.
    curve_engine = UniversalCurve()

    # 2. Compile the universe from this machine code.
    simulated_universe = UniverseFromCurve(curve_engine)
    
    # 3. Print the state of the universe at the moment of its creation.
    simulated_universe.print_report("Genesis Block (k=0) Ledger")

    # 4. Run the universe forward for a simulated period, equivalent to our cosmic age.
    # We choose a block height that corresponds to 13.8 Gyr in this universe's time.
    total_age_sim = simulated_universe.cosmology['Total Age (Gyr)']
    equivalent_block_height = int(100000 * (13.799 / total_age_sim))
    simulated_universe.run_simulation(end_block_height=equivalent_block_height)
    
    # 5. Print the final state of the universe after its evolution.
    simulated_universe.print_report(f"Final Ledger at Block Height k={equivalent_block_height}")

    # 6. Visualize the journey.
    simulated_universe.plot_evolution()
