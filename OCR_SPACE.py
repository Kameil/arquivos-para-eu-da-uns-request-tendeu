import os, requests, json

a = os.environ['api_key']

def ocr_space_url(url, overlay=False, api_key=a, language='eng', timeout=60):

    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image', timeout=timeout,
                      data=payload,
                      )
    return r.content.decode()



class ocr:
    def __init__(self, lang='eng', api_key='hello world', overlay=False):
        self.language = lang
        self.api = api_key
        
    def image(self, image_url, timeout=30):
        self.to_string = ocr_space_url(url=image_url, language=self.language, overlay=False, api_key=self.api, timeout=timeout)
        response_json = json.loads(self.to_string)
        parsed_text = response_json['ParsedResults'][0]['ParsedText']
        return parsed_text
