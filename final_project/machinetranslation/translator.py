import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

lenguage_translator = LanguageTranslatorV3(version="2018-05-01", authenticator=authenticator)

lenguage_translator.set_service_url(url)



