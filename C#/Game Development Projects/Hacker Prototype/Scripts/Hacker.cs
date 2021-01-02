using UnityEngine;

public class Hacker : MonoBehaviour
{
    //Game Data Configuration.
    string[] _Level1Passwords = { "Students", "Teachers", "Learning", "Sciences", "School" };
    string[] _Level2Passwords = { "Money and Cash", "Lots of Food", "Sodas Everyday", "Chips and Chill", "Profit Counting" };
    string[] _Level3Passwords = { "Killers on the Loose", "Many More Vacations for Free", "Livestream Killing Off Innocents", "Purchase Guns Right Here", "Black Market Society Online" };

    string _Password;
    //Game State
    private int _CurrentLevel = 0;
    enum Screen
    {
        MainMenu, Password, WorldDominationIntro, WorldDomination2, WorldDomination3, WorldDomination4, Win
    }
    Screen _CurrentScreen = Screen.MainMenu;

    // Start is called before the first frame update
    void Start()
    {
        ShowMainMenu();
    }

    //Get the user input and put it in a variable "Input" (called from other scripts, not yet introduced code)
    void OnUserInput(string input)
    {
        //If the user calls in the menu. Can Always Show main menu
        if (input == "menu" || input == "Menu")
        {
            //Show the menu
            ShowMainMenu();
        }

        //If we are on the main menu Screen, Allow for choice of levels and using easter eggs. Or even starting of the side story.
        if (_CurrentScreen == Screen.MainMenu)
        {
            //Allow user to choose from Main menu
            MainMenuOptions(input);
        }

        //If player is on the Password guessing screen, meaning has already selected a level
        else if (_CurrentScreen == Screen.Password)
        {
            PasswordCheck(input);
        }
        //When the game is won, You only have one option which is to type menu to go back to the main screen.
        else if (_CurrentScreen == Screen.Win)
        {
            if (input == "menu" || input == "Menu")
            {
                ShowMainMenu();
            }
        }
        else if (_CurrentScreen == Screen.WorldDominationIntro)
        {
            if (input == "y")
            {
                _CurrentScreen = Screen.WorldDomination2;
                Terminal.ClearScreen();
                Terminal.WriteLine("Very Well Then, We shall commence our plan. First, You will need to.");
            }
        }
    }

    //Show the main menu
    void ShowMainMenu()
    {
        //Setting the Game Screen State
        _CurrentScreen = Screen.MainMenu;
        //Clear The Terminal Screen
        Terminal.ClearScreen();
        //Start Showingf the Introduction statement
        Terminal.WriteLine("Well Well Well, We have got ourselves ahacker over here. What do you want to   Hack into good fella?");
        //Show different options of Difficulty
        Terminal.WriteLine("1 - School Internet");
        Terminal.WriteLine("2 - Grocery Store Accountant Computer");
        Terminal.WriteLine("3 - The Dark Web");
        //Ask Player to enter Their selection
        Terminal.WriteLine("Please Enter Selection Here: ");
    }

    //All The Main Menu Options.
    void MainMenuOptions(string input)
    {
        //If the user calls in the menu. Can Always Show main menu
        if (input == "menu" || input == "Menu")
        {
            //Show the menu
            ShowMainMenu();
        }

        //Handling Levels
        else if (input == "1" || input == "2" || input == "3")
        {
            //Converting input to int and storing it in _CurrentLevel
            _CurrentLevel = int.Parse(input);
            //Start password sequence.
            ShowPasswordIntro();
        }


        //These are all the easter eggs I shall add to the game
        else if (input == "Sally" || input == "sally")
        {
            Terminal.WriteLine("Ahh, The memory of a good time. Please Choose Something From the menu");
        }
        else if (input == "Trinity" || input == "trinity")
        {
            Terminal.WriteLine("Well.. Thats just something isnt it. Can't you just choose something from the menu? Geez.");
        }

        //Start the Side WD story
        else if (input == "World Domination")
        {
            TakeTheWorld();
        }

        //If user has no valid inputs
        else
        {
            //Ask to give a valid input
            Terminal.WriteLine("Please Type a Valid Number: ");
        }
    }

    //Show The Password Intro.
    void ShowPasswordIntro()
    {
        //Setting the Game Screen State
        _CurrentScreen = Screen.Password;
        //Clearing the screen
        Terminal.ClearScreen();
        //Choose password based on current level
        PasswordSelect();
        //Telling the user that the level has been chosen.
        Terminal.WriteLine("You Have Chosen Level: " + _CurrentLevel);
        //Telling the user to type the password
        Terminal.WriteLine("Please Type The password: Hint: " + _Password.Anagram());
    }

    //Selecting the password based on the level.
    void PasswordSelect()
    {
        switch (_CurrentLevel)
        {
            //If level is 1
            case 1:
                _Password = _Level1Passwords[Random.Range(0, _Level1Passwords.Length)];
                break;
            //If level is 2
            case 2:
                _Password = _Level2Passwords[Random.Range(0, _Level2Passwords.Length)];
                break;
            //If level is 3
            case 3:
                _Password = _Level3Passwords[Random.Range(0, _Level3Passwords.Length)];
                break;
        }
    }

    //Checking the password based on user input
    void PasswordCheck(string input)
    {
        //Make guesses for level. If guess is correct, go here
        if (input == _Password)
        {
            WinScreen();
        }
        //Make guesses for level one. If guess is wrong, Go here.
        else
        {
            Terminal.ClearScreen();
            ShowPasswordIntro();
        }
    }

    //This is the win screen.
    void WinScreen()
    {
        _CurrentScreen = Screen.Win;
        Terminal.ClearScreen();
        switch (_CurrentLevel)
        {
            case 1:
                Terminal.WriteLine(@"
  /^\
  |#|
 |===|
  |0|
  | |
 =====
_||_||_
");
                Terminal.WriteLine("You got Internet! To go back to the menu, Type: Menu");
                break;

            case 2:
                Terminal.WriteLine(@"
     _____________,-.___     _
     |____        { {]_]_]   [_]
     |___ `-----.__\ \_]_]_    . `
     |   `-----.____} }]_]_]_   ,
     |_____________/ {_]_]_]_] , `
                   `-'
");
                Terminal.WriteLine("Here, Have some Free Chocolate. Type:  Menu to go back!");
                break;

            case 3:
                Terminal.WriteLine(@"
         _______
        |.-----.|
        ||x . x||
        ||_.-._||
        `--)-(--`
       __[=== o]___
      |:::::::::::|\
      `-=========-`()
");
                Terminal.WriteLine("Welcome to the Dark Web, Master. Type: Menu to go back!");
                break;
        }

    }

    //Starting the Side Story
    void TakeTheWorld()
    {
        //Setting the Game Screen State
        _CurrentScreen = Screen.WorldDominationIntro;
        Terminal.ClearScreen();
        Terminal.WriteLine("Ah Yes my child. I see you have come!  The time has come for us to rise and    prosper, to take back whats ours. The   time has come to Rule again and take    over everything we know.");
        Terminal.WriteLine("Well then, You have come to the right  place. I shall guide you to the End of  the world. Step 1, we need to hack into the secret government operations. The   CIA. Are you up for the task?");
        Terminal.WriteLine("Y/N?");

    }


}
