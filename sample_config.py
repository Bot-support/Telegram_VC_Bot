HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ
    from dotenv import load_dotenv
    
    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SESSION_STRING = environ["SESSION_STRING"]  # Check Readme for session
    ARQ_API_KEY = environ["ARQ_API_KEY"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = "3088812"
    API_HASH = "d51f13802ef40ccb115e333a5f9dc9e7"
    ARQ_API_KEY = "IFRNXG-FTVINV-FESSFW-LDMSCZ-ARQ"
# don't make changes below this line
ARQ_API = "https://thearq.tech"
