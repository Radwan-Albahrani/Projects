using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SpawnManager : MonoBehaviour
{
    //Getting The EnemyShip Prefab
    [SerializeField]
    private GameObject _EnemyShipPrefab;
    //Getting the Powerup Prefabs
    [SerializeField]
    private GameObject[] _Powerups;

    //Spawn Containers
    [SerializeField]
    private GameObject _EnemyContainer;
    [SerializeField]
    private GameObject _PowerupContainer;

    private void Start()
    {
        StartCoroutine(EnemySpawning());
        StartCoroutine(PowerUpSpawnRoutine());
    }



    //Spawning Coroutines.
    IEnumerator EnemySpawning()
    {
        while(true)
        {
            yield return new WaitForSeconds(2);
            //Spawn Enemy and Save it in Variable, Then Parent it to Container
            GameObject _SpawnedEnemy = Instantiate(_EnemyShipPrefab, new Vector3(Random.Range(-8f, 8f), 6.6f, 0), Quaternion.identity);
            _SpawnedEnemy.transform.parent = _EnemyContainer.transform;
        }

    }
    IEnumerator PowerUpSpawnRoutine()
    {
        
        while(true)
        {
            int Randompowerup = Random.Range(0, 3);
            yield return new WaitForSeconds(10);
            GameObject _SpawnedPowerup = Instantiate(_Powerups[Randompowerup], new Vector3(Random.Range(-8f, 8f), 6.6f, 0), Quaternion.identity);
            _SpawnedPowerup.transform.parent = _PowerupContainer.transform;
        }
    }
}
