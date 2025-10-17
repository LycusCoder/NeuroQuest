# 🎉 What's New - Medieval Explorer v1.1

## ✨ Latest Updates

### 🆕 Settings Menu with COG Icon
**Press ESC to open the new settings menu!**

- **Icon:** ⚙️ COG wheel in title bar
- **Location:** Accessible anytime with ESC key
- **Features:** Full customization of game experience

---

## 🎮 New Features

### 1. Character Selection System
**Choose your explorer type!**

**Available Characters:**
- ⚔️ **Knight** - Balanced warrior (Silver/Gray)
  - Visual: Gray metallic appearance
  - Style: Traditional medieval knight

- 🔮 **Mage** - Mystical explorer (Purple)
  - Visual: Purple robed appearance
  - Style: Magical practitioner

- 🏹 **Archer** - Swift ranger (Green)
  - Visual: Green forest appearance
  - Style: Agile woodsman

**How to Use:**
1. Press **ESC** to open settings
2. Go to **"Karakter"** tab
3. Click on character icon
4. Character changes instantly!
5. Settings auto-saved

---

### 2. Gameplay Customization
**Fine-tune your experience!**

**Walk Speed:**
- Range: 3.0 to 12.0
- Default: 5.0
- Control: Slider with real-time preview
- Effect: Immediate on apply

**Sprint Speed:**
- Range: 6.0 to 20.0
- Default: 10.0
- Control: Slider with real-time preview
- Effect: Hold Shift to sprint

**Mouse Sensitivity:**
- Range: 0.001 to 0.010
- Default: 0.003
- Control: Precise slider
- Effect: Camera rotation speed

---

### 3. Graphics Settings
**Optimize for your system!**

**Shadows:**
- Toggle: On/Off
- Default: On
- Effect: Instant toggle of all shadows
- Performance: ~20% FPS boost when off

**World Size:**
- Range: 10 to 30 tiles
- Default: 20 tiles
- Effect: Requires game restart
- Note: Larger = longer load, more exploration

---

### 4. Settings Persistence
**Your preferences remember!**

**What's Saved:**
- ✅ Character selection
- ✅ Walk & sprint speeds
- ✅ Mouse sensitivity
- ✅ Shadow preference
- ✅ World size preference

**Storage:**
- Location: `user://settings.cfg`
- Format: ConfigFile (Godot native)
- Auto-load: On game start
- Auto-save: When you apply settings

---

## 🛠️ Enhanced Features

### Sprint System
**Hold Shift to run faster!**

- **Default Sprint Speed:** 10.0 (2x walk speed)
- **Customizable:** Yes, via settings
- **Visual Feedback:** Smooth speed transition
- **Controls:** Hold Shift + WASD

### UI Updates
**Better information display!**

- ✅ Updated controls info with Shift key
- ✅ Settings menu shortcut (ESC + ⚙️ icon)
- ✅ Real-time value display on sliders
- ✅ Current character indicator
- ✅ Clear tab organization

---

## 📚 Documentation Updates

### New Documentation Structure

**Phase Documentation:**
```
/app/docs/phases/
├── phase_1_project_setup.md
├── phase_2_world_generation.md
├── phase_3_player_controls.md
├── phase_4_ui_settings.md
└── phase_5_documentation.md
```

**Documentation Index:**
- `/app/docs/README.md` - Complete documentation index
- Organized by user type (users, developers)
- Clear navigation paths
- Phase-by-phase implementation guide

**New Docs:**
- ✅ `WHATS_NEW.md` - This file!
- ✅ Phase documents (5 detailed files)
- ✅ Documentation index
- ✅ Updated all existing docs

---

## 🎯 Controls Summary

### Updated Control Scheme

| Key | Action | Notes |
|-----|--------|-------|
| **W** | Move Forward | - |
| **S** | Move Backward | - |
| **A** | Move Left | - |
| **D** | Move Right | - |
| **Shift** | Sprint | 🆕 Hold for faster movement |
| **Mouse** | Look Around | Configurable sensitivity |
| **ESC** | Settings Menu | 🆕 Open customization panel |

---

## 💡 Tips & Tricks

