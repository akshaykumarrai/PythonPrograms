import random

def guess_my_number(total_attempts , start_range ,end_range ):
  if start_range>end_range :
    start_range,end_range = end_range,start_range
    
  random_number = random.randint(start_range , end_range)
  no_of_attempts = 0
  winning_message = " Yay! You are awesome as you guessed correctly "
  losing_message  = " Sorry ! You lost and no attempts left "
  missed_message =  "Ooops You Missed That's incoorect"
  
  
  num_tries= 0
  while num_tries<total_attempts :
    attempt=in(input("Guess the number"))
    
    if attempt == random_number:
      print(wining_message)
      return
    print(miss_message)
    
    if attempt<random_number:
      print("Go higher ! ")
    else:
      print("Go lower !")
    num_tries +=1
  print(losing_message)
  
  
guess_your_number(total_attempts, start_range, end_range)  
