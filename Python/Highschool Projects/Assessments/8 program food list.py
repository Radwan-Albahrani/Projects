listoffood = ["Chicken","Tomato","Rice","Rotten Flesh","fish","expired chips"]
like_food = []
dislike_food = []

for liked in listoffood:
    if liked == "Rotten Flesh" or liked == "expired chips":
        dislike_food.append(liked)
    else:
        like_food.append(liked)
print("liked foods: " + str(like_food))
print("disliked foods: " +str(dislike_food))
