reels_array = []
recent_activity_array = []
    
#Add part number to list 
def add_reel():
    part_number = input ("Please enter a part #: ")
    reels_array.append(part_number.upper())
    print(part_number.upper() + " has been added!\n")
    recent_activity_array.append(part_number.upper() + " was added to shortage list" )
    #Ask user if they would like to input another part number
    def add_repeat():
        add_repeat_question = input ("Would you like to add another? (y/n) : ")
        if  add_repeat_question.lower() == "y" :
            add_reel()
        elif add_repeat_question.lower() == "n" :
            print("")
            main()
        else:
            print("Enter a valid response!")
            add_repeat()
    add_repeat()
            
#Delete part number from list           
def delete_reel():
    #Ask user if they would like to input another part number
    def delete_repeat():
        if len(reels_array)  == 0:
            print("The list is now empty!\n")
            main()
        else:
            delete_repeat_question = input ("Would you like to remove another? (y/n) : ")
            if  delete_repeat_question.lower() == "y" :
                delete_reel()
            elif delete_repeat_question.lower() == "n" :
                print("")
                main()
            else:
                print("Enter a valid response!")
                delete_repeat()
    if len(reels_array) == 0:
        print("No reels to remove!\n")
        main()
    else:
        part_number = input ("Please enter a part #: ").upper()
        if part_number in reels_array:
            reels_array.remove(part_number.upper())
            print(part_number.upper() + " has been removed!\n")
            recent_activity_array.append(part_number.upper() + " was removed from shortage list" )
            delete_repeat()
        else:
            print("Part number not found in list please enter another! \n")
            delete_reel()
        
#Display reels_array as list        
def view_list():
    if len(reels_array) == 0 :
        print("List is empty!\n")
        main()
    else:
        print('\n'.join(reels_array))
        print()
        main()

#Display all recent activity    
def recent_activity():
    if len(recent_activity_array) == 0:
        print("No recent activity!\n")
        main()
    else:
        print('\n'.join(recent_activity_array))
        print()
        main()
            
def main():
    print ("What would you like to do? ")
    print ("a) Add reel")
    print ("b) Remove reel")
    print ("c) See list")
    print("d) Recent activity")
    print("e) Quit program")
    action_choice = input ("\nPlease enter your selection: ")
    if action_choice.lower() == "a" and len(action_choice) == 1:
        add_reel()
    elif action_choice.lower() == "b" and len(action_choice) == 1:
        delete_reel()
    elif action_choice.lower() == "c" and len(action_choice) == 1:
        view_list()
    elif action_choice.lower() == "d" and len(action_choice) == 1:
        recent_activity()
    elif action_choice.lower() == "e" and len(action_choice) == 1:
        quit()
    else:
        print("Enter a valid response!\n")
        main()
        
main()

