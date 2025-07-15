def get_num_words(book_text):
  words = book_text.split()  
  return len(words)


def get_character_count(book_text):
  lowercase_text = book_text.lower()
  character_count = {}
  for char in lowercase_text:
    if char.isalpha(): 
      is_letter_present = char in character_count
      if is_letter_present:
        character_count[char] += 1
      else:
        character_count[char] = 1
  return character_count

def sort(item):
  return item["num"]
        
def get_sorted_list_of_dictionaries(character_count):
  dictionaries_list = []
  for key, value in character_count.items():
    dictionaries_list.append({"character": key, "num": value})
  dictionaries_list.sort(key=sort, reverse=True)  

  return dictionaries_list