using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Laser : MonoBehaviour
{
    //Laser speed
    [SerializeField]
    private int _Speed = 10;
    void Update()
    {
        //movement
        transform.Translate(Vector3.up * _Speed * Time.deltaTime);

        //destroy laser
        if(transform.position.y > 6f)
        {
            Destroy(gameObject);
        }
    }
}
