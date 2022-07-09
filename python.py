print("Welcome to Quizzie Rascals")
playing=input("Do you want to play? ")
if playing.lower()!="Yes":
    quit()
print("Okay lets play: ") 
score=0  
answer1=input("What the does the CPU stands for? ")
if answer1.lower()=="cental processing unit" :
    print("correct") 
    score+=1
else:
    
    print("incorrect")      
answer2=input("What the does the PSU stands for? ")
if answer2.lower()=="power supply unit" :
    print("correct") 
    score+=1
else:
  
    print("incorrect")    
answer3=input("What the does the RAM stands for? ")  
if answer3.lower()=="random Access memory" :
    print("correct") 
    score+=1    
else:
    print("incorrect")    
answer4=input("What the does the GUI stands for? ")  
if answer4.lower()=="graphic user interface" :
    print("correct")
    score+=1 
else:
    print("incorrect")  

print( "You have scored " + str(score))
print( "You have scores " + str((score/5 )* 100)+ "%") 

