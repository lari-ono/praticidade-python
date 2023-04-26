from PIL import Image

# abrir arquivo
imagem = Image.open("./imagem/motobomba_wp.tif")

#salvar o arquivo com outro formato
imagem.save("motobomba_wp.png")

# RGB - jpg | RGBA - png (quantidade de transparência) 
# Ex: .convert("RGB")

#se forem muitos arquivos
lista_arquivos = os.listdir("./imagem")

for imagem in list_arquivos:
  imagem = Image.open(f'imagens/{arquivo}')

  #salvar o arquivo com outro formato
  imagem.save(f'tiff/{arquivo.replace("png", "tiff")}')