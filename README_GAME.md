# Medieval Explorer - Game 3D Santai Jalan-Jalan

## Deskripsi
Game eksplorasi 3D santai dengan tema medieval menggunakan KayKit Medieval Hexagon Pack. Jelajahi dunia hexagonal yang diisi dengan bangunan, pohon, gunung, dan berbagai dekorasi medieval.

## Cara Main

### Instalasi Godot Engine
1. Download Godot Engine 4.2+ dari https://godotengine.org/download
2. Extract dan jalankan Godot
3. Import project ini (pilih folder /app)

### Kontrol
- **WASD** - Bergerak (W: maju, S: mundur, A: kiri, D: kanan)
- **Mouse** - Lihat sekeliling (gerakkan mouse untuk mengontrol kamera)
- **ESC** - Lepas/tangkap cursor mouse

### Fitur
- World procedurally generated dengan 20x20 hexagonal tiles
- Third-person camera yang smooth
- Berbagai bangunan medieval (rumah, tavern, gereja, dll)
- Dekorasi alam (pohon, batu, gunung)
- Lighting dinamis dengan shadows
- Sky environment yang indah

## Struktur Project

```
/app/
├── project.godot          # File konfigurasi Godot
├── scenes/
│   ├── main.tscn         # Scene utama dunia
│   └── player.tscn       # Scene player dengan camera
├── scripts/
│   ├── player.gd         # Script kontrol player
│   └── world_generator.gd # Script generator dunia
└── addons/
    └── kaykit_medieval_hexagon_pack/  # 3D Assets
```

## Pengembangan Selanjutnya

Fitur yang bisa ditambahkan:
- [ ] Mini-map untuk navigasi
- [ ] Interaksi dengan bangunan (masuk ke dalam)
- [ ] NPC sederhana
- [ ] Musik dan sound effects
- [ ] Day/night cycle
- [ ] Weather system
- [ ] Quest system sederhana
- [ ] Inventory system
- [ ] Save/load game

## Credits
- Assets: KayKit Medieval Hexagon Pack by Kay Lousberg (CC0 License)
- Engine: Godot Engine 4.2+
