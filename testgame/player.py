import pygame

class Player():
    def __init__(self):
        self.player_hp = 100
        print("Player Created")

    def print_player_health(self):
        print(f"Player health is at {self.player_hp}.")
    
    def damage_hp(self,damage:int):
        self.player_hp -= damage
        

class Human(Player):
    def __init__(self):
        super().__init__()
        
if __name__ == "__main__":
    
    test_player = Player()
    print(test_player.player_hp)
    test_player.print_player_health()
    test_player.damage_hp(damage=5)
    test_player.print_player_health()
    
    
    test_human = Human()
    test_human