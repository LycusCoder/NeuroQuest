using UnityEngine;
using UnityEditor;

/// <summary>
/// Editor script to create Player and Camera setup automatically
/// Run from Unity Editor: Tools > GameSantai > Create Player Setup
/// </summary>
public class GameSantaiEditorSetup : MonoBehaviour
{
#if UNITY_EDITOR
    [MenuItem("Tools/GameSantai/Create Player Setup")]
    public static void CreatePlayerSetup()
    {
        // Create Ground
        GameObject ground = CreateGround();
        
        // Create Player
        GameObject player = CreatePlayer();
        
        // Create Camera
        GameObject camera = CreateCamera(player);
        
        // Create Lighting
        GameObject light = CreateDirectionalLight();
        
        Debug.Log("✓ Player setup created successfully!");
        Debug.Log("  - Ground: 50x50 meter plane");
        Debug.Log("  - Player: Capsule with CharacterController and scripts");
        Debug.Log("  - Camera: Third Person Camera with orbit control");
        Debug.Log("  - Light: Directional light for scene");
        Debug.Log("\nPress Play to test the walking experience!");
        
        Selection.activeGameObject = player;
    }
    
    static GameObject CreateGround()
    {
        // Check if ground already exists
        GameObject existingGround = GameObject.Find("Ground");
        if (existingGround != null)
        {
            Debug.Log("Ground already exists, skipping...");
            return existingGround;
        }
        
        // Create plane (10x10 units = 100 square units, scale 5 = 50x50 meters)
        GameObject ground = GameObject.CreatePrimitive(PrimitiveType.Plane);
        ground.name = "Ground";
        ground.transform.position = Vector3.zero;
        ground.transform.localScale = new Vector3(5, 1, 5); // 50x50 meters
        
        // Add material
        Material groundMat = new Material(Shader.Find("Universal Render Pipeline/Lit"));
        groundMat.color = new Color(0.3f, 0.5f, 0.3f); // Green-ish
        ground.GetComponent<Renderer>().material = groundMat;
        
        // Set layer to ground
        ground.layer = LayerMask.NameToLayer("Default");
        
        Debug.Log("✓ Created Ground (50x50 meters)");
        return ground;
    }
    
    static GameObject CreatePlayer()
    {
        // Check if player already exists
        GameObject existingPlayer = GameObject.FindGameObjectWithTag("Player");
        if (existingPlayer != null)
        {
            Debug.Log("Player already exists, skipping...");
            return existingPlayer;
        }
        
        // Create capsule as placeholder character
        GameObject player = GameObject.CreatePrimitive(PrimitiveType.Capsule);
        player.name = "Player";
        player.tag = "Player";
        player.transform.position = new Vector3(0, 1, 0);
        
        // Remove default collider (CharacterController will handle collision)
        DestroyImmediate(player.GetComponent<Collider>());
        
        // Add CharacterController
        CharacterController charController = player.AddComponent<CharacterController>();
        charController.center = Vector3.zero;
        charController.radius = 0.5f;
        charController.height = 2f;
        
        // Add scripts
        player.AddComponent<PlayerController>();
        player.AddComponent<PlayerAnimatorController>();
        
        // Add PlayerInput component
        var playerInput = player.AddComponent<UnityEngine.InputSystem.PlayerInput>();
        
        // Try to assign input actions if they exist
        string inputActionsPath = "Assets/Scripts/PlayerInputActions.inputactions";
        var inputActions = AssetDatabase.LoadAssetAtPath<UnityEngine.InputSystem.InputActionAsset>(inputActionsPath);
        if (inputActions != null)
        {
            playerInput.actions = inputActions;
            Debug.Log("✓ Assigned InputActions to Player");
        }
        else
        {
            Debug.LogWarning("⚠ InputActions not found at: " + inputActionsPath);
        }
        
        // Add Animator (for when animations are ready)
        Animator animator = player.AddComponent<Animator>();
        
        // Create simple material for player
        Material playerMat = new Material(Shader.Find("Universal Render Pipeline/Lit"));
        playerMat.color = new Color(0.8f, 0.4f, 0.2f); // Orange-ish
        player.GetComponent<Renderer>().material = playerMat;
        
        Debug.Log("✓ Created Player with CharacterController and scripts");
        return player;
    }
    
