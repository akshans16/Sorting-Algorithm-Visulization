# CreditScreen.py
import pygame
from CommonFun import Main
 

cf = Main()
pygame.init()

class CreditScreen:
    """
        This class represents the credit screen for the sorting algorithm visualization program.
    """
    def __init__(self):

        """
        This method initializes the credit screen object.
        """
        
        self.startCreditScreen = True
        self.window = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
        self.surface = pygame.display.get_surface()
        self.mid_w, self.mid_h = self.surface.get_width() // 2, self.surface.get_height() // 2
        self.WHITE = 255, 255, 255
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def reset_keys(self):
        """
        This method resets the key press flags to False after each frame is drawn.
        """
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_credit_screen(self):
        """
        This method draws the credit screen elements.
        """
        self.surface.fill(self.WHITE)
        cf.draw_text("SORTING ALGORITHM VISUALIZATION", 40, self.mid_w, 50, self.window)
        cf.draw_text("[ CREDITS ]", 28, self.mid_w, 150, self.window)
        cf.draw_text("Developed by —› Akshansh Khare ", 24, self.mid_w, 250, self.window)
        cf.draw_text("Designer —› Akshansh Khare", 24, self.mid_w, 300, self.window)
        cf.draw_text(" Tools and Technologies —› pygame, VS Code", 24, self.mid_w, 350, self.window)
        # cf.draw_text(" Mohammad Arman —› [Technical Writer]", 24, self.mid_w, 400, self.window)
        cf.draw_text("( Press BACKSPACE to return to menu )", 24, self.mid_w, 500, self.window)
        pygame.display.update()
        self.reset_keys()

    

    def run_credit_screen(self):
        """
        This method handles the main loop of the credit screen.
        """
        while self.startCreditScreen:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        return
                        
            self.draw_credit_screen()

if __name__ == "__main__":
    cs = CreditScreen()
    cs.run_credit_screen()
    
