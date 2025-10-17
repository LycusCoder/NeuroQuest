extends CanvasLayer

# References
@onready var panel = $Panel
@onready var speed_slider = $Panel/SettingsContainer/TabContainer/Gameplay/SpeedSlider
@onready var speed_value = $Panel/SettingsContainer/TabContainer/Gameplay/SpeedValue
@onready var sprint_slider = $Panel/SettingsContainer/TabContainer/Gameplay/SprintSlider
@onready var sprint_value = $Panel/SettingsContainer/TabContainer/Gameplay/SprintValue
@onready var mouse_slider = $Panel/SettingsContainer/TabContainer/Gameplay/MouseSlider
@onready var mouse_value = $Panel/SettingsContainer/TabContainer/Gameplay/MouseValue
@onready var shadows_check = $Panel/SettingsContainer/TabContainer/Graphics/ShadowsCheck
@onready var world_size_slider = $Panel/SettingsContainer/TabContainer/Graphics/WorldSizeSlider
@onready var world_size_value = $Panel/SettingsContainer/TabContainer/Graphics/WorldSizeValue
@onready var current_character_label = $Panel/SettingsContainer/TabContainer/Karakter/CurrentLabel

# Settings
var current_character = "knight"
var walk_speed = 5.0
var sprint_speed = 10.0
var mouse_sensitivity = 0.003
var shadows_enabled = true
var world_size = 20

# Player reference
var player = null

func _ready():
	# Hide panel at start
	panel.visible = false
	
	# Load settings from file if exists
	load_settings()
	
	# Find player
	call_deferred("find_player")

func find_player():
	# Find player node in scene tree
	var root = get_tree().get_root()
	for child in root.get_children():
		var found = find_player_recursive(child)
		if found:
			player = found
			break
	
	if player:
		apply_settings_to_player()

func find_player_recursive(node):
	if node.name == "Player" or node.has_method("_is_player"):
		return node
	
	for child in node.get_children():
		var found = find_player_recursive(child)
		if found:
			return found
	
	return null

func _input(event):
	if event.is_action_pressed("ui_cancel"):
		toggle_menu()
		get_viewport().set_input_as_handled()

func toggle_menu():
	panel.visible = !panel.visible
	
	if panel.visible:
		# Show menu
		Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)
		update_ui_from_settings()
	else:
		# Hide menu - return to game
		if player:
			Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)

func update_ui_from_settings():
	# Update all UI elements to match current settings
	speed_slider.value = walk_speed
	speed_value.text = "%.1f" % walk_speed
	
	sprint_slider.value = sprint_speed
	sprint_value.text = "%.1f" % sprint_speed
	
	mouse_slider.value = mouse_sensitivity
	mouse_value.text = "%.3f" % mouse_sensitivity
	
	shadows_check.button_pressed = shadows_enabled
	
	world_size_slider.value = world_size
	world_size_value.text = str(int(world_size))
	
	current_character_label.text = "Karakter saat ini: " + current_character.capitalize()

# Character selection
func _on_character_selected(character_type: String):
	current_character = character_type
	current_character_label.text = "Karakter saat ini: " + character_type.capitalize()
	
	# Apply character model
	if player:
		change_player_character(character_type)
	
	print("Character changed to: ", character_type)

func change_player_character(character_type: String):
	if not player:
		return
	
	# Find player mesh
	var mesh_node = player.get_node_or_null("MeshInstance3D")
	if not mesh_node:
		return
	
	# Change color based on character type
	var material = StandardMaterial3D.new()
	
	match character_type:
		"knight":
			material.albedo_color = Color(0.7, 0.7, 0.8)  # Silver/Gray for knight
		"mage":
			material.albedo_color = Color(0.5, 0.3, 0.8)  # Purple for mage
		"archer":
			material.albedo_color = Color(0.3, 0.7, 0.3)  # Green for archer
	
	if mesh_node.mesh:
		mesh_node.set_surface_override_material(0, material)

func _on_speed_changed(value: float):
	walk_speed = value
	speed_value.text = "%.1f" % value

func _on_sprint_changed(value: float):
	sprint_speed = value
	sprint_value.text = "%.1f" % value

func _on_mouse_changed(value: float):
	mouse_sensitivity = value
	mouse_value.text = "%.3f" % value

func _on_shadows_toggled(enabled: bool):
	shadows_enabled = enabled
	
	# Apply shadows setting immediately
	var light = get_tree().get_first_node_in_group("directional_light")
	if light and light is DirectionalLight3D:
		light.shadow_enabled = enabled

func _on_world_size_changed(value: float):
	world_size = int(value)
	world_size_value.text = str(world_size)

func _on_reset_pressed():
	# Reset to default values
	walk_speed = 5.0
	sprint_speed = 10.0
	mouse_sensitivity = 0.003
	shadows_enabled = true
	world_size = 20
	current_character = "knight"
	
	update_ui_from_settings()
	
	if player:
		change_player_character("knight")
	
	print("Settings reset to default")

func _on_apply_pressed():
	# Apply settings to player
	apply_settings_to_player()
	
	# Save settings to file
	save_settings()
	
	print("Settings applied and saved")

func apply_settings_to_player():
	if not player:
		return
	
	# Apply speed settings
	if player.has_method("set_speeds"):
		player.set_speeds(walk_speed, sprint_speed)
	elif "speed" in player:
		player.speed = walk_speed
		if "walk_speed" in player:
			player.walk_speed = walk_speed
		if "sprint_speed" in player:
			player.sprint_speed = sprint_speed
	
	# Apply mouse sensitivity
	if "mouse_sensitivity" in player:
		player.mouse_sensitivity = mouse_sensitivity
	
	print("Settings applied to player")

func _on_close_button_pressed():
	toggle_menu()

func save_settings():
	var config = ConfigFile.new()
	
	config.set_value("gameplay", "walk_speed", walk_speed)
	config.set_value("gameplay", "sprint_speed", sprint_speed)
	config.set_value("gameplay", "mouse_sensitivity", mouse_sensitivity)
	config.set_value("graphics", "shadows_enabled", shadows_enabled)
	config.set_value("graphics", "world_size", world_size)
	config.set_value("character", "current_character", current_character)
	
	var err = config.save("user://settings.cfg")
	if err != OK:
		print("Error saving settings: ", err)
	else:
		print("Settings saved successfully")

func load_settings():
	var config = ConfigFile.new()
	var err = config.load("user://settings.cfg")
	
	if err != OK:
		print("No settings file found, using defaults")
		return
	
	# Load values
	walk_speed = config.get_value("gameplay", "walk_speed", 5.0)
	sprint_speed = config.get_value("gameplay", "sprint_speed", 10.0)
	mouse_sensitivity = config.get_value("gameplay", "mouse_sensitivity", 0.003)
	shadows_enabled = config.get_value("graphics", "shadows_enabled", true)
	world_size = config.get_value("graphics", "world_size", 20)
	current_character = config.get_value("character", "current_character", "knight")
	
	print("Settings loaded successfully")
