# 🏰 Medieval Explorer - Game 3D Santai Jalan-Jalan

![Godot Engine](https://img.shields.io/badge/Godot-4.2+-blue.svg)
![License](https://img.shields.io/badge/License-CC0-green.svg)

Game eksplorasi 3D santai dengan tema medieval yang dibuat menggunakan **Godot Engine** dan **KayKit Medieval Hexagon Pack**.

## 🎮 Tentang Game

**Medieval Explorer** adalah game walking simulator santai dimana kamu bisa jalan-jalan dan mengeksplorasi dunia medieval yang indah. Dunia ini dihasilkan secara procedural dengan lebih dari 200+ asset 3D termasuk bangunan, pohon, gunung, dan berbagai dekorasi medieval.

### ✨ Fitur
- 🗺️ **Procedural World Generation** - Dunia hexagonal yang unique setiap kali generate
- 👁️ **Third-Person Camera** - Kontrol kamera yang smooth dan responsif
- 🏛️ **200+ Medieval Assets** - Bangunan, pohon, batu, gunung, dan banyak lagi
- 🎨 **Low-poly Art Style** - Visual yang clean dan optimal
- ☀️ **Dynamic Lighting** - Pencahayaan realistis dengan shadows
- 🎯 **Simple Controls** - WASD + Mouse, mudah dipelajari
- ⚙️ **Settings Menu** - Customizable character, speed, dan graphics
- 🎮 **3 Playable Characters** - Knight, Mage, Archer dengan warna berbeda

## 🚀 Quick Start

### Persyaratan
- **Godot Engine 4.2+** ([Download disini](https://godotengine.org/download))
- **RAM:** 2GB minimum (4GB recommended)
- **Storage:** ~100MB

### Langkah Install
1. Download dan install Godot Engine 4.2+
2. Clone atau download repository ini
3. Buka Godot dan pilih **"Import"**
4. Navigate ke folder project dan pilih `project.godot`
5. Klik **"Import & Edit"**
6. Tekan **F5** untuk main!

📖 **Panduan lengkap:** Lihat [QUICKSTART.md](QUICKSTART.md) atau [SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md)

## 🎯 Kontrol

| Tombol | Aksi |
|--------|------|
| **W** | Maju |
| **S** | Mundur |
| **A** | Kiri |
| **D** | Kanan |
| **Shift** | Lari (Sprint) |
| **Mouse** | Lihat sekeliling |
| **ESC** | ⚙️ Menu Pengaturan |

## 📁 Struktur Project

```
/app/
├── project.godot              # Godot project config
├── scenes/
│   ├── main.tscn             # Main world scene
│   ├── player.tscn           # Player character
│   └── ui.tscn               # UI overlay
├── scripts/
│   ├── player.gd             # Player movement & camera
│   ├── world_generator.gd    # Basic world generator
│   ├── improved_world_generator.gd  # Enhanced generator
│   └── game_manager.gd       # Game state manager
├── addons/
│   └── kaykit_medieval_hexagon_pack/  # 3D Assets (200+ models)
└── README.md
```

## 🛠️ Customization

### Ubah Ukuran World
Edit `world_size` di `WorldGenerator` node:
- **10** = World kecil (cepat load)
- **20** = World medium (default)
- **30** = World besar (butuh waktu load lebih lama)

### Ubah Kecepatan Player
Di `scripts/player.gd`, ubah:
```gdscript
var speed = 5.0  # Increase untuk lebih cepat
```

### Ubah Sensitivitas Mouse
Di `scripts/player.gd`, ubah:
```gdscript
var mouse_sensitivity = 0.003  # Increase untuk lebih sensitif
```

## 📦 Export Game

Untuk membuat standalone executable:

1. Di Godot Editor: **Project → Export**
2. Pilih platform target (Windows, Linux, macOS, Web)
3. Download export templates jika belum ada
4. Klik **"Export Project"**
5. Game siap dibagikan!

Export presets sudah dikonfigurasi di `export_presets.cfg`.

## 🎨 Assets Used

The **Medieval Hexagon Pack** is a bundle of game assets that contains over **200 stylised medieval hexagonal tiles, buildings, and props!** Perfect for making RTS games, cozy village builders, or whatever hexagonal adventure you can think of.

### Contents

- **Hexagonal tiles** for roads, rivers, oceans/lakes, and coasts.
- **A ton of buildings,** including a blacksmith, lumbermill, church, tavern, market, windmill, watermill, a mine, a well, regular houses, barracks, an archery range + more. All come in **4 different colors** (blue/red/green/yellow) for versus gameplay 
- **Nature props** like trees, rocks, hills, mountains and clouds!
- **A bunch of units** (in the extra version)
- **User guide** with tips and tricks!

[![Medieval Hexagon Pack Contents](https://img.itch.zone/aW1hZ2UvMjY2ODI5MC8xNTkwNTU5OS5qcGc=/original/8LGCsA.jpg)](https://kaylousberg.itch.io/kaykit-medieval-hexagon)

### Features
- **200 Low poly optimized models**, suitable for all ranges of games, including mobile.
- **Textured** using a single gradient atlas texture (1024x1024) that can be downsampled to 128x128 for further optimization
- **Free for personal and commercial use**, no attribution required. (CC0 Licensed)
- Included files are **.FBX**, **.GLTF**, The files are compatible with pretty much any 3D game engine on the market (including **Unity, Godot, Unreal Engine, Roblox,** and more).

## More information

### Versions

By purchasing the extra version you get some additional content while also supporting me to continue creating game assets :)

More information about the extra and source version you can find on my [itch.io page](https://kaylousberg.itch.io/kaykit-medieval-hexagon)

### Join the Community

If you have any suggestions or questions, or just want to show of your project you're welcome to join the [KayKit Discord Server](https://discord.gg/JC7HGnnUqH) 

### Additional support 

Love my game assets? Help me create more by supporting me on [Patreon](https://www.patreon.com/kaylousberg/posts). Get **early access**, **vote on future packs**, and **receive a mystery character every month**.

Can't contribute financially? Simply spread the word to your gamedev friends or favorite content creators. Your support means a lot :) 


[![Support on Patreon](https://img.itch.zone/aW1nLzEyOTMyMjQ3LnBuZw==/original/Sa%2Furp.png)](https://www.patreon.com/kaylousberg/posts)

## License

Licensed under CC0 1.0 Universal, see [LICENSE.txt](LICENSE.txt) for more information.