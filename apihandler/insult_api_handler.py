from api_handler import APIHandler
from bs4 import BeautifulSoup as bs
import requests


class InsultAPIHandler(APIHandler):
    
    def request_data(url: str):
        return bs(requests.get("https://insult.mattbas.org/api/en/insult.html") \
                            .content, "html.parser") \
                            .find("h1") \
                            .text

        
       
