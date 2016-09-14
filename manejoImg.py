from PIL import Image
from sys import argv
import sys
from os import path
from PIL import ImageDraw
from PIL import ImageTk

OUTPUT_FILE = 'output.png'


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
  #WORKING_IMAGE = image
  image = to_binary(image, 240)
