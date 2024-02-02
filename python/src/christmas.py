def verse_name(number):
    names = ["first", "second", "third", "fourth",
             "fifth", "sixth", "seventh", "eighth",
             "ninth", "tenth", "eleventh", "twelfth"]
    return names[number - 1]


def verse_header(number):
    return f"""\
On the {verse_name(number)} day of Christmas
My true love gave to me:"""


def verse_counting_line(number):
    lines = {
        1: "A partridge in a pear tree.",
        2: "Two turtle doves and",
        12: "Twelve drummers drumming",
        11: "Eleven pipers piping",
        10: "Ten lords a-leaping",
        9: "Nine ladies dancing",
        8: "Eight maids a-milking",
        7: "Seven swans a-swimming",
        6: "Six geese a-laying",
        5: "Five golden rings",
        4: "Four calling birds",
        3: "Three french hens",
    }
    return lines[number]


def verse_body(number):
    lines = (verse_counting_line(i) for i in range(number, 0, -1))
    return "\n".join(lines)


def whole_verse(number):
    header = verse_header(number)
    body = verse_body(number)
    return f"{header}\n{body}\n"


def whole_song():
    verses = (whole_verse(i) for i in range(1, 13))
    return "\n".join(verses)
