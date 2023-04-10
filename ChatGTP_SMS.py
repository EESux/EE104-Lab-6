# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 10:06:40 2023
References: https://www.twilio.com/blog/sms-chatbot-openai-python
@author: chris.pham
"""

# Run this program in the same directory where you have both this program
#  and ngrok and .env file with OPENAI_API_KEY

# STEP 1:
# Run from CMD (in administrator mode), type
# ngrok http 5000, and copy the Forwarding https://########.ngrok.io
# then add it to your Twilio Webhook box under "A MESSAGE COMES IN"

# STEP 2: run this program


from flask import Flask, request
from flask_cors import CORS  #remember to pip install flask_cors
from twilio.twiml.messaging_response import MessagingResponse
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask(__name__)
CORS(app)

@app.route("/sms", methods=['POST'])
def chatgpt():
    """get incoming message"""
    inb_msg = request.form['Body'].lower()
    print(inb_msg)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=inb_msg,
        max_tokens=3000,
        temperature=0.7
    )
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()
    # Add a message
    resp.message(response["choices"][0]["text"])
    print(response["choices"][0]["text"])

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)


