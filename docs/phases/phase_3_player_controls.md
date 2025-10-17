# Phase 3: Player Character & Controls

**Status:** ✅ Completed

## Overview
Implementasi player character dengan third-person camera dan kontrol WASD + Mouse.

## Tasks Completed

### 1. Player Scene Structure
**File:** `scenes/player.tscn`

**Hierarchy:**
```
Player (CharacterBody3D)
├── CollisionShape3D (Capsule)
├── MeshInstance3D (Visual representation)
└── CameraPivot (Node3D)
    └── Camera3D (Third-person view)
```

### 2. Basic Player Controller
**File:** `scripts/player.gd`

**Features:**
- ✅ WASD movement
- ✅ Mouse look (Y-axis rotation + camera pitch)
- ✅ Gravity simulation
- ✅ Ground collision
- ✅ Mouse capture/release (ESC)
- ✅ Smooth movement with `move_and_slide()`

**Settings:**
- Walk speed: 5.0 units/sec
- Mouse sensitivity: 0.003
- Camera angle: -45° to -10°

### 3. Enhanced Player Controller
**File:** `scripts/enhanced_player.gd`

**Additional Features:**
- ✅ Sprint capability (Shift key)
- ✅ Smooth acceleration/deceleration
- ✅ Lerp-based movement
- ✅ Visual feedback (character tilt)
- ✅ Configurable via @export parameters

**Enhanced Settings:**
- Walk speed: 5.0 units/sec
- Sprint speed: 10.0 units/sec
- Acceleration: 10.0
- Deceleration: 15.0

### 4. Camera System
**Type:** Third-person pivot-based

**Configuration:**
- Distance: 6 units behind player
- Height: 3 units above player
- FOV: 70°
- Smooth rotation following player

### 5. Settings Integration
**Features:**
- ✅ `_is_player()` method for identification
- ✅ `set_speeds()` method for runtime adjustment
- ✅ Dynamic speed changes from settings menu
- ✅ Mouse sensitivity adjustment

## Files Created
- `/app/scenes/player.tscn`
- `/app/scripts/player.gd` (68 lines)
- `/app/scripts/enhanced_player.gd` (106 lines)

## Technical Implementation

### Movement System
```gdscript
func _physics_process(delta):
    # Gravity
    if not is_on_floor():
        velocity.y -= gravity * delta
    
    # Input
    var input_dir = Input.get_vector(
        "move_left", "move_right", 
        "move_forward", "move_backward"
    )
    
    # Direction relative to player rotation
    var direction = (transform.basis * Vector3(
        input_dir.x, 0, input_dir.y
    )).normalized()
    
    # Apply movement
    if direction:
        velocity.x = direction.x * speed
        velocity.z = direction.z * speed
    else:
        velocity.x = move_toward(velocity.x, 0, speed)
        velocity.z = move_toward(velocity.z, 0, speed)
    
    move_and_slide()
```

### Camera Control
```gdscript
func _input(event):
    if event is InputEventMouseMotion:
        # Rotate player
        rotate_y(-event.relative.x * mouse_sensitivity)
        
        # Rotate camera pitch
        var camera_rotation = camera_pivot.rotation.x
        camera_rotation -= event.relative.y * mouse_sensitivity
        camera_rotation = clamp(
            camera_rotation, 
            deg_to_rad(camera_min_angle),
            deg_to_rad(camera_max_angle)
        )
        camera_pivot.rotation.x = camera_rotation
```

### Sprint System (Enhanced)
```gdscript
is_sprinting = Input.is_action_pressed("ui_shift")
var target_speed = sprint_speed if is_sprinting else walk_speed
current_speed = lerp(current_speed, target_speed, acceleration * delta)
```

## Controls Mapping

| Input | Action |
|-------|--------|
| W | Move Forward |
| S | Move Backward |
| A | Move Left |
| D | Move Right |
| Mouse X | Rotate Character |
| Mouse Y | Camera Pitch |
| Shift | Sprint (Enhanced) |
| ESC | Settings Menu |

## Physics Configuration

**CharacterBody3D:**
- Capsule collision (radius: 0.5, height: 2.0)
- Position: (0, 1, 0) - elevated above ground

**Camera:**
- Transform: (0, 3, 6) - behind and above
- Rotation: Looking slightly down

## Testing Results

✅ **Movement:** Smooth WASD controls
✅ **Mouse Look:** Responsive camera rotation
✅ **Sprint:** Noticeable speed increase
✅ **Collision:** Proper ground detection
✅ **Camera:** No clipping through terrain
✅ **Settings:** Dynamic speed adjustment working

## Challenges & Solutions

**Challenge 1:** Player falling through world
**Solution:** Added ground check and position clamping

**Challenge 2:** Mouse too sensitive/slow
**Solution:** Configurable sensitivity with good default (0.003)

**Challenge 3:** Camera clipping
**Solution:** Positioned camera pivot at eye level (1.5 units)

**Challenge 4:** Jerky movement
**Solution:** Used lerp for smooth acceleration in enhanced version

## Comparison: Basic vs Enhanced

| Feature | Basic | Enhanced |
|---------|-------|----------|
| Movement | Single speed | Walk + Sprint |
| Acceleration | Instant | Smooth lerp |
| Feel | Responsive | Polished |
| Visual Feedback | None | Character tilt |
| Exports | Fixed values | Configurable |
| Lines of Code | 68 | 106 |

## Next Phase
→ Phase 4: UI & Settings Menu

---
**Completed:** Player character with controls
**Duration:** ~40 minutes
**Lines of Code:** ~170
**Controller Versions:** 2 (basic + enhanced)
