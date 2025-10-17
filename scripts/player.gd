extends CharacterBody3D

# Player movement settings
var speed = 5.0
var walk_speed = 5.0
var sprint_speed = 10.0
var jump_velocity = 4.5
var mouse_sensitivity = 0.003
var camera_min_angle = -45.0
var camera_max_angle = -10.0

# Get the gravity from the project settings
var gravity = ProjectSettings.get_setting("physics/3d/default_gravity")

@onready var camera_pivot = $CameraPivot
@onready var camera = $CameraPivot/Camera3D

func _ready():
	# Capture mouse
	Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)

func _is_player():
	# Helper method for settings menu to find player
	return true

func set_speeds(walk: float, sprint: float):
	# Called by settings menu
	walk_speed = walk
	sprint_speed = sprint
	speed = walk

func _input(event):
	if event is InputEventMouseMotion:
		# Rotate player body left/right
		rotate_y(-event.relative.x * mouse_sensitivity)
		
		# Rotate camera up/down
		var camera_rotation = camera_pivot.rotation.x
		camera_rotation -= event.relative.y * mouse_sensitivity
		camera_rotation = clamp(camera_rotation, deg_to_rad(camera_min_angle), deg_to_rad(camera_max_angle))
		camera_pivot.rotation.x = camera_rotation
	
	if event.is_action_pressed("ui_cancel"):
		# Release mouse with ESC key
		if Input.get_mouse_mode() == Input.MOUSE_MODE_CAPTURED:
			Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)
		else:
			Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)

func _physics_process(delta):
	# Add gravity
	if not is_on_floor():
		velocity.y -= gravity * delta
	
	# Get input direction
	var input_dir = Input.get_vector("move_left", "move_right", "move_forward", "move_backward")
	
	# Calculate movement direction relative to player rotation
	var direction = (transform.basis * Vector3(input_dir.x, 0, input_dir.y)).normalized()
	
	if direction:
		velocity.x = direction.x * speed
		velocity.z = direction.z * speed
	else:
		velocity.x = move_toward(velocity.x, 0, speed)
		velocity.z = move_toward(velocity.z, 0, speed)
	
	move_and_slide()
	
	# Keep player on ground level minimum
	if position.y < 0:
		position.y = 0
