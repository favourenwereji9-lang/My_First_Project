my_list = ["mummy", "hannah", "mom", "murder for a jar of red rum", "clown", "seagull", "tomatto","no lemon","some men intrerpret nine memos", "madam"]
for items in my_list:
    clean_items = items.lower().replace(" ", "").replace(" ", "")


    if clean_items == clean_items[::-1]:
        print(f"{items} ia a palindrome")
    else:
        print(f"{items} is not a palindrome")

