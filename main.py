import random


"""
1 for Snake 
-1 for water 
0 for gun

"""
computer = random.choice([-1, 0, 1])

youstr =input("Enter your choice Type s for snake , w for water and g for gun :")
youDict= {
    "s":1,
    "w":-1,
    "g":0
}
reverseDict ={
        -1: "Water",
         1: 'Snake',
         0:"Gun",
}
you =youDict[youstr]
print(f"You chose: { reverseDict[you]}.\n Computer Chose : { reverseDict[computer]}.")
#shortcut way to get logic as below
# if (computer-you ==1) or (computer-you ==-2):#  -1
#           print("You Wins!")
# else :
#          print("You Lose!")

if (computer == you):
        print("It's a Draw !")
else :
  if((computer == -1) and (you==0)):#  -1
            print("You Lose!")
  elif ((computer == 0) and (you==-1)):#  1
            print("You Wins!")
  elif ((computer == 0) and (you==1)):#  -1
             print("You Lose!")
  elif ((computer == 1) and (you==0)):#  1
         print("You Wins!")
  elif ((computer == 1) and (you== -1)):#  2
                 print("You Lose!")
  elif ((computer == -1) and (you== 1)):#  -2
        print("You Wins!")
  else:       
        print("enter valid choice :")



