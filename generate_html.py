import json
import os
import config
from typing import TypedDict, List

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

marvel_folder = os.path.join(os.getcwd(), config.CHARACTERS_DATA_PATH)
marvel_characters = [os.path.join(marvel_folder, file_name) for file_name in os.listdir(marvel_folder)]
links = []
PADDING = "\n\t\t"

footer = f"""
    <footer id="page-footer">
        <a href="{config.DISCORD_SERVER}">FCRO Discord Server</a>
    </footer>"""

def generate_characters(marvel_characters, links, footer):
    for character in marvel_characters:
        with open(character, "r") as f:
            character_data: Character = json.loads(f.read())
        
        filename = character.split("/")[-1].replace(".json", ".html")

        marvel_characters_path = os.path.join(os.getcwd(), config.OUTPUT_PATH, config.CHARACTERS_URL_PATH)
        if not os.path.exists(marvel_characters_path):
            os.mkdir(marvel_characters_path)
        
        filename = os.path.join(marvel_characters_path, filename)

        with open(filename, "w") as f:
            f.write(f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="../styles.css">
        <title>{character_data['name']}</title>
    </head>
    <body>
        <ul id='navbar'>
            <li><a href="../index.html">Home</a></li>
            <li><a href="../about.html">About</a></li>
        </ul>
        <h1>{character_data['name']}</h1>
        <h2>Earth {character_data['earth']}</h2>
        <img id='character-picture' src='{character_data['imageURL']}' alt='{character_data['imageDescription']}' />
        <h2>Also known as:</h2>
        <ul id='aka-list'>
            {PADDING.join(['<li class="aka-item">' + alias + '</li>' for alias in character_data['aliases']])}
        </ul>

        <h3>Created By:</h3>
        <ul>
            {PADDING.join(['<li>' + creator['name'] + ': ' + creator['title'] + '</li>' for creator in character_data['creators']])}
        </ul>
        <h3>Description:</h3>
        <p>{character_data['description']}</p>

        <div class="header-container">
        <h3>Appearances:</h3>
        <select name="Order" id="order-changer">
            <option value="newfirst">Newest first</option>
            <option value="oldfirst">Oldest first</option>
        </select>
        </div>
        <ul id='appearances'>
            {PADDING.join(['<li>' + appearance + '</li>' for appearance in character_data['appearances']])}
        </ul>

        {footer}

        <script src='character.js'></script>
    </body>
    </html>
    """)
        
        links.append(f"<li><a href='{config.CHARACTERS_URL_PATH + '/' + filename.split('/')[-1]}'>{character_data['name'] + ' (' + ', '.join(character_data['aliases']) + ')'}</a></li>")

def generate_index(links, footer):
    filename = os.path.join(os.getcwd(), config.OUTPUT_PATH, "index.html")

    with open(filename, "w") as f:
        f.write(f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="styles.css">
        <title>FCRO</title>
    </head>
    <body>
        <ul id='navbar'>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About</a></li>
        </ul>
        <h1>Welcome to the FCRO website!</h1>
        <p>Brief description of the website</p>
        
        <h3>List of characters</h3>
        <ul>
            {PADDING.join(links)}
        </ul>

        {footer}
    </body>
    </html>""")
    
def generate_about(footer):
    filename = os.path.join(os.getcwd(), config.OUTPUT_PATH, "about.html")
    with open(filename, "w") as f:
        f.write(f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="styles.css">
        <title>About</title>
    </head>
    <body>
        <ul id='navbar'>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About</a></li>
        </ul>
        <h1>About us</h1>
        <p>Brief description</p>
        <h3>Sonar</h3>
        <p>Brief description</p>
        <h3>Ace Coronet</h3>
        <p>Brief description</p>
        
        {footer}
    </body>
    </html>
    """)
    
if __name__ == "__main__":
    if not os.path.exists(os.path.join(os.getcwd(), config.OUTPUT_PATH)):
        os.mkdir(os.path.join(os.getcwd(), config.OUTPUT_PATH));
    
    generate_characters(marvel_characters, links, footer)
    generate_index(links, footer)
    generate_about(footer)
