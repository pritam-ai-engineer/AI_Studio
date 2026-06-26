from config import EPISODES_DIR
from modules.episode_manager import create_episode

def main():

    print("="*50)
    print("AI STUDIO PRO")
    print("="*50)

    create_episode(EPISODES_DIR,5)

    print("Episode Created Successfully")

if __name__=="__main__":
    main()