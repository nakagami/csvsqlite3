##############################################################################
# The MIT License (MIT)
#
# Copyright (c) 2016 Hajime Nakagami
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
##############################################################################
# https://github.com/nakagami/csvsqlite3/
import io
import csv
import sqlite3

VERSION = (0, 1, 1)
__version__ = '%s.%s.%s' % VERSION
apilevel = '2.0'

def connect(path, encoding='utf-8', delimiter=',', tabname='csv'):
    if isinstance(path, io.StringIO):
        csvio = path
    else:
        csvio = open(path, 'r', encoding=encoding)

    cols = [r.strip() for r in csvio.readline().strip().split(delimiter)]

    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    cur.execute("CREATE TABLE %s (%s)" % (tabname, ','.join(cols)))

    sql = "INSERT INTO %s VALUES (%s)" % (tabname, ','.join('?' * len(cols)))
    for param in csv.reader(csvio, delimiter=delimiter):
        param.extend([None] * (len(cols) - len(param)))
        cur.execute(sql, param)
    conn.commit()

    return conn

