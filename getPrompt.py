from flask import *
from openAI import *

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    recipient = request.form['recipient']
    chat = request.form['chat']
    response = teamsAid(recipient, chat)
    return render_template('form.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)


""" from openAI import *

#Variables

#the ai will need the name of the *recipient* and the *chat* that needs to be rewritten
recipient = input("Who is the chat for?: ")
chat = input("What is the message?: ")

#we are calling the ai located in a different py file and giving it the recipent and chat we collected from the user. It will be stored in *reply_text*
reply_text = teamsAid(recipient, chat)

#We are then printing the ai output that is stored 
print(reply_text) """
