# Tell the user that this is a twitter beta and he needs to follow the steps
# Ask the user for his Username
# Check if the User name has an "@" in it
# If it does, print "Username complete" Else print"Username failed."
# Then Ask him For his password, And comfirm His Password.
# If the Passwords match, Move on. If they doen't match, kick him out
# Then ask Him for his tweet.
# If the tweet is less or equal to 140 characters, send the tweet.
# If the tweet is bigger then 140 characters, Tell him"Invalid length."

print("Welcome, this is a simi twitter beta program. please follow the steps.")
username = input("Please Enter Your Username: ")
if "@" in username:
    print("username complete.")
    password1 = input("Please Enter Your Password: ")
    password2 = input("Please Confirm Your Password: ")
    if password1 == password2:
        print("Password Complete.")
        tweet = input("Now you are complete, Enter your tweet: ")
        if len(tweet) >= 140:
            print("invalid length, try again.")
        else:
            print("Tweet sent.")
    else:
         print("Passwords don't match.")
    
else:
    print("Username failed,it has to be an Email.")




