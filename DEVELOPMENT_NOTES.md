# Development Notes - Medieval Explorer

## Project Overview

Ini adalah game 3D walking simulator santai yang dibuat dengan Godot Engine 4.2+ menggunakan asset KayKit Medieval Hexagon Pack.

## Tech Stack

- **Engine:** Godot Engine 4.2+
- **Language:** GDScript
- **Assets:** GLTF models (200+ medieval assets)
- **Rendering:** Forward+ renderer
- **Platform:** Cross-platform (Windows, Linux, macOS, Web)

## Architecture

### Scene Structure

```
Main (Node3D)
├── WorldEnvironment
│   └── Sky (ProceduralSky)
├── DirectionalLight3D (Sun with shadows)
├── WorldGenerator (Node3D)
│   └── Generated tiles & decorations
├── Player (CharacterBody3D)
│   ├── CollisionShape3D (capsule)
│   ├── CameraPivot (Node3D)
│   │   └── Camera3D (third-person)
│   └── MeshInstance3D (player visual)
└── UI (CanvasLayer)
    └── Labels & HUD
```

### Script Components

#### 1. player.gd (Basic Version)
- WASD movement controls
- Mouse look (Y-axis rotation + camera pitch)
- Gravity simulation
- Ground collision detection

**Key Features:**
- Third-person camera follow
- Mouse capture/release with ESC
- Smooth movement with move_and_slide()

#### 2. enhanced_player.gd (Advanced Version)
- All features dari basic version
- Sprint capability (Shift key)
- Smooth acceleration/deceleration
- Visual feedback (character tilt saat bergerak)
- Better camera controls

**Improvements:**
- Lerp-based smooth movement
- Configurable speeds via @export
- Better feel overall

#### 3. world_generator.gd (Basic Version)
- Generate hexagonal grid world
- Random placement of decorations
- 5 types: tiles, buildings, trees, rocks, mountains
- Fallback system jika assets tidak ditemukan

**Algorithm:**
```
For each hex coordinate (q, r):
  1. Convert hex to world position
  2. Add base tile (grass)
  3. Random chance for decoration:
     - 5% buildings
     - 10% trees
     - 5% rocks
     - 3% mountains
```

#### 4. improved_world_generator.gd (Advanced Version)
- All features dari basic version
- Distance-based density (buildings di center, nature di edges)
- More asset variety
- Performance stats logging
- Seed support untuk reproducible worlds

**Improvements:**
```
Distance zones:
  - Center (0-30%): 12% buildings, 15% trees, 5% rocks
  - Middle (30-70%): 5% buildings, 20% trees, 5% rocks, 3% mountains
  - Outer (70-100%): 25% trees, 5% rocks, 5% mountains
```

## Hexagonal Grid System

Game menggunakan flat-top hexagonal grid dengan axial coordinates (q, r).

### Coordinate Conversion

```gdscript
func hex_to_world(q: int, r: int) -> Vector3:
    var x = hex_size * (sqrt(3) * q + sqrt(3)/2 * r)
    var z = hex_size * (3.0/2 * r)
    return Vector3(x, 0, z)
```

**Why hexagons?**
- Assets sudah designed untuk hex grid
- Natural untuk organic world layouts
- Better untuk pathfinding (6 neighbors vs 4)

## Asset Loading

Assets di-load secara dynamic dari folder:
```
res://addons/kaykit_medieval_hexagon_pack/Assets/gltf/
```

### Loading Strategy

1. **Try load GLTF:**
   ```gdscript
   if ResourceLoader.exists(path):
       var scene = load(path)
       var instance = scene.instantiate()
   ```

2. **Fallback if failed:**
   - Create procedural meshes (planes, boxes)
   - Apply simple materials
   - Ensure collision shapes exist

### Asset Categories

- `tiles/base/` - Ground tiles (grass, dirt, stone)
- `buildings/neutral/` - Houses, taverns, churches
- `decoration/nature/` - Trees, rocks, mountains
- `decoration/props/` - Misc decorations

