using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class EnemyAI : MonoBehaviour
{
    //Get Player
    private Transform _Player;

    //Needed Components
    private Animator _Animations;
    private NavMeshAgent _Navigation;
    private SphereCollider _EnemyCollider;

    //Sound Effects
    public AudioClip[] EnemySFX;
    public AudioSource PlayEnemySFX;
    
    // Start is called before the first frame update
    void Start()
    {
        //Find Player and get the transform Component
        _Player = GameObject.FindGameObjectWithTag("Player").transform;
        
        //Get the necessary Components
        _Navigation = GetComponent<NavMeshAgent>();
        _Animations = GetComponent<Animator>();
        _EnemyCollider = GetComponent<SphereCollider>();
    }

    // Update is called once per frame
    void Update()
    {
        if(_Animations.GetBool("Dead") == false)
        {
            //Enable Navigation
            _Navigation.enabled = true;
            //Set destination to player's position
            _Navigation.SetDestination(_Player.position);
        }
        else
        {
            //Disabling movement, hitbox, and making sure it sticks to its place.
            _Navigation.updatePosition = false;
            _Navigation.updateRotation = false;
            _EnemyCollider.enabled = false;
            PlayEnemySFX.loop = false;
        }
    }

    //Check for collisions
    private void OnTriggerEnter(Collider other)
    {
        //If collided with player
        if (other.transform.tag == "Player")
        {
            //Get Player Script
            Player player = GameObject.Find("Player").GetComponent<Player>();
            //If player has health
            if (player.CurrentHealth > 0)
            {
                //Remove Health
                player.HealthSystem();
                //Play Animation
                _Animations.SetBool("Attacking", true);
                //Play bite SFX
                PlayEnemySFX.PlayOneShot(EnemySFX[0], 3f);
            }

        }
    }
    private void OnTriggerExit(Collider other)
    {
        //If collided with player
        if (other.transform.tag == "Player")
        {
            _Animations.SetBool("Attacking", false);
        }
    }
}
