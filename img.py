from PIL import Image
img  = Image.open("img.gif")
resized = img.resize((1920, 1080))
resized.save("logo.gif")