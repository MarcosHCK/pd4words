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
from argparse import ArgumentParser
from ebook import Ebook
from measures import Complexity
from measures import Length
from measures import Repetitiveness
import nltk, os

nltk_models = [ 'punkt', 'wordnet' ]
nltk_path = os.path.realpath ('./nltk/')

def program ():

  parser = ArgumentParser (description = 'pd4words')

  # Options
  parser.add_argument ('--language', help = 'Language to use', metavar = 'LANGUAGE', type = str, default = 'spanish')

  # Subsystems
  parser.add_argument ('--complexity', help = 'Measure EBook language-wise complexity', metavar = 'FILE', type = str)
  parser.add_argument ('--length', help = 'Measure EBook language-wise length', metavar = 'FILE', type = str)
  parser.add_argument ('--repetitiveness', help = 'Measure EBook language-wise repetitiveness', metavar = 'FILE', type = str)

  args = parser.parse_args ()

  # Get nltk ready

  if os.path.exists (nltk_path):

    nltk.data.path.append (nltk_path)

  else:

    os.makedirs (nltk_path)

    nltk.data.path.append (nltk_path)

    for model in nltk_models:

      nltk.download (model, download_dir = nltk_path)

  language = args.language

  if args.complexity != None:

    ebook = Ebook (args.complexity, language = language)
    words = ebook.words ()

    print (Complexity (words))

  elif args.length != None:

    ebook = Ebook (args.length, language = language)
    words = ebook.words ()

    print (Length (words))

  elif args.repetitiveness != None:

    ebook = Ebook (args.repetitiveness, language = language)
    words = ebook.words ()

    print (Repetitiveness (words))

program ()
