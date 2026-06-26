from config import CHARACTERS_DIR, EPISODES_DIR, PROMPTS_DIR
from modules.stats_manager import count_directories, count_files

def show_dashboard():

    print("="*60)
    print("                 AI STUDIO PRO v1.3")
    print("="*60)

    print(f"Project      : Chimpanzee Crazy")
    print(f"Characters   : {count_directories(CHARACTERS_DIR)}")
    print(f"Episodes     : {count_directories(EPISODES_DIR)}")
    print(f"Prompt Files : {count_files(PROMPTS_DIR)}")

    print("="*60)
