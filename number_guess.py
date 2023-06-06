import random
import math

def guessNo():
   number = 101
   count = 0
   lower = int(input("enter the lower bound value: "))
   upper = int(input("enter the upper bound value: "))
   guessNum = random.randint(lower,upper)
   
   print(f"you have {round(math.log(upper-lower+1,2))} guesses")
   
   while(count<math.log(upper-lower+1,2)):
       count+=1
    
       number = int(input("enter a no. between 1-100: "))
       
       if(guessNum>number):
           print("the no. is smaller please enter a greater no.")
           
       elif(guessNum<number):
           print("the no. is greater please enter a smaller no.")
           
       elif(guessNum==number):
           print(f"you guessed the no. correct in {count} guesses and the no. was {guessNum}")
           break
   if (count>=math.log(upper-lower+1,2)):
        print(f"Your guesses are over and the no. was {guessNum}")     
           
guessNo()