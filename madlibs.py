print("Welcome to Madlibs :)")
print("Instructions: Its's Easy! Fill in the given blanks with words in the paragraph")
n = int(input("Enter '1' to start or '0'to exit: "))
if(n==1):
    print("The Dog is a __________ animal. It is one of the most obedient animals. \
    There are many kinds of __________ in the world. Some of the are very friendly while \
    some of them a dangerous. Dogs are of different color __________ black, red, white \
    and brown. Some old them have slippery shiny skin and some have __________ skin. \
    Dogs are carnivorous animals. They like eating meat. They have four legs, two \
    ears and a tail. Dogs are trained to perform different tasks. They protect us \
    from thieves __________ our house. They are __________ animals. A dog is called \
    man’s best __________ . They are used by the police to find hidden things. \
    They are one of the most useful animals in the world.")

    adj = input("1) Enter the adjuctive: ")
    noun1 = input("2) Enter Noun 1: ")
    verb1 = input("4) Enter Verb 1: ")
    verb2 = input("5) Enter Verb 2: ")
    gerund1 = input("6) Enter the 1st 'ing' word: ")
    gerund2 = input("7) Enter the 2nd 'ing' word: ")
    noun2 = input("3) Enter Noun 2: ")
    
    madlibs = f"The Dog is a {adj} animal. It is one of the most obedient animals. \
    There are many kinds of {noun1} in the world. Some of the are very friendly while \
    some of them a dangerous. Dogs are of different color {verb1} black, red, white \
    and brown. Some old them have slippery shiny skin and some have {verb2} skin. \
    Dogs are carnivorous animals. They like eating meat. They have four legs, two \
    ears and a tail. Dogs are trained to perform different tasks. They protect us \
    from thieves {gerund1} our house. They are {gerund2} animals. A dog is called \
    man’s best {noun2}. They are used by the police to find hidden things. \
    They are one of the most useful animals in the world."
    print(madlibs)

else:
    print("You Exited, Have a nice day!")

