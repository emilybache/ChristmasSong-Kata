package codingdojo;

import org.approvaltests.Approvals;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class ChristmasSongTest {

    @Test
    void first_two_lines_any_verse() {
        var expected = """
                On the fourth day of Christmas
                My true love sent to me:""";
        assertEquals(expected, new ChristmasSong().verseHeader(4));
    }

    @Test
    void verse_1_body() {
        var expected = "A partridge in a pear tree.";
        assertEquals(expected, new ChristmasSong().verseBody(1));
    }
    @Test
    void verse_2_body() {
        var expected = """
                Two turtle doves and
                A partridge in a pear tree.""";
        assertEquals(expected, new ChristmasSong().verseBody(2));
    }

    @Test
    void verse_3_lines() {
        var expected = List.of(
                "Three french hens",
                "Two turtle doves and",
                "A partridge in a pear tree.");
        assertEquals(expected, new ChristmasSong().verseBodyLines(3));
    }

    @Test
    void verse_spacing() {
        var verses = List.of("one", "two");
        var actual = ChristmasSong.printVerses(verses.stream());
        assertEquals("""
                one
                
                two""", actual);
    }

    @Test
    void generate_all_verses() {
        List<String> verses = new ChristmasSong().allVerses().toList();
        assertEquals(12, verses.size());
        assertEquals(verses.getFirst(), """
                On the first day of Christmas
                My true love sent to me:
                A partridge in a pear tree.""");
    }

    @Test
    void whole_song() {
        Approvals.verify(ChristmasSong.print());
    }

}
