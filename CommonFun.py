import pygame


class Main:
    def draw_text(self, text, size, x, y,window):
        self.WHITE = 0,0,0
        self.font_name = 'Techno Race Font.otf'
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        window.blit(text_surface, text_rect)

    
    
    
        