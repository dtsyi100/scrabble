uppercase_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowercase_letters = []
uppercase_points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#convert uppercase letters to lowercase letters
for letter in uppercase_letters:
    letter = letter.lower()
    lowercase_letters.append(letter)

#full letter list
total_letters = uppercase_letters + lowercase_letters

#full point list
total_points = uppercase_points + uppercase_points

#making letter to point dictionary
letters_to_points = {key:value for key, value in zip(total_letters, total_points)}

#adding key, value to point dictionary
letters_to_points[" "] = 0

#this function scores every word played
def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letters_to_points.get(letter, 0)
    return point_total

#test scoring
brownie_points = score_word("BROWNIE")
#print(brownie_points)

#players and words played by players
player_to_words = {
"player1":["BLUE", "TENNIS", "EXIT"],
"wordNerd":["EARTH", "EYES", "MACHINE"],
"Lexi Con":["ERASER", "BELLY", "HUSKY"],
"Prof Reader":["ZAP", "COMA", "PERIOD"]}

#players and points scored by players
player_to_points = {}

#getting key, values in dict to use .items()
for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points

print(player_to_points)

def play_word(player, word):
    if player in player_to_words.keys():
        player_to_words[player] += [word]
    return player_to_words


play_word("player1", "HOLY")
print(player_to_words)
