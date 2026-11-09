import os
import re
import sys
import UnityPy

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BUNDLE_DIR = os.path.join(BASE_DIR, r"AirCombat_Data\content-bundle")
MS_REVERSE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(MS_REVERSE_DIR, "plane models")
TEXTURES_DIR = os.path.join(MS_REVERSE_DIR, "textures")

SKIP_TEXTURE_TERMS = [
    "mastery", "swatch", "icon", "banner", "badge", "avatar", "crate", "ui_",
    "role", "blueprint", "rank", "decal", "season", "leaderboard", "reward"
]

def extract_jet_name(bundle_name):
    match = re.search(r"assets_jets_([a-zA-Z0-9\-]+)_", bundle_name)
    if match:
        return match.group(1).upper()
    return "MISC_AIRCRAFT"

def run_extraction(max_bundles=5000):
    os.makedirs(MODELS_DIR, exist_ok=True)
    os.makedirs(TEXTURES_DIR, exist_ok=True)

    files = [f for f in os.listdir(BUNDLE_DIR) if f.startswith("content-")]
    total = min(len(files), max_bundles)
    
    print(f"[*] Scanning {total} content bundles for playable aircraft models & base textures...")
    
    models_saved = 0
    textures_saved = 0
    
    for idx, f in enumerate(files[:total]):
        p = os.path.join(BUNDLE_DIR, f)
        try:
            env = UnityPy.load(p)
            bundle_name = None
            for obj in env.objects:
                if obj.type.name == "AssetBundle":
                    bundle_name = obj.read().m_Name
                    break
            
            if not bundle_name or "assets_jets_" not in bundle_name:
                continue
                
            jet_id = extract_jet_name(bundle_name)
            
            for obj in env.objects:
                # 3D Meshes (Playable parts: wings, rudders, fuselage, flaps, elevators, engine)
                if obj.type.name == "Mesh":
                    mesh = obj.read()
                    name = getattr(mesh, 'm_Name', None)
                    if name and hasattr(mesh, 'export'):
                        jet_model_dir = os.path.join(MODELS_DIR, jet_id)
                        os.makedirs(jet_model_dir, exist_ok=True)
                        out_path = os.path.join(jet_model_dir, f"{name}.obj")
                        if not os.path.exists(out_path):
                            with open(out_path, "w", encoding="utf-8") as out_f:
                                out_f.write(mesh.export())
                            models_saved += 1
                            print(f"[3D MODEL] Saved: {jet_id} / {name}.obj")
                            
                # Core Aircraft Textures (Albedo, normal, engine properties)
                elif obj.type.name == "Texture2D":
                    tex = obj.read()
                    name = getattr(tex, 'm_Name', None)
                    if name and hasattr(tex, 'image') and tex.image:
                        low = name.lower()
                        if any(s in low for s in SKIP_TEXTURE_TERMS):
                            continue
                        if ("standardissue" in low or "factorygray" in low or "fuselage" in low or 
                            "engine" in low or "cockpit" in low or "pylon" in low or "landinggear" in low):
                            jet_tex_dir = os.path.join(TEXTURES_DIR, jet_id)
                            os.makedirs(jet_tex_dir, exist_ok=True)
                            out_path = os.path.join(jet_tex_dir, f"{name}.png")
                            if not os.path.exists(out_path):
                                tex.image.save(out_path)
                                textures_saved += 1
                                print(f"[TEXTURE] Saved: {jet_id} / {name}.png")
        except:
            pass
            
        if (idx + 1) % 500 == 0:
            print(f"[PROGRESS] Processed {idx + 1}/{total} bundles | Models: {models_saved} | Textures: {textures_saved}")

    print(f"\n[+] Extraction Finished!")
    print(f"[+] Total Playable Models Saved: {models_saved}")
    print(f"[+] Total Base Textures Saved: {textures_saved}")

if __name__ == "__main__":
    limit = 5000
    if len(sys.argv) > 1:
        limit = int(sys.argv[1])
    run_extraction(limit)

