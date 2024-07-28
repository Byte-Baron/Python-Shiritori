print("\n" * 40)
print("Welcome to the Shiritori (q for exit)\n")
def shiritori():
    used_words = []
    last_character = ''
    
    while True:
        current_word = input("Your word : ")
        print()

        if current_word == "q":
            break
        
        elif current_word in used_words:
            print("\nYou have already used that word! Try again.\n")
            continue

        elif last_character and current_word[0].lower() != last_character.lower():
            print(f"\nThe word must start with '{last_character}'. Try again.\n")
            continue

        used_words.append(current_word)
        last_character = current_word[-1]
        print(f"You said: {current_word}\n")

shiritori()
