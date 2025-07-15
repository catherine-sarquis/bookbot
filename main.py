from stats import get_num_words, get_character_count, get_sorted_list_of_dictionaries
from print_report import print_report

def get_book_text(book):
  book_content = book.read()
  return book_content
  
def main():
  with open('books/frankenstein.txt') as book:
    book_text = get_book_text(book)
    num_words = get_num_words(book_text)
    # print(f"{num_words} words found in the document")
    character_count = get_character_count(book_text)
    sorted_list = get_sorted_list_of_dictionaries(character_count)
    print_report(num_words, sorted_list)
    
main()
    