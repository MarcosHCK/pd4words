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
from common import chunked
from peewee import fn
from words import Words

def Complexity (words : dict[str, int]) -> float:

  total = Words.select (fn.SUM (Words.freq)).scalar ()
  rank = 0

  for chunk in chunked (words.keys (), 128):

    chunk = Words.select (Words.word, Words.freq).where (Words.word.in_ (chunk)).order_by (Words.word)

    for word, freq in ((word.word, word.freq) for word in chunk):

      oddiness = 1 - freq / total
      rank = rank + words [word] * oddiness

  return rank

def Length (words : dict[str, int]) -> int:

  return sum (words.values ())

def Repetitiveness (words : dict[str, int]) -> float:

  total = sum (words.values ())
  fract = len (words) / total
  return fract
