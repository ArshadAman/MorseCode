from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6z'

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/make-code", methods=["GET", "POST"])
def make():
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}

    def encrypt(text):
        morse_code = ""
        for letter in text:
            if letter != " ":
                morse_code = morse_code + MORSE_CODE_DICT[letter]+" "
            else:
                morse_code += " "

        return morse_code

    if request.method == "POST":
        morse_text = request.form["morse_text"]
        upper_morse = morse_text.upper()
        output = encrypt(upper_morse)
    else:
        output = "Please Enter The Text and Click Morse Me"
        
    return render_template("make.html", output=output)

@app.route("/decode", methods=["GET", "POST"])
def decode():
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}

    MORSE_INVERTED = {value: key for key, value in MORSE_CODE_DICT.items()}
    MORSE_INVERTED[""] = " "
    def decrypt(morse_code):
        text = ""
        morse_text=""
        morse_list = []
        morse_code+= " "

        for morse in morse_code:
            if morse != " ":
                morse_text += morse
            else:
                morse_list.append(morse_text)
                morse_text = ""
        for item in morse_list:
            text += MORSE_INVERTED[item]
        return text.title()

    if request.method == "POST":
        morse_code = request.form["morse_code"]
        output = decrypt(morse_code)
    else:
        output = "Please Enter The Morse Code and Click Decrypt"

    return render_template("decrypt.html", output= output)


if __name__ == "__main__":
    app.run()