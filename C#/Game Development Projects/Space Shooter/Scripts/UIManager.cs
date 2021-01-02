using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class UIManager : MonoBehaviour
{
    //Getting All the necessary sprites
    public Sprite[] Lives;
    //Getting the ImageUI Element
    public Image LivesImageDisplay;
    //Score Display
    [SerializeField]
    private Text _ScoreDisplay;
    //Title Screen
    [SerializeField]
    private GameObject _Titlescreen;
 
    //Keeping Track of the score
    public int Score;

   //Check Boolians to see if The game started
    public bool GameON = false;

    //Getting the player Gameobject
    [SerializeField]
    private GameObject _Player;
    //Getting The Spawn Manager
    [SerializeField]
    private GameObject _SpawnManager;

    void Update()
    {
        //Checking if The game Hasnt started
        if (GameON == false)
        {
            //Checking if player has pressed Space bar
            if (Input.GetKeyDown(KeyCode.Space))
            {
                //Starting the game
                GameON = true;

                //instantiating player
                Instantiate(_Player, new Vector3(0, -3, 0), Quaternion.identity);
                //Setting Spawn Manager to active
                _SpawnManager.SetActive(true);
                //setting the title screen to active
                _Titlescreen.SetActive(false);
            }
        }
    }
    //The Update Lives void
    public void UpdateLives(int CurrentLives)
    {
        //Displaying lives in Console
        Debug.Log("Current Lives = " + CurrentLives);
        //Displaying lives in UI
        LivesImageDisplay.sprite = Lives[CurrentLives];
    }
    //Score Status Void
    public void ScoreStatus(int CurrentScore)
    {
        //Adding Score to the variable
        Score += CurrentScore;
        //displaying Score in console
        Debug.Log("CurrentScore = " + Score);
        //Displaying score in UI
        _ScoreDisplay.text = "Score: " + Score;
    }

    //Getting the scene to change back routine
    public IEnumerator GameOver()
    {
        yield return new WaitForSeconds(2.52f);
        SceneManager.LoadScene("StartScreen", LoadSceneMode.Single);
    }
}
