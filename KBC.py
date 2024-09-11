# ALL QUESTION FUNCTIONS

def q1():
  print("Your First question for 1,000 is on your screen\n")
  print("What is the capital of India?\n")
  print("a. Mumbai", "b. New Delhi",end=" ")
  print("c. Chennai", "d. Kolkata\n")

  x=input("Your answer:")
  if x=="b":
    print("\nCongratulations! You have won Rs.1,000\nLet's move to the next question.")
    q2()
  elif x=="q":
    print("You Take home Rs. 0")
    return
  else:
     print("Sorry! You have lost the game")


def q2():
  print("Next question for Rs.2,000 on your screen\n")
  print("What Language is this code for KBC written in?\n")
  print("a. C++", "b. Java",end=" ")
  print("c. Python", "d. HTML\n")
  x=input("Your answer:")
  if x=="c":
    print("\nCongratulations! You have won Rs.2,000\nLet's move to the next question.")
    q3()
  elif x=="q":
    print("You Take home Rs.1,000")
    return
  else:
    print("Sorry! You have lost the game")

def q3():
  print("Next question for Rs.3,000 on your screen\n")
  print("Name the highest Mountain Peak in the world?")
  print("a. Mount Everest", "b. K2",end=" ")
  print("c. Kangchenjunga", "d. Lhotse\n")
  x=input("Your answer:")
  if x=="a":
    print("\nCongratulations! You have won Rs.3,000\nLet's move to the next question.")
    q4()
  elif x=="q":
    print("You Take home Rs.2,000")
    return
  else:
    print("Sorry! You have lost the game")

def q4():
  print("Next question for Rs.5,000 on your screen\n")
  print("Total States in India?\n")
  print("a. 25", "b. 28",end=" ")
  print("c. 30", "d. 27\n")
  x=input("Your answer:")
  if x=="b":
    print("\nCongratulations! You have won Rs.5,000\nLet's move to the next question.")
    q5()
  elif x=="q":
    print("You Take home Rs.3,000")
    return
  else:
     print("Sorry! You have lost the game")

def q5():
  print("Next question for Rs.10,000 on your screen\n")
  print("Which god is also known as ‘Gauri Nandan’?\n")
  print("a. Agni", "b. Indra",end=" ")
  print("c. Hanuman", "d. Ganesha\n")
  x=input("Your answer:")
  if x=="d":
    print("\nCongratulations! You have won Rs.10,000\nLet's move to the next question.")
    q6()
  elif x=="q":
    print("You Take home Rs.5,000")
    return
  else:
    print("Sorry! You have lost the game")

def q6():
  print("Next question for Rs.20,000 on your screen\n")
  print("Who wrote India's National Anthem?\n")
  print("a. Rabindrabath Tagore", "b. R.K Narayan",end=" ")
  print("c. Chetan Bhagat", "d. Lal Bahadur Shastri\n")
  x=input("Your answer:")
  if x=="a":
    print("\nCongratulations! You have won Rs.20,000\nLet's move to the next question.")
    q7()
  elif x=="q":
    print("You Take home Rs.10,000")
    return
  else:
    print("Sorry! You have lost the game")

def q7():
  print("Next question for Rs.40,000 on your screen\n")
  print("Which city is known as Pink City in India?\n")
  print("a. Banglore", "b. Mysore",end=" ")
  print("c. Jaipur", "d. Ahemdabad\n")
  x=input("Your answer:")
  if x=="c":
    print("\nCongratulations! You have won Rs.40,000\nLet's move to the next question.")
    q8()
  elif x=="q":
    print("You Take home Rs.20,000")
    return
  else:
    print("Sorry! You have lost the game")

def q8():
  print("Next question for Rs.80,000 on your screen\n")
  print("When is the National Hindi Diwas celebrated?\n")
  print("a. 13 september", "b. 14 september",end=" ")
  print("c. 14 july", "d. 15 august\n")
  x=input("Your answer:")
  if x=="b":
    print("\nCongratulations! You have won Rs.80,000\nLet's move to the next question.")
    q9()
  elif x=="q":
    print("You Take home Rs.40,000")
    return
  else:
    print("Sorry! You have lost the game")

def q9():
  print("Next question for Rs.1,60,000 on your screen\n")
  print("Who wrote Vande Mataram?\n")
  print("a. Sarat Chandra Chattopadhya", "b. Rabindranath Tagore",end=" ")
  print("c. Bankim Chandra Chatterjee", "d. Ishwar Chandra Vidyasagar\n")
  x=input("Your answer:")
  if x=="c":
    print("\nCongratulations! You have won Rs.1,60,000\nLet's move to the next question.")
    q10()
  elif x=="q":
    print("You Take home Rs.80,000")
    return
  else:
     print("Sorry! You have lost the game")

