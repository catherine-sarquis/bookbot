def get_book_text(book):
  book_content = book.read()
  return book_content

def get_num_words(book_text):
  words = book_text.split()
  return len(words)
  
def main():
  with open('books/frankenstein.txt') as book:
    book_text = get_book_text(book)
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")
    # print(book_text)
    
main()
    