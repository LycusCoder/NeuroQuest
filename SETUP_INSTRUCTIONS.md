# Setup Instructions - Medieval Explorer

## Langkah-Langkah Setup

### 1. Install Godot Engine

**Windows:**
1. Download Godot 4.2+ dari https://godotengine.org/download
2. Download versi "Standard" (bukan Mono/C#)
3. Extract file ZIP
4. Jalankan `Godot_v4.x_win64.exe`

**Linux:**
1. Download Godot 4.2+ dari https://godotengine.org/download
2. Extract file
3. Beri permission executable: `chmod +x Godot_v4.x_linux.x86_64`
4. Jalankan: `./Godot_v4.x_linux.x86_64`

**macOS:**
1. Download Godot 4.2+ dari https://godotengine.org/download
2. Buka DMG file dan drag Godot ke Applications
3. Jalankan dari Applications

### 2. Import Project

1. Buka Godot Engine
2. Klik "Import" di Project Manager
3. Browse ke folder `/app` (folder yang berisi file `project.godot`)
4. Klik "Import & Edit"

### 3. Run Game

Setelah project terbuka di Godot Editor:

**Method 1 - Quick Play:**
1. Tekan **F5** atau klik tombol "Play" (▶️) di toolbar atas
2. Game akan langsung mulai

**Method 2 - Play Scene:**
1. Buka `scenes/main.tscn` dari FileSystem panel
2. Tekan **F6** atau klik "Play Scene" (🎬)

### 4. Controls

Saat game berjalan:
- **WASD** - Gerak (W: maju, S: mundur, A: kiri, D: kanan)
- **Mouse** - Putar kamera (gerakkan mouse)
- **ESC** - Lepas/tangkap cursor mouse (untuk keluar dari game)

## Troubleshooting

### Game tidak bisa dijalankan
- Pastikan Godot versi 4.2 atau lebih baru
- Cek console di bagian bawah Godot Editor untuk error messages
- Pastikan semua file assets ada di folder `addons/`

### Mouse tidak bekerja
- Tekan ESC untuk toggle mode mouse
- Pastikan window game dalam focus

### World tidak muncul / hitam
- Tunggu beberapa detik, world generation membutuhkan waktu
- Cek Output panel di Godot untuk pesan "World generation complete!"
- Jika masih hitam, coba restart game

### Frame rate rendah
1. Di Godot Editor, klik Project > Project Settings
2. Cari "Rendering" > "Quality"
3. Turunkan shadow quality atau disable shadows
4. Kurangi `world_size` di WorldGenerator (default: 20)

## Customization

### Ubah Ukuran World
1. Buka `scenes/main.tscn`
2. Pilih node "WorldGenerator"
3. Di Inspector panel, ubah nilai "World Size" (default: 20)
4. Nilai lebih kecil = world lebih kecil, load lebih cepat
5. Nilai lebih besar = world lebih luas, tapi load lebih lama

### Ubah Kecepatan Player
1. Buka `scripts/player.gd`
2. Ubah nilai `speed = 5.0` (baris 4)
3. Nilai lebih besar = bergerak lebih cepat

### Ubah Sensitivitas Mouse
1. Buka `scripts/player.gd`
2. Ubah nilai `mouse_sensitivity = 0.003` (baris 6)
3. Nilai lebih besar = mouse lebih sensitif

## Export Game

Untuk membuat executable game:

1. Di Godot Editor: Project > Export
2. Pilih platform (Windows, Linux, macOS, Web, Android)
3. Setup export template (download jika belum ada)
4. Klik "Export Project"
5. Pilih lokasi dan nama file
6. Game siap didistribusikan!

## System Requirements

**Minimum:**
- OS: Windows 7+, Linux, macOS 10.12+
- Processor: 2 GHz dual-core
- Memory: 2 GB RAM
- Graphics: OpenGL 3.3 compatible
- Storage: 100 MB

**Recommended:**
- OS: Windows 10+, Linux, macOS 11+
- Processor: 3 GHz quad-core
- Memory: 4 GB RAM
- Graphics: Dedicated GPU with Vulkan support
- Storage: 100 MB
