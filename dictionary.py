from PyDictionary import PyDictionary

dictonary = PyDictionary()

while True:
    dict_choice = int(input("Enter your choice:\n[1] Synonym\n[2] Antonym\n"))
    
    if (dict_choice == 1):
        word = input("Enter word for it's synonym (or q to quit): ")
        print(dictonary.synonym(word))
    
    elif (dict_choice == 2):
        word = input("Enter word for it's antonym (or q to quit): ")
        print(dictonary.antonym(word))

    else:
        print("Invaild input, try again!")