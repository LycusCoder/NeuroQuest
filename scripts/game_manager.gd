extends Node

# Singleton untuk manage game state

var is_paused = false

func _ready():
	# Set untuk akses global
	pass

func _input(event):
	# Quick quit dengan Q (untuk development)
	if event.is_action_pressed("ui_cancel") and Input.is_key_pressed(KEY_SHIFT):
		get_tree().quit()

func toggle_pause():
	is_paused = !is_paused
	get_tree().paused = is_paused
