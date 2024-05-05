
from PIL import Image

def to_grayscale(image):
    # Converte a imagem para tons de cinza
    grayscale_image = image.convert('L')
    return grayscale_image

def binarize(image, threshold=100):
    # Binariza a imagem com um limite especificado
    binarized_image = image.point(lambda p: p > threshold and 255)
    return binarized_image

# Carrega a imagem
image = Image.open('Lena.jpg')

# Converte para tons de cinza
grayscale_image = to_grayscale(image)

# Binariza a imagem
binarized_image = binarize(grayscale_image)

# Exibe as imagens
grayscale_image.show()
binarized_image.show()

#Salva as imagens
grayscale_image.save('grayscale.jpg')
binarized_image.save('binarized.jpg')