## Camera System

Third-person camera menggunakan pivot system:

```
Player (CharacterBody3D)
  └── CameraPivot (Node3D at eye-level)
      └── Camera3D (offset behind & above)
```

**Benefits:**
- Player rotates → camera follows automatically
- Camera pitch independent dari player body
- Easy to adjust distance & angle

## Performance Considerations

### Optimization Techniques

1. **LOD (Level of Detail):**
   - Assets already low-poly optimized
   - Single 1024x1024 texture atlas

2. **Instancing:**
   - Each asset instantiated from scene
   - Godot automatically batches similar meshes

3. **Collision:**
   - Simple shapes (boxes, capsules)
   - Fallback tiles use StaticBody3D

4. **World Size:**
   - Configurable via @export
   - 20x20 = 400 tiles (good balance)
   - Larger = more load time, more memory

### Performance Tips

- Reduce `world_size` untuk devices lemah
- Disable shadows di DirectionalLight3D
- Lower texture quality in project settings
- Use Web export dengan compression

## Input System

Godot's built-in Input Map:

```
move_forward  -> W key (Physical keycode 87)
move_backward -> S key (Physical keycode 83)
move_left     -> A key (Physical keycode 65)
move_right    -> D key (Physical keycode 68)
ui_shift      -> Shift key (Physical keycode 4194325)
ui_cancel     -> ESC key (built-in)
```

## Export Configuration

Pre-configured export presets untuk:
- **Windows Desktop** (.exe)
- **Linux/X11** (.x86_64)
- **Web** (HTML5)

Settings di `export_presets.cfg`.

## Future Enhancements

Possible additions:

### Gameplay
- [ ] Minimap dengan fog of war
- [ ] Quest markers
- [ ] Interactable NPCs
- [ ] Day/night cycle
- [ ] Weather system
- [ ] Sound effects & music
- [ ] Save/load system

### Technical
- [ ] Procedural building interiors
- [ ] Chunk-based loading untuk larger worlds
- [ ] Multiplayer networking
- [ ] VR support
- [ ] Mobile touch controls

### Polish
- [ ] Character customization
- [ ] Better UI/UX
- [ ] Settings menu
- [ ] Keybinding customization
- [ ] Accessibility options

## Known Limitations

1. **No Vertical Terrain:**
   - All tiles at Y=0
   - Could add elevation system later

2. **Static World:**
   - Generated once at start
   - No runtime modifications

3. **Simple Collision:**
   - Basic shapes only
   - No detailed mesh collision

4. **No Persistence:**
   - World regenerated each run
   - No save system (yet)

## Debugging Tips

### Enable Debug Output
```gdscript
# In world_generator.gd
print("Generating tile at: ", hex_pos)
```

### View Collision Shapes
In Godot Editor:
- Debug → Visible Collision Shapes

### Performance Monitoring
In-game:
- Debug → Monitor (shows FPS, draw calls, etc)

### Common Issues

**World tidak muncul:**
- Check Output panel untuk errors
- Verify assets path di script
- Try fallback mode (comment out asset loading)

**Movement terasa janky:**
- Check frame rate (should be 60+ FPS)
- Reduce world size
- Disable shadows

**Mouse tidak kerja:**
- Check if window has focus
- Press ESC to toggle capture mode
- Check Input Map settings

## Contributing

Untuk contribute ke project:

1. Test changes di Godot Editor
2. Ensure no errors di Output panel
3. Test export untuk target platform
4. Update documentation jika perlu

## Credits

- **Assets:** Kay Lousberg (KayKit Medieval Hexagon Pack)
- **Engine:** Godot Engine Contributors
- **Developer:** [Your Name]

## License

- **Code:** MIT License (or your choice)
- **Assets:** CC0 1.0 Universal (dari KayKit)

---

**Last Updated:** 2025
**Godot Version:** 4.2+
**Project Status:** Completed MVP, ready for enhancements
