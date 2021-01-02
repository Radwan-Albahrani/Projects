using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{
    //Ui Elements
    [SerializeField]
    private Text _Score;
    [SerializeField]
    private Text _Health;
    [SerializeField]
    private Text _Objective;
    
    //Variables
    public int CurrentHealth;
    private int _CurrentScore;
    private int _DifficultyScore;
    private float _DieRotation;
    private float _DieSpeed = 0.5f;

    //Checks
    private bool _IsGameOver = false;
    private bool _isDead = false;
    private bool _Transition = false;

    //GameObjects
    [SerializeField]
    private GameObject _Gameover;

    // Start is called before the first frame update
    void Start()
    {
        //Resetting UI elements
        _Health.text = null;
        _Score.text = null;
        _Gameover.SetActive(false);
    }

    //Called Every Frame
    private void Update()
    {
        //Check if the Game is Over
        if(_IsGameOver == true)
        {
            //Wait for player to press Space
            if (Input.GetKeyDown(KeyCode.Space))
            {
                //Restart Game
                SceneManager.LoadScene("StartOver", LoadSceneMode.Single);
                _IsGameOver = false;
            }
        }
        //If Player is dead
        if(_isDead == true)
        {
            //Start adding Diespeed to Dierotation
            _DieRotation += _DieSpeed;
            //Rotate the camera up using the DieRotation
            Camera.main.transform.rotation = Quaternion.Euler(transform.localEulerAngles.x - _DieRotation, transform.localEulerAngles.y, transform.localEulerAngles.z);
        }
        
    }

    //Starting the Game Void
    public void StartGame(string LoadSceneName)
    {
        //Swap Scenes
        StartCoroutine(LoadingScene(LoadSceneName));
        //Start the SpawnManager
        SpawnManager Go = GameObject.Find("SpawnManager").GetComponent<SpawnManager>();
        Go.StartGame();
        //Display Score 0
        _Score.text = "Score: 0";
        //Display Current Health
        _Health.text = "Health: " + CurrentHealth;
        //Disabling the player's Navigation Agent
        Player Nav = GameObject.Find("Player").GetComponent<Player>();
        Nav.Navigation.enabled = false;
    }

    //Updating The Score in the UI
    public void ScoreUpdate(int Score)
    {
        //Add recieved Score to Current Score
        _CurrentScore += Score;
        //Display Score
        _Score.text = "Score: " + _CurrentScore;
        //Add Score to Difficulty Score
        _DifficultyScore += Score;
        
        //If we reach a score of:
        if(_DifficultyScore == 50)
        {
            //Get the SpawnManager Script
            SpawnManager Difficulty = GameObject.Find("SpawnManager").GetComponent<SpawnManager>();
            //Increase Difficulty of game
            Difficulty.IncreaseDifficulty();
            //Reset Difficulty Score
            _DifficultyScore = 0;
        }
    }

    //Updaing Health in the UI
    public void HealthUpdate(int Health)
    {
        //Update the UI Health using Recieved Health From player
        _Health.text = "Health: " + Health;
        //Make Current Health = to this recieved Health
        CurrentHealth = Health;
    }

    //Updating The Objective
    public void Objective(int ObjectiveNum)
    {
        //If The game just started
        if(ObjectiveNum == 0)
        {
            //Shot the first objective
            _Objective.text = "Objective: Get The Coin";
        }

        //If its not the first objective
        else
        {
            //Start Fading out and giving the objective
            _Transition = true;
            //In case the player finishes objectives too fast, make sure to show the previous, just finished objective.
            if (ObjectiveNum - 1 == 1)
            {
                //Show the Second objective
                _Objective.text = "Objective: Buy Your Weapon";
            }

            if (ObjectiveNum - 1 == 2)
            {
                //Show the Third Objective.
                _Objective.text = "Objective: Go through The door leading to the lab";
            }

            if (ObjectiveNum - 1 == 3)
            {
                //Show the forth objective.
                _Objective.text = "Objective: Survive";
            }
            //Stop the previous coroutine
            StopCoroutine(ChangeObjective(ObjectiveNum - 1));
            //Start the new coroutine with the correct objective num
            StartCoroutine(ChangeObjective(ObjectiveNum));
        }
    }

    //Game Over
    public void GameOver()
    {
        //Start the Game Over Coroutine
        StartCoroutine(StartGameOver());
    }

    //Game Over Coroutine
    IEnumerator StartGameOver()
    {
        //Set Isdead to true to start Death Anim
        _isDead = true;
        yield return new WaitForSeconds(1);
        //Speed Up Death Anim by a bit
        _DieSpeed += 0.5f;
        yield return new WaitForSeconds(1);
        //Set is dead to false to stop rotation
        _isDead = false;
        //Teleport Camera Away from Everything
        Camera.main.transform.position = new Vector3(300, 200, 300);
        //Reset Camera Rotations
        Camera.main.transform.localEulerAngles = new Vector3(0, 0, 0);
        //Enable GameOver text
        _Gameover.SetActive(true);
        //Set The Game over to true.
        _IsGameOver = true;

    }
    //Objective Change coroutine
    IEnumerator ChangeObjective(int ObjectiveNum)
    {
        //Set The color to Green
        _Objective.color = Color.green;
        //Start Fading out.
        while (_Transition)
        {
            //make a color variable so that you are able to modify it
            Color newColor = _Objective.color;
            //Reduce the alpha part of the color by an amount till it fades out in a duration of 2 seconds
            newColor.a -= Time.deltaTime / 2;
            //Set the Color to this new color
            _Objective.color = newColor;
            //If it reaches 0 or below
            if(newColor.a <= 0)
            {
                //Set it back to 0
                newColor.a = 0;
                //Stop the loop
                _Transition = false;
            }
            yield return null;
        }

        if (ObjectiveNum == 1)
        {
            //Show the Second objective
            _Objective.text = "Objective: Buy Your Weapon";
        }

        if (ObjectiveNum == 2)
        {
            //Show the Third Objective.
            _Objective.text = "Objective: Go through The door leading to the lab";
        }

        if(ObjectiveNum == 3)
        {
            //Show the forth objective.
            _Objective.text = "Objective: Survive";
        }

        //Set the color to red but keep it transparent
        _Objective.color = new Color(1, 0, 0, 0);
        //Start fading in.
        while (!_Transition)
        {
            //Set the color to a variable so you can modify it
            Color newColor = _Objective.color;
            //Start adding Opacity to the Color in a matter of 2 seconds
            newColor.a += Time.deltaTime / 2;
            //Set the color to the new color
            _Objective.color = newColor;
            //If the color has reached 1 or higher yet.
            if (newColor.a >= 1)
            {
                //Stop the loop
                _Transition = true;
                //Set it back to 1
                newColor.a = 1;
            }
            yield return null;
        }
    }
   
    IEnumerator LoadingScene(string LoadSceneName)
    {
        //Start Loading the Wanted Scene in the background
        AsyncOperation loadscene = SceneManager.LoadSceneAsync(LoadSceneName, LoadSceneMode.Additive);

        //Wait for the scene to fully load.
        while(loadscene.progress != 1f)
        {
            Debug.Log("Loading Scene. Progress: " + loadscene.progress);
            yield return null;
        }
        
        //Get the needed scene from the scene name given
        Scene SceneToLoad = SceneManager.GetSceneByName(LoadSceneName);

        //Check if the scene is valid
        if (SceneToLoad.IsValid())
        {
            //After scene loads, teleport player to correct position
            GameObject.Find("Player").transform.position = new Vector3(-10f, 3f, 10f);
            GameObject.Find("Player").transform.localEulerAngles = new Vector3(0, 0, 0);


            //Find the necessary gameobjects and move them to the new scene
            SceneManager.MoveGameObjectToScene(GameObject.Find("Player"), SceneToLoad);
            SceneManager.MoveGameObjectToScene(GameObject.Find("Canvas"), SceneToLoad);
            SceneManager.MoveGameObjectToScene(GameObject.Find("GameManager"), SceneToLoad);
            SceneManager.MoveGameObjectToScene(GameObject.Find("SpawnManager"), SceneToLoad);

            //Get The previous Scene
            Scene PreviousScene = SceneManager.GetActiveScene();

            //Unload Previous scene.
            SceneManager.UnloadSceneAsync(PreviousScene);

            //Activate the New scene
            SceneManager.SetActiveScene(SceneToLoad);
        }
    }
}

