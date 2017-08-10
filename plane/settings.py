class Settings():
    """飞机大战"""
    def __init__(self):
        self.screen_width=400
        self.screen_height=600
        self.bg_color=(255,255,255)

    def out(self):
        font=pygame.font.Font(None,32)
        text=pygame.rander('Score: %d'%score,1,(0,0,0))
        screen.blit(text,(0,0))
