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
from biblio import Biblio
from common import chunked
from dateutil.parser import isoparse
from peewee import fn
import os

def Curate (database : str, first_year : int) -> dict[int, str]:

  biblio = Biblio (database)
  books = {}

  Books = biblio.Books
  Data = biblio.Data

  years = Books.select (fn.strftime ('%Y', Books.pubdate)).order_by (fn.strftime ('%Y', Books.pubdate))
  years = years.scalars ()

  if first_year != None:

    years = ( year for year in years if int (year) >= first_year )

  for year in years:

    sample = Books.select (Data.format, Data.name, Books.path, Books.title).join (Data, on = (Books.id == Data.book)).where (fn.strftime ('%Y', Books.pubdate) == str (year)).limit (10)
    sample = [ (book.data.format, book.data.name, book.path, book.title) for book in sample ]
    books [year] = sample

  return books
