package codingdojo;

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import static java.lang.StringTemplate.STR;

public class ChristmasSong {

    public String verseHeader(int verseNumber) {
        var verseNames = List.of("first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth");
        var verseName = verseNames.get(verseNumber - 1);
        return STR."""
                On the \{verseName} day of Christmas
                My true love sent to me:""";
    }

    public String verseBody(int verseNumber) {
        return String.join("\n", verseBodyLines(verseNumber));
    }

    public List<String> verseBodyLines(int verseNumber) {
        var lines = List.of(
                "A partridge in a pear tree.",
                "Two turtle doves and",
                "Three french hens",
                "Four calling birds",
                "Five golden rings",
                "Six geese a-laying",
                "Seven swans a-swimming",
                "Eight maids a-milking",
                "Nine ladies dancing",
                "Ten lords a-leaping",
                "Eleven pipers piping",
                "Twelve drummers drumming"
        );
        return lines.subList(0, verseNumber).reversed();
    }

    public static String printVerses(Stream<String> verses) {
        return verses.collect(Collectors.joining("\n\n"));
    }

    public Stream<String> allVerses() {
        return IntStream.rangeClosed(1, 12).mapToObj(n -> STR."""
        \{verseHeader(n)}
        \{verseBody(n)}"""
        );
    }

    public static String print() {
        return printVerses(new ChristmasSong().allVerses());
    }

    public static void main() {
        System.out.print(print());
    }
}