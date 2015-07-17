from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello') #madlib-input when game option == YES; when == no it goes goodbye; otherwise /hello
def say_hello():
    game_option = request.args.get("game_option")

    if game_option == "YES":
        return render_template("madlib-input.html")
    elif game_option == "NO":
        return render_template("goodbye.html")
    else:
        return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route('/madlib')
def madlib():
    relative1 = request.args.get("relative1")
    adjective1 = request.args.get("adjective1")
    adjective2 = request.args.get("adjective2")
    adjective3 = request.args.get("adjective3")
    roomPerson1 = request.args.get("roomPerson1")
    adjective4 = request.args.get("adjective4")
    adjective5 = request.args.get("adjective5")
    verbEndingED = request.args.get("verbEndingED")
    bodypart = request.args.get("bodypart")
    verbEndingING = request.args.get("verbEndingING")
    pluralnoun = request.args.get("pluralnoun")
    noun = request.args.get("noun")
    adverb = request.args.get("adverb")
    verb1 = request.args.get("verb1")
    verb2 = request.args.get("verb2")
    relative2 = request.args.get("relative2")
    yourname = request.args.get("yourname")

    return render_template("madlib-output.html", relative1=relative1, adjective1=adjective1, adjective2=adjective2, adjective3=adjective3, roomPerson1=roomPerson1, adjective4=adjective4, adjective5=adjective5, verbEndingED=verbEndingED, bodypart=bodypart, verbEndingING=verbEndingING, pluralnoun=pluralnoun, noun=noun, adverb=adverb, verb1=verb1, verb2=verb2, relative2=relative2, yourname=yourname)
if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)

