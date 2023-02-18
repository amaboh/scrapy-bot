Scrape Data and create prompts on LinkedIn profiles


This project is based on my interest of learning from others through interviews and having deep philosophical discussions sometimes on my podcast and sometimes over coffee or beer.

Project scope:
We would first be scraping data from a users LinkedIn profile using Scrapy and then implementing another python script using chatGPT API to query the users porfile

## File structure
- Basic Scrapy Spider
- outputProfile.json
- profileChatBot : Python script to create prompts or queries based on the profile scraped from LinkedIn


# Getting Started 
This projects can be done as one or seperately depending on your choice be it to learn how to use Scrapy to scrape data behind User sign in walls, or to use OpenAi's ChatGPT to create chat interface to query JSON documents 


# Getting started with Scrapy for scraping data
1. Clone this project: `git clone git@github.com:amaboh/scrapy-bot.git`
2. Create a Python Virtual Environment: `python3 -m venv venv`
3. Activate the Python Virtual Environment: `source venv/bin/activate`
4. Install Scrapy using pip: `pip install scrapy`
5. Listing the scrapy projects `scrapy list` 
6. Running the scrapy project: `scrapy crawl quotes` 

# Getting started - ChatGPT API from open AI for prompt engineering
1. Create a Python Virtual Environment: `python3 -m venv venv` optional
2. Activate the Python Virtual Environment: `source venv/bin/activate` optional
3. install openai using pip: `pip install openai`
4. install file dependencies: pip `pip install dotenv` to load environment variables
4. Grap a copy of OpenAI keys from here: https://platform.openai.com/account/api-keys
5. Run script: `python profileChatBot.py`


# Ways to improve this application
- make a bot capable of extracting any content from any website and using chatGPT to make prompts
- Make a UI that enables users to upload any file or document and use chatGPT to make prompts to document or file





