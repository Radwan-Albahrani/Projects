# Sci-Fi Shooter Game

This game was created in the Unity Engine, and can only be played on computer devices. You can test it out for yourself [here](https://drive.google.com/file/d/1bAyWLWmLj8xMiGGk3SZAh4v5HWnL1kmV/view?usp=sharing). This game was also made to teach a class about game development fundamentals and C# Fundamentals. All scripts are made using C#.

You can find a link to the Youtube Demo [here](https://youtu.be/UkZGW-gn39k).

## Documentation

This section will describe how some of the code was created in brief. You can find the code above for more detail. All code has been commented on for easier understanding.

Each function starting with an underscore is only accessed through the current script and is considered private.

### Player.cs

This script is responsible for player actions. Mouse movement, character movement, collision detection with the coins and the shop, health management, and So on. The first section of the script declares all the necessary variables required. All of these variables are then assigned through the Unity interface. All necessary player components and UI images are pre-made on a canvas so they can be assigned to these variables. Variables are organized based on type, as you can see from the script.

Any components that cant be assigned through the unity engine are then acquired through the `GetComponent` Function. This was used to get the character controller, the NavMesh, the particles, the ammo text, the coin text, and then connect the script to the GameManager Script.

In the `update` Function (Which is called on each frame), All the required functions to make the character move and look and shoot are called as long as the player is still alive.

* The `_Movement` function is used to dictate player movement through the mesh. During the starting sequence, the player is not allowed to jump anywhere, as the NavMesh is more restrictive in that area.
* The `_MouseLook` Function moves the camera based on the mouse movement.
* The `_ManageWeapon` Function ensures the weapon can shoot at specific intervals (as to not just kill the ammo with one press of a button). The weapon is still an assault rifle so the interval is shot, but RayCasting can happen extremely quickly, which is why the weapon has to be limited with an interval either way. This function also checks for ammo, allows for reloading, does all the RayCasting logic, and manages reloading text.
* The `_ManageInventory` ensures the player has the coin or not.
* The `HealthSystem` Script manages losing health based on enemy action. It also connects with the GameManager script to display that health.
* The `Reloading` Coroutine is responsible for playing the reloading animation and returning max ammo to the player.
* `OnTiggerStay` is a built in function that checks if the user is within a collider. I used this function on the player script to check for the coin, the shop, and the door to start the game.
* `OnTriggerExit` Will reset UI elements when the user exits collider.

### GameManager.cs

This function is responsible for taking care of UI elements like Score, Health, and Objective. It will also make sure the game is over or still running based on the player health, acquired from the player script.

* `Update` function will check if the game is over, and play the death animation accordingly, as well as allow the player to start over when dead.
* `StartGame` Will start the game through the spawn manager, and allow for enemy spawning, as well as display the proper UI elements. It will also disable Navigation Restrictions for the player, as colliders will now take care of all the player restrictions.
* `ScoreUpdate` Will update the score each time an enemy dies. Each enemy is worth the amount of points given when the function is called, which allows for flexibility when adding enemies (since the score is not fixed). This function is also responsible for increasing the difficulty every 50 points.
* `HealthUpdate` Is responsible for displaying the correct amount of health on screen.
* `Objective` Is responsible for displaying the current player objective. It is also flexible because the objective is determined by a number given when the function is called.
* `GameOver` Will end the game.

Some routines are then given at the bottom of the script to add some dynamic animations in the game. Objectives don't just flicker away, they turn green then fade into the next objective. GameOver doesn't just happen, the death animation is played and then the GameOver screen is displayed.

### EnemyAI.cs

This script is very simple, as the only objective it has is ensure the enemies are tracking the player, and ensuring health is decreasing when the enemy hits the player. it is also responsible for playing enemy sound effects like the attack sound effect or the walking sound effect.

### SpawnManager.cs

This script is responsible for determining the location an enemy will spawn, as well as increase the difficulty when needed by decreasing time per spawn and radius of spawn to a minimum of 4 and a minimum of 1 second.

## Images
![Game Image](../../../../_Images/Sci-fi%20Shooter%201.png)
![Game Image 2](../../../../_Images/Sci-fi%20Shooter%202.png)