### Character Selection
- **Experiment!** Try all characters to find your favorite
- **Visual Variety:** Each character has distinct color
- **No Stats:** Currently cosmetic only (future stats planned)

### Speed Settings
- **Too Slow?** Increase walk speed to 7-8
- **Too Fast?** Decrease to 3-4 for cinematic feel
- **Sprint:** Set 2-3x your walk speed for good contrast

### Mouse Sensitivity
- **Default (0.003)** works for most people
- **FPS Players:** Try 0.005-0.007 for faster look
- **Casual:** Try 0.001-0.002 for slower, more controlled

### Performance
- **Low FPS?** Turn off shadows for instant boost
- **Fast Load?** Reduce world size to 10-15
- **Best Experience:** Keep shadows on with world size 20

---

## 🔄 Migration from v1.0

**Nothing to do!** Updates are automatic:

1. **Settings:** Will use defaults first time
2. **Character:** Starts as Knight
3. **Gameplay:** Same as before until you change
4. **Controls:** ESC now opens settings instead of just releasing mouse

**Note:** Press ESC twice if you want to release mouse (once for menu, click outside + ESC to release)

---

## 🐛 Bug Fixes

### Fixed in v1.1
- ✅ Mouse capture now works with settings menu
- ✅ Player methods support dynamic speed changes
- ✅ Settings properly apply to both player controller versions
- ✅ Character colors render correctly
- ✅ Shadow toggle works immediately

---

## 📊 Technical Changes

### New Files Added
```
scenes/settings_menu.tscn       (217 lines)
scripts/settings_menu.gd        (245 lines)
docs/phases/*.md                (5 files, ~39 KB)
docs/README.md                  (Documentation index)
WHATS_NEW.md                    (This file)
```

### Modified Files
```
scenes/main.tscn                (Added settings menu)
scenes/main_improved.tscn       (Added settings menu)
scenes/ui.tscn                  (Updated controls text)
scripts/player.gd               (Added set_speeds, _is_player)
scripts/enhanced_player.gd      (Added set_speeds, _is_player)
README.md                       (Updated features & controls)
```

### Code Additions
- **Settings System:** ~250 lines
- **Player Integration:** ~20 lines
- **UI Updates:** ~10 lines
- **Documentation:** ~25,000 words

---

## 🚀 What's Next?

### Planned Features (Future)
- [ ] Audio settings (music & SFX volume)
- [ ] Key rebinding
- [ ] Character stats (speed multipliers per character)
- [ ] More characters (Warrior, Ranger, Wizard)
- [ ] Graphics quality presets
- [ ] FOV slider
- [ ] Language selection

### Requested Features
Have ideas? Document them and implement incrementally!

---

## 🎓 How to Use New Features

### Quick Start with Settings

1. **Launch Game**
   - Press F5 in Godot
   - Wait for world generation

2. **Open Settings**
   - Press **ESC** key
   - Settings menu appears

3. **Choose Character**
   - Click **"Karakter"** tab
   - Click character icon
   - See instant color change

4. **Adjust Speed**
   - Click **"Gameplay"** tab
   - Move sliders
   - See values update

5. **Apply Settings**
   - Click **"Terapkan"** button
   - Settings saved automatically
   - Close with ESC or button

---

## 📞 Support

### Common Questions

**Q: How do I open settings?**
A: Press the **ESC** key anytime during gameplay.

**Q: Why can't I see my character change?**
A: You're in third-person view. The character capsule changes color - look at your player model.

**Q: Settings not saving?**
A: Make sure to click "Terapkan" (Apply) before closing the menu.

**Q: Game too slow after settings?**
A: Open settings, click "Reset ke Default" to restore original values.

**Q: Where are settings stored?**
A: In `user://settings.cfg` (Godot user data folder, persistent across sessions).

---

## 🎉 Enjoy!

**Medieval Explorer v1.1** is now more customizable than ever!

- ⚙️ Open settings with **ESC**
- 🎮 Choose your character
- 🏃 Adjust your speed
- 🎨 Optimize graphics
- 💾 Save your preferences

**Happy Exploring! 🏰✨**

---

*Last Updated: 2025*
*Version: 1.1*
*Status: Production Ready ✅*
