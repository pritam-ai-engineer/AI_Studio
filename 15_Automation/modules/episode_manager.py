from utils.logger import log

FILES = [
    "Script.md",
    "Scenes.md",
    "Prompt.md",
    "Thumbnail.md",
    "Metadata.md",
]


def create_episode(base_path, episode_number):

    episode = base_path / f"Episode_{episode_number:03d}"

    episode.mkdir(parents=True, exist_ok=True)

    for file in FILES:
        (episode / file).touch(exist_ok=True)

    log(f"Episode {episode_number:03d} Created")

    print(f"\n✅ Episode_{episode_number:03d} Created\n")