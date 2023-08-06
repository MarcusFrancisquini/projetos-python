from rembg import remove
from PIL import Image
import easygui

inputPath = easygui.fileopenbox(title='Selecione a imagem')
outputPath = easygui.filesavebox(title='Salvar como...')

input = Image.open(inputPath)
output = remove(input)
output.save(outputPath)

# SALVAR IMAGEM NO FORMATO .png
