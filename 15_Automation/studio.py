"""
===========================================================
AI Studio Pro v1.4
Main Application

Author : Pritam Kumar
===========================================================
"""

from config import EPISODES_DIR, CHARACTERS_DIR

from modules.dashboard import show_dashboard
from modules.menu_manager import show_menu
from modules.episode_manager import create_episode
from modules.character_manager import create_character
from modules.list_manager import list_characters
from modules.database_manager import initialize_database


def main():

    # Initialize SQLite Database
    initialize_database()

    while True:

        # Dashboard
        show_dashboard()

        # Menu
        show_menu()

        # User Input
        choice = input("\nSelect Option : ").strip()

        # -------------------------------------------------
        # 1. NEW EPISODE
        # -------------------------------------------------

        if choice == "1":

            try:

                number = int(input("\nEpisode Number : "))

                create_episode(EPISODES_DIR, number)

                print("\n✅ Episode Created Successfully.\n")

            except ValueError:

                print("\n❌ Please enter a valid episode number.\n")

        # -------------------------------------------------
        # 2. NEW CHARACTER
        # -------------------------------------------------

        elif choice == "2":

            name = input("\nCharacter Name : ").strip()

            if name:

                create_character(CHARACTERS_DIR, name)

            else:

                print("\n❌ Character name cannot be empty.\n")

        # -------------------------------------------------
        # 3. LIST CHARACTERS
        # -------------------------------------------------

        elif choice == "3":

            list_characters(CHARACTERS_DIR)

        # -------------------------------------------------
        # 4. PROMPT MANAGER
        # -------------------------------------------------

        elif choice == "4":

            print("\n🚧 Prompt Manager (Coming Soon)\n")

        # -------------------------------------------------
        # 5. ASSET MANAGER
        # -------------------------------------------------

        elif choice == "5":

            print("\n🚧 Asset Manager (Coming Soon)\n")

        # -------------------------------------------------
        # 6. METADATA GENERATOR
        # -------------------------------------------------

        elif choice == "6":

            print("\n🚧 Metadata Generator (Coming Soon)\n")

        # -------------------------------------------------
        # 7. BACKUP PROJECT
        # -------------------------------------------------

        elif choice == "7":

            print("\n🚧 Backup Project (Coming Soon)\n")

        # -------------------------------------------------
        # 8. EXIT
        # -------------------------------------------------

        elif choice == "8":

            print("\n👋 Thank you for using AI Studio Pro.\n")
            break

        # -------------------------------------------------
        # INVALID OPTION
        # -------------------------------------------------

        else:

            print("\n❌ Invalid option.")
            print("Please choose a number between 1 and 8.\n")


if __name__ == "__main__":
    main()