from christmas import verse_header, verse_name, verse_counting_line
from christmas import whole_verse, verse_body, whole_song


def test_verse_header():
    header = verse_header(1)
    assert header == """\
On the first day of Christmas
My true love gave to me:"""


def test_number_to_verse_name():
    assert "first" == verse_name(1)
    assert "second" == verse_name(2)


def test_verse_header_two():
    header = verse_header(2)
    assert header == """\
On the second day of Christmas
My true love gave to me:"""


def test_counting_line():
    assert verse_counting_line(1) == "A partridge in a pear tree."
    assert verse_counting_line(2) == "Two turtle doves and"


def test_verse_1():
    verse = whole_verse(1)
    assert verse == """\
On the first day of Christmas
My true love gave to me:
A partridge in a pear tree.
"""


def test_body():
    body = verse_body(2)
    assert body == """\
Two turtle doves and
A partridge in a pear tree."""


def test_verse_2():
    verse = whole_verse(2)
    assert verse == """\
On the second day of Christmas
My true love gave to me:
Two turtle doves and
A partridge in a pear tree.
"""


def test_verse_12():
    verse = whole_verse(12)
    assert verse == """\
On the twelfth day of Christmas
My true love gave to me:
Twelve drummers drumming
Eleven pipers piping
Ten lords a-leaping
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree.
"""


def test_whole_song():
    song = whole_song()
    assert song == """\
On the first day of Christmas
My true love gave to me:
A partridge in a pear tree.

On the second day of Christmas
My true love gave to me:
Two turtle doves and
A partridge in a pear tree.

On the third day of Christmas
My true love gave to me:
Three french hens
Two turtle doves and
A partridge in a pear tree.

On the fourth day of Christmas
My true love gave to me:
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree.

On the fifth day of Christmas
My true love gave to me:
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree.

On the sixth day of Christmas
My true love gave to me:
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree.

On the seventh day of Christmas
My true love gave to me:
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree.

On the eighth day of Christmas
My true love gave to me:
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree.

On the ninth day of Christmas
My true love gave to me:
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree.

On the tenth day of Christmas
My true love gave to me:
Ten lords a-leaping
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree.

On the eleventh day of Christmas
My true love gave to me:
Eleven pipers piping
Ten lords a-leaping
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree.

On the twelfth day of Christmas
My true love gave to me:
Twelve drummers drumming
Eleven pipers piping
Ten lords a-leaping
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves and
A partridge in a pear tree.
"""
