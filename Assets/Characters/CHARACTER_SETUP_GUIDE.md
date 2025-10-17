# Character Setup Guide for GameSantai

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
