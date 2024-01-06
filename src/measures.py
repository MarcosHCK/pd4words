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
from words import Words
from peewee import fn
import itertools

batchsz = 128

def chunked (it, size):

  it = iter (it)

  while True:

    chunk = tuple (itertools.islice (it, size))

    if not chunk:
      return
    yield chunk

def Complexity (words : dict[str, int]) -> float:

  total = Words.select (fn.SUM (Words.freq)).scalar ()
  rank = 0

  for chunk in chunked (words.keys (), batchsz):

    chunk = Words.select (Words.word, Words.freq).where (Words.word.in_ (chunk)).order_by (Words.word)

    for word, freq in ((word.word, word.freq) for word in chunk):

      oddiness = 1 - freq / total
      rank = rank + words [word] * oddiness

  return rank
