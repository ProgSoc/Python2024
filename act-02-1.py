from svg_turtle import SvgTurtle # pip install svg-turtle
from math import cos, sin, pi
from bs4 import BeautifulSoup # pip install beautifulsoup4
from urllib.request import urlopen
from math import lcm
import re

def spiro(orbit, planet, rate = 1.0):
  STEP = 0.1

  img_size = int(2 * (orbit + planet))
  turtle = SvgTurtle(img_size, img_size)
  rotation = 0
  cycle = (2 * pi) * lcm(100, int(100 * rate)) / 100
  turtle.teleport(orbit + planet, 0)

  while rotation <= 2 * pi:
    planet_x = orbit * cos(rotation)
    planet_y = orbit * sin(rotation)
    moon_x = planet_x + planet * cos(rotation * rate)
    moon_y = planet_y + planet * sin(rotation * rate)
    turtle.goto(moon_x, moon_y)
    rotation += STEP
  svg = turtle.to_svg().replace("<svg", f'<svg viewBox="0 0 {img_size} {img_size}"')
  return re.sub(r" width=\"[^\"]*\"| height=\"[^\"]*\"", '', svg)

with open("act-02-1-spiro.svg", "w") as f:
  f.write(spiro(50, 15, 8))
