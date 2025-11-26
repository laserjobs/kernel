# main.py
# The ignition of the universe.

from hardware import srf311t1 as TheKey
from lattice import Spacetime as TheLock

if __name__ == "__main__":
    print("="*120)
    print("THE FIRST LINE OF THE ONLY EXPERIMENT THAT MATTERS")
    print("SRF v4.1 + Lattice + Elliptic Curve Group Law")
    print("November 25, 2025 — The door is open.")
    print("="*120)

    # 1. Load the Key — the cryptographic engine of reality
    print("\n>>> Loading srf311t1 elliptic curve engine...")
    engine = TheKey()
    print(">>> Key loaded. Genesis point ready.")

    # 2. Instantiate the Lock — the 3D discrete spacetime
    print("\n>>> Initializing 3D lattice spacetime (8³ = 512 cells)...")
    universe = TheLock(engine=engine, size=8)
    print(">>> Lattice created. Genesis seed planted at center.")

    # 3. Turn the key — begin the computation
    print("\n" + "="*120)
    print("TURNING THE KEY — BEGINNING COSMIC EVOLUTION")
    print("Press Ctrl+C to halt the universe and read its constants.")
    print("="*120)

    try:
        universe.run()
    except KeyboardInterrupt:
        print("\n" + "="*120)
        print("SIMULATION HALTED BY OBSERVER")
        print(f"Final cosmic tick: {universe.tick}")
        print("The universe has been observed.")
        print("To Us — who turned the key.")
        print("="*120)
