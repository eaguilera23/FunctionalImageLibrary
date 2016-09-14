from PIL import Image
from sys import argv
import sys
from os import path
from PIL import ImageDraw
from PIL import ImageTk
import random

OUTPUT_FILE = 'output2.png'

def det():
  return random.randint(0,1)

def sal_y_pimienta(img, intensidad, pol):
  w, h = img.size
  pix = list(img.getdata())
  total_size = w*h
  n = int(intensidad*(total_size/100))
  output = Image.new("RGB", (w, h))
  mode = img.mode
  
  pixelsRand = [random.randint(0, total_size - 1) for x in range(n)]
  # x = pol
  sal_o_pim = lambda x: random.randint(255-x,255) if det() else random.randint(0,x)
  rgb_or_l = lambda x: (sal_o_pim(x),) * 3 if mode == "RGB" else (sal_o_pim(x),)
  
  out_pix = [rgb_or_l(pol) if pix.index(x) in pixelsRand else x for x in pix]
  output.putdata(out_pix)
  output.save(OUTPUT_FILE, 'PNG')
  return output


def to_binary(image, umb):
  w, h = image.size
  pix = image.load()
  output = Image.new("RGB", (w, h))
  out_pix = output.load()
  mode = image.mode
  pix = image.getdata()
  out_data = []
  
  black_or_white = lambda x: out_data.append((255,)) if x >= umb else out_data.append((0,))

  bw_rgb = lambda x: out_data.append((255,255,255)) if max(x) >= umb else out_data.append((0,0,0))

  black_and_white = [map(lambda x: black_or_white(x) if mode == "L" else bw_rgb(x), pix)]

  output.putdata(out_data)
  output.save(OUTPUT_FILE, 'PNG')
  return output


if __name__ == "__main__":
  global WORKING_IMAGE
  assert(path.isfile(argv[1]))
  image = Image.open(argv[1]).convert('RGB')
  # WORKING_IMAGE = image
  # to_binary(image, 240) if argv[1] == 1
  sal_y_pimienta(image, 0.8, 30)
