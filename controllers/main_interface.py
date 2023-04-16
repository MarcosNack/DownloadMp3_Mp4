import os
from PySide6.QtWidgets import (QMainWindow, QMessageBox, QFileDialog)

from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from controllers.download_youtube import DownloadYoutubeMp3, DownloadYoutubeMp4
from views.main_interface import Ui_TelaDownload

from msgbox.msgboxpadrao import *

import youtube_dl

from pytube import Playlist

from time import sleep

class DownloadYoutube(QMainWindow, Ui_TelaDownload):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Download Youtube')
        #Roda pé do sistema
        self.label.setText('Version 1.0.0')
        #Ocultar Barra de Status
        self.qf_status_bar.setVisible(False)
        
        #Incluir o icone na interface
        icon = QIcon(r"icon.ico")
        self.setWindowIcon(icon)
        #Bottom BAIXAR > Realizar o download
        self.btn_baixar.clicked.connect(self.yt_downloader)        
        #Bottom Fechar > Fechar a tela
        self.btn_fechar.clicked.connect(self.yt_exit)
        #Bottom Link
        self.btn_link.clicked.connect(self.SelectCaminho)
        self.btn_link.setText("")
        self.btn_link.setVisible(False)
        
        #Variável caminho
        self.caminho_salvar = ""

    def SelectCaminho(self):
        self.caminho_salvar = QFileDialog.getExistingDirectory(self, "Selecione a pasta p/Salvar", self.caminho_salvar)
        self.btn_link.setText(f"Caminho: {self.caminho_salvar}. Click aqui para alterar o caminho.")
        
        
    def yt_downloader(self):
        self.qf_status_bar.setVisible(True)
        self.update()  
        valid = ""
        if self.txt_link.text() == "": #Validar se foi informado o link para download
            valid = "--> Informar o Link para Download."

        if not self.rbtn_mp3.isChecked() and not self.rbtn_mp4.isChecked(): #Validar se foi marcado a opção para Download
            if valid == "":
                valid = "--> Selecionar uma das opções para Download."

            else:
                valid = f"{valid}\n--> Selecionar uma das opções para Download."

        if valid != "":
            msg_info = f'Por gentileza preencher o(s) campo(s) abaixo:\n{valid}'
            MsgBoxErro(self, msg_info=msg_info)

        else:
            #Selecionar a pasta para salvar o arquivo
            if self.caminho_salvar == "":
                self.caminho_salvar = QFileDialog.getExistingDirectory(self, "Selecione a pasta p/Salvar")
                
                self.btn_link.setText(f"Caminho: {self.caminho_salvar}. Click aqui para alterar o caminho.")
                self.btn_link.setVisible(True)
                
                        
            # else:
            #     self.caminho_salvar = QFileDialog.getExistingDirectory(self, "Selecione a pasta p/Salvar", self.caminho_salvar)
                                                                   
            if self.caminho_salvar == "":
                msg_info = f'Por gentileza definir a pasta para salvar o(s) arquivo(s)!'
                MsgBoxErro(self, msg_info=msg_info)

            else:  
                
                
                self.Download()

            self.qf_status_bar.setVisible(False)
            self.txt_link.setText("")
            self.chb_baixar_playlist.setChecked(False)

    def Download(self):
        link = self.txt_link.text()
        if self.rbtn_mp3.isChecked():  
            if self.chb_baixar_playlist.isChecked():
                #Baixar a Playlist MP4
                playlist = Playlist(link)
                
                msf_info = ""
                # playlist = Playlist(link)
                if len(playlist) > 0:                    
                    for url in playlist.video_urls:                    
                        status_download = DownloadYoutubeMp3(youtube_video_url=url, caminho_salvar=self.caminho_salvar)
                                                
                        msf_info = f"{msf_info}Playlist {status_download['MSG_INFO']}\n"
                    MsgBoxInformation(self, msg_info=msf_info)
    
                else:
                    MsgBoxErro(self, "Playlist Invalida...")                    
             
            else:
                #Baixar o mp3 individual     
                status_download = DownloadYoutubeMp3(youtube_video_url=link, caminho_salvar=self.caminho_salvar)
                MsgBoxInformation(self, msg_info=status_download["MSG_INFO"])
                  
        elif self.rbtn_mp4.isChecked():
            if self.chb_baixar_playlist.isChecked():                
                #Baixar a Playlist MP4
                #Baixar a Playlist MP4
                playlist = Playlist(link)
                                    
                # playlist = Playlist(link)
                msf_info = ""
                if len(playlist) > 0:                    
                    for url in playlist.video_urls:
                        status_download = DownloadYoutubeMp4(youtube_video_url=url, caminho_salvar=self.caminho_salvar)
                        
                        msf_info = f"{msf_info}Playlist {status_download['MSG_INFO']}\n"
                    MsgBoxInformation(self, msg_info=msf_info)
    
                else:
                    MsgBoxErro(self, "Playlist Invalida...")
    
            else:
                status_download = DownloadYoutubeMp4(youtube_video_url=link, caminho_salvar=self.caminho_salvar)
                MsgBoxInformation(self, msg_info=status_download["MSG_INFO"])
                        
    def yt_exit(self):
        self.close()
