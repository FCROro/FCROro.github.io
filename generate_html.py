import json
import os
import config
from typing import TypedDict, List
from jinja2 import Environment, FileSystemLoader

TEMPLATE_DIR = os.path.join(os.getcwd(), config.TEMPLATES_PATH)


class Creator(TypedDict):
    name: str
    title: str

class Character(TypedDict):
    name: str
    imageURL: str
    imageDescription: str
    aliases: List[str]
    earth: str
    description: str
    creators: List[Creator]
    appearances: List[str]
    endpoint: str


def load_characters() -> List[Character]:
    marvel_folder = os.path.join(os.getcwd(), config.CHARACTERS_DATA_PATH)
    marvel_characters = [os.path.join(marvel_folder, file_name) for file_name in os.listdir(marvel_folder)]

    characters: List[Character] = []
    for character in marvel_characters:
        with open(character, "r") as f:
            character_data: Character = json.loads(f.read())

        filename = character.split("/")[-1].replace(".json", ".html")

        marvel_characters_path = os.path.join(os.getcwd(), config.OUTPUT_PATH, config.CHARACTERS_URL_PATH)
        if not os.path.exists(marvel_characters_path):
            os.mkdir(marvel_characters_path)
        
        character_data["endpoint"] = f"{config.CHARACTERS_URL_PATH}/{filename}"
        characters.append(character_data)
    return characters

if __name__ == "__main__":
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    index = env.get_template("index.jinja")
    about = env.get_template("about.jinja")
    character = env.get_template("character.jinja")
    characters = load_characters()

    with open(os.path.join(os.getcwd(), config.OUTPUT_PATH, "index.html"), "w") as f:
        f.write(index.render(characters=characters))

    with open(os.path.join(os.getcwd(), config.OUTPUT_PATH, "about.html"), "w") as f:
        f.write(about.render())

    for character_data in characters:
        with open(os.path.join(os.getcwd(), config.OUTPUT_PATH, character_data["endpoint"]), "w") as f:
            f.write(character.render(character=character_data))
