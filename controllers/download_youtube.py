import os
from moviepy import editor

from pytube import YouTube

# Função para realizar o download e extrair o audi (MP3)
def DownloadYoutubeMp3(youtube_video_url, caminho_salvar):  
    try:
        # Realizar o Download do arquivo MP4
        yt_obj = YouTube(youtube_video_url)
        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
        caminho_arq_mp4 = filters.get_highest_resolution().download(output_path=rf'{caminho_salvar}/')
        caminho_arq_mp3 = caminho_arq_mp4.replace(".mp4", ".mp3")
        
        # Converter o arquivo MP4 em MP3
        video = editor.VideoFileClip(caminho_arq_mp4)
        aud = video.audio
        aud.write_audiofile(caminho_arq_mp3)
        
        # Fechar os arquivos MP4 e MP3
        video.close()
        aud.close()
        
        # Remover o arquivo MP4
        os.remove(caminho_arq_mp4)
        
        # Gerar mensagem final do processamento        
        msg_info = {
            "STATUS": "OK",
            "MSG_INFO": "MP3 baixado com sucesso!"
        }
        return msg_info

    except:
        msg_info = {
            "STATUS": "Erro",
            "MSG_INFO": "Erro no Download"
        }
        return msg_info

# Função para realizar o download do video (MP4)
def DownloadYoutubeMp4(youtube_video_url, caminho_salvar):
    try:
        # Realiza o Download do video (MP4)        
        yt_obj = YouTube(youtube_video_url)
        filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
        filters.get_highest_resolution().download(output_path=rf'{caminho_salvar}/')
        
        # Gerar mensagem final do processamento        
        msg_info = {
            "STATUS": "OK",
            "MSG_INFO": "MP4 baixado com sucesso!"
        }
        return msg_info

    except:
        msg_info = {
            "STATUS": "Erro",
            "MSG_INFO": "Erro no Download"
        }
        return msg_info


