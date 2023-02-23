import time


print("Input minutes:")
minutes=int(input())
print("Input seconds:")
seconds=int(input())


if seconds >60:
	print("Error: Seconds Input too large! Try 60 or less.")
	exit()
print("You have input:",minutes,"Minutes",seconds,"seconds")
print("Is that Correct? (Please use a simple 'yes' or 'no)")
Answer = str(input())


if Answer =="yes"or"Yes":
  print("Your timer has begun!")
else:
 print("Sorry about that. Please try again!")
 exit()

	
while seconds>-1:
 if seconds ==0:
	 minutes-=1
	 seconds+=60
 seconds-=1
 print("Minutes:",minutes,"Seconds:",seconds)
 time.sleep(1)
	
#Countdown 2.0 update plans below:
	
#import tkinter and design a countdown page to implement this.
#Add hours and try to learn how to keep the countdown on 1 line.
#Format time in 00:00:00

#Bugs
#Bug where if minutes = 0 and seconds = 0 the timer will resort to negative values.
#Try creating a check for this and ending the code if the check is met with a send away message.