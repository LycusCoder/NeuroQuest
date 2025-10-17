extends Node3D

# Enhanced world generator dengan lebih banyak variasi

@export var world_size = 20
@export var seed_value = 0  # 0 = random, lainnya = fixed seed
var hex_size = 2.0
var assets_path = "res://addons/kaykit_medieval_hexagon_pack/Assets/gltf/"

func _ready():
	if seed_value > 0:
		seed(seed_value)
	else:
		randomize()
	
	generate_world()

func generate_world():
	print("🏰 Starting Medieval World Generation...")
	var start_time = Time.get_ticks_msec()
	
	var tiles_created = 0
	var decorations_created = 0
	
	# Create hexagonal grid
	for q in range(-world_size/2, world_size/2):
		for r in range(-world_size/2, world_size/2):
			var hex_pos = hex_to_world(q, r)
			
			# Add base tile
			add_base_tile(hex_pos)
			tiles_created += 1
			
			# Distance from center (for variation)
			var distance_from_center = sqrt(q*q + r*r)
			var normalized_distance = distance_from_center / (world_size / 2.0)
			
			# Random decorations with density based on distance
			var decoration_chance = randf()
			
			# More buildings near center, more nature at edges
			if normalized_distance < 0.3:  # Center area - more buildings
				if decoration_chance < 0.12:
					add_building(hex_pos)
					decorations_created += 1
				elif decoration_chance < 0.25:
					add_tree(hex_pos)
					decorations_created += 1
				elif decoration_chance < 0.30:
					add_rock(hex_pos)
					decorations_created += 1
			elif normalized_distance < 0.7:  # Middle area - mixed
				if decoration_chance < 0.05:
					add_building(hex_pos)
					decorations_created += 1
				elif decoration_chance < 0.20:
					add_tree(hex_pos)
					decorations_created += 1
				elif decoration_chance < 0.25:
					add_rock(hex_pos)
					decorations_created += 1
				elif decoration_chance < 0.28:
					add_mountain(hex_pos)
					decorations_created += 1
			else:  # Outer area - mostly nature
				if decoration_chance < 0.25:
					add_tree(hex_pos)
					decorations_created += 1
				elif decoration_chance < 0.30:
					add_rock(hex_pos)
					decorations_created += 1
				elif decoration_chance < 0.35:
					add_mountain(hex_pos)
					decorations_created += 1
	
	var end_time = Time.get_ticks_msec()
	var generation_time = (end_time - start_time) / 1000.0
	
	print("✅ World Generation Complete!")
	print("📊 Stats:")
	print("   - Tiles: ", tiles_created)
	print("   - Decorations: ", decorations_created)
	print("   - Time: ", "%.2f" % generation_time, " seconds")

func hex_to_world(q: int, r: int) -> Vector3:
	# Convert hexagonal coordinates to world position (flat-top hexagons)
	var x = hex_size * (sqrt(3) * q + sqrt(3)/2 * r)
	var z = hex_size * (3.0/2 * r)
	return Vector3(x, 0, z)

func add_base_tile(pos: Vector3):
	# Try to load actual tile model first
	var tile_variants = [
		"tiles/base/tile_grass.gltf",
		"tiles/base/tile_dirt.gltf"
	]
	
	var tile_loaded = false
	var tile_path = assets_path + tile_variants[randi() % tile_variants.size()]
	
	if ResourceLoader.exists(tile_path):
		var tile_scene = load(tile_path)
		if tile_scene:
			var tile = tile_scene.instantiate()
			tile.position = pos
			add_child(tile)
			tile_loaded = true
	
	if not tile_loaded:
		# Fallback: create hexagon-ish plane
		create_fallback_tile(pos)

func create_fallback_tile(pos: Vector3):
	var static_body = StaticBody3D.new()
	static_body.position = pos
	
	# Create hexagonal-looking mesh
	var mesh_instance = MeshInstance3D.new()
	var plane_mesh = PlaneMesh.new()
	plane_mesh.size = Vector2(hex_size * 1.8, hex_size * 1.8)
	mesh_instance.mesh = plane_mesh
	
	# Vary grass color slightly
	var color_variation = randf_range(-0.1, 0.1)
	var material = StandardMaterial3D.new()
	material.albedo_color = Color(0.3 + color_variation, 0.6 + color_variation, 0.2 + color_variation)
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
		"buildings/neutral/house_type04.gltf",
		"buildings/neutral/house_type05.gltf",
		"buildings/neutral/house_type06.gltf",
		"buildings/neutral/house_type07.gltf",
		"buildings/neutral/house_type08.gltf",
	]
	
	var building_path = assets_path + building_types[randi() % building_types.size()]
	if ResourceLoader.exists(building_path):
		var building_scene = load(building_path)
		if building_scene:
			var building = building_scene.instantiate()
			building.position = pos + Vector3(0, 0.5, 0)
			building.rotation.y = deg_to_rad(randf_range(0, 360))
			add_child(building)

func add_tree(pos: Vector3):
	var tree_types = [
		"decoration/nature/tree_single_A.gltf",
		"decoration/nature/tree_single_B.gltf",
		"decoration/nature/trees_A_small.gltf",
		"decoration/nature/trees_A_large.gltf",
		"decoration/nature/trees_B_small.gltf",
	]
	
	var tree_path = assets_path + tree_types[randi() % tree_types.size()]
	if ResourceLoader.exists(tree_path):
		var tree_scene = load(tree_path)
		if tree_scene:
			var tree = tree_scene.instantiate()
			tree.position = pos + Vector3(0, 0.5, 0)
			tree.rotation.y = deg_to_rad(randf_range(0, 360))
			add_child(tree)

func add_rock(pos: Vector3):
	var rock_types = [
		"decoration/nature/rock_single_A.gltf",
		"decoration/nature/rock_single_B.gltf",
		"decoration/nature/rock_single_C.gltf",
		"decoration/nature/rocks_A.gltf",
	]
	
	var rock_path = assets_path + rock_types[randi() % rock_types.size()]
	if ResourceLoader.exists(rock_path):
		var rock_scene = load(rock_path)
		if rock_scene:
			var rock = rock_scene.instantiate()
			rock.position = pos + Vector3(0, 0.5, 0)
			rock.rotation.y = deg_to_rad(randf_range(0, 360))
			add_child(rock)

func add_mountain(pos: Vector3):
	var mountain_types = [
		"decoration/nature/hills_A.gltf",
		"decoration/nature/hills_B.gltf",
		"decoration/nature/hills_C.gltf",
		"decoration/nature/mountain_A.gltf",
	]
	
	var mountain_path = assets_path + mountain_types[randi() % mountain_types.size()]
	if ResourceLoader.exists(mountain_path):
		var mountain_scene = load(mountain_path)
		if mountain_scene:
			var mountain = mountain_scene.instantiate()
			mountain.position = pos + Vector3(0, 0.5, 0)
			mountain.rotation.y = deg_to_rad(randf_range(0, 360))
			add_child(mountain)
