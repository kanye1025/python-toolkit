#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""A lightweight wrapper around pymysql.

Originally part of the Tornado framework.  The tornado.database module
is slated for removal in Tornado 3.0, and it is now available separately
as torndb.
"""

from __future__ import absolute_import, division, with_statement

import copy
import itertools
import logging
import os
import time

try:
    #import pymysql.constants
    #import pymysql.converters
    #import pymysql.cursors
    import pymysql.connections
    import pymysql.converters
    import pymysql.cursors

    from pymysql.charset import Charsets,Charset
    def by_id(self, id):
        try:
            return self._by_id[id]
        except:
            return None
    Charsets.by_id = by_id
    _charsets = Charsets()
    _charsets.add(Charset(1, 'big5', 'big5_chinese_ci', 'Yes'))
    _charsets.add(Charset(2, 'latin2', 'latin2_czech_cs', ''))
    _charsets.add(Charset(3, 'dec8', 'dec8_swedish_ci', 'Yes'))
    _charsets.add(Charset(4, 'cp850', 'cp850_general_ci', 'Yes'))
    _charsets.add(Charset(5, 'latin1', 'latin1_german1_ci', ''))
    _charsets.add(Charset(6, 'hp8', 'hp8_english_ci', 'Yes'))
    _charsets.add(Charset(7, 'koi8r', 'koi8r_general_ci', 'Yes'))
    _charsets.add(Charset(8, 'latin1', 'latin1_swedish_ci', 'Yes'))
    _charsets.add(Charset(9, 'latin2', 'latin2_general_ci', 'Yes'))
    _charsets.add(Charset(10, 'swe7', 'swe7_swedish_ci', 'Yes'))
    _charsets.add(Charset(11, 'ascii', 'ascii_general_ci', 'Yes'))
    _charsets.add(Charset(12, 'ujis', 'ujis_japanese_ci', 'Yes'))
    _charsets.add(Charset(13, 'sjis', 'sjis_japanese_ci', 'Yes'))
    _charsets.add(Charset(14, 'cp1251', 'cp1251_bulgarian_ci', ''))
    _charsets.add(Charset(15, 'latin1', 'latin1_danish_ci', ''))
    _charsets.add(Charset(16, 'hebrew', 'hebrew_general_ci', 'Yes'))
    _charsets.add(Charset(18, 'tis620', 'tis620_thai_ci', 'Yes'))
    _charsets.add(Charset(19, 'euckr', 'euckr_korean_ci', 'Yes'))
    _charsets.add(Charset(20, 'latin7', 'latin7_estonian_cs', ''))
    _charsets.add(Charset(21, 'latin2', 'latin2_hungarian_ci', ''))
    _charsets.add(Charset(22, 'koi8u', 'koi8u_general_ci', 'Yes'))
    _charsets.add(Charset(23, 'cp1251', 'cp1251_ukrainian_ci', ''))
    _charsets.add(Charset(24, 'gb2312', 'gb2312_chinese_ci', 'Yes'))
    _charsets.add(Charset(25, 'greek', 'greek_general_ci', 'Yes'))
    _charsets.add(Charset(26, 'cp1250', 'cp1250_general_ci', 'Yes'))
    _charsets.add(Charset(27, 'latin2', 'latin2_croatian_ci', ''))
    _charsets.add(Charset(28, 'gbk', 'gbk_chinese_ci', 'Yes'))
    _charsets.add(Charset(29, 'cp1257', 'cp1257_lithuanian_ci', ''))
    _charsets.add(Charset(30, 'latin5', 'latin5_turkish_ci', 'Yes'))
    _charsets.add(Charset(31, 'latin1', 'latin1_german2_ci', ''))
    _charsets.add(Charset(32, 'armscii8', 'armscii8_general_ci', 'Yes'))
    _charsets.add(Charset(33, 'utf8', 'utf8_general_ci', 'Yes'))
    _charsets.add(Charset(34, 'cp1250', 'cp1250_czech_cs', ''))
    _charsets.add(Charset(35, 'ucs2', 'ucs2_general_ci', 'Yes'))
    _charsets.add(Charset(36, 'cp866', 'cp866_general_ci', 'Yes'))
    _charsets.add(Charset(37, 'keybcs2', 'keybcs2_general_ci', 'Yes'))
    _charsets.add(Charset(38, 'macce', 'macce_general_ci', 'Yes'))
    _charsets.add(Charset(39, 'macroman', 'macroman_general_ci', 'Yes'))
    _charsets.add(Charset(40, 'cp852', 'cp852_general_ci', 'Yes'))
    _charsets.add(Charset(41, 'latin7', 'latin7_general_ci', 'Yes'))
    _charsets.add(Charset(42, 'latin7', 'latin7_general_cs', ''))
    _charsets.add(Charset(43, 'macce', 'macce_bin', ''))
    _charsets.add(Charset(44, 'cp1250', 'cp1250_croatian_ci', ''))
    _charsets.add(Charset(45, 'utf8mb4', 'utf8mb4_general_ci', 'Yes'))
    _charsets.add(Charset(46, 'utf8mb4', 'utf8mb4_bin', ''))
    _charsets.add(Charset(47, 'latin1', 'latin1_bin', ''))
    _charsets.add(Charset(48, 'latin1', 'latin1_general_ci', ''))
    _charsets.add(Charset(49, 'latin1', 'latin1_general_cs', ''))
    _charsets.add(Charset(50, 'cp1251', 'cp1251_bin', ''))
    _charsets.add(Charset(51, 'cp1251', 'cp1251_general_ci', 'Yes'))
    _charsets.add(Charset(52, 'cp1251', 'cp1251_general_cs', ''))
    _charsets.add(Charset(53, 'macroman', 'macroman_bin', ''))
    _charsets.add(Charset(54, 'utf16', 'utf16_general_ci', 'Yes'))
    _charsets.add(Charset(55, 'utf16', 'utf16_bin', ''))
    _charsets.add(Charset(57, 'cp1256', 'cp1256_general_ci', 'Yes'))
    _charsets.add(Charset(58, 'cp1257', 'cp1257_bin', ''))
    _charsets.add(Charset(59, 'cp1257', 'cp1257_general_ci', 'Yes'))
    _charsets.add(Charset(60, 'utf32', 'utf32_general_ci', 'Yes'))
    _charsets.add(Charset(61, 'utf32', 'utf32_bin', ''))
    _charsets.add(Charset(63, 'binary', 'binary', 'Yes'))
    _charsets.add(Charset(64, 'armscii8', 'armscii8_bin', ''))
    _charsets.add(Charset(65, 'ascii', 'ascii_bin', ''))
    _charsets.add(Charset(66, 'cp1250', 'cp1250_bin', ''))
    _charsets.add(Charset(67, 'cp1256', 'cp1256_bin', ''))
    _charsets.add(Charset(68, 'cp866', 'cp866_bin', ''))
    _charsets.add(Charset(69, 'dec8', 'dec8_bin', ''))
    _charsets.add(Charset(70, 'greek', 'greek_bin', ''))
    _charsets.add(Charset(71, 'hebrew', 'hebrew_bin', ''))
    _charsets.add(Charset(72, 'hp8', 'hp8_bin', ''))
    _charsets.add(Charset(73, 'keybcs2', 'keybcs2_bin', ''))
    _charsets.add(Charset(74, 'koi8r', 'koi8r_bin', ''))
    _charsets.add(Charset(75, 'koi8u', 'koi8u_bin', ''))
    _charsets.add(Charset(77, 'latin2', 'latin2_bin', ''))
    _charsets.add(Charset(78, 'latin5', 'latin5_bin', ''))
    _charsets.add(Charset(79, 'latin7', 'latin7_bin', ''))
    _charsets.add(Charset(80, 'cp850', 'cp850_bin', ''))
    _charsets.add(Charset(81, 'cp852', 'cp852_bin', ''))
    _charsets.add(Charset(82, 'swe7', 'swe7_bin', ''))
    _charsets.add(Charset(83, 'utf8', 'utf8_bin', ''))
    _charsets.add(Charset(84, 'big5', 'big5_bin', ''))
    _charsets.add(Charset(85, 'euckr', 'euckr_bin', ''))
    _charsets.add(Charset(86, 'gb2312', 'gb2312_bin', ''))
    _charsets.add(Charset(87, 'gbk', 'gbk_bin', ''))
    _charsets.add(Charset(88, 'sjis', 'sjis_bin', ''))
    _charsets.add(Charset(89, 'tis620', 'tis620_bin', ''))
    _charsets.add(Charset(90, 'ucs2', 'ucs2_bin', ''))
    _charsets.add(Charset(91, 'ujis', 'ujis_bin', ''))
    _charsets.add(Charset(92, 'geostd8', 'geostd8_general_ci', 'Yes'))
    _charsets.add(Charset(93, 'geostd8', 'geostd8_bin', ''))
    _charsets.add(Charset(94, 'latin1', 'latin1_spanish_ci', ''))
    _charsets.add(Charset(95, 'cp932', 'cp932_japanese_ci', 'Yes'))
    _charsets.add(Charset(96, 'cp932', 'cp932_bin', ''))
    _charsets.add(Charset(97, 'eucjpms', 'eucjpms_japanese_ci', 'Yes'))
    _charsets.add(Charset(98, 'eucjpms', 'eucjpms_bin', ''))
    _charsets.add(Charset(99, 'cp1250', 'cp1250_polish_ci', ''))
    _charsets.add(Charset(101, 'utf16', 'utf16_unicode_ci', ''))
    _charsets.add(Charset(102, 'utf16', 'utf16_icelandic_ci', ''))
    _charsets.add(Charset(103, 'utf16', 'utf16_latvian_ci', ''))
    _charsets.add(Charset(104, 'utf16', 'utf16_romanian_ci', ''))
    _charsets.add(Charset(105, 'utf16', 'utf16_slovenian_ci', ''))
    _charsets.add(Charset(106, 'utf16', 'utf16_polish_ci', ''))
    _charsets.add(Charset(107, 'utf16', 'utf16_estonian_ci', ''))
    _charsets.add(Charset(108, 'utf16', 'utf16_spanish_ci', ''))
    _charsets.add(Charset(109, 'utf16', 'utf16_swedish_ci', ''))
    _charsets.add(Charset(110, 'utf16', 'utf16_turkish_ci', ''))
    _charsets.add(Charset(111, 'utf16', 'utf16_czech_ci', ''))
    _charsets.add(Charset(112, 'utf16', 'utf16_danish_ci', ''))
    _charsets.add(Charset(113, 'utf16', 'utf16_lithuanian_ci', ''))
    _charsets.add(Charset(114, 'utf16', 'utf16_slovak_ci', ''))
    _charsets.add(Charset(115, 'utf16', 'utf16_spanish2_ci', ''))
    _charsets.add(Charset(116, 'utf16', 'utf16_roman_ci', ''))
    _charsets.add(Charset(117, 'utf16', 'utf16_persian_ci', ''))
    _charsets.add(Charset(118, 'utf16', 'utf16_esperanto_ci', ''))
    _charsets.add(Charset(119, 'utf16', 'utf16_hungarian_ci', ''))
    _charsets.add(Charset(120, 'utf16', 'utf16_sinhala_ci', ''))
    _charsets.add(Charset(128, 'ucs2', 'ucs2_unicode_ci', ''))
    _charsets.add(Charset(129, 'ucs2', 'ucs2_icelandic_ci', ''))
    _charsets.add(Charset(130, 'ucs2', 'ucs2_latvian_ci', ''))
    _charsets.add(Charset(131, 'ucs2', 'ucs2_romanian_ci', ''))
    _charsets.add(Charset(132, 'ucs2', 'ucs2_slovenian_ci', ''))
    _charsets.add(Charset(133, 'ucs2', 'ucs2_polish_ci', ''))
    _charsets.add(Charset(134, 'ucs2', 'ucs2_estonian_ci', ''))
    _charsets.add(Charset(135, 'ucs2', 'ucs2_spanish_ci', ''))
    _charsets.add(Charset(136, 'ucs2', 'ucs2_swedish_ci', ''))
    _charsets.add(Charset(137, 'ucs2', 'ucs2_turkish_ci', ''))
    _charsets.add(Charset(138, 'ucs2', 'ucs2_czech_ci', ''))
    _charsets.add(Charset(139, 'ucs2', 'ucs2_danish_ci', ''))
    _charsets.add(Charset(140, 'ucs2', 'ucs2_lithuanian_ci', ''))
    _charsets.add(Charset(141, 'ucs2', 'ucs2_slovak_ci', ''))
    _charsets.add(Charset(142, 'ucs2', 'ucs2_spanish2_ci', ''))
    _charsets.add(Charset(143, 'ucs2', 'ucs2_roman_ci', ''))
    _charsets.add(Charset(144, 'ucs2', 'ucs2_persian_ci', ''))
    _charsets.add(Charset(145, 'ucs2', 'ucs2_esperanto_ci', ''))
    _charsets.add(Charset(146, 'ucs2', 'ucs2_hungarian_ci', ''))
    _charsets.add(Charset(147, 'ucs2', 'ucs2_sinhala_ci', ''))
    _charsets.add(Charset(159, 'ucs2', 'ucs2_general_mysql500_ci', ''))
    _charsets.add(Charset(160, 'utf32', 'utf32_unicode_ci', ''))
    _charsets.add(Charset(161, 'utf32', 'utf32_icelandic_ci', ''))
    _charsets.add(Charset(162, 'utf32', 'utf32_latvian_ci', ''))
    _charsets.add(Charset(163, 'utf32', 'utf32_romanian_ci', ''))
    _charsets.add(Charset(164, 'utf32', 'utf32_slovenian_ci', ''))
    _charsets.add(Charset(165, 'utf32', 'utf32_polish_ci', ''))
    _charsets.add(Charset(166, 'utf32', 'utf32_estonian_ci', ''))
    _charsets.add(Charset(167, 'utf32', 'utf32_spanish_ci', ''))
    _charsets.add(Charset(168, 'utf32', 'utf32_swedish_ci', ''))
    _charsets.add(Charset(169, 'utf32', 'utf32_turkish_ci', ''))
    _charsets.add(Charset(170, 'utf32', 'utf32_czech_ci', ''))
    _charsets.add(Charset(171, 'utf32', 'utf32_danish_ci', ''))
    _charsets.add(Charset(172, 'utf32', 'utf32_lithuanian_ci', ''))
    _charsets.add(Charset(173, 'utf32', 'utf32_slovak_ci', ''))
    _charsets.add(Charset(174, 'utf32', 'utf32_spanish2_ci', ''))
    _charsets.add(Charset(175, 'utf32', 'utf32_roman_ci', ''))
    _charsets.add(Charset(176, 'utf32', 'utf32_persian_ci', ''))
    _charsets.add(Charset(177, 'utf32', 'utf32_esperanto_ci', ''))
    _charsets.add(Charset(178, 'utf32', 'utf32_hungarian_ci', ''))
    _charsets.add(Charset(179, 'utf32', 'utf32_sinhala_ci', ''))
    _charsets.add(Charset(192, 'utf8', 'utf8_unicode_ci', ''))
    _charsets.add(Charset(193, 'utf8', 'utf8_icelandic_ci', ''))
    _charsets.add(Charset(194, 'utf8', 'utf8_latvian_ci', ''))
    _charsets.add(Charset(195, 'utf8', 'utf8_romanian_ci', ''))
    _charsets.add(Charset(196, 'utf8', 'utf8_slovenian_ci', ''))
    _charsets.add(Charset(197, 'utf8', 'utf8_polish_ci', ''))
    _charsets.add(Charset(198, 'utf8', 'utf8_estonian_ci', ''))
    _charsets.add(Charset(199, 'utf8', 'utf8_spanish_ci', ''))
    _charsets.add(Charset(200, 'utf8', 'utf8_swedish_ci', ''))
    _charsets.add(Charset(201, 'utf8', 'utf8_turkish_ci', ''))
    _charsets.add(Charset(202, 'utf8', 'utf8_czech_ci', ''))
    _charsets.add(Charset(203, 'utf8', 'utf8_danish_ci', ''))
    _charsets.add(Charset(204, 'utf8', 'utf8_lithuanian_ci', ''))
    _charsets.add(Charset(205, 'utf8', 'utf8_slovak_ci', ''))
    _charsets.add(Charset(206, 'utf8', 'utf8_spanish2_ci', ''))
    _charsets.add(Charset(207, 'utf8', 'utf8_roman_ci', ''))
    _charsets.add(Charset(208, 'utf8', 'utf8_persian_ci', ''))
    _charsets.add(Charset(209, 'utf8', 'utf8_esperanto_ci', ''))
    _charsets.add(Charset(210, 'utf8', 'utf8_hungarian_ci', ''))
    _charsets.add(Charset(211, 'utf8', 'utf8_sinhala_ci', ''))
    _charsets.add(Charset(223, 'utf8', 'utf8_general_mysql500_ci', ''))
    _charsets.add(Charset(224, 'utf8mb4', 'utf8mb4_unicode_ci', ''))
    _charsets.add(Charset(225, 'utf8mb4', 'utf8mb4_icelandic_ci', ''))
    _charsets.add(Charset(226, 'utf8mb4', 'utf8mb4_latvian_ci', ''))
    _charsets.add(Charset(227, 'utf8mb4', 'utf8mb4_romanian_ci', ''))
    _charsets.add(Charset(228, 'utf8mb4', 'utf8mb4_slovenian_ci', ''))
    _charsets.add(Charset(229, 'utf8mb4', 'utf8mb4_polish_ci', ''))
    _charsets.add(Charset(230, 'utf8mb4', 'utf8mb4_estonian_ci', ''))
    _charsets.add(Charset(231, 'utf8mb4', 'utf8mb4_spanish_ci', ''))
    _charsets.add(Charset(232, 'utf8mb4', 'utf8mb4_swedish_ci', ''))
    _charsets.add(Charset(233, 'utf8mb4', 'utf8mb4_turkish_ci', ''))
    _charsets.add(Charset(234, 'utf8mb4', 'utf8mb4_czech_ci', ''))
    _charsets.add(Charset(235, 'utf8mb4', 'utf8mb4_danish_ci', ''))
    _charsets.add(Charset(236, 'utf8mb4', 'utf8mb4_lithuanian_ci', ''))
    _charsets.add(Charset(237, 'utf8mb4', 'utf8mb4_slovak_ci', ''))
    _charsets.add(Charset(238, 'utf8mb4', 'utf8mb4_spanish2_ci', ''))
    _charsets.add(Charset(239, 'utf8mb4', 'utf8mb4_roman_ci', ''))
    _charsets.add(Charset(240, 'utf8mb4', 'utf8mb4_persian_ci', ''))
    _charsets.add(Charset(241, 'utf8mb4', 'utf8mb4_esperanto_ci', ''))
    _charsets.add(Charset(242, 'utf8mb4', 'utf8mb4_hungarian_ci', ''))
    _charsets.add(Charset(243, 'utf8mb4', 'utf8mb4_sinhala_ci', ''))
    _charsets.add(Charset(244, 'utf8mb4', 'utf8mb4_german2_ci', ''))
    _charsets.add(Charset(245, 'utf8mb4', 'utf8mb4_croatian_ci', ''))
    _charsets.add(Charset(246, 'utf8mb4', 'utf8mb4_unicode_520_ci', ''))
    _charsets.add(Charset(247, 'utf8mb4', 'utf8mb4_vietnamese_ci', ''))
    #_charsets.add(Charset(255, None, None, ''))
    _charsets.add(Charset(255, 'utf8', 'utf8_general_ci', 'Yes'))
    pymysql.connections.charset_by_id = _charsets.by_id

except ImportError:
    # If pymysql isn't available this module won't actually be useable,
    # but we want it to at least be importable on readthedocs.org,
    # which has limitations on third-party modules.
    if 'READTHEDOCS' in os.environ:
        pymysql = None
    else:
        raise





version = "0.3"
version_info = (0, 3, 0, 0)

class Connection(object):
    """A lightweight wrapper around pymysql DB-API connections.

    The main value we provide is wrapping rows in a dict/object so that
    columns can be accessed by name. Typical usage::

        db = torndb.Connection("localhost", "mydatabase")
        for article in db.query("SELECT * FROM articles"):
            print article.title

    Cursors are hidden by the implementation, but other than that, the methods
    are very similar to the DB-API.

    We explicitly set the timezone to UTC and assume the character encoding to
    UTF-8 (can be changed) on all connections to avoid time zone and encoding errors.

    The sql_mode parameter is set by default to "traditional", which "gives an error instead of a warning"
    (http://dev.mysql.com/doc/refman/5.0/en/server-sql-mode.html). However, it can be set to
    any other mode including blank (None) thereby explicitly clearing the SQL mode.
    """
    def __init__(self, host, database, user=None, password=None,
                 max_idle_time=7 * 3600, connect_timeout=10, 
                 time_zone="+0:00", charset = "utf8", sql_mode="TRADITIONAL"):
        self.host = host
        self.database = database
        self.max_idle_time = float(max_idle_time)

        args = dict(conv=CONVERSIONS, charset=charset,
                    db=database, init_command=('SET time_zone = "%s"' % time_zone),
                    connect_timeout=connect_timeout, sql_mode=sql_mode)
        if user is not None:
            args["user"] = user
        if password is not None:
            args["passwd"] = password

        # We accept a path to a MySQL socket file or a host(:port) string
        if "/" in host:
            args["unix_socket"] = host
        else:
            self.socket = None
            pair = host.split(":")
            if len(pair) == 2:
                args["host"] = pair[0]
                args["port"] = int(pair[1])
            else:
                args["host"] = host
                args["port"] = 3306

        self._db = None
        self._db_args = args
        self._last_use_time = time.time()
        try:
            self.reconnect()
        except Exception:
            logging.error("Cannot connect to MySQL on %s", self.host,
                          exc_info=True)

    def __del__(self):
        self.close()

    def close(self):
        """Closes this database connection."""
        if getattr(self, "_db", None) is not None:
            self._db.close()
            self._db = None

    def reconnect(self):
        """Closes the existing database connection and re-opens it."""
        self.close()
        #self._db = pymysql.connect(**self._db_args)
        self._db = pymysql.connect(**self._db_args)
        self._db.autocommit(True)

    def iter(self, query, *parameters, **kwparameters):
        """Returns an iterator for the given query and parameters."""
        self._ensure_connected()
        cursor = pymysql.cursors.SSCursor(self._db)
        try:
            self._execute(cursor, query, parameters, kwparameters)
            column_names = [d[0] for d in cursor.description]
            for row in cursor:
                yield Row(zip(column_names, row))
        finally:
            cursor.close()

    def query(self, query, *parameters, **kwparameters):
        """Returns a row list for the given query and parameters."""
        cursor = self._cursor()
        try:
            self._execute(cursor, query, parameters, kwparameters)
            column_names = [d[0] for d in cursor.description]
            return [Row(itertools.zip_longest(column_names, row)) for row in cursor]
        finally:
            cursor.close()

    def get(self, query, *parameters, **kwparameters):
        """Returns the (singular) row returned by the given query.

        If the query has no results, returns None.  If it has
        more than one result, raises an exception.
        """
        rows = self.query(query, *parameters, **kwparameters)
        if not rows:
            return None
        elif len(rows) > 1:
            raise Exception("Multiple rows returned for Database.get() query")
        else:
            return rows[0]

    # rowcount is a more reasonable default return value than lastrowid,
    # but for historical compatibility execute() must return lastrowid.
    def execute(self, query, *parameters, **kwparameters):
        """Executes the given query, returning the lastrowid from the query."""
        return self.execute_lastrowid(query, *parameters, **kwparameters)

    def execute_lastrowid(self, query, *parameters, **kwparameters):
        """Executes the given query, returning the lastrowid from the query."""
        cursor = self._cursor()
        try:
            self._execute(cursor, query, parameters, kwparameters)
            return cursor.lastrowid
        finally:
            cursor.close()

    def execute_rowcount(self, query, *parameters, **kwparameters):
        """Executes the given query, returning the rowcount from the query."""
        cursor = self._cursor()
        try:
            self._execute(cursor, query, parameters, kwparameters)
            return cursor.rowcount
        finally:
            cursor.close()

    def executemany(self, query, parameters):
        """Executes the given query against all the given param sequences.

        We return the lastrowid from the query.
        """
        return self.executemany_lastrowid(query, parameters)

    def executemany_lastrowid(self, query, parameters):
        """Executes the given query against all the given param sequences.

        We return the lastrowid from the query.
        """
        cursor = self._cursor()
        try:
            cursor.executemany(query, parameters)
            return cursor.lastrowid
        finally:
            cursor.close()

    def executemany_rowcount(self, query, parameters):
        """Executes the given query against all the given param sequences.

        We return the rowcount from the query.
        """
        cursor = self._cursor()
        try:
            cursor.executemany(query, parameters)
            return cursor.rowcount
        finally:
            cursor.close()

    update = execute_rowcount
    updatemany = executemany_rowcount

    insert = execute_lastrowid
    insertmany = executemany_lastrowid

    def _ensure_connected(self):
        # Mysql by default closes client connections that are idle for
        # 8 hours, but the client library does not report this fact until
        # you try to perform a query and it fails.  Protect against this
        # case by preemptively closing and reopening the connection
        # if it has been idle for too long (7 hours by default).
        if (self._db is None or
            (time.time() - self._last_use_time > self.max_idle_time)):
            self.reconnect()
        self._last_use_time = time.time()

    def _cursor(self):
        self._ensure_connected()
        return self._db.cursor()

    def _execute(self, cursor, query, parameters, kwparameters):
        try:
            return cursor.execute(query, kwparameters or parameters)
        except OperationalError:
            logging.error("Error connecting to MySQL on %s", self.host)
            self.close()
            raise


class Row(dict):
    """A dict that allows for object-like property access syntax."""
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

if pymysql is not None:
    # Fix the access conversions to properly recognize unicode/binary
    FIELD_TYPE = pymysql.constants.FIELD_TYPE
    FLAG = pymysql.constants.FLAG
    CONVERSIONS = copy.copy(pymysql.converters.conversions)

    field_types = [FIELD_TYPE.BLOB, FIELD_TYPE.STRING, FIELD_TYPE.VAR_STRING]
    if 'VARCHAR' in vars(FIELD_TYPE):
        field_types.append(FIELD_TYPE.VARCHAR)

    for field_type in field_types:
        # CONVERSIONS[field_type] = [(FLAG.BINARY, str)] + CONVERSIONS[field_type]
        CONVERSIONS[field_type] = [(FLAG.BINARY, str)].append(CONVERSIONS[field_type])

    # Alias some common MySQL exceptions
    IntegrityError = pymysql.IntegrityError
    OperationalError = pymysql.OperationalError
