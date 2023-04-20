import random
# version 1.1.1
       # Do you remember those days when we used to play cricket with our fingers?  
       # Those were some of the best times, filled with happy memories. 
       # This is a 1v1 offline finger cricket game that I made using Python.
       # You can play it with your friend and recall those 
       # sweet memories of childhood. Enjoy!

class Player1:
   runs = 0
   def __init__(self, computer):
      self.computer = computer

   def play(self, player):
      self.user = player
      
      while True:
         if self.computer == self.user:
            print("OUT!")
            print("Total Score:",Player1.runs)
            print("-------------------")
            break
         elif (0<=self.user<=6):
            Player1.runs+=self.user
            print("Score:",Player1.runs)
            self.computer = random.randint(0,6)  
            self.user = int(input("Enter Number between 0 to 6: "))  
                  
         else:
            print("!!! Please enter valid digit bewtween 0 to 6 !!!")   
            self.computer = random.randint(0,6) 
            self.user = int(input("Enter Number between 0 to 6: "))
            

class Player2:
   runs = 0
   def __init__(self, computer):
      self.computer = computer

   def play(self, player, player1):
      self.user = player
      
      while True:
         if self.computer == self.user:
            print("OUT!")
            print("Total Runs:",Player2.runs)
            print("-------------------")
            if player1.runs == Player2.runs:
                print("Draw!!!")
            else:    
                print("Player1 WIN!!!")
            break
         elif (0<=self.user<=6):
            Player2.runs+=self.user
            print("Score:",Player2.runs) 
            if player1.runs < Player2.runs:
               print("-------------------")
               print("Player2 WIN!")
               break
            else:   
               self.computer = random.randint(0,6)       
               self.user = int(input("Enter Number between 0 to 6: "))  
                           
         else:
            print("!!! Please enter valid digit bewtween 0 to 6 XXX !!!")   
            self.computer = random.randint(0,6) 
            self.user = int(input("Enter Number between 0 to 6: "))
            


#-------------------------------------------------------------------------------   
rand = random.randint(0,6)  

print("-------Let's  Play-------")
print("----Player1's Batting----")
print("-------------------------")

p1 = Player1(rand)
player = int(input("Enter Number between 0 to 6: "))
p1.play(player)

rand = random.randint(0,6)  

print("-Player2's Batting-")
print("-------------------")
player = int(input("Enter Number between 0 to 6: "))

p2 = Player2(rand)
p2.play(player, p1)