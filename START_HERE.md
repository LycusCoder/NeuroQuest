# 🎮 START HERE - Medieval Explorer

Selamat datang di **Medieval Explorer**! 

Game 3D santai jalan-jalan dengan tema medieval. ✨

---

## 🚀 Mulai Dalam 3 Langkah

### 1️⃣ Install Godot Engine
Download dari: **https://godotengine.org/download**
- Pilih versi **4.2+** (Standard, bukan Mono)
- Extract dan jalankan

### 2️⃣ Import Project
- Buka Godot
- Klik **"Import"**
- Pilih folder `/app` (yang berisi file `project.godot`)
- Klik **"Import & Edit"**

### 3️⃣ Play!
- Tekan **F5** atau klik tombol Play ▶️
- Tunggu 5-10 detik (world generation)
- Mulai jalan-jalan! 🎉

---

## 🎯 Kontrol Game

```
W / A / S / D    →  Bergerak
Mouse            →  Lihat sekeliling  
ESC              →  Lepas/tangkap mouse
Shift (optional) →  Lari lebih cepat
```

---

## 📖 Dokumentasi Lengkap

Pilih panduan sesuai kebutuhan:

### 🏃 Quick Start
➡️ **[QUICKSTART.md](QUICKSTART.md)** - 5 menit setup

### 📚 User Manual
➡️ **[USER_GUIDE.md](USER_GUIDE.md)** - Panduan lengkap bermain & customize

### 🔧 Setup Detail
➡️ **[SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md)** - Instalasi platform-specific

### 💻 Technical Docs
➡️ **[DEVELOPMENT_NOTES.md](DEVELOPMENT_NOTES.md)** - Architecture & code

### 📊 Project Overview
➡️ **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Complete project info

### 🎮 Game Info
➡️ **[README_GAME.md](README_GAME.md)** - About the game

---

## ❓ Troubleshooting Cepat

**Game lambat?**
→ Kurangi world size: Edit `WorldGenerator` → `World Size` dari 20 ke 10

**World hitam?**
→ Tunggu 5-10 detik, atau restart game (F5)

**Mouse tidak bekerja?**
→ Tekan ESC untuk toggle mouse mode

**Lebih banyak solusi:** Lihat [USER_GUIDE.md](USER_GUIDE.md#-troubleshooting)

---

## 🛠️ Quick Customization

### Ukuran World
```
Godot Editor → scenes/main.tscn → WorldGenerator node
→ World Size: 10 (small), 20 (default), 30 (large)
```

### Kecepatan Player
```
scripts/player.gd → var speed = 5.0
→ Ubah ke 8.0 untuk lebih cepat
```

### Sensitivitas Mouse
```
scripts/player.gd → var mouse_sensitivity = 0.003
→ Ubah ke 0.005 untuk lebih sensitif
```

**Panduan lengkap:** [USER_GUIDE.md](USER_GUIDE.md#️-customization-guide)

---

## 🎨 Fitur Game

✅ Procedural world generation (400 tiles)
✅ 200+ medieval 3D assets
✅ Third-person camera
✅ Smooth controls (WASD + Mouse)
✅ Dynamic lighting & shadows
✅ Cross-platform (Windows, Linux, macOS, Web)

---

## 📦 Export Game

Untuk membuat file executable:

1. **Project** → **Export**
2. Pilih platform (Windows / Linux / Web)
3. Download templates (jika diminta)
4. **Export!**

**Detailed guide:** [SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md#export-game)

---

## 🌟 What's Next?

Setelah main game:

1. ✅ **Customize** - Ubah world size, speed, dll
2. ✅ **Export** - Buat executable untuk teman
3. ✅ **Modify** - Tambah fitur baru (lihat enhancement ideas)
4. ✅ **Learn** - Study code untuk learn Godot

**Ideas untuk enhance:** [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md#-future-enhancement-ideas)

---

## 📁 File Structure (Simple)

```
/app/
├── project.godot        ← Main project file
├── scenes/              ← Game scenes
│   ├── main.tscn       
│   └── player.tscn     
├── scripts/             ← GDScript code
│   ├── player.gd       
│   └── world_generator.gd
└── addons/              ← 3D assets (200+)
```

---

## 🎓 Perfect For

- ✅ Relaxing exploration
- ✅ Learning Godot Engine
- ✅ Base untuk game project
- ✅ Quick medieval world generator
- ✅ Walking simulator fans

---

## 📞 Need Help?

1. Check **[USER_GUIDE.md](USER_GUIDE.md)** - most comprehensive
2. Check **[QUICKSTART.md](QUICKSTART.md)** - quick answers
3. Check Godot docs: https://docs.godotengine.org/
4. Ask Godot community: https://godotengine.org/community

---

## 🎉 Ready?

**Tekan F5 dan mulai explore! 🏰**

Enjoy your medieval adventure! ✨

---

*Game dibuat dengan ❤️ menggunakan Godot Engine & KayKit Medieval Hexagon Pack*
