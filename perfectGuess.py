import random
n= random.randint(1,100)
a=-1
guesses=0
while (a!=n):
   guesses+=1
   a =int(input("Guess a number :"))
   if(a<=0 or a>100):
        print("Please enter number in range 1 to 100 :")
   elif(a<n):
        print ("Higher number please:")
     
   elif(a>n):
        print ("Lower number please :")
   elif(a==n):
       print (f"you have Guessed number correctly in {guesses} attempt :")
       break 