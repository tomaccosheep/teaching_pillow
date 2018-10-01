import colorsys
from PIL import Image
img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        if i + 50 < width and j + 50 < height:
            color_list = [0, 0, 0]
            for k in range(len(color_list)):
                for l in range(0, 50):
                    color_list[k] += (pixels[i + l, j][k])/50
                
        else:
            color_list = pixels[i, j]
        #h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        #h = ((h) // user_input) * user_input
        #s = 1
        #v = .5
        #r, g, b = colorsys.hsv_to_rgb(h, s, v)
        pixels[i, j] = (int(color_list[0]), int(color_list[1]), int(color_list[2]))
img.show()
