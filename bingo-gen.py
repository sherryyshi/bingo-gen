from jinja2 import FileSystemLoader, Environment, select_autoescape
import random

env = Environment(
    loader = FileSystemLoader("."),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template("bingo.html")

questions = [
    "Ask someone: \"What is your New Year resolution?\"",
    "Sing a catchy song out loud with a group of 5+ people!",
    "Ask someone: \"Who is your favorite musical artist?\"",
    "Find someone who lives alone.",
    "Find someone who did not study computer science in school.",
    "Find someone that eats lunch with their team on a regular basis.",
    "Find someone that has gone on a hike longer than 5 miles in 2019.",
    "Find someone who does not have Instagram.",
    "Find someone who lives alone.",
    "Find someone who lives on the eastside.",
    "Play 2 truths and a lie with someone!",
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
    "Find someone who lives on the eastside.",
    "Find someone who is not self hosting.",
    "Find someone who did not study computer science in school.",
    "Find someone who joined Microsoft after October 1, 2019 at 4:20pm!",
    "Find someone who can juggle!",
    "Find someone who shares a rare hobby with you.",
    "Find someone who is a middle child.",
    "Find someone who works on a tented project.",
    "Find someone who failed a phishing test.",
    "Find someone who has a Non-Microsoft pen right now.",
    "Ask someone: \"What is your New Year resolution?\" ",
    "Ask someone: What's your favorite movie/song?",
    "Ask someone: What's the best Microsoft cafeteria?",
    "Ask someone: What's your favorite Microsoft perk?",
    "Ask someone: \"Where do you see yourself in 10 years?\"",
    "Ask someone: \"What is your favorite Microsoft product?\"",
    "Sing a catchy song out loud with a group of 5+ people!",
    "Introduce yourself to a member of COSINE leadership.",
    "Play 2 Minute-to-Win-it Games!",
    "Get a selfie with all events in the background",
    "Introduce yourself to someone without speaking. ",
    "Mark this square if more than 7 people put you down as an answer.",
]

with open("bingo-sheets.html", "w") as bingo_file:
    with open("bingo-header.html", "r") as bingo_header_file:
        bingo_file.write(bingo_header_file.read())

    for sheet_number in range(600):
        sheet = random.sample(questions, 25)
        sheet[12] = "BINGO"
        n = 5

        grid = [sheet[i:i + n] for i in range(0, len(sheet), n)]

        bingo_file.write(template.render(grid=grid))

    with open("bingo-footer.html", "r") as bingo_footer_file:
        bingo_file.write(bingo_footer_file.read())