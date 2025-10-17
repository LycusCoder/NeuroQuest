using UnityEngine;
using UnityEngine.InputSystem;

/// <summary>
/// Third Person Camera that follows the player and allows orbit control
/// Smooth camera movement with mouse input
/// </summary>
public class ThirdPersonCamera : MonoBehaviour
{
    [Header("Target Settings")]
    [SerializeField] private Transform target;
    [SerializeField] private Vector3 targetOffset = new Vector3(0, 1.5f, 0);
    
    [Header("Camera Distance")]
    [SerializeField] private float distance = 5.0f;
    [SerializeField] private float minDistance = 2.0f;
    [SerializeField] private float maxDistance = 10.0f;
    [SerializeField] private float zoomSpeed = 2.0f;
    
    [Header("Camera Rotation")]
    [SerializeField] private float rotationSpeed = 5.0f;
    [SerializeField] private float minVerticalAngle = -20f;
    [SerializeField] private float maxVerticalAngle = 80f;
    
    [Header("Camera Smoothing")]
    [SerializeField] private float positionSmoothTime = 0.1f;
    [SerializeField] private float rotationSmoothTime = 0.1f;
    
    [Header("Input Settings")]
    [SerializeField] private bool invertY = false;
    [SerializeField] private float mouseSensitivity = 1.0f;
    
    [Header("Collision Detection")]
    [SerializeField] private bool checkCollision = true;
    [SerializeField] private float collisionRadius = 0.3f;
    [SerializeField] private LayerMask collisionLayers;
    
    // Private variables
    private float currentX = 0f;
    private float currentY = 20f;
    private float currentDistance;
    
    private Vector3 currentVelocity;
    private float rotationYVelocity;
    private float rotationXVelocity;
    
    private Vector2 lookInput;
    private float scrollInput;
    
    // Input System
    private PlayerInput playerInput;
    private InputAction lookAction;
    private InputAction scrollAction;
    
    void Start()
    {
        // Initialize camera position
        currentDistance = distance;
        
        // Find target if not assigned
        if (target == null)
        {
            GameObject player = GameObject.FindGameObjectWithTag("Player");
            if (player != null)
            {
                target = player.transform;
            }
            else
            {
                Debug.LogError("ThirdPersonCamera: No target assigned and no GameObject with 'Player' tag found!");
            }
        }
        
        // Setup Input System
        playerInput = GetComponent<PlayerInput>();
        if (playerInput != null)
        {
            lookAction = playerInput.actions["Look"];
            scrollAction = playerInput.actions["Scroll"];
        }
        
        // Lock cursor (optional - comment out if you don't want cursor locked)
        // Cursor.lockState = CursorLockMode.Locked;
        // Cursor.visible = false;
    }
    
    void LateUpdate()
    {
        if (target == null) return;
        
        // Get input
        GetCameraInput();
        
        // Handle camera rotation
        HandleRotation();
        
        // Handle zoom
        HandleZoom();
        
        // Calculate desired camera position
        Vector3 desiredPosition = CalculateCameraPosition();
        
        // Check for collision
        if (checkCollision)
        {
            desiredPosition = CheckCameraCollision(desiredPosition);
        }
        
        // Smoothly move camera to desired position
        transform.position = Vector3.SmoothDamp(transform.position, desiredPosition, ref currentVelocity, positionSmoothTime);
        
        // Look at target
        Vector3 lookAtPosition = target.position + targetOffset;
        transform.LookAt(lookAtPosition);
    }
    
    void GetCameraInput()
    {
        // Using Input System
        if (lookAction != null)
        {
            lookInput = lookAction.ReadValue<Vector2>();
        }
        else
        {
            // Fallback to old Input System
            lookInput.x = Input.GetAxis("Mouse X");
            lookInput.y = Input.GetAxis("Mouse Y");
        }
        
        // Scroll for zoom
        if (scrollAction != null)
        {
            scrollInput = scrollAction.ReadValue<float>();
        }
        else
        {
            scrollInput = Input.GetAxis("Mouse ScrollWheel");
        }
    }
    
    void HandleRotation()
    {
        // Only rotate when right mouse button is held (or always rotate - your choice)
        bool shouldRotate = Input.GetMouseButton(1) || lookInput.magnitude > 0.1f;
        
        if (shouldRotate)
        {
            float mouseX = lookInput.x * rotationSpeed * mouseSensitivity;
            float mouseY = lookInput.y * rotationSpeed * mouseSensitivity;
            
            if (invertY)
            {
                mouseY = -mouseY;
            }
            
            // Smooth rotation
            currentX = Mathf.SmoothDamp(currentX, currentX + mouseX, ref rotationXVelocity, rotationSmoothTime);
            currentY = Mathf.SmoothDamp(currentY, currentY - mouseY, ref rotationYVelocity, rotationSmoothTime);
            
            // Clamp vertical angle
            currentY = Mathf.Clamp(currentY, minVerticalAngle, maxVerticalAngle);
        }
    }
    
    void HandleZoom()
    {
        if (Mathf.Abs(scrollInput) > 0.01f)
        {
            currentDistance -= scrollInput * zoomSpeed;
            currentDistance = Mathf.Clamp(currentDistance, minDistance, maxDistance);
        }
    }
    
    Vector3 CalculateCameraPosition()
    {
        // Calculate position based on rotation and distance
        Quaternion rotation = Quaternion.Euler(currentY, currentX, 0);
        Vector3 direction = rotation * Vector3.back;
        
        Vector3 targetPosition = target.position + targetOffset;
        return targetPosition + direction * currentDistance;
    }
    
    Vector3 CheckCameraCollision(Vector3 desiredPosition)
    {
        Vector3 targetPosition = target.position + targetOffset;
        Vector3 direction = desiredPosition - targetPosition;
        float targetDistance = direction.magnitude;
        
        RaycastHit hit;
        if (Physics.SphereCast(targetPosition, collisionRadius, direction.normalized, out hit, targetDistance, collisionLayers))
        {
            // Camera hit something, move it closer
            return targetPosition + direction.normalized * (hit.distance - collisionRadius);
        }
        
        return desiredPosition;
    }
    
    // Public methods
    public void SetTarget(Transform newTarget)
    {
        target = newTarget;
    }
    
    public void ResetCamera()
    {
        currentX = 0f;
        currentY = 20f;
        currentDistance = distance;
    }
    
    // Gizmos for debugging
    void OnDrawGizmosSelected()
    {
        if (target == null) return;
        
        Gizmos.color = Color.yellow;
        Gizmos.DrawWireSphere(target.position + targetOffset, 0.3f);
        
        Gizmos.color = Color.cyan;
        Gizmos.DrawLine(target.position + targetOffset, transform.position);
    }
}