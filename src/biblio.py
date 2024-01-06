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
from database import Config
from peewee import BareField
from peewee import BlobField
from peewee import BooleanField
from peewee import FloatField
from peewee import IntegerField
from peewee import Model
from peewee import SQL
from peewee import SqliteDatabase
from peewee import TextField
from peewee import TimestampField

class BaseModel (Model):

	class Meta:

		database = None

class UnknownField (object):

	def __init__(self, *_, **__): pass

class Biblio ():

	def __init__ (self, filename):

		self.database = SqliteDatabase (database = filename)

		self.Authors = self.define_Authors ()
		self.Books = self.define_Books ()
		self.BooksAuthorsLink = self.define_BooksAuthorsLink ()
		self.BooksCustomColumn5Link = self.define_BooksCustomColumn5Link ()
		self.BooksCustomColumn8Link = self.define_BooksCustomColumn8Link ()
		self.BooksLanguagesLink = self.define_BooksLanguagesLink ()
		self.BooksPluginData = self.define_BooksPluginData ()
		self.BooksPublishersLink = self.define_BooksPublishersLink ()
		self.BooksRatingsLink = self.define_BooksRatingsLink ()
		self.BooksSeriesLink = self.define_BooksSeriesLink ()
		self.BooksTagsLink = self.define_BooksTagsLink ()
		self.Comments = self.define_Comments ()
		self.ConversionOptions = self.define_ConversionOptions ()
		self.CustomColumn2 = self.define_CustomColumn2 ()
		self.CustomColumn3 = self.define_CustomColumn3 ()
		self.CustomColumn4 = self.define_CustomColumn4 ()
		self.CustomColumn5 = self.define_CustomColumn5 ()
		self.CustomColumn8 = self.define_CustomColumn8 ()
		self.CustomColumns = self.define_CustomColumns ()
		self.Data = self.define_Data ()
		self.Feeds = self.define_Feeds ()
		self.Identifiers = self.define_Identifiers ()
		self.Languages = self.define_Languages ()
		self.LibraryId = self.define_LibraryId ()
		self.MetadataDirtied = self.define_MetadataDirtied ()
		self.Preferences = self.define_Preferences ()
		self.Publishers = self.define_Publishers ()
		self.Ratings = self.define_Ratings ()
		self.Series = self.define_Series ()
		self.Tags = self.define_Tags ()

	def define_Authors (self):

		class Authors (BaseModel):

			link = TextField (constraints=[SQL("DEFAULT '""'")])
			name = TextField (unique=True)
			sort = TextField (null=True)

			class Meta:

				table_name = 'authors'

	def define_Books (self):

		class Books (BaseModel):

			author_sort = TextField (index=True, null=True)
			flags = IntegerField (constraints=[SQL("DEFAULT 1")])
			has_cover = BooleanField (constraints=[SQL("DEFAULT 0")], null=True)
			isbn = TextField (constraints=[SQL("DEFAULT '""'")], null=True)
			last_modified = TimestampField (constraints=[SQL("DEFAULT \"2000-01-01 00:00:00+00:00\"")])  # TIMESTAMP
			lccn = TextField (constraints=[SQL("DEFAULT '""'")], null=True)
			path = TextField (constraints=[SQL("DEFAULT '""'")])
			pubdate = TimestampField (constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)  # TIMESTAMP
			series_index = FloatField (constraints=[SQL("DEFAULT 1.0")])
			sort = TextField (index=True, null=True)
			timestamp = TimestampField (constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)  # TIMESTAMP
			title = TextField (constraints=[SQL("DEFAULT 'Unknown'")])
			uuid = TextField (null=True)

			class Meta:

				table_name = 'books'

		Books._meta.database = self.database
		return Books

	def define_BooksAuthorsLink (self):

		class BooksAuthorsLink (BaseModel):

			author = IntegerField (index=True)
			book = IntegerField (index=True)

			class Meta:

				table_name = 'books_authors_link'
				indexes = ((('book', 'author'), True))

		BooksAuthorsLink._meta.database = self.database
		return BooksAuthorsLink

	def define_BooksCustomColumn5Link (self):

		class BooksCustomColumn5Link (BaseModel):

			book = IntegerField (index=True)
			value = IntegerField (index=True)

			class Meta:

				table_name = 'books_custom_column_5_link'
				indexes = ((('book', 'value'), True))

		BooksCustomColumn5Link._meta.database = self.database
		return BooksCustomColumn5Link

	def define_BooksCustomColumn8Link (self):

		class BooksCustomColumn8Link (BaseModel):

			book = IntegerField (index=True)
			value = IntegerField (index=True)

			class Meta:

				table_name = 'books_custom_column_8_link'
				indexes = ((('book', 'value'), True))

		BooksCustomColumn8Link._meta.database = self.database
		return BooksCustomColumn8Link

	def define_BooksLanguagesLink (self):

		class BooksLanguagesLink (BaseModel):

			book = IntegerField (index=True)
			item_order = IntegerField (constraints=[SQL("DEFAULT 0")])
			lang_code = IntegerField (index=True)

			class Meta:

				table_name = 'books_languages_link'
				indexes = ((('book', 'lang_code'), True))

		BooksLanguagesLink._meta.database = self.database
		return BooksLanguagesLink

	def define_BooksPluginData (self):

		class BooksPluginData (BaseModel):

			book = UnknownField (null=True)  # INTEGER NON
			name = UnknownField (null=True)  # TEXT NON
			val = UnknownField (null=True)  # TEXT NON

			class Meta:

				table_name = 'books_plugin_data'
				indexes = ((('book', 'name'), True))

		BooksPluginData._meta.database = self.database
		return BooksPluginData

	def define_BooksPublishersLink (self):

		class BooksPublishersLink (BaseModel):

			book = IntegerField (unique=True)
			publisher = IntegerField (index=True)

			class Meta:

				table_name = 'books_publishers_link'

		BooksPublishersLink._meta.database = self.database
		return BooksPublishersLink

	def define_BooksRatingsLink (self):

		class BooksRatingsLink (BaseModel):

			book = IntegerField (index=True)
			rating = IntegerField (index=True)

			class Meta:

				table_name = 'books_ratings_link'
				indexes = ((('book', 'rating'), True))

		BooksRatingsLink._meta.database = self.database
		return BooksRatingsLink

	def define_BooksSeriesLink (self):

		class BooksSeriesLink (BaseModel):

			book = IntegerField (unique=True)
			series = IntegerField (index=True)

			class Meta:

				table_name = 'books_series_link'

		BooksSeriesLink._meta.database = self.database
		return BooksSeriesLink

	def define_BooksTagsLink (self):

		class BooksTagsLink(BaseModel):

			book = IntegerField (index=True)
			tag = IntegerField (index=True)

			class Meta:

				table_name = 'books_tags_link'
				indexes = ((('book', 'tag'), True))

		BooksTagsLink._meta.database = self.database
		return BooksTagsLink

	def define_Comments (self):

		class Comments (BaseModel):

			book = UnknownField (null=True, unique=True)  # INTEGER NON
			text = UnknownField (null=True)  # TEXT NON

			class Meta:
	
				table_name = 'comments'

		Comments._meta.database = self.database
		return Comments

	def define_ConversionOptions (self):

		class ConversionOptions (BaseModel):

			book = IntegerField (index=True, null=True)
			data = BlobField ()
			format = TextField (index=True)

			class Meta:

				table_name = 'conversion_options'
				indexes = ((('format', 'book'), True))

		ConversionOptions._meta.database = self.database
		return ConversionOptions

	def define_CustomColumn2 (self):

		class CustomColumn2(BaseModel):

			book = IntegerField (null=True, unique=True)
			value = IntegerField ()

			class Meta:

				table_name = 'custom_column_2'

		CustomColumn2._meta.database = self.database
		return CustomColumn2

	def define_CustomColumn3 (self):

		class CustomColumn3 (BaseModel):

			book = IntegerField (null=True, unique=True)
			value = TextField ()

			class Meta:

				table_name = 'custom_column_3'

		CustomColumn3._meta.database = self.database
		return CustomColumn3

	def define_CustomColumn4 (self):

		class CustomColumn4 (BaseModel):

			book = IntegerField (null=True, unique=True)
			value = FloatField ()

			class Meta:

				table_name = 'custom_column_4'

		CustomColumn4._meta.database = self.database
		return CustomColumn4

	def define_CustomColumn5 (self):

		class CustomColumn5 (BaseModel):

			value = TextField (unique=True)

			class Meta:
	
				table_name = 'custom_column_5'

		CustomColumn5._meta.database = self.database
		return CustomColumn5

	def define_CustomColumn8 (self):

		class CustomColumn8 (BaseModel):

			value = TextField (unique=True)

			class Meta:

				table_name = 'custom_column_8'

		CustomColumn8._meta.database = self.database
		return CustomColumn8

	def define_CustomColumns (self):

		class CustomColumns (BaseModel):

			datatype = TextField ()
			display = TextField (constraints=[SQL("DEFAULT '\"{}\"'")])
			editable = BooleanField (constraints=[SQL("DEFAULT 1")])
			is_multiple = BooleanField (constraints=[SQL("DEFAULT 0")])
			label = TextField (unique=True)
			mark_for_delete = BooleanField (constraints=[SQL("DEFAULT 0")])
			name = TextField ()
			normalized = BooleanField ()

			class Meta:

				table_name = 'custom_columns'

		CustomColumns._meta.database = self.database
		return CustomColumns

	def define_Data (self):

		class Data (BaseModel):

			book = IntegerField (index=True, null=False)  # INTEGER NON
			format = TextField (index=True, null=False)  # TEXT NON
			name = TextField (null=False)  # TEXT NON
			uncompressed_size = UnknownField (null=True)  # INTEGER NON

			class Meta:
				table_name = 'data'
				indexes = ((('book', 'format'), True))

		Data._meta.database = self.database
		return Data

	def define_Feeds (self):

		class Feeds (BaseModel):

			script = TextField ()
			title = TextField (unique=True)

			class Meta:

				table_name = 'feeds'

		Feeds._meta.database = self.database
		return Feeds

	def define_Identifiers (self):

		class Identifiers (BaseModel):

			book = UnknownField (null=True)  # INTEGER NON
			type = UnknownField (constraints=[SQL("DEFAULT \"isbn\"")], null=True)  # TEXT NON
			val = UnknownField (null=True)  # TEXT NON

			class Meta:
				table_name = 'identifiers'
				indexes = ((('book', 'type'), True))

		Identifiers._meta.database = self.database
		return Identifiers

	def define_Languages (self):

		class Languages (BaseModel):

			lang_code = UnknownField (null=True, unique=True)  # TEXT NON

			class Meta:

				table_name = 'languages'

		Languages._meta.database = self.database
		return Languages

	def define_LibraryId (self):

		class LibraryId (BaseModel):

			uuid = TextField (unique=True)

			class Meta:

				table_name = 'library_id'

		LibraryId._meta.database = self.database
		return LibraryId

	def define_MetadataDirtied (self):

		class MetadataDirtied (BaseModel):

			book = IntegerField (unique=True)

			class Meta:

				table_name = 'metadata_dirtied'

		MetadataDirtied._meta.database = self.database
		return MetadataDirtied

	def define_Preferences (self):

		class Preferences (BaseModel):

			key = UnknownField (null=True, unique=True)  # TEXT NON
			val = UnknownField (null=True)  # TEXT NON

			class Meta:

				table_name = 'preferences'

		Preferences._meta.database = self.database
		return Preferences

	def define_Publishers (self):

		class Publishers (BaseModel):

			name = TextField (unique=True)
			sort = TextField (null=True)

			class Meta:

				table_name = 'publishers'

		Publishers._meta.database = self.database
		return Publishers

	def define_Ratings (self):

		class Ratings (BaseModel):

			rating = IntegerField (null=True, unique=True)

			class Meta:

				table_name = 'ratings'

		Ratings._meta.database = self.database
		return Ratings

	def define_Series (self):

		class Series (BaseModel):

			name = TextField (unique=True)
			sort = TextField (null=True)

			class Meta:
	
				table_name = 'series'

		Series._meta.database = self.database
		return Series

	def define_Tags (self):

		class Tags (BaseModel):

			name = TextField (index=True)

			class Meta:

				table_name = 'tags'

		Tags._meta.database = self.database
		return Tags

