using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EnemyAI : MonoBehaviour
{
    //Variable for your speed.
    [SerializeField]
    private float _Speed = 5f;
    //Variable to get the animator component
    private Animator _anim;
    //Variable to get the Animation Clip
    [SerializeField]
    private AnimationClip _Explosionclip;
    //Variable to Check if a collision has occurred
    private bool _HasBeenHit = false;
    //Getting The Sprite Renderer
    private SpriteRenderer _EnemySprite;
    //Getting the UIScript
    private UIManager _ScoreDisplay;
    //Getting the AudioSource
    [SerializeField]
    private AudioClip _ExplosionAudio;

    //Thrusters
    [SerializeField]
    private GameObject[] _Thrusters;
    
    void Start()
    {
        //Getting the animator component from the enemy
        _anim = GetComponent<Animator>();
        //Getting the Sprite renderer component from the enemy
        _EnemySprite = GetComponent<SpriteRenderer>();
        //Getting the UImanager script from the Canvas
        _ScoreDisplay = GameObject.Find("Canvas").GetComponent<UIManager>();
    }

    // Update is called once per frame
    void Update()
    {
        //Move down
        if (_HasBeenHit == false)
        {
            transform.Translate(Vector3.down * Time.deltaTime * _Speed);
        }
        
        //When off screen, respawn back on top at a random X position between the bounds of the screen.
        if(transform.position.y < -6.6f)
        {
            transform.position = new Vector3(Random.Range(-9.000000f, 9.00000f), 6.6f, 0);
        }
    }
    private void OnTriggerEnter2D(Collider2D other)
    {
        if (_HasBeenHit == false)

        {
            
            Debug.Log(transform.name + " Collided with: " + other.name);
            //Collision with Laser Behavior
            if (other.tag == "Laser")
            {
                //Setting HasbeenHit to true qas to completely stop detecting any collisions
                _HasBeenHit = true;
                //Destroying the laser
                Destroy(other.gameObject);
                //Setting the Sorting Layer to Background
                _EnemySprite.sortingLayerName = "Background";
                //Playing the explosion animation
                _anim.Play("Explosion_Animation");
                //Null Check
                if(_ScoreDisplay != null)
                {
                    //Changing the score
                    _ScoreDisplay.ScoreStatus(10);
                }

                //Playing The AudioClip
                AudioSource.PlayClipAtPoint(_ExplosionAudio, Camera.main.transform.position);
                //Deactivating Thrusters
                _Thrusters[0].SetActive(false);
                _Thrusters[1].SetActive(false);
                //Destroying The enemy after the explosion animation is done.
                Destroy(this.gameObject, _Explosionclip.length);
            }
            //Collision with Player behavior
            else if (other.tag == "Player")
            {
                //Setting hasbeenhit to True as to avoid any collisions
                _HasBeenHit = true;
                //Getting the Script component from the player
                Player player = other.GetComponent<Player>();
                //Making sure the script component is there
                if (player != null)
                {
                    //Decreasing the player health
                    player.HealthSystem();
                    //Setting the Sorting Layer to Background
                    _EnemySprite.sortingLayerName = "Background";
                    //Exploding the Enemy
                    _anim.Play("Explosion_Animation");
                    //Playing The AudioClip
                    AudioSource.PlayClipAtPoint(_ExplosionAudio, Camera.main.transform.position);
                    //Deactivating Thrusters
                    _Thrusters[0].SetActive(false);
                    _Thrusters[1].SetActive(false);
                    //Destroying the enemy after The explosion is done.
                    Destroy(this.gameObject, _Explosionclip.length);

                }
            }
        }
    }

           
}
