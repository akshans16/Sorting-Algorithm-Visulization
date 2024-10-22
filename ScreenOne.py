import pygame
from CommonFun import Main
from ScreenTwo import OptionMenu
from ScreenFour import CreditScreen



cf = Main()


class FirstScreen:


    def __init__(self) :

        pygame.init()
        self.runningScreenOne = True

        self.font_size = 30

        self.curr_screen = None
        
        
        self.window = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN) # the screen will open in maximum size
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        pygame.display.set_caption("Sorting Algorithm Visulization")

        
        self.surface = pygame.display.get_surface() #get the surface of the current active display
        self.mid_w, self.mid_h = self.surface.get_width()/2, self.surface.get_height()/2#create an array of surface.width and surface.height

        self.bubblex, self.bubbley = self.mid_w, self.mid_h - 120 
        self.selectionx, self.selectiony = self.mid_w, self.mid_h - 80
        self.insertionx, self.insertiony = self.mid_w, self.mid_h - 40
        self.mergex, self.mergey = self.mid_w, self.mid_h 
        self.quickx, self.quicky = self.mid_w, self.mid_h + 40
        self.creditx,self.credity = self.mid_w, self.mid_h + 80
        self.quitx, self.quity = self.mid_w, self.mid_h + 120

        self.state = "Bubble Sort"
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -150
        self.cursor_rect.midtop = self.bubblex+self.offset,self.bubbley

         #### Colors ####
        self.WHITE = 255,255,255
        self.BLACK = 0,0,0
        self.BACKGROUND_COLOR = self.BLACK
    
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
    
    def check_events(self):
        self.reset_keys()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.runningScreenOne = False
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def draw_cursor(self):
        # Ensure the cursor is rendered within the screen boundaries
        self.cursor_rect.clamp_ip(self.window.get_rect())
        cf.draw_text("»", 50, self.cursor_rect.x, self.cursor_rect.y,self.window)

    def draw_on_screen(self):
        self.window.fill(self.WHITE)

        cf.draw_text("Sorting Algorithm Visualization", 50, self.mid_w, 50,self.window)

        cf.draw_text("[ MAIN MENU ]",35, self.mid_w, 150, self.window)
        

        cf.draw_text("Bubble Sort", self.font_size, self.bubblex, self.bubbley,self.window)
        cf.draw_text("Selection Sort", self.font_size, self.selectionx, self.selectiony,self.window)
        cf.draw_text("Insertion Sort", self.font_size, self.insertionx, self.insertiony,self.window)
        cf.draw_text("Merge Sort", self.font_size, self.mergex, self.mergey,self.window)
        cf.draw_text("Quick Sort", self.font_size, self.quickx, self.quicky,self.window)
        cf.draw_text("Credits", self.font_size, self.creditx, self.credity,self.window)
        cf.draw_text("Quit", self.font_size, self.quitx, self.quity,self.window)

        self.draw_cursor()
        
        pygame.display.flip()
    
    def move_cursor(self):
        
        if self.DOWN_KEY:
            if self.state == "Bubble Sort":
                self.cursor_rect.midtop = (self.selectionx + self.offset,self.selectiony)
                self.state = "Selection Sort"

            elif self.state == "Selection Sort":
                self.cursor_rect.midtop = (self.insertionx + self.offset,self.insertiony)
                self.state = "Insertion Sort"

            elif self.state == "Insertion Sort":
                self.cursor_rect.midtop = (self.mergex + self.offset, self.mergey)
                self.state = "Merge Sort"

            elif self.state == "Merge Sort":
                self.cursor_rect.midtop = (self.quickx + self.offset, self.quicky)
                self.state = "Quick Sort"

            elif self.state == "Quick Sort":
                self.cursor_rect.midtop = (self.creditx + self.offset, self.credity)
                self.state = "Credits"

            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.quitx + self.offset,self.quity)
                self.state = "Quit"

            elif self.state == "Quit":
                self.cursor_rect.midtop = (self.bubblex + self.offset, self.bubbley)
                self.state = "Bubble Sort"

        elif self.UP_KEY:

            if self.state == "Bubble Sort":
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = "Quit"
            elif self.state == "Selection Sort":
                self.cursor_rect.midtop = (self.bubblex + self.offset, self.bubbley)
                self.state = "Bubble Sort"
            elif self.state == "Insertion Sort":
                self.cursor_rect.midtop = (
                    self.selectionx + self.offset,
                    self.selectiony,
                )
                self.state = "Selection Sort"
            elif self.state == "Merge Sort":
                self.cursor_rect.midtop = (
                    self.insertionx + self.offset,
                    self.insertiony,
                )
                self.state = "Insertion Sort"
            elif self.state == "Quick Sort":
                self.cursor_rect.midtop = (self.mergex + self.offset, self.mergey)
                self.state = "Merge Sort"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.quickx + self.offset, self.quicky)
                self.state = "Quick Sort"
            elif self.state == "Quit":
                self.cursor_rect.midtop = (self.creditx + self.offset, self.credity)
                self.state = "Credits"

    def check_input(self):

        self.move_cursor()
        if self.START_KEY:
            if self.state == "Bubble Sort":
                st = OptionMenu()
                st.run_OptionMenu(self.state)
                
            elif self.state == "Selection Sort":
                st = OptionMenu()
                st.run_OptionMenu(self.state)

            elif self.state == "Insertion Sort":
                st = OptionMenu()
                st.run_OptionMenu(self.state)

            elif self.state == "Merge Sort":
                st = OptionMenu()
                st.run_OptionMenu(self.state)

            elif self.state == "Quick Sort":
                st = OptionMenu()
                st.run_OptionMenu(self.state)

            elif self.state == "Credits":
                om = CreditScreen()
                om.run_credit_screen()

            elif self.state == "Quit":
                self.runningScreenOne = False
                # pygame.quit()


    def run_Screen_One(self):

    
        pygame.display.update()

        while self.runningScreenOne:
            
            self.check_events()
            self.check_input()
            self.draw_on_screen()

            
            
if __name__ == '__main__':
    pygame.init()
    screen = FirstScreen()
    screen.run_Screen_One()