def q10():
  print("Next question for Rs.3,20,000 on your screen\n")
  print("How many major religions are there in India?\n")
  print("a. 5", "b. 6",end=" ")
  print("c. 7", "d. 8\n")
  x=input("Your answer:")
  if x=="b":
    print("\nCongratulations! You have won Rs.3,20,000\nLet's move to the next question.")
    q11()
  elif x=="q":
    print("You Take home Rs.1,60,000")
    return
  else:
    print("Sorry! You have lost the game")

def q11():
  print("Next question for Rs.6,40,000 on your screen\n")
  print("Which one has never been the state of India?\n")
  print("a. Goa", "b. Vrindachal",end=" ")
  print("c. Uttranchal", "d. Chattisgarh\n")
  x=input("Your answer:")
  if x=="b":
    print("\nCongratulations! You have won Rs.6,40,000\nLet's move to the next question.")
    q12()
  elif x=="q":
    print("You Take home Rs.3,20,000")
    return
  else:
    print("Sorry! You have lost the game")

def q12():
  print("Next question for Rs.12,50,000 on your screen\n")
  print("The National Stadium in Delhi was earlier known by the name?\n")
  print("a. Irwin Stadium", "b. Mountbatton Stadium",end=" ")
  print("c. Wellington Stadium", "d. Canning Stadium\n")
  x=input("Your answer:")
  if x=="a":
    print("\nCongratulations! You have won Rs.12,50,000\nLet's move to the next question.")
    q13()
  elif x=="q":
    print("You Take home Rs.6,40,000")
    return
  else:
    print("Sorry! You have lost the game")

def q13():
  print("Next question for Rs.25,00,000 on your screen\n")
  print("The largest Buddhist Monastery in India is located at?\n")
  print("a. Sarnath,U.P", "b. Tawang, Arunanchal Pradesh",end=" ")
  print("c. Dharmshala, Himachal Pradesh", "d. Gangtok,Sikkim\n")
  x=input("Your answer:")
  if x=="b":
    print("\nCongratulations! You have won Rs.25,00,000\nLet's move to the next question.")
    q14()
  elif x=="q":
    print("You Take home Rs.12,50,000")
    return
  else:
    print("Sorry! You have lost the game")

def q14():
  print("Next question for Rs.50,00,000 on your screen\n")
  print("Which Indian monument was originally built as a victory tower to commemorate the defeat of the Khan of Khambhat?\n")
  print("a. Qutub Minar", "b. India Gate",end=" ")
  print("c. Char Minar", "d. Vijay Stambha\n")
  x=input("Your answer:")
  if x=="d":
    print("\nCongratulations! You have won Rs.50,00,000\nLet's move to the next question.")
    q15()
  elif x=="q":
    print("You Take home Rs.25,00,000")
    return
  else: 
    print("Sorry! You have lost the game")

def q15():
  print("Next question for Rs.1,00,00,000 on your screen\n")
  print("Who among the following was killed during 'Operation Bluestar' of 1984?\n")
  print("a. Baba Santa Singh", "b. Haji Mastan",end=" ")
  print("c. Homi Jehangir Bhabha", "d. Jarnail Singh Bhindrawale\n") 
  x=input("Your answer:")
  if x=="d":
    print("\nCongratulations! You have won Rs.1,00,00,000\nLet's move to the next question.")
    q16()
  elif x=="q":
    print("You Take home Rs.50,00,000")
    return
  else:
    print("Sorry! You have lost the game")

def q16():
  print("Next question for Rs.7,00,00,000 on your screen\n")
  print("Which former Indian President died as a result of a road accident?\n")
  print("a. Giani Zail Singh", "b. Faqruddin Ali Ahmed",end=" ")
  print("c. Rajendra Prasad", "d. R.Venkataraman\n")
  x=input("Your answer:")
  if x=="a":
    print("\nCongratulations! You have won Rs.7,00,00,000\nHere is your cheque!\nThank You for playing KBC")
  elif x=="q":
    print("You Take home Rs.1,00,00,000")
    return
  else:
    print("Sorry! You have lost the game")

# MAIN BODY FROM HERE


print("Welcome to Kaun Banega Crorepati\nHere,you have to answer 16 questions\nand you have a chance to win 7 crore\n")
print("If at any question you feel you don't know the answer\nthen you can quit the game by pressing 'q'!\n")
print("Choose correct option by typing that alphabet only!\n")
a=input("Are you ready to play? Y/N:")
if (a=="N" or a=="n"):
  print("Goodluck for next Time")
elif (a=="Y" or a=="y"):
  print("Okay,lets start\n")
  q1()
else:
  print("Invalid Input")
