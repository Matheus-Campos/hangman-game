import random

possible_words = [
  'words',
  'world',
  'apple',
  'couch',
  'teeth',
  'foot',
  'liver',
  'chicken',
  'horse',
  'farm',
  'forehead'
]

def get_random_word():
  return random.sample(possible_words, 1)[0]
