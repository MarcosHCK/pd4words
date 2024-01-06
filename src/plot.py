# Copyright (c) 2023-2025
# This file is part of pd4words.
#
# pd4words is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pd4words is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pd4words. If not, see <http://www.gnu.org/licenses/>.
#
import matplotlib.pyplot as pyplot
import json

def avg_repetitiveness (books):

  total = 0

  for book in books:
    total += book [1] ['repetitiveness']
  return total / len (books)

def total_complexity (books):

  total = 0

  for book in books:
    total += book [1] ['complexity']
  return total

def total_length (books):

  total = 0

  for book in books:
    total += book [1] ['length']
  return total

def Plot (curated : str):

  pyplot.axhline (0, color = 'black')
  pyplot.axvline (0, color = 'black')
  pyplot.xlim ([ 0, 1 ])
  pyplot.ylim ([ 0, 1 ])

  def plot_complexity (data):

    x = data.keys ()
    y = [ total_complexity (books) / total_length (books) for year, books in data.items () ]

    pyplot.plot (x, y, color = 'blue', label = 'complexity')

  def plot_length (data):

    x = data.keys ()
    y = [ total_length (books) for year, books in data.items () ]

    m = max (y)
    y = [ length / max (y) for length in y ]

    pyplot.plot (x, y, color = 'green', label = 'length')

  def plot_repetitiveness (data):

    x = data.keys ()
    y = [ avg_repetitiveness (books) for year, books in data.items () ]

    pyplot.plot (x, y, color = 'red', label = 'repetitiveness')

  with open (curated, mode = 'r') as f:

    data = json.load (f)

    plot_complexity (data)
    plot_length (data)
    plot_repetitiveness (data)
    pyplot.show ()
