from Game.Game import *
import sys
import esky
if hasattr(sys, "frozen"):
    app = esky.Esky(sys.executable, "http://www.proglab.com/my_game/")
    app.auto_update()

game = Game()
game.show_start_screen()

while game.running:
    game.new()
    game.run()
    game.show_game_over_screen()

pygame.quit()
# backgroung
# background = pygame.image.load(os.path.join(IMAGE_FOLDER, "background.jpg")).convert()
# window.blit(background, (0,0))