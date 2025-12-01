import random

rooms = {
    "Hall": "A wide hall with old paintings on the wall. 🖼️",
    "Kitchen": "A messy kitchen with broken utensils. 🍴",
    "Garden": "A peaceful garden with cool breeze. 🌿",
    "Library": "A silent room filled with dusty books. 📚",
    "Basement": "A dark basement… you hear faint noises. 🕳️"
}

treasure_room = random.choice(list(rooms.keys()))
lives = 3

print("===== TREASURE HUNT GAME 🏆 =====")
print("Find the treasure hidden in one of the rooms.")
print("You have 3 lives.\n")

while lives > 0 and len(rooms) > 0:
    print("Rooms Available:")
    for r in rooms:
        print(" -", r)

    choice = input("\nEnter room name: ").strip().title()

    if choice not in rooms:
        print("❌ Invalid or Already Visited room! Try again.\n")
        continue

    print(f"\nYou entered the {choice}...")
    print(rooms[choice])

    if choice == treasure_room:
        print("\n🎉 Congratulations! You found the treasure 🏆")
        print("YOU WIN!")
        break
    else:
        lives -= 1
        print("\n❌ No treasure here!")
        print("Lives left:", lives, "❤️\n")

        # Remove room after entering
        del rooms[choice]

if lives == 0:
    print("\n💀 GAME OVER! The treasure was in:", treasure_room)
elif len(rooms) == 0:
    print("\n📦 All rooms explored but no treasure found!")
    print("The treasure was in:", treasure_room)
