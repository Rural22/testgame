from food import Food
from sprite import Sprite
from pygame import Surface


class FoodManager:
    def __init__(self, amount: int, resolution: tuple[int, int]):
        self.resolution = resolution
        self.food = self.create_food(amount)
        self.food_multiplier = 1

    def create_food(self, amount: int) -> list[Food]:
        food = []
        for i in range(amount):
            food.append(Food(self.resolution))

        return food

    def collision(self, sprite: Sprite):
        eaten_food = []
        for i, f in enumerate(self.food):
            if f.is_colliding(sprite.player_pos):
                print("FOOD COLLIDE")
                eaten_food.append(i)
        
        if not eaten_food:
            return 0
                
        score_value = self._food_remove(eaten_food)
        self.food_multiplier += 1
        return score_value
        
    def _food_remove(self,eaten_food:list[int]):
        if not eaten_food:
            return 0
        score_value = 0
        for i in eaten_food:
            self.food.pop(i)
            score_value += 1
        for j in range(self.food_multiplier):
            self.food.append(Food(self.resolution))
            print(self.food_multiplier)
        
        return score_value

    def render_screen(self,screen:Surface):
        for food in self.food:
            food.render(screen)