# 📖 User Guide - Medieval Explorer

Panduan lengkap untuk bermain dan memodifikasi Medieval Explorer.

## 🎮 Cara Bermain

### Starting the Game

1. **Launch Godot Engine**
2. **Import Project** - Pilih folder `/app`
3. **Press F5** - Atau klik tombol Play ▶️
4. **Wait** - World akan di-generate (5-10 detik)
5. **Explore!** - Mulai jalan-jalan!

### Kontrol Dasar

#### Movement
- **W** - Jalan maju
- **A** - Jalan ke kiri
- **S** - Jalan mundur
- **D** - Jalan ke kanan
- **Shift + WASD** - Sprint (lari lebih cepat) *[jika pakai enhanced_player.gd]*

#### Camera
- **Gerakkan Mouse** - Lihat sekeliling
  - Kiri/Kanan: Putar karakter
  - Atas/Bawah: Lihat ke atas/bawah
- **ESC** - Toggle mouse capture
  - Captured: Mouse mengontrol camera
  - Released: Mouse bisa klik UI/keluar

### Tips Bermain

1. **Eksplorasi Santai**
   - Tidak ada waktu atau musuh
   - Jalan-jalan dengan pace kamu sendiri
   - Enjoy the scenery!

2. **Cari Bangunan**
   - Bangunan lebih banyak di area center
   - Ada berbagai jenis: rumah, tavern, gereja, dll
   - Setiap playthrough punya layout berbeda

3. **Area Natural**
   - Bagian luar world lebih banyak pohon & gunung
   - Good untuk screenshot nature

4. **Lepas Mouse**
   - Tekan ESC untuk lepas cursor
   - Berguna kalau mau pause atau keluar

## 🛠️ Customization Guide

### Mengubah Ukuran World

**Via Godot Editor:**
1. Buka scene `scenes/main.tscn` atau `scenes/main_improved.tscn`
2. Klik node **"WorldGenerator"** di Scene tree
3. Di Inspector panel (kanan), cari property **"World Size"**
4. Ubah nilai:
   - `10` = Small world (100 tiles) - cepat, cocok untuk test
   - `15` = Medium-small (225 tiles)
   - `20` = Medium (400 tiles) - **default**, balanced
   - `25` = Medium-large (625 tiles)
   - `30` = Large (900 tiles) - banyak eksplorasi, load lebih lama

**Via Script:**
Atau edit langsung di `scripts/world_generator.gd`:
```gdscript
@export var world_size = 20  # Ubah angka ini
```

### Mengubah Kecepatan Player

**File:** `scripts/player.gd` atau `scripts/enhanced_player.gd`

```gdscript
# Basic version
var speed = 5.0  # Default walking speed

# Enhanced version
@export var walk_speed = 5.0    # Normal walking
@export var sprint_speed = 10.0  # Sprint speed (Shift)
```

**Rekomendasi:**
- `3.0` - Slow, lebih cinematic
- `5.0` - Normal (default)
- `8.0` - Fast
- `12.0` - Very fast

### Mengubah Sensitivitas Mouse

**File:** `scripts/player.gd` atau `scripts/enhanced_player.gd`

```gdscript
var mouse_sensitivity = 0.003  # Default

# Try these:
# 0.001 - Sangat lambat
# 0.002 - Lambat
# 0.003 - Normal (default)
# 0.005 - Cepat
# 0.010 - Sangat cepat
```

### Mengubah Camera Angle

**File:** `scripts/player.gd`

```gdscript
var camera_min_angle = -45.0  # Paling ke bawah
var camera_max_angle = -10.0  # Paling ke atas

# More range:
var camera_min_angle = -70.0  # Look more down
var camera_max_angle = 10.0   # Look more up
```

### Fixed Seed World

Untuk generate world yang sama setiap kali:

**File:** `scripts/improved_world_generator.gd`

```gdscript
@export var seed_value = 0  # 0 = random

# Change to any number:
@export var seed_value = 12345  # Same world every time
```

### Mengubah Decoration Density

