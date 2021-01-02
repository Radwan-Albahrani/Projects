using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Powerup : MonoBehaviour
{
    //Speed of powerup Going down
    [SerializeField]
    private float _Speed = 3.0f;
    //Powerup ID
    [SerializeField]
    private int _PowerupID; //0 for triple shot, 1 for speed. 2 for shield
    //Getting The powerup AudioClip
    [SerializeField]
    private AudioClip _PowerUpSfx;
    
    // Update is called once per frame
    void Update()
    {
        //Making the powerup Move down with speed
        transform.Translate(Vector3.down * _Speed * Time.deltaTime);
        //Destroying powerup if off screen
        if(transform.position.y < -6.6f)
        {
            Destroy(this.gameObject);
        }
    }

    //Collision checks
    private void OnTriggerEnter2D(Collider2D other)
    {
        //Display object who collided with Powerup
        Debug.Log(transform.name + " Collided with: " + other.name);
        //Checking for the player tag
        if(other.tag == "Player")
        {
            //Access the player
            Player player = other.GetComponent<Player>();
            if (player != null)
            {
                //Enable tripleshot here
                if (_PowerupID == 0)
                {
                    player.TripleShotPowerupOn();
                    
                }
                //Enable speed boost here
                else if (_PowerupID == 1)
                {
                    player.SpeedBoostPowerUp();
                    
                }
                //Enable Shields here
                else if (_PowerupID == 2)
                {
                    player.ShieldPowerUp();
                    
                }
                //Playing Audio Source
                AudioSource.PlayClipAtPoint(_PowerUpSfx, Camera.main.transform.position);
                //Destroying Powerup
                Destroy(this.gameObject);
            }
        }

    }
}
