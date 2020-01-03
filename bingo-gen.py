from jinja2 import FileSystemLoader, Environment, select_autoescape
import random

# The number of unique Bingo cards
num_cards = 20
questions = [
    "Ask someone: “What is the best piece of career advice you’ve received?”",
    "Ask someone: “What is the last book you finished reading?”",
    "Ask someone: “What would be the name of your autobiography?”",
    "Ask someone: “Who is your favorite musical artist?”",
    "Ask someone: “What is one food you could not give up?”",
    "Ask someone: “What award would you love to win and for what achievement?”",
    "Ask someone: “What is something you are proud of?”",
    "Ask someone: “What team are you on and what do you do?”",
    "Ask someone: “Tell me your life story in 1 minute.”",
    "Ask someone: “What would you do if you were not in tech?”",
    "Ask someone: \"What is your New Year resolution?\" ",
    "Ask someone: What's your favorite movie/song?",
    "Ask someone: What's the best Microsoft cafeteria?",
    "Ask someone: What's your favorite Microsoft perk?",
    "Ask someone: \"Where do you see yourself in 10 years?\"",
    "Ask someone: \"What is your favorite Microsoft product?\"",
    "Find someone who knows what “VAIL” stands for.",
    "Find someone who speaks more than one language.",
    "Find someone who plays an instrument!",
    "Find someone that’s done something that you’ve wanted to do.",
    "Find someone that’s worked here that has interned at Microsoft previously twice.",
    "Find someone who knows what “COSINE” stands for.",
    "Find someone that eats lunch with their team on a regular basis.",
    "Find someone that has gone on a hike longer than 5 miles in 2019.",
    "Find someone who does not have Instagram.",
    "Find someone who lives alone.",
    "Find someone who lives on the east side.",
    "Find someone who is not self hosting.",
    "Find someone who did not study computer science in school.",
    "Find someone who joined Microsoft after October 1, 2019!",
    "Find someone who can juggle!",
    "Find someone who shares a rare hobby with you.",
    "Find someone who is a middle child.",
    "Find someone who works on a tented project.",
    "Find someone who failed a phishing test.",
    "Find someone who is wearing Microsoft swag.",
    "Find someone who has a blog.",
    "Find someone who has 500+ LinedIn connections.",
    "Find someone who plays Pokemon Go.",
    "Find someone who flosses every day.",
    "Find someone who uses a reusable cup in the office!",
    "Find someone who drives an electric vehicle.",
    "Find someone who has been to more than 10 countries (other than the airport)."
    "Sing a catchy song out loud with a group of 5+ people!",
    "Introduce yourself to a member of COSINE leadership.",
    "Play 2 Minute-to-Win-it Games!",
    "Get a selfie with the cooking demonstration.",
    "Mark this square if more than 7 people put you down as an answer.",
    "Play 2 truths and a lie with someone!",
]

env = Environment(
    loader = FileSystemLoader("."),
    autoescape=select_autoescape(['html', 'xml'])
)

# Define some tests to determine the type of the question.
def is_type_ask(question):
    return question.startswith("Ask")

def is_type_find(question):
    return question.startswith("Find")

env.tests['type_ask'] = is_type_ask
env.tests['type_find'] = is_type_find

# Load the template
template = env.get_template("bingo-page.html")

# Write to resulting page.
with open("./bingo-sheets.html", "w") as bingo_file:
    # First, insert the HTML header.
    with open("bingo-header.html", "r") as bingo_header_file:
        bingo_file.write(bingo_header_file.read())

    # Loop through the template num_cards times to produce that many unique Bingo cards
    for i in range(num_cards):
        # Get a random sample of 25 questions from the question bank
        card = random.sample(questions, 25)

        # Replace the center grid with "BINGO"
        card[12] = "BINGO"

        # Split the list into 5 lists of 5 to form the grid
        grid = [card[i:i + 5] for i in range(0, len(card), 5)]

        bingo_file.write(template.render(grid=grid))

    # Insert HTML footer at the bottom.
    with open("bingo-footer.html", "r") as bingo_footer_file:
        bingo_file.write(bingo_footer_file.read())