**File:** `scripts/improved_world_generator.gd`

Di fungsi `generate_world()`, ubah percentage:

```gdscript
# Center area
if decoration_chance < 0.12:  # Buildings (default 12%)
    add_building(hex_pos)
elif decoration_chance < 0.25:  # Trees (default 13%)
    add_tree(hex_pos)

# Increase buildings to 20%:
if decoration_chance < 0.20:  # More buildings!
    add_building(hex_pos)
```

### Switching Player Controllers

Game punya 2 versi player controller:

**Basic Version** (`player.gd`):
- Simple WASD movement
- Mouse look
- One speed only

**Enhanced Version** (`enhanced_player.gd`):
- WASD + Sprint
- Smooth acceleration
- Better feel

**To Switch:**
1. Buka `scenes/player.tscn`
2. Pilih root node "Player"
3. Di Inspector, cari property "Script"
4. Klik dan pilih script yang diingin:
   - `res://scripts/player.gd` (basic)
   - `res://scripts/enhanced_player.gd` (enhanced)

### Switching World Generators

Game punya 2 versi world generator:

**Basic Version** (`world_generator.gd`):
- Random placement
- Same density everywhere

**Improved Version** (`improved_world_generator.gd`):
- Distance-based placement
- More variety
- Stats logging

**To Switch:**

**Method 1 - Change Main Scene:**
Di Godot: Project → Project Settings → Application → Run
- `res://scenes/main.tscn` (basic generator)
- `res://scenes/main_improved.tscn` (improved generator)

**Method 2 - Edit Scene:**
1. Buka `scenes/main.tscn`
2. Pilih node "WorldGenerator"
3. Di Inspector, ubah Script ke:
   - `res://scripts/world_generator.gd` (basic)
   - `res://scripts/improved_world_generator.gd` (improved)

## 🎨 Visual Customization

### Mengubah Sky Color

**File:** `scenes/main.tscn`

Di Inspector untuk node "Sky" → "Sky Material":
```
Sky Top Color: Blue tinggi
Sky Horizon Color: Warna horizon
Ground Horizon Color: Warna ground di horizon
Ground Bottom Color: Ground di bawah
```

### Mengubah Lighting

**File:** `scenes/main.tscn`

Pilih node "DirectionalLight3D", ubah:
- **Light Energy:** `1.0` (default) - increase untuk lebih terang
- **Light Color:** Default putih - bisa diubah untuk mood berbeda
  - Kuning muda: Sunset vibe
  - Biru muda: Night/moon vibe
- **Shadow Enabled:** On/Off - disable untuk performa lebih baik

### Disable Shadows (Performance Boost)

1. Pilih "DirectionalLight3D"
2. Uncheck **"Shadow Enabled"**
3. FPS akan naik significantly

## 🚀 Export & Sharing

### Membuat Executable

1. **Open Export Menu:**
   - Project → Export
   - Atau: Shift + Ctrl + E

2. **Select Platform:**
   - Windows Desktop (.exe)
   - Linux/X11 (.x86_64)
   - Web (HTML5)

3. **Download Templates:**
   - First time: Klik "Manage Export Templates"
   - Download versi yang sesuai dengan Godot version

4. **Export:**
   - Klik platform
   - Klik "Export Project"
   - Pilih lokasi & nama file
   - Done!

### Export Tips

**For Best File Size:**
- Di export settings, enable "Embed PCK"
- Enable "Optimize for Size"
- Compress textures

**For Best Performance:**
- Use 64-bit architecture
- Enable texture compression (S3TC untuk desktop)
- Optimize mesh LODs

**For Web:**
- Will be larger file size
- Needs web server to run
- Some browsers may have issues

### Sharing Your Game

After export:

**Windows:**
- Share the `.exe` file
- Atau zip dengan DLL files kalau ada

**Linux:**
- Share the `.x86_64` file
- Chmod +x for executable permission

**Web:**
- Upload ke web hosting
- Atau use itch.io for easy hosting

## ❓ Troubleshooting

