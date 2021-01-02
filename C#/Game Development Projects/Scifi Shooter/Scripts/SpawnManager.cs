using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class SpawnManager : MonoBehaviour
{
    //Variables
    private float Seconds = 3f;
    private float _radius = 10;

    //Spawnable Objects
    [SerializeField]
    private GameObject _Enemy;

    //When Called, Start spawning Spawnable Objects
    public void StartGame()
    {
        StartCoroutine(Spawn());
    }
    //When Called, Increase difficulty of game
    public void IncreaseDifficulty()
    {
        if(Seconds > 1f)
        {
            Seconds -= 0.2f;
        }
        if(_radius > 4f)
        {
            _radius -= 0.5f;
        }
    }

    //Find Random Point in mesh
    public Vector3 RandomNavmeshLocation()
    {
        //Get a randopoint within a sphere by with a radius
        Vector3 RandomPoint = Random.insideUnitSphere * _radius;
        //Add that random point to the player's position
        RandomPoint += GameObject.Find("Player").transform.position;
        //Define a Mesh hit, to be able to store mesh information
        NavMeshHit hit;
        //Define final position.
        Vector3 finalPosition = Vector3.zero;
        //If Random point around the player by is 1 unit away from any navmesh 
        if (NavMesh.SamplePosition(RandomPoint, out hit, _radius, 1))
        {
            //Give it that navmesh position
            finalPosition = hit.position;
        }
        //Return that final position to whoever called this method
        return finalPosition;
    }

    //Spawning
    IEnumerator Spawn()
    {
        Player player = GameObject.FindGameObjectWithTag("Player").GetComponent<Player>();
        //Keep Looping while player is alive
        while(player.CurrentHealth > 0)
        {
            //Wait an amount of seconds
            yield return new WaitForSeconds(Seconds);
            //Spawn a Crate in the map
            Instantiate(_Enemy, RandomNavmeshLocation() , Quaternion.identity);
        }
    }

}
