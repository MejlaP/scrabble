# list of letters
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# lists of points
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# create dictionary - letters as the keys, points as the values
letter_to_points = {letter: point for letter, point in zip(letters, points)}

# Add an element to dictionary => key is " " and value is 0
letter_to_points[" "] = 0

## SCORE A WORD ##
# def function that will take in a word and return how many points that word is worth
def score_word(word):
  point_total = 0
  for letter in word:
    # convert every letter in the word into a uppercase
    letter = letter.upper()
    # to get a value from a dictionary
    point_total += letter_to_points.get(letter, 0)
  return point_total

# run score_word function with an input of "brownie"
brownie_points = score_word("brownie")
# print the achieved points
print(f"For the word 'brownie' achieved points: {brownie_points}")

## SCORE A GAME ##
# dictionary that maps players to a list of the words they have played
player_to_words = {'player1': ['Blue', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'],'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}

# will contain the mapping of players to how many points they’ve scored
player_to_points = {}

# def function - iterate through the items in player_to_words
# call each player and each list of words
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    # inner loop that goes through each word in words
    for word in words:
      player_points += score_word(word)
    # setting current player value to be a key of player_to_points, with a value of player_points
    player_to_points[player] = player_points

# call function update_point_totals
update_point_totals()
# print users and their points
print(player_to_points)

# def function that would take in player and word, and add that word to the list of words they’ve played
def play_word(player, word):
  player_to_words[player].append(word)
  # call function update_point_totals any time a word is played
  update_point_totals()
  print(f"{player} added the word '{word}'")

# call function for player with a new word
play_word('player1', 'dog')
play_word('wordNerd', 'enter')
# print current score
print(player_to_points)

