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
import json, os, subprocess, sys

extensions = { 'EPUB' : 'epub' }

def selfcall (*args) -> str:

  proc = subprocess.Popen ([ sys.executable, sys.argv [0] ] + list (args),
    stderr = subprocess.PIPE,
    stdout = subprocess.PIPE,
    text = True)
  stdout, stderr = proc.communicate ()

  if proc.returncode != 0:

    print (stderr, file = sys.stderr)
    exit (-1)

  else:

    return stdout

def Article (booklist : dict[int,list[str]], root : str) -> dict[int,list[(str,dict[str,str])]]:

  article = {}

  with open (booklist, mode = 'r') as stream:

    books = json.load (stream)

    for year, bunch in books.items ():

      entry = []

      for format_, name, path, title in bunch:

        if not format_ in extensions:

          raise Exception (f'Unknown book format {format_}')

        path = os.path.join (root, path, f'{name}.{extensions [format_]}')

        complexity = float (selfcall ('--complexity', path))
        length = int (selfcall ('--length', path))
        repetitiveness = float (selfcall ('--repetitiveness', path))

        entry.append ((title, { 'complexity' : complexity, 'length' : length, 'repetitiveness' : repetitiveness }))

      article [year] = entry

  return article
