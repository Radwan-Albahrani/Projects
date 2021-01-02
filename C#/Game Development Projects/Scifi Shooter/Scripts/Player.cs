using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;
using UnityEngine.UI;
using UnityStandardAssets.Characters.FirstPerson;
using UnityStandardAssets.Utility;

public class Player : MonoBehaviour
{
    //Variables
    private float _Speed = 3.5f;
    private float _Gravity = 1f;
    private float _yVelocity;
    private float _JumpSpeed = 15f;
    private float _FireRate = 0.01f;
    private float _CanFire = 0.0f;
    private int _CurrentAmmo;
    private int _MaxAmmo = 150;
    public int CurrentHealth = 30;
    private bool _Isreloading = false;
    private bool _HasCoin = false;
    private bool _SceneStarting = false;


    //Handlers
    private CharacterController _PlayerController;
    private ParticleSystem _MuzzleShot;
    private GameManager _GameManager;
    public NavMeshAgent Navigation;

    //First-person Character Handlers
    [SerializeField]
    private MouseLook _Mouse;
    [SerializeField]
    private FOVKick _FOVkick = new FOVKick();

    //UI Items
    [SerializeField]
    private Sprite[] _InvSprites;
    [SerializeField]
    private Sprite[] _UISprites;
    private Text _AmmoCount;
    private Image _Inventory;
    [SerializeField]
    private Text _UserFriendly;
    [SerializeField]
    private Image _ButtonPress;
    [SerializeField]
    private Image _Background;

    //AudioSources
    [SerializeField]
    private AudioSource _ShootSoundEffect;
    [SerializeField]
    private AudioSource _ReloadSFX;
    [SerializeField]
    private AudioClip[] _PlayerSFX;
    [SerializeField]
    private AudioSource _PlaySoundEffects;

    //Animators
    [SerializeField]
    private Animator _ReloadAnimation;

    //GameObjects
    [SerializeField]
    private GameObject _Weapon;
    [SerializeField]
    private GameObject _HitMarkerPrefab;
    [SerializeField]
    private GameObject _Shop;

    // Start is called before the first frame update
    void Start()
    {
        //Getting the components and assigning them to the handlers
        _PlayerController = GetComponent<CharacterController>();
        Navigation = GetComponent<NavMeshAgent>();
        _MuzzleShot = GameObject.Find("Muzzle_Flash").GetComponent<ParticleSystem>();
        _AmmoCount = GameObject.Find("Ammo").GetComponent<Text>();
        _Inventory = GameObject.Find("InvSlot").GetComponent<Image>();
        _GameManager = GameObject.Find("GameManager").GetComponent<GameManager>();


        //Setting Health Variable in GameManager
        _GameManager.CurrentHealth = CurrentHealth;

        //Setting the objective in the Game Manager
        _GameManager.Objective(0);

        //Locking and hiding the cursor
        _Mouse.UpdateCursorLock();

        //Setting up the FOV kick 
        _FOVkick.Setup(Camera.main);

        //Setting the initial location of mouse
        _Mouse.Init(transform, Camera.main.transform);

        //Setting The Ammo
        _CurrentAmmo = _MaxAmmo;
        _AmmoCount.text = null;

        //Resetting UI
        _UserFriendly.text = null;
        _ButtonPress.sprite = _UISprites[0];
        _Background.sprite = _UISprites[0];

        //Deactivating Weapon
        _Weapon.SetActive(false);
    }