### Game Lambat / Low FPS

**Solutions:**
1. Kurangi `world_size` (20 → 15 atau 10)
2. Disable shadows di DirectionalLight3D
3. Di Project Settings:
   - Rendering → Quality → Lower settings
4. Close aplikasi lain

### World Tidak Muncul / Hitam

**Solutions:**
1. Tunggu 5-10 detik (generation time)
2. Check Output panel di Godot untuk errors
3. Verify assets ada di folder `addons/`
4. Try restart game (F5)

### Mouse Tidak Bekerja

**Solutions:**
1. Click di window game untuk focus
2. Tekan ESC untuk toggle mouse capture
3. Check Input Map settings di Project Settings

### Player Jatuh Terus Kebawah

**Solutions:**
1. Check collision shapes di tiles
2. Verify player punya CollisionShape3D
3. Check ground position (should be Y=0)

### Tidak Bisa Export

**Solutions:**
1. Download export templates:
   - Editor → Manage Export Templates
2. Check Godot version matches template version
3. Ensure no errors di Output panel
4. Try different export platform

### Assets Tidak Muncul

**Solutions:**
1. Verify folder structure:
   ```
   /app/addons/kaykit_medieval_hexagon_pack/Assets/gltf/
   ```
2. Check Output panel untuk asset loading errors
3. Fallback mode akan create simple shapes

## 🎓 Advanced Topics

### Adding New Assets

1. Put GLTF files di appropriate folder
2. Update arrays di world generator:
   ```gdscript
   var building_types = [
       "buildings/neutral/house_type01.gltf",
       "buildings/neutral/YOUR_NEW_BUILDING.gltf"  # Add here
   ]
   ```

### Creating New Decorations

1. Create new function in world generator:
   ```gdscript
   func add_flower(pos: Vector3):
       var flower_path = assets_path + "decoration/flower.gltf"
       # ... loading code
   ```

2. Call in `generate_world()`:
   ```gdscript
   elif rand < 0.35:  # 5% flowers
       add_flower(hex_pos)
   ```

### Modifying Camera Distance

**File:** `scenes/player.tscn`

1. Select "Camera3D" node
2. In Inspector, change "Transform" → "Position":
   - Z value: Distance behind player
     - `4.0` - Close
     - `6.0` - Default
     - `10.0` - Far
   - Y value: Height above player
     - `2.0` - Low
     - `3.0` - Default
     - `5.0` - High

### Adding Jump

Add to player script:

```gdscript
func _physics_process(delta):
    # ... existing code ...
    
    # Jump
    if Input.is_action_just_pressed("ui_accept") and is_on_floor():
        velocity.y = jump_velocity
```

Then add input in Project Settings:
- Input Map → Add "ui_accept" → Space key

## 📚 Resources

### Learning More

- **Godot Docs:** https://docs.godotengine.org/
- **GDScript Tutorial:** https://gdscript.com/
- **Godot Discord:** https://discord.gg/godot

### Asset Packs

- **KayKit Website:** https://kaylousberg.com/
- **Itch.io:** https://kaylousberg.itch.io/
- **More Free Assets:** Search "CC0 game assets"

### Community

- **r/godot** - Reddit community
- **Godot Forums** - Official forums
- **YouTube** - Many Godot tutorials

## 💡 Ideas for Enhancement

Kalau mau develop lebih lanjut:

1. **Gameplay:**
   - Add collectibles
   - Add NPCs to talk to
   - Quest system
   - Achievement system

2. **Visual:**
   - Day/night cycle
   - Weather (rain, fog)
   - Particle effects
   - Post-processing

3. **Audio:**
   - Background music
   - Footstep sounds
   - Ambient nature sounds

4. **QoL:**
   - Settings menu
   - Save/load system
   - Minimap
   - Teleport points

## 📞 Support

Issues? Ideas?
- Check `DEVELOPMENT_NOTES.md` for technical details
- Check Godot documentation
- Ask di Godot community forums

---

**Enjoy exploring your medieval world! 🏰✨**
