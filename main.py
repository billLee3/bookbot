from stats import get_word_count, get_num_per_character, build_console_report
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        book_text = get_book_text(sys.argv[1])
        num_words = get_word_count(get_book_text(sys.argv[1]))
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        #print(get_num_per_character(book_text))
        dict = get_num_per_character(book_text)
        report_list = build_console_report(dict)
        for report in report_list:
            if str.isalpha(report["char"]):
                print(f"{report["char"]}: {report["num"]}")
        print("============= END ===============")

