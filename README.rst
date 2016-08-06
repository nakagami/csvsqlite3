=============
csvsqlite3
=============

Csv reader like PEP 249 API.

Requirements
-----------------

- Python 3.x


Installation
-----------------

::

    $ pip install csvsqlite3

Example
-----------------

::

   import csvsqlite3
   conn = minitds.connect('/foo/bar/baz.csv')
   cur = conn.cursor()
   cur.execute('select * from csv')
   for r in cur.fetchall():
      print(r[0], r[1])
   conn.close()