    static GameObject CreateCamera(GameObject player)
    {
        // Find main camera
        Camera mainCam = Camera.main;
        GameObject cameraObj;
        
        if (mainCam != null)
        {
            cameraObj = mainCam.gameObject;
            Debug.Log("Using existing Main Camera");
        }
        else
        {
            cameraObj = new GameObject("Main Camera");
            cameraObj.tag = "MainCamera";
            Camera cam = cameraObj.AddComponent<Camera>();
            cameraObj.AddComponent<AudioListener>();
            Debug.Log("✓ Created Main Camera");
        }
        
        // Add ThirdPersonCamera script
        ThirdPersonCamera tpCamera = cameraObj.GetComponent<ThirdPersonCamera>();
        if (tpCamera == null)
        {
            tpCamera = cameraObj.AddComponent<ThirdPersonCamera>();
        }
        
        // Add PlayerInput for camera controls
        var playerInput = cameraObj.GetComponent<UnityEngine.InputSystem.PlayerInput>();
        if (playerInput == null)
        {
            playerInput = cameraObj.AddComponent<UnityEngine.InputSystem.PlayerInput>();
            
            // Try to assign input actions
            string inputActionsPath = "Assets/Scripts/PlayerInputActions.inputactions";
            var inputActions = AssetDatabase.LoadAssetAtPath<UnityEngine.InputSystem.InputActionAsset>(inputActionsPath);
            if (inputActions != null)
            {
                playerInput.actions = inputActions;
            }
        }
        
        // Set player as target using SerializedObject (proper way)
        SerializedObject serializedCamera = new SerializedObject(tpCamera);
        SerializedProperty targetProperty = serializedCamera.FindProperty("target");
        targetProperty.objectReferenceValue = player.transform;
        serializedCamera.ApplyModifiedProperties();
        
        // Position camera
        cameraObj.transform.position = player.transform.position + new Vector3(0, 2, -5);
        cameraObj.transform.LookAt(player.transform.position + Vector3.up);
        
        Debug.Log("✓ Configured Third Person Camera");
        return cameraObj;
    }
    
    static GameObject CreateDirectionalLight()
    {
        // Check if directional light exists
        Light[] lights = FindObjectsOfType<Light>();
        foreach (Light light in lights)
        {
            if (light.type == LightType.Directional)
            {
                Debug.Log("Directional light already exists");
                return light.gameObject;
            }
        }
        
        // Create directional light
        GameObject lightObj = new GameObject("Directional Light");
        Light light = lightObj.AddComponent<Light>();
        light.type = LightType.Directional;
        light.color = Color.white;
        light.intensity = 1f;
        lightObj.transform.rotation = Quaternion.Euler(50, -30, 0);
        
        Debug.Log("✓ Created Directional Light");
        return lightObj;
    }
    
    [MenuItem("Tools/GameSantai/Create Simple Animator")]
    public static void CreateSimpleAnimator()
    {
        // This will create a basic animator controller for testing
        // In actual use, you'll want to use Mixamo animations
        
        string path = "Assets/Characters/Animations/PlayerAnimatorController.controller";
        
        // Create animator controller
        UnityEditor.Animations.AnimatorController controller = UnityEditor.Animations.AnimatorController.CreateAnimatorControllerAtPath(path);
        
        // Add parameters
        controller.AddParameter("IsMoving", AnimatorControllerParameterType.Bool);
        controller.AddParameter("Speed", AnimatorControllerParameterType.Float);
        
        // Create states
        var rootStateMachine = controller.layers[0].stateMachine;
        var idleState = rootStateMachine.AddState("Idle");
        var walkState = rootStateMachine.AddState("Walk");
        
        // Set as default state
        rootStateMachine.defaultState = idleState;
        
        // Create transitions
        var idleToWalk = idleState.AddTransition(walkState);
        idleToWalk.AddCondition(UnityEditor.Animations.AnimatorConditionMode.If, 0, "IsMoving");
        idleToWalk.hasExitTime = false;
        idleToWalk.duration = 0.1f;
        
        var walkToIdle = walkState.AddTransition(idleState);
        walkToIdle.AddCondition(UnityEditor.Animations.AnimatorConditionMode.IfNot, 0, "IsMoving");
        walkToIdle.hasExitTime = false;
        walkToIdle.duration = 0.1f;
        
        AssetDatabase.SaveAssets();
        AssetDatabase.Refresh();
        
        Debug.Log("✓ Created Animator Controller at: " + path);
        Debug.Log("⚠ Note: This is a placeholder. Add actual animations from Mixamo for full functionality.");
        
        // Try to assign to player
        GameObject player = GameObject.FindGameObjectWithTag("Player");
        if (player != null)
        {
            Animator animator = player.GetComponent<Animator>();
            if (animator != null)
            {
                animator.runtimeAnimatorController = controller;
                Debug.Log("✓ Assigned Animator Controller to Player");
            }
        }
    }
#endif
}