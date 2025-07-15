# BookBot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

## How to Use BookBot

1. **Clone the repository**  
  ```bash
  git clone https://github.com/yourusername/bookbot.git
  cd bookbot
  ```

2. **Download books to analyse**  
  
    1. Save your book in the `books/` directory as a `.txt` file.
    2. A good place to copy the text of books from is the Gutenberg Project. Browse the catalog here: https://www.gutenberg.org/cache/epub/feeds/
    3. From the CSV file available, make a note of the number in the first 'Text#' column of the book you're interested in.  
    4. Replace the number in this link with the 'Text#' number of your book: https://www.gutenberg.org/cache/epub/12345  
    5. Create a blank `.txt` file named after your book. Open up the txt file of your book; copy and paste everything into the blank `.txt` file.

3. **Run BookBot**  
  Make sure you have Python installed.
  Execute the main script with the path of your book file to get a report of the book:
  ```bash
  python main.py books/your_book.txt
  ```

## Features

- Counts words and characters in a book.

## Ideas
- display character frequency as a percentage
- list the 10 most frequent words used
- print the longest word
- estimate total time to read



## Contributing

Feel free to open issues or submit pull requests to improve BookBot!