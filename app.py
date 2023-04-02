from flask import Flask, request, render_template
from requests import post
import openai

app = Flask(__name__)

# Set the OpenAI API key
# get this key from https://chat.openai.com/chat 
# API Refernece -> create your key. 
# ITS SHOWN ONCE. KEEP IT ON YOUR COMPUTER FOR API ACCESS 
#

openai.api_key = "your_key_from_openai"

# Ask a question
def askQuestion (qry):
    
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=qry,
    temperature=0,
    max_tokens=500,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\""]
)

    # Print the response
    print ('##### ANSWER FROM CHATGPT ####### ')
    #print(response["choices"][0]["text"])
    response_data = response["choices"][0]["text"]
    return response_data

@app.route('/')
def gotoIndex ():
    return render_template('ask.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']  # Make an API call to the chatbot
    print ('question =', question)
  
    #response = post('http://example.com/chatbot', json={'question': question})
    #response_data = 'ANSWER IS FROM SERVER' # response.json()
    response_data = askQuestion (question)
    print ('response_data =', response_data)
    return render_template('ask.html', response_data=response_data, question=question) 

if __name__ == '__main__':
    app.run(debug=True)

# Created by Bahadur Singh 