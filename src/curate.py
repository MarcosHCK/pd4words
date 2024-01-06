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
from dateutil.parser import isoparse
from ebooklib import epub as Epub
from lxml import etree
import os

def Curate (root : str, language : str) -> dict[int, str]:

  books = {}

  for shelf in os.scandir (root):

    if not shelf.is_dir ():

      raise Exception (f'foreign file in library folder: {shelf.name}')
    else:

      for book in os.scandir (shelf.path):

        if not book.is_dir ():

          raise Exception (f'foreign file in shelf folder: {book.name}')
        else:

          file = os.path.join (book.path, 'metadata.opf')

          if os.path.exists (file):

            root = etree.parse (file).getroot ()
            meta = root.find ('.//{http://www.idpf.org/2007/opf}metadata')
            date = meta.find ('.//{http://purl.org/dc/elements/1.1/}date').text

          else:

            file = os.path.join (book.path, f'{book.name}.epub')

            if os.path.exists (file):

              epub = Epub.read_epub (file, options = { 'ignore_ncx' : True })
              date = epub.get_metadata ('DC', 'date') [0] [0]

            else:

              got = False

              for file in os.scandir (book.path):

                if file.name.endswith ('.epub'):

                  file = file.path
                  epub = Epub.read_epub (file, options = { 'ignore_ncx' : True })
                  date = epub.get_metadata ('DC', 'date') [0] [0]

                  got = True
                  break

              if not got:

                raise Exception (f'Book {book.path} could not be assessed')

          date = isoparse (date)

          try:

            books [date.year].append (book.path)

          except KeyError:

            books [date.year] = [ book.path ]

  return books
