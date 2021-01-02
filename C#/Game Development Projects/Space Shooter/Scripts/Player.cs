using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;


public class Player : MonoBehaviour
{
    //Variable to get the animator component
    private Animator _anim;
    //Getting The Sprite Renderer
    private SpriteRenderer _PlayerSprite;
    //Accessing The UI manager
    private UIManager _uiManager;
    //Accessing the AudipClip
    [SerializeField]
    private AudioClip _ExplosionAudio;
    
    //Prefabs
    [SerializeField]
    private GameObject _LaserPrefab;
    [SerializeField]
    private GameObject _TripleShotPrefab;
    [SerializeField]
    private GameObject _Shield;
    [SerializeField]
    private GameObject _Thruster;
    [SerializeField]
    private GameObject[] _PlayerHurt;



    //Has exploded check:
    private bool _HasExploded = false;
    
    //Powerup Checks
    public bool CanTripleShot = false;
    public bool CanSpeedBoost = false;
    public bool ShieldActive = false;

    //Health
    public int health = 3;
    
    //Speed
    [SerializeField]
    private float _Speed = 5;
    
    //Fire rate and cooldown system
    [SerializeField]
    private float _FireRate = 0.25f;

    
    //Hidden Variables
    //A variable that decides which Engine failure starts first
    private int _EngineFailure;
    //A variable thats responsible for keeping up with the player, enabling cooldown.
    private float _CanFire = 0.0f;


    // Start is called before the first frame update
    void Start()
    {
        health = 3;
        //Getting The Animator component from the player
        _anim = GetComponent<Animator>();
        //Getting the Sprite Renderer Component from the player
        _PlayerSprite = GetComponent<SpriteRenderer>();
        //Getting The UI Manager Script from the Canvas
        _uiManager = GameObject.Find("Canvas").GetComponent<UIManager>();
        //Null Checking
        if(_uiManager != null)
        {
            //Setting the Starting lives into the UI
            _uiManager.UpdateLives(health);
        }
        //Choosing which engine failure shows up first
        _EngineFailure = Random.Range(0, 2);
        //Setting Starting Position
        transform.position = new Vector3(0, -3, 0);
    }

    // Update is called once per frame
    void Update()
    {
        if(_HasExploded == false)
        {
            Movement();
            _PlayerAnimation();



            //Everytime the player hits Spacebar, Laser spawns.
            if (Input.GetKeyDown(KeyCode.Space) || Input.GetMouseButtonDown(0))
            {
                Shoot();
            }
            //Shield Testing
            if (ShieldActive == true)
            {
                _Shield.SetActive(true);
            }

            else if (ShieldActive == false)
            {
                _Shield.SetActive(false);
            }
        }
        
    }

    //Input Methods
    private void Movement()
    {
        //Speed boost check
        if (CanSpeedBoost == true)
        {
            _Speed = 10;
            
        }

        //Getting Player Input
        float HorizontalInput = Input.GetAxis("Horizontal");
        float VerticalInput = Input.GetAxis("Vertical");

        //Assigning Direction and moving player
        Vector3 Direction = new Vector3(HorizontalInput, VerticalInput, 0);
        transform.Translate(Direction * _Speed * Time.deltaTime);

        //Restricting Player on the Y
        transform.position = new Vector3(transform.position.x, Mathf.Clamp(transform.position.y, -4.2f, 4.2f), 0);

        //Restricting Player on the X, Wraping mechanism
        if (transform.position.x > 9.3f)
        {
            transform.position = new Vector3(-9.3f, transform.position.y, 0);
        }
        else if (transform.position.x < -9.3f)
        {
            transform.position = new Vector3(9.3f, transform.position.y, 0);
        }
    }
    private void Shoot()
    {
        if (Time.time > _CanFire)
        {
            
            if(CanTripleShot == true)
            {
                Instantiate(_TripleShotPrefab, transform.position, Quaternion.identity);
            }
            else
            { 
                Instantiate(_LaserPrefab, transform.position + new Vector3(0, 0.15f, 0), Quaternion.identity);
            }
            //cooldown
            _CanFire = _FireRate + Time.time;
        }
        
    }
    //Powerup Voids
    public void TripleShotPowerupOn()
    {
        CanTripleShot = true;
        StartCoroutine(TripleShotPowerDownRoutine());
    }
    public void SpeedBoostPowerUp()
    {
        CanSpeedBoost = true;
        StartCoroutine(speedboostPowerDownRoutine());

    }
    public void ShieldPowerUp()
    {
        ShieldActive = true;
        _Shield.SetActive(true);
    }
    //Cooldown Voids
    private IEnumerator TripleShotPowerDownRoutine()
    {
        yield return new WaitForSeconds(5);
        CanTripleShot = false;
    }
    private IEnumerator speedboostPowerDownRoutine()
    {
        yield return new WaitForSeconds(5);
        _Speed = 5f;
        CanSpeedBoost = false;
    }
    //Health System (With Shield Check)
    public void HealthSystem()
    {
        //If the shield is active, no health will be lost.
        if(ShieldActive == true)
        {
            ShieldActive = false;
            _Shield.SetActive(false);
            return;
        }
        //Subtracting health from the player
        health = health - 1;
        //Adding the Damaged effect
        if(_EngineFailure == 0)
        {
            _PlayerHurt[0].SetActive(true);
            _EngineFailure = 1;
        }
        else
        {
            _PlayerHurt[1].SetActive(true);
            _EngineFailure = 0;
        }

        //Updating lives display
        _uiManager.UpdateLives(health);
        //If the player health is 0
        if (health == 0)
        {
            //Set Hasexploded to true to Stop player movement and shooting
            _HasExploded = true;
            //Change the player to Untagged as to avoid any collisions
            gameObject.tag = "Untagged";
            //Set sorting layer to background as to avoid display glitches
            _PlayerSprite.sortingLayerName = "Background";
            //Turning All SFXs
            _Thruster.SetActive(false);
            _PlayerHurt[0].SetActive(false);
            _PlayerHurt[1].SetActive(false);
            //Play animation
            _anim.Play("Player_Explosion");
            //Playing The AudioClip
            AudioSource.PlayClipAtPoint(_ExplosionAudio, Camera.main.transform.position);
            //Destroy Object after animation.
            StartCoroutine(_uiManager.GameOver());
        }
    }
    //Player Animations for Left and right
    private void _PlayerAnimation()
    {
        //if A or Left arrow key pressed.
        if (Input.GetKeyDown(KeyCode.A) || Input.GetKeyDown(KeyCode.LeftArrow))
        {
            _anim.SetBool("Turn_Left", true);

        }
        //If A or left arrow key Lifted up.
        else if (Input.GetKeyUp(KeyCode.A) || Input.GetKeyUp(KeyCode.LeftArrow))
        {
            _anim.SetBool("Turn_Left", false);
        }
        //if d or right arrow key pressed.
        if (Input.GetKeyDown(KeyCode.D) || Input.GetKeyDown(KeyCode.RightArrow))
        {
            _anim.SetBool("Turn_Right", true);
        }
        //If d or right arrow key Lifted up.
        else if (Input.GetKeyUp(KeyCode.D) || Input.GetKeyUp(KeyCode.RightArrow))
        {
            _anim.SetBool("Turn_Right", false);
        }

    }


}
