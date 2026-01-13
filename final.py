import pyxel
import random

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Avoid Game")
        self.player_x = 80
        self.player_y = 100
        self.enemies = []
        self.score = 0
        self.is_game_over = False
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.is_game_over:
            if pyxel.btnp(pyxel.KEY_R): 
                self.player_x = 80
                self.enemies = []
                self.score = 0
                self.is_game_over = False
            return

        if pyxel.btn(pyxel.KEY_LEFT) and self.player_x > 0:
            self.player_x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT) and self.player_x < pyxel.width - 8:
            self.player_x += 2

        if pyxel.frame_count % 20 == 0:
            self.enemies.append([random.randint(0, pyxel.width - 8), 0])

        new_enemies = []
        for enemy in self.enemies:
            enemy[1] += 2 
            if (abs(self.player_x - enemy[0]) < 6 and abs(self.player_y - enemy[1]) < 6):
                self.is_game_over = True
            if enemy[1] < pyxel.height:
                new_enemies.append(enemy)
            else:
                self.score += 30
        self.enemies = new_enemies

    def draw(self):
        pyxel.cls(0) 
        if self.is_game_over:
            pyxel.text(60, 50, "GAME OVER", 7)
            pyxel.text(50, 70, "Press R to Restart", 6)
            pyxel.text(55, 90, f"FINAL SCORE: {self.score}", 7)
        else:
            pyxel.rect(self.player_x, self.player_y, 8, 8, 10)
            for enemy in self.enemies:
                pyxel.circ(enemy[0], enemy[1], 4, 8)
            pyxel.text(5, 5, f"SCORE: {self.score}", 7)
App()