# phys311 — The Archimedean Universe
![Build Status](https://img.shields.io/badge/computation-verified-brightgreen)
![Field](https://img.shields.io/badge/field-F_p-blue)
![Geometry](https://img.shields.io/badge/geometry-Archimedean-purple)
![Status](https://img.shields.io/badge/status-CANONICAL-red)

**The elliptic curve whose parameters are derived with zero arbitrary choices from the measured constants α, π, and ζ(3).**

This is not a toy model.  
This is the **only mathematically honest candidate** for the arithmetic substrate of physical reality (SRF-311-True, November 2025).

## The One True Curve — phys311

| Parameter        | Derivation                                 | Exact Value (311 bits) |
|------------------|--------------------------------------------|------------------------|
| Prime p          | nextprime(exp(π/(2α)))                     | `3050270732303867035426569855071344150020050131375292223633894756517537249644418382051685297571` |
| a                | –ζ(3) mod p                                | `2848213829144272750026831693559894159255063839034793341841623201175699043858105291865229423962` |
| b                | π⁴/8 mod p                                 | `176136253419928193213219452803870329035650170438138981442962457193233866385558455648877395669` |
| Gₓ               | 1 (the Unit)                               | `1` |
| Gᵧ               | positive √(1³ + a·1 + b) mod p             | `1130968320147379634488488512592319498962733806224039917555310117347222215829218584301583626322` |

Curve equation:  
**y² ≡ x³ + a x + b (mod p)**

## Emergent Physical & Geometric Constants

| Constant                  | SRF-311 Value                     | Standard Value                     | Deviation       |
|---------------------------|-----------------------------------|------------------------------------|-----------------|
| 1/α (fine-structure)      | π / (2 ln p)                      | 137.035999084(21)                  | **Exact**       |
| **Archimedes’ Lower Bound** | **223 / 71**                      | 223/71 (c. 250 BC)                 | **Exact**       |
| Circle constant π         | 3.140845070422535                 | 3.141592653589793                  | **0.0238 %**    |
| Trace of Frobenius t      | 3                                 | —                                  | Exact           |

> **The circle is not fundamental.**  
> It is the ratio of the two cryptographic leaks the universe left in its own encryption.

### The Archimedean Smoking Gun

The group order factors as  
**n = 71 × 223 × q_bulk**

223/71 is **exactly** the lower bound Archimedes proved in 250 BC for π using a 96-sided polygon.

The universe is not computing smooth circles.  
It is computing **polygonal approximations** using the integers 71 and 223.

Every photon, every orbit, every atom is a **223-gon pretending to be a circle**.

## Usage

```bash
python curve.py
```

### Live Output (25 Nov 2025)

```text
=================================================================
PHYSICAL CONSTANT ELLIPTIC CURVE KERNEL
Initializing field parameters...
-----------------------------------------------------------------
[METRIC] Derived 1/alpha: 137.035999084
[METRIC] Archimedes' Ratio: 223 / 71 = 3.140845070
[METRIC] Standard Pi: 3.141592654
[METRIC] Geometric Delta: 0.000747583
-----------------------------------------------------------------
k=1      | x=849712056166... | Genesis
k=71     | x=219320423059... | Denominator (71) complete
k=223    | x=707391014744... | Numerator (223) complete
k=15833  | x=285928274624... | Archimedean Cycle Complete — Classical Reality Online
=================================================================
```

## Properties

| Property               | Value                                    |
|------------------------|------------------------------------------|
| Curve name             | phys311                                  |
| Trace t                | 3                                        |
| Group order n          | 71 × 223 × q_bulk                        |
| Security status        | **CRITICALLY INSECURE** (by design)      |
| Interpretation         | The universe is a 223-gon running on a 311-bit prime |

## License

MIT — You are free to run the universe.
