from PIL import Image
from sys import argv
import sys
from os import path
from PIL import ImageDraw
from PIL import ImageTk
import random

OUTPUT_FILE = 'output2.png'

# INCOMPLETO
def blur(image, n):
  w, y = image.size
  pix = img.load()
  output = Image.new("RGB", (w,h))

  # me regresa el pixel ya modificado
  def new_pixel(array):
    return array[0]/5, array[1]/5, array[2]/5

  # returns a list of lists
  # each list is a pixel
  five_pixels = lambda i,j: [ list(pix[i,j]), list(pix[i-1,j]), list(pix[i+1,j]), list(pix[i,j+1]), list(pix[i,j-1]) ]
  # Esto es igual al original
  col_totals = lambda i,j: [ sum(x) for x in zip(*five_pixels(i)(j)) ]

  # Esto me genera mi arreglo que se convertirá en la imagen
  # Necesitamos procesar este array varias veces
  pre_out = [ [ new_pixel(col_totals(i)(j)) for j in range(h) ] for i in range(w) ]
  output.putdata(out_pix)
  output.save(OUTPUL_FILE, 'PNG')
  return output

def sal_y_pimienta(img, intensidad, pol):
  def det():
    return random.randint(0,1)
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
