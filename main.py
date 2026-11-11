def create_player():
    return {
        "energy": 5,
        "location": "Beach",
        "has_rope": False,
        "has_lantern": False
    }


def take_action(player, choice):
    location = player["location"]
    messages = []
    outcome = None

    if choice == "1":
        if location == "Jungle":
            player["location"] = "Beach"
            player["energy"] -= 1
            messages.append("You have returned to the Beach.")

        elif location == "Beach":
            messages.append("You are already on the Beach.")

        else:
            messages.append(
                "You must return to the Jungle before going to the Beach."
            )

    elif choice == "2":
        if location in ("Beach", "Cave"):
            player["location"] = "Jungle"
            player["energy"] -= 1
            messages.append("You are now in the Jungle.")

        elif location == "Jungle":
            messages.append("You are already in the Jungle.")

        else:
            messages.append(
                "You cannot go directly to the Jungle from here."
            )

    elif choice == "3":
        if location in ("Jungle", "Old Bridge"):
            player["location"] = "Cave"
            player["energy"] -= 1
            messages.append("You have entered the Cave.")

        elif location == "Cave":
            messages.append("You are already in the Cave.")

        else:
            messages.append(
                "You must reach the Jungle or Old Bridge first."
            )

    elif choice == "4":
        messages.append("Thanks for playing Mystery Island!")
        outcome = "quit"

    elif choice == "5":
        if location == "Beach":
            if not player["has_rope"]:
                player["has_rope"] = True
                messages.append("You found a rope on the Beach!")
                messages.append("Rope added to your inventory.")

            else:
                messages.append("You already have the rope.")

        else:
            messages.append(
                "You must be on the Beach to find the rope."
            )

    elif choice == "6":
        if location == "Cave" and player["has_rope"]:
            player["location"] = "Old Bridge"
            player["energy"] -= 1
            messages.append("You crossed the Old Bridge!")

        elif location == "Lighthouse":
            player["location"] = "Old Bridge"
            player["energy"] -= 1
            messages.append("You returned to the Old Bridge.")

        elif location == "Old Bridge":
            messages.append("You are already at the Old Bridge.")

        elif location == "Cave":
            messages.append(
                "You need a rope to cross the Old Bridge."
            )

        else:
            messages.append(
                "You must reach the Cave or Lighthouse first."
            )

    elif choice == "7":
        if location == "Cave":
            if not player["has_lantern"]:
                player["has_lantern"] = True
                messages.append(
                    "You found a lantern inside the Cave!"
                )
                messages.append(
                    "Lantern added to your inventory."
                )

            else:
                messages.append("You already have the lantern.")

        else:
            messages.append(
                "You must be in the Cave to find the lantern."
            )

    elif choice == "8":
        if location == "Old Bridge":
            player["location"] = "Lighthouse"
            player["energy"] -= 1
            messages.append(
                "You have reached the Lighthouse!"
            )

        elif location == "Lighthouse":
            messages.append(
                "You are already at the Lighthouse."
            )

        else:
            messages.append(
                "You must reach the Old Bridge first."
            )

    elif choice == "9":
        if location == "Lighthouse" and player["has_lantern"]:
            messages.append(
                "Congratulations! You activated the Lighthouse!"
            )
            messages.append("YOU WIN!")
            outcome = "win"

        elif location != "Lighthouse":
            messages.append(
                "You must reach the Lighthouse first."
            )

        else:
            messages.append(
                "You need a lantern to activate the Lighthouse."
            )

    else:
        messages.append(
            "Invalid choice. Please try again."
        )

    if player["location"] != location:
        messages.append(
            f"Your remaining energy is: {player['energy']}"
        )

    if player["energy"] <= 0:
        messages.append(
            "Game Over! You have run out of energy."
        )
        outcome = "lose"

    return messages, outcome


def main():
    print("Welcome to Mystery Island!")

    name = input("What is your name? ")

    play_again = True

    while play_again:
        player = create_player()

        print("\nWelcome,", name)
        print("Your energy is:", player["energy"])
        print("Your current location is:", player["location"])

        print("\nYou wake up on a mysterious island.")
        print("You are standing on the Beach.")
        print(
            "The lighthouse is dark, and you need to restore its light."
        )

        while True:
            print("\nWhat would you like to do?")
            print("1. Explore the Beach")
            print("2. Go to the Jungle")
            print("3. Go to the Cave")
            print("4. Quit Game")
            print("5. Search for Rope")
            print("6. Go to the Old Bridge")
            print("7. Search for Lantern")
            print("8. Go to the Lighthouse")
            print("9. Activate the Lighthouse")

            choice = input("Enter your choice (1-9): ")

            messages, outcome = take_action(player, choice)

            for message in messages:
                print(message)

            if outcome is not None:
                break

        answer = input(
            "\nWould you like to play again? (yes/no): "
        )

        if answer.strip().lower() == "yes":
            print("\nRestarting game...")

        else:
            play_again = False
            print(
                "Goodbye! Thanks for playing Mystery Island!"
            )


if __name__ == "__main__":
    main()