from PIL import Image
img = Image.open("crash.gif")
r = img.resize((1920, 1080))
r.save("Crash.gif")