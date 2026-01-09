# How to set up the website

These files should be uploaded under a branch called `development`. You should also set up GitHub Pages for this repository, so the repository name should be called `yourusername.github.io`. In addition, you should set up GitHub Actions on this project for automated uploading. Note that there is a limited amount of minutes you can use GitHub Actions for free each month, so I suggest uploading new information in bulk.

# How to change some of the text on the website

Head over to the `generate_html.py` script, where you will find a function for each web page. For example, if you want to edit your information, you can head over to the `generate_about` function, and edit the text between the `<p></p>` tags.

# How to change the graphics of the website

I only used one `.css` file, called `styles.css`, all pages use this file.

# How to edit the Discord link

The Discord server link is in the file `config.py`.

# How to add new characters information

Create a new file with the file extension `.json` under the `data` directory. The file schema should be as follows:

```json
{
    "name": "Character Name",
    "imageURL": "Image URL for the Character",
    "imageDescription": "A Description of the Image (i.e. Image from abc #n, Illustrated by xyz)",
    "aliases": ["A list of aliases", "like so"],
    "earth": "Earth Number (i.e. 616)",
    "description": "A Description of the Character",
    "creators": [
        {
            "name": "The name of a creator of the character",
            "title": "Their job in the creation of the character, for example writer"
        },
        {
            "name": "The name of a creator of the character",
            "title": "Their job in the creation of the character, for example illustrator"
        }
    ],
    "appearances": [
        "The list of all appearances in desending order, for example:",
        "xyz #3",
        "xyz #2",
        "xyz #1"
    ]
}
```