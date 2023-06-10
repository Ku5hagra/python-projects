def lets_play_again():
    print("\nDo you Want to play again? (y or n)")

    answer=input(">").lower()
    if answer=='y':
        dark_room()
    else:
        exit()
def dark_room():
    print("\nYou are standing in a dark room.")
    print("There is a door to your left and another to your right.")
    print("Which door will you enter into?")
    print("Type 'l' to enter left door or type 'r' to enter right door")
    dark_room_ans=input(">").lower()
    if dark_room_ans=='l' :
        snake_room()
    elif dark_room_ans=='r' :
        monster_room()
    
def snake_room():
    print("\nThere is snake here.")
    print("Behind snake there is another door.")
    print("The snake is having its eggs!")
    print("Now What would you do?")
    print("Choose one of this options(1 or 2):")
    print("1). Take the eggs.")
    print("2). Taunt the snake")
    snake_room_ans=input(">")
    if snake_room_ans=='1' :
        print("You want eggs not the treasure! That's why snake killed you. *_*")
        print("Game Over!!")
        
        lets_play_again()
    elif snake_room_ans=='2' :
        treasure_room()

def monster_room():
    print("\nNow you have entered the room of the monster.")
    print("The monster is sleeping. Zzzzzzz!!")
    print("Behind the monster's room there is another door.")
    print("Now What would you do?")
    print("Choose one of this options(1 or 2):")
    print("1). Go through the next door silently.")
    print("2). Kill the monster and show it your courage!")
    monster_room_ans=input(">")
    if monster_room_ans=='2' :
        print("Monster was too hungry and strong, it ate you! *_*")
        print("Game Over!!")
        
        lets_play_again()
    elif monster_room_ans=='1' :
        treasure_room()

def treasure_room():
    print("\nWell done! you have reached the treasure room.")
    print("But the monkey sitting next to the treasure tells you that - ")
    print("'if you take this treasure with you, I will die!!'")
    print("Now What would you do?")
    print("Choose one of this options(1 or 2):")
    print("1). Still take the treasure with you.")
    print("2). Leave the treasure to protect the life of the monkey.")
    treasure_room_ans=input(">").lower()
    if treasure_room_ans=='1' :
        print("\nYou have become evil due to your greed! you don't deserve this treasure!")
        print("Game Over!!")
        lets_play_again()
    elif treasure_room_ans=='2' :
        print("You are good human being you can take this treasure with you and noone will be killed.")
        print("Congratulations!! you have won the game.")
        lets_play_again()
dark_room()

