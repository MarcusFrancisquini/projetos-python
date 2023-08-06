import os
from pytube import YouTube

yt = YouTube(str(input('Entre com a URL do vídeo \n>> ')))

video = yt.streams.filter(only_audio=True).first()

print('Onde deseja salvar o arquivo? (deixe em branco para salvar no diretório atual)')
outputPath = str(input('>> ')) or '.'

outFile = video.download(output_path=outputPath)

base, ext = os.path.splitext(outFile)
newFile = base + '.mp3'
os.rename(outFile, newFile)

print(yt.title + ' foi baixado com sucesso!')
