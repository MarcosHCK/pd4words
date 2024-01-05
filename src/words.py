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
from database import Database
from peewee import AutoField
from peewee import CharField
from peewee import CompositeKey
from peewee import DateField
from peewee import FloatField
from peewee import IntegerField
from peewee import Model
from peewee import SQL
from peewee import TextField

database = Database ('.environment', 'Words', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True })

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class CoN(BaseModel):
    freq = IntegerField(null=True)
    sig = FloatField(null=True)
    w1_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    w2_id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'co_n'
        indexes = (
            (('w1_id', 'sig'), False),
            (('w1_id', 'w2_id'), True),
            (('w2_id', 'sig'), False),
        )
        primary_key = CompositeKey('w1_id', 'w2_id')

class CoS(BaseModel):
    freq = IntegerField(null=True)
    sig = FloatField(null=True)
    w1_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    w2_id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'co_s'
        indexes = (
            (('w1_id', 'sig'), False),
            (('w1_id', 'w2_id'), True),
            (('w2_id', 'sig'), False),
        )
        primary_key = CompositeKey('w1_id', 'w2_id')

class InvSo(BaseModel):
    s_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    so_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)

    class Meta:
        table_name = 'inv_so'
        primary_key = False

class InvW(BaseModel):
    pos = IntegerField(constraints=[SQL("DEFAULT 0")])
    s_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    w_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)

    class Meta:
        table_name = 'inv_w'
        indexes = (
            (('w_id', 's_id'), False),
        )
        primary_key = False

class Sentences(BaseModel):
    s_id = AutoField()
    sentence = TextField()

    class Meta:
        table_name = 'sentences'

class SentencesTagged(BaseModel):
    s_id = AutoField()
    sentence = TextField(null=True)

    class Meta:
        table_name = 'sentences_tagged'

class Sources(BaseModel):
    date = DateField(index=True, null=True)
    so_id = AutoField()
    source = CharField(null=True)

    class Meta:
        table_name = 'sources'

class Words(BaseModel):
    freq = IntegerField(null=True)
    w_id = AutoField()
    word = CharField(unique=True)

    class Meta:
        table_name = 'words'

