extends CharacterBody3D

# Enhanced player controller with sprint and smooth movement

# Movement settings
@export var walk_speed = 5.0
@export var sprint_speed = 10.0
@export var acceleration = 10.0
@export var deceleration = 15.0
@export var jump_velocity = 4.5

# Camera settings
@export var mouse_sensitivity = 0.003
@export var camera_min_angle = -60.0
@export var camera_max_angle = -10.0
@export var camera_smooth_speed = 10.0

# State
var current_speed = walk_speed
var is_sprinting = false

# Physics
var gravity = ProjectSettings.get_setting("physics/3d/default_gravity")

# Nodes
@onready var camera_pivot = $CameraPivot
@onready var camera = $CameraPivot/Camera3D
@onready var mesh = $MeshInstance3D

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

func _input(event):
	if event is InputEventMouseMotion and Input.get_mouse_mode() == Input.MOUSE_MODE_CAPTURED:
		# Rotate player body left/right
		rotate_y(-event.relative.x * mouse_sensitivity)
		
		# Rotate camera up/down
		var camera_rotation = camera_pivot.rotation.x
		camera_rotation -= event.relative.y * mouse_sensitivity
		camera_rotation = clamp(camera_rotation, deg_to_rad(camera_min_angle), deg_to_rad(camera_max_angle))
		camera_pivot.rotation.x = camera_rotation
	
	# Toggle mouse capture
	if event.is_action_pressed("ui_cancel"):
		if Input.get_mouse_mode() == Input.MOUSE_MODE_CAPTURED:
			Input.set_mouse_mode(Input.MOUSE_MODE_VISIBLE)
		else:
			Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)

func _physics_process(delta):
	# Gravity
	if not is_on_floor():
		velocity.y -= gravity * delta
	
	# Sprint
	is_sprinting = Input.is_action_pressed("ui_shift")
	var target_speed = sprint_speed if is_sprinting else walk_speed
	current_speed = lerp(current_speed, target_speed, acceleration * delta)
	
	# Get input direction
	var input_dir = Input.get_vector("move_left", "move_right", "move_forward", "move_backward")
	
	# Calculate movement direction relative to player rotation
	var direction = (transform.basis * Vector3(input_dir.x, 0, input_dir.y)).normalized()
	
	# Apply movement with smooth acceleration/deceleration
	if direction:
		var accel = acceleration if velocity.length() < current_speed else deceleration
		velocity.x = lerp(velocity.x, direction.x * current_speed, accel * delta)
		velocity.z = lerp(velocity.z, direction.z * current_speed, accel * delta)
	else:
		velocity.x = lerp(velocity.x, 0.0, deceleration * delta)
		velocity.z = lerp(velocity.z, 0.0, deceleration * delta)
	
	# Apply movement
	move_and_slide()
	
	# Keep player above ground
	if position.y < 0:
		position.y = 0
	
	# Simple visual feedback - tilt mesh slightly when moving
	if mesh and direction:
		var tilt_angle = -input_dir.y * 0.05  # Slight forward/backward tilt
		mesh.rotation.x = lerp(mesh.rotation.x, tilt_angle, 5.0 * delta)
	elif mesh:
		mesh.rotation.x = lerp(mesh.rotation.x, 0.0, 5.0 * delta)
