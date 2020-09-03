import pygame
from pygame.locals import *
from Pilha import *
import os
from random import randint


class Observer():
    _observers = []
    def __init__(self):
        self._observers.append(self)
        self._observables = {}
    def observe(self, event_name, callback):
        self._observables[event_name] = callback


class Event():
    def __init__(self, name, data, autofire = True):
        self.name = name
        self.data = data
        if autofire:
            self.fire()
    def fire(self):
        for observer in Observer._observers:
            if self.name in observer._observables:
                observer._observables[self.name](self.data)

class Card(pygame.sprite.Sprite):
    _uniqueId = 0
    
    def __init__(self, path, collisionRect = None):
        super(Card, self).__init__()
        self.collisionRect = collisionRect
        self.surf = pygame.image.load(path).convert()
        self.id = Card._uniqueId
        Card._uniqueId += 1

        self.zero_rect = self.surf.get_rect()
        self.start_rect = self.zero_rect.move(randint(0, 600), randint(0, 340))
        
        while(self.start_rect.colliderect(self.collisionRect)):
            self.start_rect = self.zero_rect.move(randint(0, 600), randint(0, 340))
        
        self.rect = self.start_rect
        
        self.selected = False
        self.locked = False
        self.needsCheck = True
    
    def handleMouseClick(self, mouse_pos):
        if(not self.locked and self.rect.collidepoint(mouse_pos)):
            if(self.selected == False):
                self.selected = True
            else:
                self.selected = False
        else:
            if(self.selected):
                self.selected = False
    
    def handleCollision(self):
         if(not self.locked and self.collisionRect):
                if(self.rect.colliderect(self.collisionRect) and self.needsCheck):
                    Event('cardCollided',self)
                else:
                    self.rect = self.start_rect
                    self.needsCheck = True
           
    
    def update(self, mousePos):
        if(self.selected):
            self.rect = self.zero_rect.move(mousePos)
        else:
            self.handleCollision()
                    
        
class StaticItem(pygame.sprite.Sprite):
    def __init__(self,path,pos):
        super(StaticItem,self).__init__()
        self.surf = pygame.image.load(path).convert()
        self.rect = self.surf.get_rect().move(pos)
    
    def handleMouseClick(self, mouse_pos):
         pass
            
    def update(self,mousePos):
        pass

class GameMode:
    Playing, Win, Lose = range(3)

class App(Observer):
    def __init__(self):
        Observer.__init__(self)
        self._running = True
        self._display_surf = None
        self.pilha = Pilha()
        self.size = self.width, self.height = 640, 400
        
             
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        
        self.bgroundImage = pygame.image.load("./images/background3.jpg")
      
        self.cardMark = StaticItem("./images/stock_boardmark.png", (320,50))
        cardsList = []
        for f in os.listdir("./images/cards/"):
            if f[-3:] == "png":
                cardsList.append(Card("./images/cards/"+f, self.cardMark.rect))
                
        self.maxStack = len(cardsList)
        
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.cardMark)
        for card in cardsList:
            self.all_sprites.add(card)
            
        self._nextId = 0

        
        self._gameMode = GameMode.Playing
        self._gameTime = 10
        self._elapsed_time = 0
        self._currentTime = 0
        self.start_ticks=pygame.time.get_ticks()
        
        pygame.font.init()
        self.font = pygame.font.Font('freesansbold.ttf', 32) 
        self.win_text = self.font.render('Game won!', True, (0,255,0), (0,0,128)) 
        self.lose_text = self.font.render('Game lost!', True, (0,255,0), (0,0,128)) 
        self.textRect = self.win_text.get_rect()
        self.textRect.center = (320,200)
        
        self.hud_text = self.font.render('Time: ' + str(self._gameTime - self._elapsed_time), True, (0,255,0), (0,0,128)) 
  

    def cardCollided(self,card):
        if(card):
            print("card ", card.id, " collided. Next id = ", self._nextId)
            if(card.id == self._nextId):
                card.locked = True
                self._nextId += 1
                #-------------ENQUEUE--------------
                #push card to the stack
                self.pilha.push(card)
                #test if the stack size is equal to self._maxStack
                if self.pilha.size() == self.maxStack:
                    #if this test succeeds, make self._gameMode = GameMode.Win
                    self._gameMode = GameMode.Win
                
            else:
                card.needsCheck = False

        
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in self.all_sprites:
                sprite.handleMouseClick(pygame.mouse.get_pos())
        
                
    def on_loop(self):
        if(self._gameMode == GameMode.Playing):
            self.elapsed_time = (pygame.time.get_ticks()-self.start_ticks)/1000
            self._currentTime = int(self._gameTime - self.elapsed_time)
            current = str(self._currentTime)
            self.hud_text = self.font.render('Time: ' + current, True, (0,255,0), (0,0,128)) 
            if(self._currentTime <= 0):
                self._gameMode = GameMode.Lose
        
        for sprite in self.all_sprites:
            sprite.update(pygame.mouse.get_pos())
            
    def on_render(self):
        # draw the black background onto the surface
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self.bgroundImage, (0,0))
        
        for sprite in self.all_sprites:
            self._display_surf.blit(sprite.surf,sprite.rect)
        
        self._display_surf.blit(self.hud_text,self.hud_text.get_rect())
        
        if(self._gameMode == GameMode.Win):
            self._display_surf.blit(self.win_text,self.textRect)
        
        elif(self._gameMode == GameMode.Lose):
            self._display_surf.blit(self.lose_text,self.textRect)
        
        pygame.display.update()
            
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.observe('cardCollided', theApp.cardCollided)
    theApp.on_execute()