using UnityEngine;

/// <summary>
/// Handles character animations for Idle and Walk states
/// Works with both Mixamo animations and placeholder setup
/// </summary>
[RequireComponent(typeof(Animator))]
public class PlayerAnimatorController : MonoBehaviour
{
    [Header("Animation Parameters")]
    [SerializeField] private string isMovingParam = "IsMoving";
    [SerializeField] private string speedParam = "Speed";
    
    [Header("Animation Smoothing")]
    [SerializeField] private float animationSmoothTime = 0.1f;
    
    private Animator animator;
    private float currentSpeed;
    private float speedVelocity;
    
    void Awake()
    {
        animator = GetComponent<Animator>();
        
        if (animator == null)
        {
            Debug.LogWarning("PlayerAnimatorController: No Animator component found. Animations will not work.");
        }
    }
    
    void Start()
    {
        // Verify animator parameters exist
        if (animator != null && animator.runtimeAnimatorController != null)
        {
            CheckAnimatorParameters();
        }
    }
    
    void CheckAnimatorParameters()
    {
        // Check if required parameters exist in the animator
        bool hasIsMoving = false;
        bool hasSpeed = false;
        
        foreach (AnimatorControllerParameter param in animator.parameters)
        {
            if (param.name == isMovingParam) hasIsMoving = true;
            if (param.name == speedParam) hasSpeed = true;
        }
        
        if (!hasIsMoving)
        {
            Debug.LogWarning($"PlayerAnimatorController: Parameter '{isMovingParam}' not found in Animator Controller.");
        }
        
        if (!hasSpeed)
        {
            Debug.LogWarning($"PlayerAnimatorController: Parameter '{speedParam}' not found in Animator Controller.");
        }
    }
    
    /// <summary>
    /// Set whether the character is moving
    /// </summary>
    public void SetMoving(bool isMoving)
    {
        if (animator != null)
        {
            animator.SetBool(isMovingParam, isMoving);
        }
    }
    
    /// <summary>
    /// Set movement speed for blend tree animations
    /// </summary>
    public void SetSpeed(float speed)
    {
        if (animator != null)
        {
            // Smooth the speed value
            currentSpeed = Mathf.SmoothDamp(currentSpeed, speed, ref speedVelocity, animationSmoothTime);
            animator.SetFloat(speedParam, currentSpeed);
        }
    }
    
    /// <summary>
    /// Trigger an animation by name
    /// </summary>
    public void TriggerAnimation(string triggerName)
    {
        if (animator != null)
        {
            animator.SetTrigger(triggerName);
        }
    }
    
    /// <summary>
    /// Get current animation state info
    /// </summary>
    public AnimatorStateInfo GetCurrentStateInfo(int layer = 0)
    {
        if (animator != null)
        {
            return animator.GetCurrentAnimatorStateInfo(layer);
        }
        return default;
    }
    
    /// <summary>
    /// Check if a specific animation is playing
    /// </summary>
    public bool IsPlayingAnimation(string animationName, int layer = 0)
    {
        if (animator != null)
        {
            AnimatorStateInfo stateInfo = animator.GetCurrentAnimatorStateInfo(layer);
            return stateInfo.IsName(animationName);
        }
        return false;
    }
}