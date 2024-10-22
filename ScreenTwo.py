import pygame
from ScreenThree import TestScreen
from CommonFun import Main


cf = Main()
pygame.init()

class OptionMenu:
    def __init__(self):
        self.WHITE = 255,255,255
        self.runOptionMenu = True
        self.window = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
        self.surface = pygame.display.get_surface() #get the surface of the current active display
        self.mid_w, self.mid_h = self.surface.get_width()/2, self.surface.get_height()/2
        self.ascendingx, self.ascendingy = self.mid_w-130,self.mid_h
        self.descendingx,self.descendingy = self.mid_w-130,self.mid_h+30
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100
        self.cursor_rect.midtop = self.ascendingx+self.offset, self.ascendingy
        self.UP_KEY, self.DOWN_KEY,self.ENTER_KEY,self.BACK_KEY = False,False,False,False
        self.optionState = 'Ascending Order'
    
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY,self.ENTER_KEY,self.BACK_KEY = False,False,False,False
    
    def draw_cursor(self):
        # Ensure the cursor is rendered within the screen boundaries
        self.cursor_rect.clamp_ip(self.window.get_rect())
        cf.draw_text("»", 40, self.cursor_rect.x, self.cursor_rect.y,self.window)
    
    def draw_option_menu(self,state):
        self.window.fill(self.WHITE)
        cf.draw_text("Sorting Algorithm Visualization", 40, self.mid_w, 50,self.window)
        cf.draw_text(f'ALGORITHM » [ {state} ]', 22, self.mid_w, 100,self.window)
        cf.draw_text('CHOOSE OPTION', 22, self.mid_w-130,310,self.window)
        cf.draw_text('Ascending Order', 20, self.ascendingx,self.ascendingy,self.window)
        cf.draw_text('Descending Order', 20, self.descendingx,self.descendingy,self.window)
        cf.draw_text('( Press Backspace to return to menu )', 22, self.mid_w, self.mid_h/2+300,self.window)
        self.algorithm_info(state)
        self.draw_cursor()
        pygame.display.flip()
    
    def algorithm_info(self,state):

        if state == "Bubble Sort":
            cf.draw_text("× DESCRIPTION ×",24,self.mid_w,150,self.window)
            cf.draw_text("Bubble Sort compares adjacent elements and",22,self.mid_w,200,self.window)
            cf.draw_text("swaps them if they are in the wrong order",22,self.mid_w,230,self.window)
            cf.draw_text("iterating through the list until it is sorted",22,self.mid_w,260,self.window)

            cf.draw_text("TIME COMPLEXITY",22,self.mid_w+100,310,self.window)
            cf.draw_text("BEST CASE | O ( n )",18,self.mid_w+110,360,self.window)
            cf.draw_text("AVERAGE CASE | O ( n^2 )",18,self.mid_w+100,390,self.window)
            cf.draw_text("WORST CASE | O ( n^2 )",18,self.mid_w+100,420,self.window)
        
        elif state == "Insertion Sort":
            cf.draw_text("× DESCRIPTION ×",24,self.mid_w,150,self.window)
            cf.draw_text("Insertion Sort iterates, inserting a new element",22,self.mid_w,200,self.window)
            cf.draw_text("into the sorted list, and moving the already sorted",22,self.mid_w,230,self.window)
            cf.draw_text("elements to the right of the inserted element.",22,self.mid_w,260,self.window)
            
            cf.draw_text("TIME COMPLEXITY",22,self.mid_w+100,310,self.window)
            cf.draw_text("BEST CASE | O( n )",18,self.mid_w+100,360,self.window)
            cf.draw_text("AVERAGE CASE | O( n^2)",18,self.mid_w+100,390,self.window)
            cf.draw_text("WORST CASE | O( n^2 )",18,self.mid_w+100,420,self.window)
        
        elif state == "Selection Sort":
            cf.draw_text("× DESCRIPTION ×",24,self.mid_w,150,self.window)
            cf.draw_text("Selection Sort iterates, selecting the smallest",22,self.mid_w,200,self.window)
            cf.draw_text("element in the unsorted list and moving it to the",22,self.mid_w,230,self.window)
            cf.draw_text("front of the sorted list.",22,self.mid_w,260,self.window)
            
            cf.draw_text("TIME COMPLEXITY",22,self.mid_w+100,310,self.window)
            cf.draw_text("BEST CASE | O( n^2 )",18,self.mid_w+100,360,self.window)
            cf.draw_text("AVERAGE CASE | O( n^2 )",18,self.mid_w+100,390,self.window)
            cf.draw_text("WORST CASE | O( n^2 )",18,self.mid_w+100,420,self.window)
        
        elif state == "Quick Sort":
            cf.draw_text("× DESCRIPTION ×",24,self.mid_w,150,self.window)
            cf.draw_text("Quick Sort recursively partitions the array",22,self.mid_w,200,self.window)
            cf.draw_text("using a pivot, arranging elements smaller and",22,self.mid_w,230,self.window)
            cf.draw_text(" larger than the pivot on its respective sides.",22,self.mid_w,260,self.window)

            cf.draw_text("TIME COMPLEXITY",22,self.mid_w+100,310,self.window)
            cf.draw_text("BEST CASE | O( n log n )",18,self.mid_w+100,360,self.window)
            cf.draw_text("AVERAGE CASE | O( n log n )",18,self.mid_w+100,390,self.window)
            cf.draw_text("WORST CASE | O( n^2 )",18,self.mid_w+100,420,self.window)
        
        elif state == "Merge Sort":
            cf.draw_text("× DESCRIPTION ×",24,self.mid_w,150,self.window)
            cf.draw_text("Merge Sort is a divide and conquer algorithm",22,self.mid_w,200,self.window)
            cf.draw_text("that sorts an array into two halves and then",22,self.mid_w,230,self.window)
            cf.draw_text("merges the sorted halves back into the original",22,self.mid_w,260,self.window)

            cf.draw_text("TIME COMPLEXITY",22,self.mid_w+100,310,self.window)
            cf.draw_text("BEST CASE | O( n log n )",18,self.mid_w+100,360,self.window)
            cf.draw_text("AVERAGE CASE | O( n log n )",18,self.mid_w+100,390,self.window)
            cf.draw_text("WORST CASE | O( n log n )",18,self.mid_w+100,420,self.window)




    

    def check_event_option_menu(self):
        self.reset_keys()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.ENTER_KEY = True
                elif event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                elif event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                elif event.key == pygame.K_UP:
                    self.UP_KEY = True

    def check_input_option_menu(self,state): 
        if self.UP_KEY :
            if self.optionState == 'Ascending Order':
                self.cursor_rect.midtop = (self.descendingx + self.offset,self.descendingy)
                self.optionState = 'Descending Order'
            elif self.optionState == 'Descending Order':
                self.cursor_rect.midtop = (self.ascendingx + self.offset, self.ascendingy)
                self.optionState = 'Ascending Order'

        elif self.DOWN_KEY:
            if self.optionState == 'Ascending Order':
                self.cursor_rect.midtop = (self.descendingx + self.offset, self.descendingy)
                self.optionState = 'Descending Order'
            elif self.optionState == 'Descending Order':
                self.cursor_rect.midtop = (self.ascendingx + self.offset, self.ascendingy)
                self.optionState = 'Ascending Order'
        
        elif self.ENTER_KEY:
            ts = TestScreen()
            if self.optionState == 'Ascending Order':
                # self.run_OptionMenu = False
                ts.testScreen_loop(state,self.optionState)
            elif self.optionState == 'Descending Order':
                # self.run_OptionMenu = False
                ts.testScreen_loop(state,self.optionState)

        elif self.BACK_KEY:
            self.runOptionMenu = False
            return
            
        
    def run_OptionMenu(self,state):
        
        pygame.display.update()

        while self.runOptionMenu:
            
            self.check_event_option_menu()
            self.check_input_option_menu(state)
            self.draw_option_menu(state)
            
        
        


if __name__ == '__main__':
    pygame.init()
    op = OptionMenu()
    op.run_OptionMenu(state="Bubble Sort")
