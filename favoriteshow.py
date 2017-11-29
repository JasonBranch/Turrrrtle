print ("Your Favorite Show")
print ("Answer the questions below to play the game.")


# variables containing all of your story info
yourshow = raw_input("What is your favorite show")
maincharacter = raw_input("Who is the main character ")
transportation = raw_input("Name a mode of transportation")
bestscene = raw_input("Describe the best episode")
dancemove = raw_input("What is your favorite dance move")
yourenemy = raw_input("Who is your enemy")
name = raw_input("What is your name")

# story here
story = "Your favorite show " + yourshow + " is not better than Seinfeld. Its not even close. If " + maincharacter + "used a" \
+ transportation + "in a foot race with Jerry they would still lose." + bestscene + \
" is still not better than when George ate a donut out the garbage. On top of that Elaine definitely do" \
 + dancemove + "better than anyone you know.Chances are the reason you and " + yourenemy + "aren't friends is because you prefer" \
  + yourshow + "over Seinfeld. Shame on you" + name + "."

print (story)

