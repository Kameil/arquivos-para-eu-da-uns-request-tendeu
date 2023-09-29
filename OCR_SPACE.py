import os
import json
import aiohttp

try:
    a = os.environ['api_key']
except KeyError:
    os.environ['api_key'] = 'helloworld'
    a = os.environ['api_key']

# 'helloworld' E a key padrao permite 10 requests a cada 10 minutos.

async def ocr_space_file(filename, overlay=False, api_key: str=a, language: str='eng', timeout: float=60):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    timeout = aiohttp.ClientTimeout(total=timeout)
    with open(filename, 'rb') as f:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            try:
                async with session.post('https://api.ocr.space/parse/image',
                                        files={filename: f},
                                        data=payload) as response:
                    return await response.text()
            except:
                return None


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

        
    async def image(self, image_url: str=None, image_path: str=None, timeout: float=30):
        if image_url is not None and image_path is None:
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
                raise KeyError('Unable to get text from image')
        elif image_path is not None and image_url is None:
            image_text = await ocr_space_file(filename=image_path,
                                              overlay=self.overlay,
                                              api_key=self.api,
                                              language=self.language,
                                              timeout=30)
            response_json = json.loads(image_text)
            try:
                parsed_text = response_json['ParsedResults'][0]['ParsedText']
                return parsed_text
            except KeyError:
                raise KeyError('Nao foi possivel obter texto da imagem.')
        elif image_url is None and image_path is None:
            raise RuntimeError('Image_url or image_path arguments are missing')
        else:
            raise('You cannot use the 2 arguments image_url and image_path')
