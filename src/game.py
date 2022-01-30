import os
import wordlist

def main():
  clear_terminal()

  while True:
    word = wordlist.get_random_word()
    attempts = 5
    shown_word = '_' * len(word)
    print('Welcome to the hangman game!')
    while attempts >= 1:
      print('--------------------')
      print(f'Attemps: {attempts}')
      print(f"Word: {' '.join(list(shown_word))}")

      letter = input('Type a letter: ')
      if len(letter) > 1 or len(letter) == 0:
        print('Invalid letter, try again.')
        continue

      indexes = find_letters_in_word(letter, word)
      if indexes is None:
        attempts -= 1
        print(f"The word doesn't contain the letter {letter}.")
      else:
        word_list = list(shown_word)
        for index in indexes:
          word_list[index] = letter
        shown_word = ''.join(word_list)
        if '_' not in shown_word:
          clear_terminal()
          print('Victory!')
          print(f'The word is {word}.')
          break
    else:
      clear_terminal()
      print('Game over! :(')

    play_again = ask_play_again()
    if not play_again:
      print('Bye.')
      break
    clear_terminal()

def find_letters_in_word(letter, word):
  if letter not in word:
    return None
  
  indexes = []
  for index in range(len(list(word))):
    if word[index] == letter:
      indexes.append(index)
  
  return indexes

def ask_play_again():
  while True:
    play_again = input('Play again? [Y/n] ')
    if play_again == 'Y' or play_again == 'y' or play_again == '':
      return True
    elif play_again == 'N' or play_again == 'n':
      return False
    else:
      print('Invalid answer.')

def clear_terminal():
  os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print('\nClosing game... Bye!')
  except:
    print('\nUnexpected error, closing game...')