    // Update is called once per frame
    void Update()
    {
        //If Health isnt 0, Allow for method Calls
        if(CurrentHealth > 0)
        {
            //Methods Called
            _MouseLook();
            _Movement();
            _ManageInventory();
            //If the weapon is active, allow the shooting method.
            if (_Weapon.activeSelf == true)
            {
                _ManageWeapon();
            }
        }
        //If health Reaches 0
        else
        {
            //Resetting UI
            _UserFriendly.text = null;
            _ButtonPress.sprite = _UISprites[0];
            _Background.sprite = _UISprites[0];
            _Weapon.SetActive(false);
            _PlaySoundEffects.Stop();
        }

    }
    //Moving Void
    private void _Movement()
    {
        
        //Creating a move direction for the player
        Vector3 MoveDirection = new Vector3(Input.GetAxis("Horizontal"), 0, Input.GetAxis("Vertical")) * _Speed;
        
        //Transforming move direction to Local Space
        MoveDirection = transform.TransformDirection(MoveDirection);
        
        //Checking if player is grounded
        if(_PlayerController.isGrounded == true)
        {
            //Keep Player Grounded
            _yVelocity = -_Gravity;
            
            //If player presses
            if(Input.GetKeyDown(KeyCode.Space) && Navigation.enabled == false)
            {
                //Jump
                _yVelocity = _JumpSpeed;
            }
        }
        
        //If player is not grounded. Get the player to the ground.
        else
        {
            //Start lowering y velocity by Gravity
            _yVelocity -= _Gravity * (Time.deltaTime * 60);

        }
        //Keep setting the Y coordinates of the player to the Y velocity
        MoveDirection.y = _yVelocity;
        //Allow player to move
        _PlayerController.Move(MoveDirection * Time.deltaTime);

        //If player Presses Shift
        if(Input.GetKeyDown(KeyCode.LeftShift))
        {
            //Increase Speed
            _Speed = 5.5f;
            //Stop Kick Down Coroutine
            StopCoroutine(_FOVkick.FOVKickDown());
            //Start Kick Up Coroutine
            StartCoroutine(_FOVkick.FOVKickUp());
        }
        //If player lets go of shift
        else if(Input.GetKeyUp(KeyCode.LeftShift))
        {
            //Return Speed to normal
            _Speed = 3.5f;
            //Stop kick Up Coroutine
            StopCoroutine(_FOVkick.FOVKickUp());
            //Start KickDown Coroutine
            StartCoroutine(_FOVkick.FOVKickDown());
        }


        //Check if we are moving, and if we are not jumping.
        if ((MoveDirection.x != 0 || MoveDirection.z != 0) && _PlayerController.isGrounded == true)
        {
            //Check if the walking Sound effect is not playing.
            if(_PlaySoundEffects.isPlaying == false)
            {
                //Play it if its not.
                _PlaySoundEffects.PlayOneShot(_PlayerSFX[0], 10f);
            }

        }

        else
        {
            //Stop sound effect if we are not moving or if we are jumping.
            _PlaySoundEffects.Stop();
        }

    }
    //Mouse Look Void
    private void _MouseLook()
    {
        _Mouse.LookRotation(transform, Camera.main.transform);
    }
    //Shooting Void
    private void _ManageWeapon()
    {
        //Check if we press the mouse button.
        if (Input.GetMouseButton(0) && _CurrentAmmo > 0)
        {
            if (Time.time > _CanFire)
            {
                //Cooldown
                _CanFire = _FireRate + Time.time;
                //Reduce ammo and desplay it
                _CurrentAmmo--;
                _AmmoCount.text = "Ammo: " + _CurrentAmmo;

                //Check if Sound effects and visual effects are playing
                if (_MuzzleShot.isPlaying == false && _ShootSoundEffect.isPlaying == false)
                {
                    //Play the Particle Animation
                    _MuzzleShot.Play();
                    _ShootSoundEffect.Play();
                }


                //Assign the point where the raycast would start at
                Ray rayOrigin = Camera.main.ViewportPointToRay(new Vector3(0.5f, 0.5f, 0));
                RaycastHit _hitInfo;
                //Cast ray from the origin point, get the info of any collider it clashes, and set the range to 100 
                if (Physics.Raycast(rayOrigin, out _hitInfo, 100))
                {
                    //Print out name of the object hit
                    Debug.Log("Hit: " + _hitInfo.transform.name);
                    //Instantiating Hit Effects
                    GameObject hitmarker = Instantiate(_HitMarkerPrefab, _hitInfo.point, Quaternion.LookRotation(_hitInfo.normal));
                    Destroy(hitmarker, 1f);
                    //If we Hit the Crate
                    if (_hitInfo.transform.tag == "Enemy")
                    {
                        //Set Death bool of animation to true
                        Animator _Animator = _hitInfo.transform.gameObject.GetComponent<Animator>();
                        _Animator.SetBool("Dead", true);
                        //Play death SFX
                        EnemyAI enemyAI = _hitInfo.transform.gameObject.GetComponent<EnemyAI>();
                        enemyAI.PlayEnemySFX.Stop();
                        enemyAI.PlayEnemySFX.PlayOneShot(enemyAI.EnemySFX[1], 3f);
                        //Destroy Enemy
                        Destroy(_hitInfo.transform.gameObject, 5);
                        _GameManager.ScoreUpdate(10);
                    }
                    else
                    {
                        if (_hitInfo.rigidbody)
                        {
                            _hitInfo.rigidbody.AddForceAtPosition(200 * transform.forward, _hitInfo.point);
                        }
                    }

                }
            }
            
        }
        //If mouse button is not pressed
        else
        {
            //Stop all effects
            _MuzzleShot.Stop();
            _ShootSoundEffect.Stop();

        }

        //Ui Reload Check.
        if (_CurrentAmmo == 0)
        {
            _UserFriendly.text = "Press          To Reload";
            _ButtonPress.sprite = _UISprites[1];
            _Background.sprite = null;
        }

        //If player presses R and isnt reloading Already
        if (Input.GetKeyDown(KeyCode.R) && _Isreloading == false)
        {
            //Set Reloading to true
            _Isreloading = true;
            //Set Ammo to 0 So he cant shoot
            _CurrentAmmo = 0;
            //Start reloading Coroutine
            StartCoroutine(Reloading());
        }

    }
    //Manage Inventory
    private void _ManageInventory()
    {
        //Inventory Change
        if (_HasCoin == true)
        {
            //If has coin, Show coin
            _Inventory.sprite = _InvSprites[1];

        }
        else
        {
            //If Doesnt have coin, Mask UI
            _Inventory.sprite = _InvSprites[0];
        }
    }
    //Health System
    public void HealthSystem()
    {
        //Reduce Health By 1
        CurrentHealth--;
        //Update Health in UI
        _GameManager.HealthUpdate(CurrentHealth);
        //If health is 0
        if(CurrentHealth <= 0)
        {
            //Start Gameover Method
            _GameManager.GameOver();
        }
    }
    //Reloading Coroutine.
    IEnumerator Reloading()
    {
        //Play the Reload Animation
        _ReloadAnimation.Play("Reload_Animation");
        //Play the reload Sound effect
        _ReloadSFX.Play();
        //Wait for 2 seconds
        yield return new WaitForSeconds(2);
        //Set Reloading to false to allow for another reload
        _Isreloading = false;
        //Reload Current ammo
        _CurrentAmmo = _MaxAmmo;
        //Reset UI
        _UserFriendly.text = null;
        _ButtonPress.sprite = _UISprites[0];
        _Background.sprite = _UISprites[0];
        //Display Ammo
        _AmmoCount.text = "Ammo: " + _CurrentAmmo;
    }
    //Coin Collection.
    private void OnTriggerStay(Collider other)
    {
        //If The Thing we collided with is the coin
        if(other.tag == "Coin")
        {
            //Print out that we collided with it
            Debug.Log("Collided with: " + other.transform.name);
            _UserFriendly.text = "Press          To Pickup";
            _ButtonPress.sprite = _UISprites[2];
            _Background.sprite = null;
            //Check for E press
            if (Input.GetKeyDown(KeyCode.E))
            {
                //Play Coin PickUp Sound
                AudioSource.PlayClipAtPoint(_PlayerSFX[1], transform.position);
                //Tell Player We got the coin
                _HasCoin = true;
                //Destroy The coin
                Destroy(other.gameObject);
                //Reset UI
                _UserFriendly.text = null;
                _ButtonPress.sprite = _UISprites[0];
                _Background.sprite = _UISprites[0];
                //Set Shark to glow
                _Shop.SetActive(true);
                //Change the objective
                _GameManager.Objective(1);
            }

        }
        //ShopSystem
        if(other.tag == "Shop")
        {
            //If player doesnt have coin
            if(_HasCoin == false)
            {
                //Tell him he doesnt have the coin
                _UserFriendly.text = "You don't have the Coin!";
            }
            else
            {
                //Interact to purchase weapon
                _UserFriendly.text = "Press          To Purchase Weapon";
                _ButtonPress.sprite = _UISprites[2];
                _Background.sprite = null;

                //if E key is pressed
                if (Input.GetKeyDown(KeyCode.E))
                {
                    //Remove coin from inventory
                    _HasCoin = false;
                    //Activate weapon
                    _Weapon.SetActive(true);
                    //Show Weapon Ammo
                    _AmmoCount.text = "Ammo: " + _CurrentAmmo;
                    //Resetting UI
                    _UserFriendly.text = null;
                    _ButtonPress.sprite = _UISprites[0];
                    _Background.sprite = _UISprites[0];
                    //Play Purchase Sound Effect
                    AudioSource.PlayClipAtPoint(_PlayerSFX[2], transform.position);
                    //Remove glow
                    _Shop.SetActive(false);
                    //Change The Objective
                    _GameManager.Objective(2);
                }
            }
        }
        //If We wanna start the game
        if(other.tag == "GameStart")
        {
            //Check if player has the weapon
            if (_Weapon.activeSelf == true && _SceneStarting == false)
            {
                //Tell Player he can Press E to start game
                _UserFriendly.text = "Press          To Start Game";
                _ButtonPress.sprite = _UISprites[2];
                _Background.sprite = null;
                //If player presses E
                if (Input.GetKeyDown(KeyCode.E) && _SceneStarting == false)
                {
                    //Tell the game that we are starting
                    _SceneStarting = true;
                    //Start the game using the game Manager
                    _GameManager.StartGame("LevelStart");
                    //Resetting UI
                    _UserFriendly.text = null;
                    _ButtonPress.sprite = _UISprites[0];
                    _Background.sprite = _UISprites[0];
                    //Change The Objective
                    _GameManager.Objective(3);
                }
            }
            //If the player does not have a weapon
            else if (_SceneStarting == false)
            {
                //Tell the player he does not have a weapon.
                _UserFriendly.text = "You Dont Have a Weapon";
                _ButtonPress.sprite = _UISprites[0];
                _Background.sprite = _UISprites[0];
            }

        }
    }
    private void OnTriggerExit(Collider other)
    {
        //Resetting UI
        _UserFriendly.text = null;
        _ButtonPress.sprite = _UISprites[0];
        _Background.sprite = _UISprites[0];
    }
}
