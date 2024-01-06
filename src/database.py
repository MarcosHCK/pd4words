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
from configparser import ConfigParser
from peewee import MySQLDatabase

mysqlmap = { 'hostname' : 'host', 'password' : 'passwd', 'username' : 'user' }

def Config (config_file = None, namespace = None, mapping = None, **kwargs):

  config = { }

  if config_file != None:

    parser = ConfigParser ()
    parser.read (config_file)

    if namespace == None:

      group = parser ['Database']

    else:

      group = f'Database.{namespace}'
      group = parser [group]

    for name, value in group.items ():

      config [name] = value

  for name, value in kwargs.items ():

    if not name in config:

      config [name] = value

  if mapping != None:

    for from_name, to_name in mapping.items ():

      try:
        config [to_name] = config [from_name]
        del config [from_name]
      except KeyError: pass

  return config

def MySQLConfig (config_file = None, namespace = None, **kwargs):

  return Config (config_file, namespace, mapping = mysqlmap, **kwargs)
