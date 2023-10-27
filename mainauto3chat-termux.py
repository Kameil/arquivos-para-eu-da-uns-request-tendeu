import requests
import subprocess
import os
from termcolor import colored

class DownloadError(Exception):
    def __init__(self, message, linha):
        super().__init__(message)
        self.linha = linha


def download_file(url, file_name):
    print('Procurando atualizações...')
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_name, "w") as file:
            file.write(response.text)
        return True
    return False

github_url = "https://raw.githubusercontent.com/Kameil/arquivos-para-eu-da-uns-request-tendeu/main/auto3chat-termux.py"
local_file_name = "bot.py" 


if download_file(github_url, local_file_name):
    try:
        if __name__ == '__main__':
                subprocess.run(["python3", local_file_name], check=True)
    except subprocess.CalledProcessError as e:
        print(colored('Erro ao executar o arquivo.', "red"), colored(' Entre em contato com o discord', 'yellow'), f'\n{str(e)}')
      
else:
    raise DownloadError('Nao foi possivel fazer o Download do autocatch.', 21)
