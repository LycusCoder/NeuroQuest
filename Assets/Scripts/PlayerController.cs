using UnityEngine;
using UnityEngine.InputSystem;

/// <summary>
/// Third Person Player Controller for Medieval Ranger
/// Controls character movement with WASD/Arrow Keys
/// </summary>
[RequireComponent(typeof(CharacterController))]
public class PlayerController : MonoBehaviour
{
    [Header("Movement Settings")]
    [SerializeField] private float walkSpeed = 3.0f;
    [SerializeField] private float runSpeed = 6.0f;
    [SerializeField] private float rotationSpeed = 10.0f;
    [SerializeField] private float gravity = -9.81f;
    
    [Header("Ground Check")]
    [SerializeField] private float groundCheckDistance = 0.2f;
    [SerializeField] private LayerMask groundLayer;
    
    // Components
    private CharacterController characterController;
    private PlayerAnimatorController animatorController;
    private Transform cameraTransform;
    
    // Movement variables
    private Vector2 moveInput;
    private Vector3 velocity;
    private bool isGrounded;
    private float currentSpeed;
    
    // Input System
    private PlayerInput playerInput;
    private InputAction moveAction;
    
    void Awake()
    {
        characterController = GetComponent<CharacterController>();
        animatorController = GetComponent<PlayerAnimatorController>();
        
        // Get camera reference
        if (Camera.main != null)
        {
            cameraTransform = Camera.main.transform;
        }
        
        // Setup Input System
        playerInput = GetComponent<PlayerInput>();
        if (playerInput != null)
        {
            moveAction = playerInput.actions["Move"];
        }
    }
    
    void Update()
    {
        // Check if grounded
        CheckGround();
        
        // Get input
        GetMovementInput();
        
        // Handle movement
        HandleMovement();
        
        // Handle rotation
        HandleRotation();
        
        // Apply gravity
        ApplyGravity();
        
        // Update animator
        UpdateAnimator();
    }
    
    void CheckGround()
    {
        // Raycast to check if player is on ground
        isGrounded = Physics.Raycast(transform.position, Vector3.down, groundCheckDistance + 0.1f, groundLayer);
        
        if (isGrounded && velocity.y < 0)
        {
            velocity.y = -2f; // Small downward force to keep grounded
        }
    }
    
    void GetMovementInput()
    {
        // Using Input System
        if (moveAction != null)
        {
            moveInput = moveAction.ReadValue<Vector2>();
        }
        else
        {
            // Fallback to old Input System
            moveInput.x = Input.GetAxis("Horizontal");
            moveInput.y = Input.GetAxis("Vertical");
        }
    }
    
    void HandleMovement()
    {
        // Calculate movement direction relative to camera
        Vector3 forward = cameraTransform != null ? cameraTransform.forward : transform.forward;
        Vector3 right = cameraTransform != null ? cameraTransform.right : transform.right;
        
        // Remove vertical component
        forward.y = 0;
        right.y = 0;
        forward.Normalize();
        right.Normalize();
        
        // Calculate desired movement direction
        Vector3 moveDirection = (forward * moveInput.y + right * moveInput.x).normalized;
        
        // Determine speed (walk by default, can add run later)
        currentSpeed = walkSpeed;
        
        // Move the character
        if (moveDirection.magnitude >= 0.1f)
        {
            characterController.Move(moveDirection * currentSpeed * Time.deltaTime);
        }
    }
    
    void HandleRotation()
    {
        // Rotate character to face movement direction
        if (moveInput.magnitude >= 0.1f)
        {
            Vector3 forward = cameraTransform != null ? cameraTransform.forward : transform.forward;
            Vector3 right = cameraTransform != null ? cameraTransform.right : transform.right;
            
            forward.y = 0;
            right.y = 0;
            forward.Normalize();
            right.Normalize();
            
            Vector3 targetDirection = (forward * moveInput.y + right * moveInput.x).normalized;
            
            if (targetDirection.magnitude >= 0.1f)
            {
                Quaternion targetRotation = Quaternion.LookRotation(targetDirection);
                transform.rotation = Quaternion.Slerp(transform.rotation, targetRotation, rotationSpeed * Time.deltaTime);
            }
        }
    }
    
    void ApplyGravity()
    {
        if (!isGrounded)
        {
            velocity.y += gravity * Time.deltaTime;
        }
        
        characterController.Move(velocity * Time.deltaTime);
    }
    
    void UpdateAnimator()
    {
        if (animatorController != null)
        {
            float moveSpeed = moveInput.magnitude;
            bool isMoving = moveSpeed > 0.1f;
            
            animatorController.SetMoving(isMoving);
            animatorController.SetSpeed(moveSpeed);
        }
    }
    
    // Public getter for movement state
    public bool IsMoving()
    {
        return moveInput.magnitude > 0.1f;
    }
    
    public float GetMoveSpeed()
    {
        return moveInput.magnitude;
    }
    
    // Gizmos for debugging
    void OnDrawGizmosSelected()
    {
        Gizmos.color = isGrounded ? Color.green : Color.red;
        Gizmos.DrawRay(transform.position, Vector3.down * (groundCheckDistance + 0.1f));
    }
}