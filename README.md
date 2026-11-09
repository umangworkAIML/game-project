# Air Combat Game Project

Comprehensive technical specifications, flight physics formulas, shaders, 3D articulated aircraft models, and base PBR textures for building an independent next-generation military flight combat game.

---

## Repository Structure

```text
game project/
├── AIRCOMBAT_ENGINE_ARCHITECTURE_SPEC.md          # Complete Engine, Flight Physics & Server Architecture Spec
├── AIRCOMBAT_ASSETS_SHADERS_MODELS_AND_AUDIO_SPEC.md # Shaders, 3D Rigging, Aerodynamic VFX & Audio Spec
├── Extract_Playable_Planes.py                     # Asset extraction & conversion pipeline
├── plane models/                                  # Articulated 3D aircraft models (.obj)
└── textures/                                      # PBR Albedo, Normal, Emissive & Material properties (.png)
```

---

## Technical Specifications Overview

### 1. Volume 1: Core Engine & Flight Simulation Architecture
* **Flight Dynamics & Aerodynamics:** Detailed mathematical formulations for Lift ($C_L$), Induced and Parasitic Drag ($C_D$), Angle of Attack (AoA), Mach Wave Drag, High-$G$ energy bleed, and dynamic pressure.
* **Server-Authoritative Multiplayer:** Tickrate configuration (30–60 Hz), Client Prediction, Lag Compensation, Server State Snapshots, and Anti-Cheat protocol verification.
* **Input & Camera Systems:** Velocity-vector chase cameras, FOV punch, screen shake, and decoupled aim assist.

### 2. Volume 2: Assets, Shaders, Models & Audio Engineering
* **Aircraft 3D Hierarchy & Locators:** Pivot points, articulated control surfaces (rudders, elevators, ailerons, flaps, airbrakes, swing wings, landing gear).
* **Multi-Layer Livery & Camouflage Shaders:** Complete production-ready HLSL Universal Render Pipeline (URP) shaders for 5-layer dynamic liveries.
* **Visual Effects (VFX):** Prandtl-Glauert condensation cones, wingtip vortex trails, Mach shock diamonds, and screen-space heat refraction.
* **Spatial Audio & Doppler System:** Realistic Doppler shift pitch calculations, missile warning receiver (RWR) threat priorities, and G-strain audio integration.

---

## 3D Models & Assets

The `plane models/` directory contains articulated Wavefront OBJ files organized with named polygon groups (`g submesh_n`), allowing developers to immediately rig and animate:
* Pitch Elevators / Stabilators
* Yaw Rudders & Vertical Stabilizers
* Roll Ailerons & Flaps
* Engine Nozzles & Variable Exhaust Petals
* Airbrakes & Retractable Landing Gear

The `textures/` directory contains clean, uncompressed base maps (Albedo, Normal, Emissive, Roughness/Metallic) without decorative skins or UI watermarks.

---

## Getting Started

1. **Blender / 3D DCC:** Import any `.obj` from `plane models/<aircraft>/` into Blender to inspect mesh topology, UV coordinates, and locator pivot positions.
2. **Unity / Unreal Engine:** Reference `AIRCOMBAT_ASSETS_SHADERS_MODELS_AND_AUDIO_SPEC.md` (Section 11) for the production C# locator script and HLSL shader code.
