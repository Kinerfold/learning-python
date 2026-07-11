import pickle

FILENAME = 'games.pkl'

games = ["Minecraft", 
         "CS2", 
         "Terraria"]

with open(FILENAME, 'wb') as file:
    pickle.dump(games, file)

with open(FILENAME, 'rb') as file:
    games = pickle.load(file)
    
    print('Мой список игр: ', games)