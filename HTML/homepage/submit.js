let testingvar = true;

function fadeout() 
{
    // Getting Required elements
    var AlertDiv = document.getElementById("SuccessAlert");
    var AlertText = document.getElementById("alert");
    var email = document.getElementById("email").value
    var subject = document.getElementById("subject");
    var comment = document.getElementById("comment");

    // Checking if any elements are null.
    if (AlertDiv == null || AlertText == null || email == null || subject == null)
    {
        console.log("Cannot find Item");
    }
    
    // Testing Email using Regular expression
    const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    let test = re.test(email);
    
    // If email not passed, Tell user through alert, then show
    if(!test)
    {
        AlertText.innerHTML = "<strong> Email Incorrect. </strong> Please try again.";
        AlertDiv.classList.add("alert-warning", "show");
        
    }
    
    // If subject not found, Tell user through alert, then show
    else if (subject.value == "")
    {
        AlertText.innerHTML = "<strong> Subject Required. </strong> Please try again."
        AlertDiv.classList.add("alert-warning", "show"); 
    }
    
    // If no comment, Tell user through alert, then show
    else if(comment.value == "")
    {
        AlertText.innerHTML = "<strong> Comment Empty. </strong> Please try again."
        AlertDiv.classList.add("alert-warning", "show");
    }
   
    // If all fields filled. Run success function.
    else
    {
        success(AlertDiv, AlertText);
    }
    
}

function success(AlertDiv, AlertText)
{
    // Hide any visible alerts.
    AlertDiv.classList.add("hide"); 
    
    // Sleep for 1 second, then return timeout promise.
    sleep(1000).then
    (() => 
    {
        // Remove any unwanted classes
        AlertDiv.classList.remove("hide", "show", "alert-warning"); 

        // Change alert Text
        AlertText.innerHTML = "<strong> Email Sent. </strong> We will get back to you shortly.";
        
        // Show alert as Success Alert
        AlertDiv.classList.add("show", "alert-success");

        // Get all input elements on the page.
        var fields = document.getElementsByTagName('input');

        // Get length of these elements.
        length = fields.length;
        
        // Loop for all input elements
        while (length--) 
        {
            // If it has any text, reset it.
            fields[length].value = ''; 
            
        }
        
        // Reset comment value as well.
        comment.value = ""; 
    }
    );
}

// Sleep function from the internet.
function sleep(ms)
{
    return new Promise(resolve => setTimeout(resolve, ms));
}