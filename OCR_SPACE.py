import os
import json
import aiohttp

try:
    a = os.environ['api_key']
except KeyError:
    os.environ['api_key'] = 'helloworld'
    a = os.environ['api_key']

# 'helloworld' E a key padrao permite 10 requests a cada 10 minutos.


async def ocr_space_url(url: str, overlay=False, api_key: str=a, language: str='eng', timeout: float=60):
    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    timeout = aiohttp.ClientTimeout(total=timeout)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.post('https://api.ocr.space/parse/image', data=payload) as response:
            return await response.text()



class Ocr:
    def __init__(self, lang: str='eng', api_key: str='helloworld', overlay=False):
        self.language = lang
        self.api = api_key
        self.overlay = overlay

        
    async def image(self, image_url: str, timeout: float=30):
        image_text = await ocr_space_url(url=image_url,
                                         language=self.language,
                                         overlay=self.overlay,
                                         api_key=self.api,
                                         timeout=timeout)
        response_json = json.loads(image_text)
        try:
            parsed_text = response_json['ParsedResults'][0]['ParsedText']
            return parsed_text
        except KeyError:
            return None
