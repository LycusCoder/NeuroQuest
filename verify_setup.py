#!/usr/bin/env python3
"""
GameSantai Project Setup Script
Downloads and organizes open source 3D assets for Unity medieval walking experience
"""

import os
import sys
import urllib.request
import zipfile
import json
from pathlib import Path

class GameSantaiSetup:
    def __init__(self):
        self.project_root = Path("/app")
        self.assets_dir = self.project_root / "Assets"
        self.environment_dir = self.assets_dir / "Environment" / "City"
        self.characters_dir = self.assets_dir / "Characters"
        self.scripts_dir = self.assets_dir / "Scripts"
        self.scenes_dir = self.assets_dir / "Scenes"
        
    def create_folder_structure(self):
        """Create necessary folder structure for the project"""
        print("📁 Creating folder structure...")
        folders = [
            self.environment_dir,
            self.characters_dir,
            self.scripts_dir,
            self.characters_dir / "Models",
            self.characters_dir / "Animations",
            self.characters_dir / "Prefabs",
            self.environment_dir / "Materials",
            self.environment_dir / "Prefabs",
        ]
        
        for folder in folders:
            folder.mkdir(parents=True, exist_ok=True)
            # Create .meta file for Unity
            meta_file = Path(str(folder) + ".meta")
            if not meta_file.exists():
                self.create_meta_file(meta_file, "folder")
            print(f"✓ Created: {folder}")
        
        print("✓ Folder structure created successfully!\n")
        
    def create_meta_file(self, path, asset_type="folder"):
        """Create Unity .meta file for proper asset tracking"""
        import uuid
        guid = str(uuid.uuid4()).replace('-', '')
        
        if asset_type == "folder":
            meta_content = f"""fileFormatVersion: 2
guid: {guid}
folderAsset: yes
DefaultImporter:
  externalObjects: {{}}
  userData: 
  assetBundleName: 
  assetBundleVariant: 
"""
        else:
            meta_content = f"""fileFormatVersion: 2
guid: {guid}
DefaultImporter:
  externalObjects: {{}}
  userData: 
  assetBundleName: 
  assetBundleVariant: 
"""
        
        with open(path, 'w') as f:
            f.write(meta_content)
    
    def download_file(self, url, destination, description=""):
        """Download file with progress indicator"""
        try:
            print(f"📥 Downloading {description}...")
            print(f"   URL: {url}")
            
            def progress_hook(block_num, block_size, total_size):
                downloaded = block_num * block_size
                if total_size > 0:
                    percent = min(downloaded * 100 / total_size, 100)
                    sys.stdout.write(f"\r   Progress: {percent:.1f}%")
                    sys.stdout.flush()
            
            urllib.request.urlretrieve(url, destination, progress_hook)
            print(f"\n✓ Downloaded: {destination}\n")
            return True
        except Exception as e:
            print(f"\n✗ Error downloading {description}: {e}\n")
            return False
    
    def create_character_placeholder(self):
        """Create a placeholder character setup guide"""
        print("🎭 Creating character placeholder and animation setup...")
        
        # Create a README for character setup
        readme_path = self.characters_dir / "CHARACTER_SETUP_GUIDE.md"
        readme_content = """# Character Setup Guide for GameSantai

## Menggunakan Mixamo untuk Free Character & Animations

### Step 1: Download Character
1. Kunjungi https://www.mixamo.com (perlu login dengan Adobe account - free)
2. Pilih character yang sesuai (contoh: "Peasant Man" atau "Knight")
3. Download dengan format: FBX for Unity (.fbx)
4. Extract ke: Assets/Characters/Models/

### Step 2: Download Animations
Download animasi berikut dari Mixamo:
1. **Idle** - Animasi diam/berdiri
2. **Walking** - Animasi berjalan santai
3. **Running** (optional) - Animasi berlari

Format download: FBX for Unity (.fbx), Without Skin (karena sudah ada character model)

### Step 3: Import ke Unity
1. Drag & drop semua file .fbx ke folder yang sesuai di Unity
2. Character model → Assets/Characters/Models/
3. Animations → Assets/Characters/Animations/

### Alternative: Unity Asset Store
Bisa juga menggunakan free assets dari Unity Asset Store:
- "Starter Assets - Third Person Character Controller" (FREE - sudah include animations)
- Search: "medieval character free" di Asset Store

## Current Project Status
- ✓ Folder structure created
- ⏳ Waiting for character assets import
- ⏳ Scripts ready to be created

## Next Steps After Import
1. Run verify_setup.py lagi untuk membuat scripts
2. Setup Animator Controller
3. Create Player Prefab
4. Setup Camera System
"""
        
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        
        print(f"✓ Created guide: {readme_path}")
        print("\n📝 NOTE: Untuk character dan animasi, silakan gunakan:")
        print("   - Mixamo (https://www.mixamo.com) - FREE dengan Adobe login")
        print("   - Unity Asset Store - Starter Assets Third Person (FREE)")
        print()
        
    def create_scene_file(self):
        """Create 01_Medieval_City scene file"""
        print("🎬 Creating scene: 01_Medieval_City.unity...")
        
        scene_path = self.scenes_dir / "01_Medieval_City.unity"
        
        # Basic Unity scene structure
        scene_content = """%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!29 &1
OcclusionCullingSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 2
  m_OcclusionBakeSettings:
    smallestOccluder: 5
    smallestHole: 0.25
    backfaceThreshold: 100
  m_SceneGUID: 00000000000000000000000000000000
  m_OcclusionCullingData: {fileID: 0}
--- !u!104 &2
RenderSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 9
  m_Fog: 0
  m_FogColor: {r: 0.5, g: 0.5, b: 0.5, a: 1}
  m_FogMode: 3
  m_FogDensity: 0.01
  m_LinearFogStart: 0
  m_LinearFogEnd: 300
  m_AmbientSkyColor: {r: 0.212, g: 0.227, b: 0.259, a: 1}
  m_AmbientEquatorColor: {r: 0.114, g: 0.125, b: 0.133, a: 1}
  m_AmbientGroundColor: {r: 0.047, g: 0.043, b: 0.035, a: 1}
  m_AmbientIntensity: 1
  m_AmbientMode: 0
  m_SubtractiveShadowColor: {r: 0.42, g: 0.478, b: 0.627, a: 1}
  m_SkyboxMaterial: {fileID: 10304, guid: 0000000000000000f000000000000000, type: 0}
  m_HaloStrength: 0.5
  m_FlareStrength: 1
  m_FlareFadeSpeed: 3
  m_HaloTexture: {fileID: 0}
  m_SpotCookie: {fileID: 10001, guid: 0000000000000000e000000000000000, type: 0}
  m_DefaultReflectionMode: 0
  m_DefaultReflectionResolution: 128
  m_ReflectionBounces: 1
  m_ReflectionIntensity: 1
  m_CustomReflection: {fileID: 0}
  m_Sun: {fileID: 0}
  m_IndirectSpecularColor: {r: 0.18028378, g: 0.22571412, b: 0.30692285, a: 1}
  m_UseRadianceAmbientProbe: 0
--- !u!157 &3
LightmapSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 12
  m_GIWorkflowMode: 1
  m_GISettings:
    serializedVersion: 2
    m_BounceScale: 1
    m_IndirectOutputScale: 1
    m_AlbedoBoost: 1
    m_EnvironmentLightingMode: 0
    m_EnableBakedLightmaps: 1
    m_EnableRealtimeLightmaps: 0
  m_LightmapEditorSettings:
    serializedVersion: 12
    m_Resolution: 2
    m_BakeResolution: 40
    m_AtlasSize: 1024
    m_AO: 0
    m_AOMaxDistance: 1
    m_CompAOExponent: 1
    m_CompAOExponentDirect: 0
    m_ExtractAmbientOcclusion: 0
    m_Padding: 2
    m_LightmapParameters: {fileID: 0}
    m_LightmapsBakeMode: 1
    m_TextureCompression: 1
    m_ReflectionCompression: 2
    m_MixedBakeMode: 2
    m_BakeBackend: 1
    m_PVRSampling: 1
    m_PVRDirectSampleCount: 32
    m_PVRSampleCount: 512
    m_PVRBounces: 2
    m_PVREnvironmentSampleCount: 256
    m_PVREnvironmentReferencePointCount: 2048
    m_PVRFilteringMode: 1
    m_PVRDenoiserTypeDirect: 1
    m_PVRDenoiserTypeIndirect: 1
    m_PVRDenoiserTypeAO: 1
    m_PVRFilterTypeDirect: 0
    m_PVRFilterTypeIndirect: 0
    m_PVRFilterTypeAO: 0
    m_PVREnvironmentMIS: 1
    m_PVRCulling: 1
    m_PVRFilteringGaussRadiusDirect: 1
    m_PVRFilteringGaussRadiusIndirect: 5
    m_PVRFilteringGaussRadiusAO: 2
    m_PVRFilteringAtrousPositionSigmaDirect: 0.5
    m_PVRFilteringAtrousPositionSigmaIndirect: 2
    m_PVRFilteringAtrousPositionSigmaAO: 1
    m_ExportTrainingData: 0
    m_TrainingDataDestination: TrainingData
    m_LightProbeSampleCountMultiplier: 4
  m_LightingDataAsset: {fileID: 0}
  m_LightingSettings: {fileID: 0}
--- !u!196 &4
NavMeshSettings:
  serializedVersion: 2
  m_ObjectHideFlags: 0
  m_BuildSettings:
    serializedVersion: 3
    agentTypeID: 0
    agentRadius: 0.5
    agentHeight: 2
    agentSlope: 45
    agentClimb: 0.4
    ledgeDropHeight: 0
    maxJumpAcrossDistance: 0
    minRegionArea: 2
    manualCellSize: 0
    cellSize: 0.16666667
    manualTileSize: 0
    tileSize: 256
    buildHeightMesh: 0
    maxJobWorkers: 0
    preserveTilesOutsideBounds: 0
    debug:
      m_Flags: 0
  m_NavMeshData: {fileID: 0}
--- !u!1 &705507993
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  serializedVersion: 6
  m_Component:
  - component: {fileID: 705507995}
  - component: {fileID: 705507994}
  m_Layer: 0
  m_Name: Directional Light
  m_TagString: Untagged
  m_Icon: {fileID: 0}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!108 &705507994
Light:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 705507993}
  m_Enabled: 1
  serializedVersion: 10
  m_Type: 1
  m_Shape: 0
  m_Color: {r: 1, g: 0.95686275, b: 0.8392157, a: 1}
  m_Intensity: 1
  m_Range: 10
  m_SpotAngle: 30
  m_InnerSpotAngle: 21.80208
  m_CookieSize: 10
  m_Shadows:
    m_Type: 2
    m_Resolution: -1
    m_CustomResolution: -1
    m_Strength: 1
    m_Bias: 0.05
    m_NormalBias: 0.4
    m_NearPlane: 0.2
    m_CullingMatrixOverride:
      e00: 1
      e01: 0
      e02: 0
      e03: 0
      e10: 0
      e11: 1
      e12: 0
      e13: 0
      e20: 0
      e21: 0
      e22: 1
      e23: 0
      e30: 0
      e31: 0
      e32: 0
      e33: 1
    m_UseCullingMatrixOverride: 0
  m_Cookie: {fileID: 0}
  m_DrawHalo: 0
  m_Flare: {fileID: 0}
  m_RenderMode: 0
  m_CullingMask:
    serializedVersion: 2
    m_Bits: 4294967295
  m_RenderingLayerMask: 1
  m_Lightmapping: 4
  m_LightShadowCasterMode: 0
  m_AreaSize: {x: 1, y: 1}
  m_BounceIntensity: 1
  m_ColorTemperature: 6570
  m_UseColorTemperature: 0
  m_BoundingSphereOverride: {x: 0, y: 0, z: 0, w: 0}
  m_UseBoundingSphereOverride: 0
  m_UseViewFrustumForShadowCasterCull: 1
  m_ShadowRadius: 0
  m_ShadowAngle: 0
--- !u!4 &705507995
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 705507993}
  m_LocalRotation: {x: 0.40821788, y: -0.23456968, z: 0.10938163, w: 0.8754261}
  m_LocalPosition: {x: 0, y: 3, z: 0}
  m_LocalScale: {x: 1, y: 1, z: 1}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {fileID: 0}
  m_RootOrder: 1
  m_LocalEulerAnglesHint: {x: 50, y: -30, z: 0}
--- !u!1 &963194225
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  serializedVersion: 6
  m_Component:
  - component: {fileID: 963194228}
  - component: {fileID: 963194227}
  - component: {fileID: 963194226}
  m_Layer: 0
  m_Name: Main Camera
  m_TagString: MainCamera
  m_Icon: {fileID: 0}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
--- !u!81 &963194226
AudioListener:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 963194225}
  m_Enabled: 1
--- !u!20 &963194227
Camera:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 963194225}
  m_Enabled: 1
  serializedVersion: 2
  m_ClearFlags: 1
  m_BackGroundColor: {r: 0.19215687, g: 0.3019608, b: 0.4745098, a: 0}
  m_projectionMatrixMode: 1
  m_GateFitMode: 2
  m_FOVAxisMode: 0
  m_Iso: 200
  m_ShutterSpeed: 0.005
  m_Aperture: 16
  m_FocusDistance: 10
  m_FocalLength: 50
  m_BladeCount: 5
  m_Curvature: {x: 2, y: 11}
  m_BarrelClipping: 0.25
  m_Anamorphism: 0
  m_SensorSize: {x: 36, y: 24}
  m_LensShift: {x: 0, y: 0}
  m_NormalizedViewPortRect:
    serializedVersion: 2
    x: 0
    y: 0
    width: 1
    height: 1
  near clip plane: 0.3
  far clip plane: 1000
  field of view: 60
  orthographic: 0
  orthographic size: 5
  m_Depth: -1
  m_CullingMask:
    serializedVersion: 2
    m_Bits: 4294967295
  m_RenderingPath: -1
  m_TargetTexture: {fileID: 0}
  m_TargetDisplay: 0
  m_TargetEye: 3
  m_HDR: 1
  m_AllowMSAA: 1
  m_AllowDynamicResolution: 0
  m_ForceIntoRT: 0
  m_OcclusionCulling: 1
  m_StereoConvergence: 10
  m_StereoSeparation: 0.022
--- !u!4 &963194228
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 963194225}
  m_LocalRotation: {x: 0, y: 0, z: 0, w: 1}
  m_LocalPosition: {x: 0, y: 1, z: -10}
  m_LocalScale: {x: 1, y: 1, z: 1}
  m_ConstrainProportionsScale: 0
  m_Children: []
  m_Father: {fileID: 0}
  m_RootOrder: 0
  m_LocalEulerAnglesHint: {x: 0, y: 0, z: 0}
"""
        
        with open(scene_path, 'w') as f:
            f.write(scene_content)
        
        # Create meta file
        meta_path = Path(str(scene_path) + ".meta")
        self.create_meta_file(meta_path, "scene")
        
        print(f"✓ Created scene: {scene_path}\n")
    
    def create_environment_placeholders(self):
        """Create placeholder environment objects using Unity primitives"""
        print("🏛️ Creating environment placeholder guide...")
        
        guide_path = self.environment_dir / "ENVIRONMENT_SETUP.md"
        guide_content = """# Environment Setup Guide

## Placeholder Setup (Sementara)
Untuk membuat prototype cepat, gunakan Unity primitives:

### Ground/Terrain (50x50 meter)
1. Di Unity: GameObject > 3D Object > Plane
2. Scale: (5, 1, 5) - ini akan membuat 50x50 meter ground
3. Position: (0, 0, 0)
4. Rename: "Ground"

### Medieval Buildings (Placeholder)
Gunakan Unity primitives untuk sementara:
1. **Main Building**: Cube (Scale: 10, 8, 10) - Bangunan utama
2. **Tower**: Cylinder (Scale: 3, 10, 3) - Menara
3. **Walls**: Cubes (Scale: 1, 4, 10) - Tembok kota
4. **Houses**: Cubes berbagai ukuran (Scale: 5, 5, 5)

## Free Medieval Assets (Recommended)
### Option 1: Unity Asset Store
- Search: "medieval" filter by "Free"
- Recommended: "Low Poly Medieval Buildings" (FREE)

### Option 2: Sketchfab
- https://sketchfab.com/
- Search: "medieval buildings"
- Filter: Free, Downloadable
- Format: FBX for Unity

### Option 3: OpenGameArt
- https://opengameart.org/
- Search: "medieval city"
- Download FBX/OBJ files

## Materials
Untuk sementara gunakan materials standar Unity dengan warna:
- Ground: Green/Brown
- Buildings: Stone Gray
- Roofs: Dark Red/Brown
"""
        
        with open(guide_path, 'w') as f:
            f.write(guide_content)
        
        print(f"✓ Created guide: {guide_path}\n")
    
    def update_editor_build_settings(self):
        """Update EditorBuildSettings to include new scene"""
        print("⚙️ Updating Editor Build Settings...")
        
        build_settings_path = self.project_root / "ProjectSettings" / "EditorBuildSettings.asset"
        
        build_settings_content = """%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!1045 &1
EditorBuildSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 2
  m_Scenes:
  - enabled: 1
    path: Assets/Scenes/01_Medieval_City.unity
    guid: 00000000000000000000000000000001
  - enabled: 0
    path: Assets/Scenes/SampleScene.unity
    guid: 00000000000000000000000000000000
  m_configObjects: {}
"""
        
        with open(build_settings_path, 'w') as f:
            f.write(build_settings_content)
        
        print(f"✓ Updated: {build_settings_path}\n")
    
    def print_summary(self):
        """Print setup summary and next steps"""
        print("\n" + "="*70)
        print("🎮 GAMESANTAI PROJECT SETUP - PHASE 1 COMPLETE")
        print("="*70)
        print("\n✅ COMPLETED:")
        print("   ✓ Folder structure created")
        print("   ✓ Scene '01_Medieval_City.unity' created")
        print("   ✓ Setup guides created")
        print("   ✓ Project configured for Unity 6000.2.8f1")
        
        print("\n📋 NEXT STEPS:")
        print("\n1. CHARACTER ASSETS (Required):")
        print("   → Download dari Mixamo: https://www.mixamo.com")
        print("   → Atau gunakan 'Starter Assets - Third Person' dari Unity Asset Store (FREE)")
        print("   → Lihat: Assets/Characters/CHARACTER_SETUP_GUIDE.md")
        
        print("\n2. ENVIRONMENT ASSETS (Optional - bisa pakai placeholder):")
        print("   → Lihat: Assets/Environment/City/ENVIRONMENT_SETUP.md")
        print("   → Atau langsung buat dengan Unity primitives")
        
        print("\n3. SCRIPTS IMPLEMENTATION:")
        print("   → Setelah import assets, jalankan script berikutnya")
        print("   → Script akan membuat:")
        print("      - PlayerController.cs (Third Person Movement)")
        print("      - ThirdPersonCamera.cs (Camera Follow)")
        print("      - PlayerAnimator.cs (Animation Controller)")
        
        print("\n🎯 CURRENT STATUS: Task 1 Complete")
        print("   Ready untuk Task 2 (Character & Control) setelah import assets")
        print("\n" + "="*70 + "\n")
    
    def run(self):
        """Run the complete setup"""
        print("\n" + "="*70)
        print("🚀 STARTING GAMESANTAI PROJECT SETUP")
        print("="*70 + "\n")
        
        try:
            # Phase 1: Folder Structure
            self.create_folder_structure()
            
            # Phase 2: Scene Creation
            self.create_scene_file()
            
            # Phase 3: Asset Guides
            self.create_character_placeholder()
            self.create_environment_placeholders()
            
            # Phase 4: Project Configuration
            self.update_editor_build_settings()
            
            # Summary
            self.print_summary()
            
            return True
            
        except Exception as e:
            print(f"\n❌ ERROR during setup: {e}")
            import traceback
            traceback.print_exc()
            return False

if __name__ == "__main__":
    setup = GameSantaiSetup()
    success = setup.run()
    
    sys.exit(0 if success else 1)
