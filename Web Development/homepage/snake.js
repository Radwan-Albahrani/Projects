const board_border = 'black';
const board_background = "lightgreen";
const snake_col = 'lightblue';
const snake_border = 'darkblue';

let snake = 
[
    {x: 200, y: 200},
    {x: 180, y: 200},
    {x: 160, y: 200},
    {x: 140, y: 200},
    {x: 120, y: 200}
]


// keeping track of score
let score = 0;

// Keeping track of food position
let food_x;
let food_y;

// When not moving, Make it false.
let changing_direction = false;

// Horizontal velocity
let dx = 20;
// Vertical velocity
let dy = 0;

// Get the canvas element
const snakeboard = document.getElementById("snakeboard");

// type cast the canvas 2d context then get it from snakeboard.
/** @type {CanvasRenderingContext2D} */
const snakeboard_ctx = snakeboard.getContext("2d");

// Adding focus to the snakeboard to prevent scrolling when focussed.
snakeboard.tabIndex = 1

// Prevent scrolling from any keydown event if canvas in focus.
snakeboard.addEventListener("keydown", function(event)
{
    event.preventDefault();
}

)

// Change canvas size based on screen
snakeboard.width = window.innerWidth - 50;
snakeboard.height = window.innerHeight - 300;

// generate food
generate_food()

// Start game
main();

// Add event listener to listen for key down.
document.addEventListener("keydown", control_snake)
// main function called repeatedly to keep the game running
function main() 
{
    if (End_Game()) 
    {
        element = document.getElementById("Score");
        element.innerText = score + " Game Over"
        element.style.color = "red";        
        document.getElementById("restart").style.visibility = "visible";
        return;
    }
    changing_direction = false;
    setTimeout(function onTick() 
    {
        clearCanvas();
        drawFood();
        move_snake();
        drawSnake();
        // Call main again
        main();
    }, 100)
    
}


// draw a border around the canvas
function clearCanvas() {

    //  Select the colour to fill the drawing
    snakeboard_ctx.fillStyle = board_background;

    //  Select the colour for the border of the canvas
    snakeboard_ctx.strokestyle = board_border;

    // Changing line width for the rectangle
    snakeboard_ctx.lineWidth = 10;

    // Draw a "filled" rectangle to cover the entire canvas
    snakeboard_ctx.fillRect(0, 0, snakeboard.width, snakeboard.height);

    // Draw a "border" around the entire canvas
    snakeboard_ctx.strokeRect(0, 0, snakeboard.width, snakeboard.height);

    // Changing Line width back to 1 for snake.
    snakeboard_ctx.lineWidth = 1;
}

// Draw the snake on the canvas
function drawSnake() 
{
    // Draw each part
    snake.forEach(drawSnakePart)
}

// Draw one snake part
function drawSnakePart(snakePart) 
{

    // Set the colour of the snake part
    snakeboard_ctx.fillStyle = snake_col;
    // Set the border colour of the snake part
    snakeboard_ctx.strokestyle = snake_border;
    // Draw a "filled" rectangle to represent the snake part at the coordinates
    // the part is located
    snakeboard_ctx.fillRect(snakePart.x, snakePart.y, 20, 20);
    // Draw a border around the snake part
    snakeboard_ctx.strokeRect(snakePart.x, snakePart.y, 20, 20);
}

function drawFood()
{
    // Choose color of the food
    snakeboard_ctx.fillStyle = 'red';

    // choose border of the food
    snakeboard_ctx.strokestyle = 'darkred';

    // Draw food based on given snake food location
    snakeboard_ctx.fillRect(food_x, food_y, 20, 20);
    snakeboard_ctx.strokeRect(food_x, food_y, 20, 20);
}

// End game if conditions for ending game have been met.
function End_Game()
{
    // declare the head.
    let head = snake[0];

    // Check if head has collided with any of the other snake parts.
    for (let i = 4; i < snake.length; i++) 
    {
        if (snake[i].x === head.x && snake[i].y === head.y) 
        {
            return true;
        }
    }
    
    // Check if head has collided with any of the walls
    const hitLeftWall = head.x < 0;
    const hitRightWall = head.x > snakeboard.width - 20;
    const hitTopWall = head.y < 0;
    const hitBottomWall = head.y > snakeboard.height - 20;
    
    // if collided with walls, end game.
    return hitLeftWall || hitRightWall || hitTopWall || hitBottomWall;
}

// Move the snake constantly in a direction.
function move_snake() 
{
    // Snake can only move if element is active.
    if (document.activeElement == snakeboard)
    {

        // Create the new Snake's head
        const head = {x: snake[0].x + dx, y: snake[0].y + dy};

        // Insert new head at start of the snake array
        snake.unshift(head);

        // Check if snake has eaten.
        const has_eaten_food = head.x === food_x && head.y == food_y;

        // If it does eat
        if(has_eaten_food)
        {
            // Increase score and show it on screen.
            score += 10;
            document.getElementById("Score").innerText = score;

            // Generate new food.
            generate_food()
        }
        else
        {
            // Pop last element in array.
            snake.pop();
        }

    }
}

// Control the snake
function control_snake(event)
{
    // Declare keycodes for arrow keys.
    const LEFT_KEY = 37;
    const RIGHT_KEY = 39;
    const UP_KEY = 38;
    const DOWN_KEY = 40;

    // if the snake is already changing direction, get out.
    if (changing_direction) return;

    // Check if canvas is focussed, and if not, get out.
    if (!(document.activeElement === snakeboard)) return;
    
    // Set changing direction to true and start changing direction
    changing_direction = true;

    // Get the pressed key
    const keyPressed = event.keyCode;

    // checks to make sure snake cant reverse on itself.
    const goingUp = dy === -20;
    const goingDown = dy === 20;
    const goingLeft = dx === -20;
    const goingRight = dx === 20;

    // If user pressed arrpw keys, move the snake to that direction accordingly
    if (keyPressed === LEFT_KEY && !goingRight) 
    {
        dx = -20;
        dy = 0;
    }
    if (keyPressed === RIGHT_KEY && !goingLeft) 
    {
        dx = 20;
        dy = 0;
    }
    if (keyPressed === UP_KEY && !goingDown) 
    {
        dx = 0;
        dy = -20;
    }

    if (keyPressed === DOWN_KEY && !goingUp) 
    {
        dx = 0;
        dy = 20;
    }
}

function random_food(max)
{
    // Get a random number within the range of the board.
    return Math.round(Math.random() * (max) / 20 ) * 20
}

function generate_food()
{
    // Get an X value using random number function within the board.
    food_x = random_food(snakeboard.width - 40);

    // Get a Y value using random number function within the board.
    food_y = random_food(snakeboard.height - 40);

    // Check if if generated number is part of the snake, and if so, generate again.
    snake.forEach(function has_eaten_food(part)
    {
        const has_eaten = part.x == food_x && part.y == food_y;
        if(has_eaten) generate_food();
    })
}

// restart function
function Restart()
{
    // hide button
    document.getElementById("restart").style.visibility = "hidden";
    
    // reset snake
    snake = 
    [
        {x: 200, y: 200},
        {x: 180, y: 200},
        {x: 160, y: 200},
        {x: 140, y: 200},
        {x: 120, y: 200}
    ]

    // reset variables.
    score = 0;
    dx = 20;
    dy = 0;
    
    // reset score text
    element = document.getElementById("Score");
    element.innerText = score
    element.style.color = "white";   

    // generate food
    generate_food()

    // Start game
    main();
}
