def get_formatted_list(sorted_list):
  formatted_list = f""
  for dictionary in range(len(sorted_list)):
    character = sorted_list[dictionary]["character"]
    character_total = sorted_list[dictionary]["num"]
    formatted_list += f"{character}: {character_total}\n"
  return formatted_list


def print_report(num_words, sorted_list, book_path):
  header = "============ BOOKBOT ============"
  analysing_message = f"Analyzing book found at {book_path}..."
  word_count_message = "----------- Word Count ----------"
  total_words_message = f"Found {num_words} total words"
  character_count_message = "--------- Character Count -------"
  
  formatted_list = get_formatted_list(sorted_list)
  
  end_message = "============= END ==============="
  report_text = f"{header}\n{analysing_message}\n{word_count_message}\n{total_words_message}\n{character_count_message}\n{formatted_list}\n{end_message}\n" 
  print(report_text)