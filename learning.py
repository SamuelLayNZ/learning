class Game:
#Defines a game title, release year, genre and produces a human friendly summary"""
    def __init__(self, title, release_year, genre):
        self.title = title
        self.release_year = release_year
        self.genre = genre
       
    def gamesummary(self):
        return '{} ({}, {})'.format(self.title, self.release_year, self.genre)

game1 = Game('Rimworld','2018','Base Builder')
game2 = Game('Factorio','2018','Base Builder')
game3 = Game('Skyrim','2011','Action RPG')

print(game1.gamesummary())

for Game

Testing yo.

Change made in VScode