import pygame  #imports pygame
from random import randint  #allows usage of the random library 
from sys import exit   #allows proper exit logic 

#The line initializes pygame 
pygame.init()

# The function below conveniently moves our obstacles (enemies) using a timer 
# It iterates through a list that contains the obstacle rectangles 
def obstacleMovement(obstacle_list): 
    if obstacle_list: # check if the list is empty 
        for obsRect in obstacle_list: 
            obsRect.x -= 5 # every single obstacle will be moved to the left 

            screen.blit(monster, obsRect) # continuosuly spawns monster 1 
           
        #line below only copies an item in list if x > 0 ; effectively deletes monsters to from far left
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list       
    else: return[] # return an empty list   

#the function below keeps track of the player's running animation. It alternates between 4 images 
def playerAnimations():
    global player, player2, player3, player2, playerIdx, playerJump
    if(player_rect.bottom < 320): 
        player = playerJump #if player is jumping
    else: 
        playerIdx += 0.1
        if(playerIdx >= len(playerRunning)):
            playerIdx = 0
        player = playerRunning[int(playerIdx)]

#the function below keeps track of the flying monster animation. It alternates between 4 images 
def flying_animation(): 
    global flying_monster, flying_monster2, flying_monster3, flying_monster4, flying_monster_index

    flying_monster_index += 0.1
    if(flying_monster_index >= len(flying_monster_list)):
        flying_monster_index = 0
    flying_monster = flying_monster_list[int(flying_monster_index)]

#The function below keeps track of the ground monster. It alternates between 2 images using a timer 
def monster_animation():
    global monster, monster2, monster_index
    monster_index += 0.1
    if(monster_index >= len(monsterList)): 
        monster_index = 0
    monster = monsterList[int(monster_index)]

#The function below keeps track of collision and the player's health 
def collision_check(player_rect, obstacle_list, flying_monster_rect):
    global hearts

    if player_rect.colliderect(flying_monster_rect):
        hearts -= 1
        flying_monster_rect.x = -100

    for obsRect in obstacle_list: 
        if player_rect.colliderect(obsRect):
            hearts -= 1
            obstacle_list.remove(obsRect)
        
    if hearts == 0:   #if player is dead
        return False
        
    return True

#The function below resets the game state after the gameover screen 
def reset_game():
    global hearts, isAlive, obstacle_rect_list, player_rect, player_gravity
    isAlive = True
    hearts = 3  # Reset hearts
    obstacle_rect_list.clear()  # Clear obstacles
    player_rect.midbottom = (300, 320)  # Reset player position
    player_gravity = 0  # Reset gravity


print ("Code works")  # tests compilability
screen = pygame.display.set_mode((800, 400))   #initializes display surface
pygame.display.set_caption('Stick Runner') 

#boolean game state 
isAlive = True

#create a clock object 
clock = pygame.time.Clock() 

#this statically creates the monster start postion 
monsterXPOS = 400

#we use this to keep player on the floor 
player_gravity = 0

#create a surface w plain color 
sky_surface = pygame.image.load('Desktop/Python/sampleProject/SampleGame/Images/SKY.jpg').convert_alpha()
sky_surface = pygame.transform.scale(sky_surface, (1000,800))

#this creates the ground 
ground_surface = pygame.image.load('Desktop/Python/sampleProject/SampleGame/Images/ground3.png').convert_alpha()
ground_surface = pygame.transform.scale(ground_surface, (1000,400))    

#this creates the ground monster
monster = pygame.image.load('Desktop/Python/sampleProject/SampleGame/Images/monsters/frame1.png').convert_alpha()
monster2 = pygame.image.load('Desktop/Python/sampleProject/SampleGame/Images/monsters/frame2.png').convert_alpha()
monster = pygame.transform.scale(monster, (30, 30))
monster2 = pygame.transform.scale(monster2, (30, 30))
monsterList = [monster, monster2]
monster_index = 0
monster_moving = monsterList[monster_index]
monster_rect = monster.get_rect(bottomright = (monsterXPOS, 320))

#line below imports the flying monster 
flying_monster = pygame.image.load('Desktop/Python/sampleProject/SampleGame/Images/flying_monsters/transparents/flying/frame-1.png').convert_alpha()
flying_monster2 = pygame.image.load('Desktop/Python/sampleProject/SampleGame/Images/flying_monsters/transparents/flying/frame-2.png').convert_alpha()
flying_monster3 = pygame.image.load('Desktop/Python/sampleProject/SampleGame/Images/flying_monsters/transparents/flying/frame-3.png').convert_alpha()
flying_monster4 = pygame.image.load('Desktop/Python/sampleProject/SampleGame/Images/flying_monsters/transparents/flying/frame-4.png').convert_alpha()

flying_monster = pygame.transform.scale(flying_monster, (30,30))
flying_monster2 = pygame.transform.scale(flying_monster2, (30,30))
flying_monster3 = pygame.transform.scale(flying_monster3, (30,30))
flying_monster4 = pygame.transform.scale(flying_monster4, (30,30))

flying_monster_rect = flying_monster.get_rect(midbottom = (500,250))

flying_monster_list = [flying_monster, flying_monster2, flying_monster3, flying_monster4]
flying_monster_index = 0
flying_monster_animation = flying_monster_list[flying_monster_index]

