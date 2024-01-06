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
from collections import Counter
from ebooklib import epub
from ebooklib import ITEM_DOCUMENT
from bs4 import BeautifulSoup
import nltk

class Ebook ():

  def __init__ (self, filename, language = 'english'):

    self.book = epub.read_epub (filename, options = { 'ignore_ncx' : True })
    self.documents = (BeautifulSoup (item.get_content (), 'html.parser') for item in self.book.get_items_of_type (ITEM_DOCUMENT))
    self.language = language

  def glob (self):

    text = ''

    for document in self.documents:

      text = text + ' ' + document.get_text ()
    return text

  def text (self):

    sentences = []
    text = self.glob ()

    for sentence in nltk.sent_tokenize (text, language = self.language):

      sentence = nltk.word_tokenize (sentence, language = self.language)
      sentences.append (sentence)

    text = ''

    for word in ( word for sentence in sentences for word in sentence ):

      text = text + ' ' + word

    return text

  def words (self):

    sentences = []
    text = self.glob ()

    for sentence in nltk.sent_tokenize (text, language = self.language):

      sentence = nltk.word_tokenize (sentence, language = self.language)
      sentences.append (sentence)

    words = [ word.lower () for sentence in sentences for word in sentence ]
    words = Counter (words)

    return words
