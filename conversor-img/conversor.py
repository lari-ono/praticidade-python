from PIL import Image
# TIF para PNG

# abrir arquivo de apenas um
imagem = Image.open("./imagem/motobomba_wp.tif")

#salvar o arquivo com outro formato
imagem.save("motobomba_wp.png")

# RGB - jpg | RGBA - png (quantidade de transparência) 
# Ex: .convert("RGB")

#se forem muitos arquivos
arquivos_origem = "C:/Users/Usuario/Downloads/conversor-img/imagem"

arquivos_destino = "C:/Users/Usuario/Downloads/"

if not os.path.exists(arquivos_destino):
    os.makedirs(arquivos_destino)

for filename in os.listdir(arquivos_origem):
    if filename.endswith(".tif"):
        with Image.open(os.path.join(arquivos_origem, filename)) as im:
            im = im.convert("RGB") # Converter para modo RGB
            im.save(os.path.join(arquivos_destino, os.path.splitext(filename)[0] + ".png"))
