import openai
import json
import os
from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.environ.get('OPENAI_API_KEYS')
model_engine = "text-davinci-003"



with open('outputProfile.json') as f:
    data = json.load(f)

print("Welcome, I am AMA ai meaning Ask Me Anthing Ai! ")
prompt = input("what would you like to know on this profile? ")    

while prompt.lower() != "quit":
    for info in data:
        completion= openai.Completion.create(
            engine=model_engine,
            prompt=prompt + f"for {info}\n",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5
            
        )
        
        response = completion.choices[0].text
        
        print("Ama ai:", response)
        print()
        prompt = input("you: ")