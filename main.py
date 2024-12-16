import subprocess
import uuid
from yt_dlp import YoutubeDL

opcoes = {
    'format': "bestvideo[ext=mp4][height<=720][vcodec~='^((he|a)vc|h26[45])']+bestaudio[ext=m4a]/best[ext=mp4][height<=720]",
    'outtmpl': f'downloads/{uuid.uuid4()}/%(title)s.%(ext)s',
}

def Download(link):
    with YoutubeDL(opcoes) as ydl:
        ydl.download([link])

    print("Download concluido")

def DownloadArquivo(nome_arquivo):

    if isinstance(nome_arquivo, str) and not nome_arquivo.strip():
        nome_arquivo = "links.txt"
    
    with open(nome_arquivo, 'r') as f:
        urls = [linha.strip() for linha in f if linha.strip()]

    with YoutubeDL(opcoes) as ydl:
        ydl.download(urls)

    print("Download concluido")

if __name__ == "__main__":
    print("Como você deseja baixar os videos?")
    print("1 - Colar o link")
    print("2 - Por arquivo")

    user_input = input("Digite a opção desejada:")

    try:
        input_int = int(user_input)
    except ValueError:
        print("Opção invalida.")
        exit()

    if input_int != 1 and input_int != 2:
        print("Opção invalida.")
        exit()

    if input_int == 1:
        link = input("Cole a URL do youtube: ")
        Download(link)
        exit()

    if input_int == 2:
        arquivo = input("Digite o nome do arquivo (com a extensao) - Padrão links.txt:")
        DownloadArquivo(arquivo)
        exit()