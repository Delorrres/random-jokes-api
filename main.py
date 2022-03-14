from flask import Flask, jsonify, request, Response
import json

app = Flask(__name__)

# KEY : VALUE
jokes_db ={
    "1": { "1st joke":  "Tech", "What kind of computer sings the best?":  "A Dell!" },
    "2": { "2nd joke":  "Tech", "What was the spider doing on the computer?":  "He was making a web-site!" },
    "3": { "3rd joke":  "Tech", "How did the man get a job at Microsoft's office?":  "Because he Excel-led in the interview!" },
    "4": { "4th joke":  "Tech", "Why did the developer become so poor?":  "Because he used up all his cache." },
    "5": { "5th joke":  "Tech", "What is a programmer's favorite eyewear?":  "Google." },
    "6": { "6th joke":  "Tech", "Which type of virus does not have any vaccine?":  "Computer virus." },
    "7": { "7th joke":  "Tech", "How do trees make use of the internet?":  "They just log in." },
    "8": { "8th joke":  "Tech", "What is another 1st joke for apple juice?":  "Phone chargers." },
    "9": { "9th joke":  "Tech", "What is the biggest lie anyone can tell?":  "I have read and agreed to all the terms and conditions." },
    "10": { "10th joke":  "Tech", "Why was the computer found cold and sneezing?":  "Because someone left it's Windows open!" }
    
}

@app.route("/")
def hello():
    return "you are that bitch, keep going"

@app.route("/jokes/")
def list_jokes():
    return jokes_db

@app.route("/newjoke/", methods=["GET","POST"])
def post_jokes():
    new_joke ={ "11th joke":  "Tech", "How many programmers does it take to change a light bulb?":  "None, because it is a hardware problem." }
    jokes_db["11"]= new_joke
    return "You added a new joke"


if __name__ == "__main__":
    app.run(host="127.0.0.1")