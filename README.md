# Networking Bingo Generator

Generates unique BINGO cards in printer-friendly HTML format based on a question bank.

See sample in `bingo-sheets.html`.

## How to use
### Requirements
* Python3
* [jinja2](https://jinja.palletsprojects.com/en/2.10.x/)  Python module.

### Instructions
* Run `py bingo-gen.py`.
* The following parameters can be modified in the script:
    * Questions used
    * Number of unique Bingo cards
* To change the look, modify the HTML/CSS in `bingo-header.html` and/or `bingo-page.html`.