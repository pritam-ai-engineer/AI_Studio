from config import EPISODES_DIR, CHARACTERS_DIR

from modules.menu_manager import show_menu
from modules.episode_manager import create_episode
from modules.character_manager import create_character
from modules.list_manager import list_characters


def main():

    while True:

        show_menu()

        choice = input("\nSelect Option : ").strip()

        if choice == "1":

            try:
                number = int(input("Episode Number : "))
                create_episode(EPISODES_DIR, number)

            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "2":

            name = input("Character Name : ").strip()

            if name:
                create_character(CHARACTERS_DIR, name)
            else:
                print("❌ Character name cannot be empty.")

        elif choice == "3":

            list_characters(CHARACTERS_DIR)

        elif choice == "8":

            print("\nThank you for using AI Studio Pro.")
            break

        else:

            print("\n❌ Invalid option. Choose 1–8.")


if __name__ == "__main__":
    main()