#code below shows the obstacles
obstacle_rect_list =  [] # create an empty list  

#import player player
player = pygame.image.load('Desktop/Python/sampleProject/SampleGame/Images/gbtemplate/Idle.png').convert_alpha()
player2 = pygame.image.load('Desktop/Python/sampleProject/SampleGame/Images/gbtemplate/Run.png').convert_alpha()
player3 = pygame.image.load('Desktop/Python/sampleProject/SampleGame/Images/gbtemplate/Run2.png').convert_alpha()
player4 = pygame.image.load('Desktop/Python/sampleProject/SampleGame/Images/gbtemplate/Run3.png').convert_alpha()
playerJump = pygame.image.load('Desktop/Python/sampleProject/SampleGame/Images/gbtemplate/Jump2.png').convert_alpha()

playerIdx = 0
player = pygame.transform.scale(player, (40, 50))
player2 = pygame.transform.scale(player2, (40, 50))
player3 = pygame.transform.scale(player3, (40, 50))
player4 = pygame.transform.scale(player4, (40, 50))
playerJump = pygame.transform.scale(playerJump, (40, 50))

playerRunning = [player, player2, player3, player4] #creates a list that holds player animations

player_rect = player.get_rect(midbottom = (300,320))  #takes a surface and draw a rectangle around it 

#line below imports the death screen
skull = pygame.image.load('Desktop/Python/sampleProject/SampleGame/Images/game_over.png').convert_alpha()
skull = pygame.transform.scale(skull, (350,350))

#The lines below imports the hearts 
heart_full1 = pygame.image.load('Desktop/Python/sampleProject/SampleGame/Images/heart.png').convert_alpha()
heart_full1 = pygame.transform.scale(heart_full1, (40, 40))
#2nd heart
heart_full2 = pygame.image.load('Desktop/Python/sampleProject/SampleGame/Images/heart.png').convert_alpha()
heart_full2 = pygame.transform.scale(heart_full2, (40, 40))
#3rd heart
heart_full3 = pygame.image.load('Desktop/Python/sampleProject/SampleGame/Images/heart.png').convert_alpha()
heart_full3 = pygame.transform.scale(heart_full3, (40, 40))

#We start the game with 3 hearts 
hearts = 3 

#create a user event via timer. This is for better enemy spawn 
obstacle_timer = pygame.USEREVENT + 1; #add 1 to avoid conflict with dedicated USEREVENT for pygame
pygame.time.set_timer(obstacle_timer, 1500) #trigger obstavle timer every 1500 milliseconds

#the code below is for the monster animation timer 
monster_timer = pygame.USEREVENT + 2
pygame.time.set_timer(monster_timer, 300)

while True:  #entire game will run in this loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #"x" button 
            pygame.QUIT  #closes; opposite of pygame init 
            exit()
    #draw elements and update eveything 
        if(isAlive):
            #code below manipulates player movement  
            #this creates a key input 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:  # checks if buttons were pressed 

                    if(player_rect.bottom == 320): player_gravity = -10
                
                if event.key == pygame.K_RIGHT: 
                    
                    player_rect.x += 20

                if event.key == pygame.K_LEFT: 
                        
                    player_rect.x -= 20
        else: 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: reset_game()

        if isAlive:        
            if event.type == obstacle_timer: 
                
                obstacle_rect_list.append(monster.get_rect(bottomright = (randint(900, 1100), 320))) #copies monster rectagnle to timer 
        
    
    if (isAlive):
        screen.blit(sky_surface, (-100,-100)) # blitz splits surface 
        screen.blit(ground_surface, (-10,50))
        
        #the lines below displays the hearts 
        if(hearts ==  1):
            screen.blit(heart_full1, (10, 10))
        if(hearts == 2):
            screen.blit(heart_full1, (10, 10)) 
            screen.blit(heart_full2, (50, 10))
        if(hearts ==3):
            screen.blit(heart_full3, (90, 10))
            screen.blit(heart_full2, (50, 10))
            screen.blit(heart_full1, (10, 10)) 
        #code below spawns the running character
        screen.blit(player, player_rect) 
        player_gravity += 0.5  #constantly fall
        player_rect.y += player_gravity #apply gravit y to y axis of pig rectangle
        if (player_rect.bottom >= 320): 
            player_rect.bottom = 320
        
        playerAnimations()
        flying_animation()
        monster_animation()

        #code below spawns the flying monster
        screen.blit(flying_monster, flying_monster_rect)   
        flying_monster_rect.x += 3

        #The line below keeps spawning flying monster on left side 
        if flying_monster_rect.x > 800:
            flying_monster_rect.x = -100

        # The line below takes care of obstacle movement 
        obstacle_rect_list = obstacleMovement(obstacle_rect_list) #ovewrite obstacle rect list using obstacleMovement function

        #This line checks if player collides
        isAlive = collision_check(player_rect,  obstacle_rect_list, flying_monster_rect)

    else: 
        screen.fill('BLACK') #display black screen if game is over 
        screen.blit(skull, (210, 20))
         
    pygame.display.update()   # keeps updating the display surface 
    clock.tick(60) #ensures constant 60 fps 
  

