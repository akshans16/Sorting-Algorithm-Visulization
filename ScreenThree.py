import pygame
import random
import math
from CommonFun import Main

cf = Main()
pygame.init()

class TestScreen:
    def __init__(self):
        
        self.runTestScreen = True
        self.width = 1280
        self.height = 720

        self.window = pygame.display.set_mode((self.width,self.height), pygame.FULLSCREEN) # the screen will open in maximum size
        self.surface = pygame.display.get_surface() #get the surface of the current active display
        self.mid_w, self.mid_h = self.surface.get_width()/2, self.surface.get_height()/2
        self.TOP_PAD =  200
        self.SIDE_PAD = 100
        

        self.WHITE = 255,255,255
        self.RED = 255,0,0
        self.GREEN = 0,255,0
        self.BLUE = 0,0,255
        self.YELLOW = 255,255,0
        

        self.isSorted = False

        #####Colors#######
        self.GRADIENTS = [(128,128,128),(160,160,160),(0,0,0)]

        self.lst = []

        

        

    def generate_random_list(self,key_flag = False):

        """Creates a list of random numbers for sorting."""

        ##### This is how I fixed the biggest problem #####
        if key_flag:
            self.lst.clear()
            key_flag = False
        ###################################################

        elements = 100
        max_val = 100
        min_val = 0

        for _ in range(elements):
            val = random.randint(min_val,max_val)
            self.lst.append(val)
        return self.lst
    

    def set_list(self, lst):

        """Sets the list to be visualized."""
        
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        
        
        self.start_x = self.SIDE_PAD // 2

    
    def draw_list(self,color_positions={},clear_bg = False):

        """Visualizes the list with colored bars."""

        lst = self.lst
        
        if clear_bg:
        
            clear_rect = (self.SIDE_PAD//2, self.TOP_PAD, 
		    				self.width - self.SIDE_PAD, self.height - self.TOP_PAD)
            pygame.draw.rect(self.window, self.WHITE,clear_rect)
        

        for i, val in enumerate(lst):
            x = self.start_x + i * self.block_width
            y = self.height - (val - self.min_val) * self.block_height
            
            color = self.GRADIENTS[i % 3] 

            if i in color_positions:
                color = color_positions[i]

            pygame.draw.rect(self.window,color,(x,y,self.block_width,self.height))
        
        if clear_bg:
            pygame.display.update()

    
    def draw_test_screen(self,algo_name,option_state):

        """Displays the initial screen elements."""

        self.surface.fill(self.WHITE)
        cf.draw_text("SORTING ALGORITHM VISUALIZATION", 40, self.mid_w,40,self.window)
        cf.draw_text(f"Algorithm : {algo_name}", 25, self.mid_w-150, 80, self.window)
        cf.draw_text(f"Order : {option_state}", 25, self.mid_w+150, 80, self.window)
        cf.draw_text("PRESS [Space] TO Start Sorting",22,self.mid_w-170,120, self.window)
        cf.draw_text("PRESS [Backspace] TO Return",22,self.mid_w+170,120, self.window)
        cf.draw_text("PRESS [R] TO Reset",22,self.mid_w,160, self.window)

        self.draw_list()

        pygame.display.update()

    def bubble_sort_algorithm(self,option_state):
        ascending = True if option_state == "Ascending Order" else False
        lst = self.lst
        for i in range(len(lst) - 1):
            for j in range (len(lst) -1-i):
                num1 = lst[j]
                num2 = lst[j+1]

                if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                    lst[j], lst[j+1] = lst[j+1],lst[j]
                    self.draw_list({j:self.GREEN,j+1:self.RED},True)
            yield True
        self.isSorted = True
        return lst
    
    def insertion_sort_algorithm(self,option_state):
        ascending = True if option_state == "Ascending Order" else False
        lst = self.lst

        for i in range(1, len(lst)):
            key = lst[i]
            j = i - 1
            while j >= 0 and ((key < lst[j] and ascending) or (key > lst[j] and not ascending)):
                lst[j + 1] = lst[j]
                self.draw_list({j + 1: self.RED, j: self.GREEN},True)
                j -= 1
            lst[j + 1] = key
            yield True
        self.isSorted = True
        return lst
    
    def selection_sort_algorithm(self,option_state):
        ascending = True if option_state == "Ascending Order" else False
        lst = self.lst

        for i in range(len(lst)):
            min_index = i
            for j in range(i + 1, len(lst)):
                if ((lst[j] < lst[min_index] and ascending) or (lst[j] > lst[min_index] and not ascending)):
                    min_index = j

            if i != min_index:
                lst[i], lst[min_index] = lst[min_index], lst[i]
                self.draw_list({i: self.RED, min_index: self.GREEN},True)
                yield True
        self.isSorted = True
        return lst



    def quick_sort_algorithm(self,option_state):
        ascending = True if option_state == "Ascending Order" else False
        lst = self.lst

        def partition(low, high):
            pivot = lst[high]
            i = low - 1

            for j in range(low, high):
                if (lst[j] <= pivot and ascending) or (lst[j] >= pivot and not ascending):
                    i += 1
                    lst[i], lst[j] = lst[j], lst[i]
                    self.draw_list({i: self.GREEN, j: self.RED},True)
                    

            lst[i + 1], lst[high] = lst[high], lst[i + 1]
            self.draw_list({i + 1: self.GREEN, high: self.RED},True)
            return i + 1

        def quick_sort(low, high):
            if low < high: 
                pivot_index = partition(low, high)

                yield from quick_sort(low, pivot_index - 1)
                
                yield from quick_sort(pivot_index + 1, high)
        
        yield from quick_sort(0, len(lst) - 1)
        yield True
        self.isSorted = True
        return lst

    def merge_sort_algorithm(self, option_state):
        ascending = True if option_state == "Ascending Order" else False
        lst = self.lst
        def merge(left, mid, right):
            sorted_list = []
            n1 = mid - left + 1
            n2 = right - mid

            a1 = [lst[left + i] for i in range(n1)]
            a2 = [lst[mid + j + 1] for j in range(n2)]

            i, j, k = 0, 0, 0

            while i < n1 and j < n2:
                if (a1[i] <= a2[j] and ascending) or (a1[i] >= a2[j] and not ascending):
                    sorted_list.append(a1[i])
                    self.draw_list({left + i: self.RED, mid + j + 1: self.GREEN}, True)
                    i += 1
                else:
                    sorted_list.append(a2[j])
                    self.draw_list({left + i: self.RED, mid + j + 1: self.GREEN}, True)
                    j += 1

            while i < n1:
                sorted_list.append(a1[i])
                
                i += 1

            while j < n2:
                sorted_list.append(a2[j])
                
                j += 1

            return sorted_list

        def merge_sort(left, right):
            if left < right:
                mid = (left + right) // 2
                yield from merge_sort(left, mid)
                
                yield from merge_sort(mid + 1, right)

                lst[left:right + 1] = merge(left, mid, right)
                # yield True
                yield lst  # Yield the sorted list for visualization

        yield from merge_sort(0, len(lst) - 1)
        yield True
        self.isSorted = True
        return lst
    


    def testScreen_loop(self,algo_name,option_state):

        """Manages the main loop, handling events and sorting."""

        clock = pygame.time.Clock()

        random_list = self.generate_random_list()
        
        self.set_list(random_list)

        sorting_algorithm_generator = None
        sorting = False
        

        while self.runTestScreen:

            clock.tick(15)

            if sorting:
                try:
                    next(sorting_algorithm_generator)
                # this exception is helping me to hold the screen after sorting is completed because when list is sorted the soring_algorithm_generator varibale is none and it will through NoneTypeError.
                except StopIteration or TypeError:
                    sorting = False
                    self.draw_test_screen(algo_name,option_state)
                
                    
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        random_list = self.generate_random_list(True)
                        return
                        
                    elif event.key == pygame.K_r:
                        random_list = self.generate_random_list(True)
                        sorting = False
                        self.isSorted = False
                        self.set_list(random_list)

                    elif event.key == pygame.K_SPACE and algo_name == "Bubble Sort":
                        sorting = True
                        if self.isSorted == True:
                            continue
                        sorting_algorithm_generator = self.bubble_sort_algorithm(option_state)

                    elif event.key == pygame.K_SPACE and algo_name == "Insertion Sort":
                        sorting = True
                        if self.isSorted == True:
                            continue
                        sorting_algorithm_generator = self.insertion_sort_algorithm(option_state)

                    elif event.key == pygame.K_SPACE and algo_name == "Selection Sort":
                        sorting = True
                        if self.isSorted == True:
                            continue
                        sorting_algorithm_generator = self.selection_sort_algorithm(option_state)

                    elif event.key == pygame.K_SPACE and algo_name == "Quick Sort":
                        sorting = True
                        if self.isSorted == True:
                            continue
                        sorting_algorithm_generator = self.quick_sort_algorithm(option_state)

                    elif event.key == pygame.K_SPACE and algo_name == "Merge Sort":
                        sorting = True
                        if self.isSorted == True:
                            continue
                        sorting_algorithm_generator = self.merge_sort_algorithm(option_state)

            self.draw_test_screen(algo_name,option_state)
            
        

if __name__ == "__main__":
    ts = TestScreen()
    ts.testScreen_loop(algo_name="Bubble Sort",option_state="Descending Order")

##### ISSUES #####
# 1. SORT BAR PROBLEM --> self.height instead of self.block_height [FIXED ]
# 2. CLEAR LIST PROBLEM --> by using key_flag in generate_random_list() function [FIXED]
# 3. CHANGING COLOR OF TWO ADJECENT BARS [Fixed]
# 4. MERGE SORTING ALGORITHM ANIMATION PROBLEM [Fixed]
    