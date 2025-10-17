extends Node3D

@export var world_size = 20
var hex_size = 2.0
var assets_path = "res://addons/kaykit_medieval_hexagon_pack/Assets/gltf/"

# Asset arrays
var tile_grass = []
var buildings = []
var trees = []
var rocks = []
var mountains = []

func _ready():
	generate_world()

func generate_world():
	print("Generating medieval world...")
	
	# Create hexagonal grid
	for q in range(-world_size/2, world_size/2):
		for r in range(-world_size/2, world_size/2):
			var hex_pos = hex_to_world(q, r)
			
			# Add base tile
			add_base_tile(hex_pos)
			
			# Random decorations
			var rand = randf()
			
			if rand < 0.05:  # 5% buildings
				add_building(hex_pos)
			elif rand < 0.15:  # 10% trees
				add_tree(hex_pos)
			elif rand < 0.20:  # 5% rocks
				add_rock(hex_pos)
			elif rand < 0.23:  # 3% mountains
				add_mountain(hex_pos)
	
	print("World generation complete!")

func hex_to_world(q: int, r: int) -> Vector3:
	# Convert hexagonal coordinates to world position
	var x = hex_size * (sqrt(3) * q + sqrt(3)/2 * r)
	var z = hex_size * (3.0/2 * r)
	return Vector3(x, 0, z)

func add_base_tile(pos: Vector3):
	# Load and add grass tile
	var tile_path = assets_path + "tiles/base/tile_grass.gltf"
	var tile_loaded = false
	
	if ResourceLoader.exists(tile_path):
		var tile_scene = load(tile_path)
		if tile_scene:
			var tile = tile_scene.instantiate()
			tile.position = pos
			add_child(tile)
			tile_loaded = true
	
	if not tile_loaded:
		# Fallback: create a simple plane with collision
		var static_body = StaticBody3D.new()
		static_body.position = pos
		
		var mesh_instance = MeshInstance3D.new()
		var plane_mesh = PlaneMesh.new()
		plane_mesh.size = Vector2(hex_size * 1.8, hex_size * 1.8)
		mesh_instance.mesh = plane_mesh
		
		var material = StandardMaterial3D.new()
		material.albedo_color = Color(0.3, 0.6, 0.2)  # Green grass
		mesh_instance.set_surface_override_material(0, material)
		
		static_body.add_child(mesh_instance)
		
		# Add collision
		var collision_shape = CollisionShape3D.new()
		var box_shape = BoxShape3D.new()
		box_shape.size = Vector3(hex_size * 1.8, 0.1, hex_size * 1.8)
		collision_shape.shape = box_shape
		static_body.add_child(collision_shape)
		
		add_child(static_body)

func add_building(pos: Vector3):
	var building_types = [
		"buildings/neutral/house_type01.gltf",
		"buildings/neutral/house_type02.gltf",
		"buildings/neutral/house_type03.gltf",
		"buildings/neutral/house_type06.gltf"
	]
	
	var building_path = assets_path + building_types[randi() % building_types.size()]
	if ResourceLoader.exists(building_path):
		var building_scene = load(building_path)
		if building_scene:
			var building = building_scene.instantiate()
			building.position = pos + Vector3(0, 0.5, 0)  # Lift slightly
			building.rotation.y = randf() * PI * 2
			add_child(building)

func add_tree(pos: Vector3):
	var tree_types = [
		"decoration/nature/tree_single_A.gltf",
		"decoration/nature/tree_single_B.gltf",
		"decoration/nature/trees_A_small.gltf"
	]
	
	var tree_path = assets_path + tree_types[randi() % tree_types.size()]
	if ResourceLoader.exists(tree_path):
		var tree_scene = load(tree_path)
		if tree_scene:
			var tree = tree_scene.instantiate()
			tree.position = pos + Vector3(0, 0.5, 0)
			tree.rotation.y = randf() * PI * 2
			add_child(tree)

func add_rock(pos: Vector3):
	var rock_types = [
		"decoration/nature/rock_single_A.gltf",
		"decoration/nature/rock_single_B.gltf",
		"decoration/nature/rock_single_C.gltf"
	]
	
	var rock_path = assets_path + rock_types[randi() % rock_types.size()]
	if ResourceLoader.exists(rock_path):
		var rock_scene = load(rock_path)
		if rock_scene:
			var rock = rock_scene.instantiate()
			rock.position = pos + Vector3(0, 0.5, 0)
			rock.rotation.y = randf() * PI * 2
			add_child(rock)

func add_mountain(pos: Vector3):
	var mountain_types = [
		"decoration/nature/hills_B.gltf",
		"decoration/nature/hills_C.gltf"
	]
	
	var mountain_path = assets_path + mountain_types[randi() % mountain_types.size()]
	if ResourceLoader.exists(mountain_path):
		var mountain_scene = load(mountain_path)
		if mountain_scene:
			var mountain = mountain_scene.instantiate()
			mountain.position = pos + Vector3(0, 0.5, 0)
			mountain.rotation.y = randf() * PI * 2
			add_child(mountain)
