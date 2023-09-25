"""
These are the main functions for Helgas Herbs.

Author: Katie Sheppard
Date:   May 18 2023
"""


import pygame
import os
from queue import LifoQueue




# Initialize Pygame
pygame.init()

pygame.mixer.init()

#create game window
screen_width = 900
screen_height = 750
window = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


"""

THE FOLLOWING ARE ALL THE DISPLAY FUNCTIONS.

↓

"""

PROJECT_ROOT_PATH_KATIE_PC = r"C:\01_MY FILES\04_GAMES\01_Helga's Herbs"
PROJECT_ROOT_PATH_WEB = ""

PROJECT_ROOT_PATH = PROJECT_ROOT_PATH_WEB
IS_WEB = True

ASSETS_PATH = r"\01_HELGAS_HERBS\02_Assets"
IMAGES_PATH = ASSETS_PATH + r"\02_images"
SPRITES_PATH = ASSETS_PATH + r"\01_sprites"
ANIMATIONS_PATH = ASSETS_PATH + r"\01_animations"
SOUNDS_PATH = ASSETS_PATH + r"\04_sounds"


def load_image(projectRootPath, path, filename, isWeb=IS_WEB):
  if isWeb:
    webPath = path.replace('\\', '/')
    if webPath.startswith('/'):
      webPath = webPath[1:len(webPath)]
    webPath += '/' + filename
    return pygame.image.load_extended(webPath)
  else:
    os.chdir(projectRootPath + path)
    return pygame.image.load_extended(filename)


def load_sound(projectRootPath, path, filename, isWeb=IS_WEB):
  if isWeb:
    webPath = path.replace('\\', '/')
    if webPath.startswith('/'):
      webPath = webPath[1:len(webPath)]
    webPath += '/' + filename
    return pygame.mixer.Sound(webPath)
  else:
    os.chdir(projectRootPath + path)
    return pygame.mixer.Sound(filename)


forestbkg = load_image(PROJECT_ROOT_PATH, IMAGES_PATH, 'Forest900x750.png')
title = load_image(PROJECT_ROOT_PATH, IMAGES_PATH, 'HelgaHerbs900x750.png')
start_button = load_image(PROJECT_ROOT_PATH, IMAGES_PATH, 'Start900x750.png')
glow_start_button = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\05_start", 'glow_start2.png') 
controls_button = load_image(PROJECT_ROOT_PATH, IMAGES_PATH,'controls900x750.png')
glow_controls_button = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\05_start", 'glow_controls900x750.png')

def display_start_screen():
    """
    Display the start screen with a "Start" button.
    """
    # os.chdir(PROJECT_ROOT_PATH + r"\02_Assets\02_images")
    hover_start = handle_hover_start()
    hover_controls = handle_hover_controls()

    window.blit(forestbkg, (0, 0))
    window.blit(title, (0, 0))
    window.blit(start_button, (0, 0))
    if hover_start:
        window.blit(glow_start_button,(0, 0))
    window.blit(controls_button, (282, 565))
    if hover_controls:
        window.blit(glow_controls_button, (0, 0)) 


quitscreen = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\02_mains",'quit2.png')
quitscreen_yes = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\02_mains", 'quit2_yes.png')
quitscreen_no = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\02_mains", 'quit2_no.png')


def display_quit_screen():
    """
    Displays the quit game screen when escaped is pressed in Helga's cart.
    """
    #os.chdir(PROJECT_ROOT_PATH + r"\02_Assets\02_images\02_mains")
    hover_yes = handle_hover_yes()
    hover_no = handle_hover_no()

    window.blit(quitscreen,(0,0))
    if hover_yes:
        window.blit(quitscreen_yes,(0,0))
    if hover_no:
        window.blit(quitscreen_no,(0,0))


pink_tint = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'Pink-Tint.png')
cat = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'cat.png')
#cand_glow = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'cand.png')
fire_glow = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'Fire-glow.png')
rack_glow = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'Rack-glow.png')
back_lights = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'Back-lights.png')
walls = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'walls.png')
table_glow = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'Table-glow.png')
lamp = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'Lamp.png')
chairs = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'Chair-4.png')
snake_plant = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'snake-plat.png')
plant2 = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'Plant-2.png')
hang_lights = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'Hang-lights.png')
dust_bag = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'bag-of-dust.png')
herb_rack = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'Herb-rack.png')
coat_stand = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'coat-stand.png')
co_top = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'Co-top-Decor.png')
#this is where home girl needs to go 


def display_front_inside_cart():
  """
    Inside the cart screen
    """
  #os.chdir(PROJECT_ROOT_PATH + r"\02_Assets\02_images\01_cart")

  #home girl
  window.blit(co_top, (0, 0))
  window.blit(coat_stand, (0, 0))
  window.blit(herb_rack, (0, 0))
  #window.blit (cand_glow,(0,0))
  window.blit(fire_glow, (0, 0))
  window.blit(rack_glow, (0, 0))
  window.blit(back_lights, (0, 0))
  window.blit(table_glow, (0, 0))
  window.blit(lamp, (0, 0))
  window.blit(chairs, (0, 0))
  window.blit(cat, (0, 0))
  window.blit(snake_plant, (0, 0))
  window.blit(plant2, (0, 0))
  window.blit(hang_lights, (0, 0))
  window.blit(dust_bag, (0, 0))
  window.blit(walls, (0, 0))
  window.blit(pink_tint, (0, 0))


#this is where home girl needs to go
paintings = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'Painting-.png')
fridge = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'Fridge.png')
back_rugs = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'Back-rugs.png')
cat_tower = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'cat-tower.png')
Ltop = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'Ltop.png')
candles = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'Candles.png')
pantry = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'Pantry.png')
front_rugs = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'Front-Rugs.png')
trim = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'trim.png')
outside_door = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'Outside-door.png')
backsplash = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'backsplash.png')
floor = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'floor.png')
bkg =  load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\01_cart", 'BKG.png')


def display_back_inside_cart():
  """
    Inside the cart screen
    """
  #os.chdir(PROJECT_ROOT_PATH + r"\02_Assets\02_images\01_cart")

  window.blit(bkg, (0, 0))
  window.blit(floor, (0, 0))
  window.blit(backsplash, (0, 0))
  window.blit(outside_door, (0, 0))
  window.blit(front_rugs, (0, 0))
  window.blit(trim, (0, 0))
  window.blit(candles, (0, 0))
  window.blit(pantry, (0, 0))
  window.blit(back_rugs, (0, 0))
  window.blit(cat_tower, (0, 0))
  window.blit(Ltop, (0, 0))
  window.blit(fridge, (0, 0))
  window.blit(paintings, (0, 0))
  #home girl


potionscreen = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\02_mains", 'pot mix2.png')


def display_potion_screen():
  """
    Display the potion mixing screen.
    """
  #os.chdir(PROJECT_ROOT_PATH + r"\02_Assets\02_images\02_mains")

  window.blit(potionscreen, (0, 0))


plant_encyclopedia = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\02_mains", 'plant_encyclopedia.png')


def display_plant_encyclopedia():
  """
    Displays the plant encyclopedia.
    """
  window.blit(plant_encyclopedia, (81, 165))


exclamation = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\04_other", 'exclamation.png')
exclamation_off = False


def display_new_order_emoji():
  """
    Display the ! emoji above box.
    """
  #os.chdir(PROJECT_ROOT_PATH + r"\02_Assets\02_images\04_other")

  if convo_done and not exclamation_off:
    window.blit(exclamation, (573, 325))


ordercheck = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\02_mains", 'orders2.png')
first_order = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\02_mains", 'orders2_first_order.png')
convo_done = False

def display_order_check():
  """
    Display orders list.
    """
  #os.chdir(PROJECT_ROOT_PATH + r"\02_Assets\02_images\02_mains")
  global convo_done

  if convo_done != True:
    window.blit(ordercheck, (0, 0))
  else:
    window.blit(first_order, (0, 0))


inventory = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\02_mains", 'inventory4.png')


def display_inventory():
  """
    Displays inventory screen.
    """
  #os.chdir(PROJECT_ROOT_PATH + r"\02_Assets\02_images\02_mains")

  x = 623
  y = 527

  window.blit(inventory, (x, y))


ginkgo_icon = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\03_plants", 'ginkgo.png')
ginseng_icon = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\03_plants", 'ginseng_root.png')
echinacea_icon = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\03_plants", 'echinacea.png')
glow_icon = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\03_plants", 'glow_berry.png')

Ossirepair_icon = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\03_plants\potion_bottles", 'echinacea_ginkgo.png')
Heartmend_icon = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\03_plants\potion_bottles", 'ginseng_root_ginkgo.png')
Blissful_glow_icon = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\03_plants\potion_bottles", 'glow_berry_ginkgo.png')
Rashbane_icon = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\03_plants\potion_bottles", 'ginseng_root_echinacea.png')
Soul_Resurgence_icon = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\03_plants\potion_bottles", 'ginseng_root_glow_berry.png')
Harmony_Flow_icon = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\03_plants\potion_bottles", 'glow_berry_echinacea.png')


potion = True


def display_pot_inventory():
    """
    Displays pot screen inventory.
    """
    #os.chdir(PROJECT_ROOT_PATH + r"\02_Assets\02_images\03_plants")

    global potion

    if not pot_one:
        window.blit(ginkgo_icon,(193,625)) #pot screen

    if not pot_two:
        window.blit(ginseng_icon,(340,625)) #pot screen

    if not pot_three:
        window.blit(echinacea_icon,(495,630)) #pot screen

    if not pot_four:
        window.blit(glow_icon,(635,625)) #pot screen

    potion_result = display_potions() 
    # print(potion_result[0])
    # print('potion_result is: ' + str(potion_result))
    # pot_select_result = handle_reset_pot_inventory()
    # print (pot_select_result) 
    # print (potion)

    if potion:
        if potion_result[0] == 'hm' and main_one != True:
            window.blit(Heartmend_icon,(208,623))
        elif potion_result[0] == 'or' and main_one != True:
            window.blit(Ossirepair_icon,(208,623)) 
        elif potion_result[0] == 'bg' and main_one != True:
            window.blit(Blissful_glow_icon,(208,623)) 
        elif potion_result[0] == 'rb' and main_two != True:
            window.blit(Rashbane_icon,(355,623)) 
        elif potion_result[0] == 'sr' and main_two != True:
            window.blit(Soul_Resurgence_icon,(355,623))  
        elif potion_result[0] == 'hf' and main_three != True:
            window.blit(Harmony_Flow_icon,(502,623))   
 
        if potion_result[1] == 'hm' and main_one != True:
            window.blit(Heartmend_icon, (208, 623))
        elif potion_result[1] == 'or' and main_one != True:
            window.blit(Ossirepair_icon, (208, 623)) 
        elif potion_result[1] == 'bg' and main_one != True:
            window.blit(Blissful_glow_icon, (208, 623)) 
        elif potion_result[1] == 'rb' and main_two != True:
            window.blit(Rashbane_icon, (355, 623))  
        elif potion_result[1] == 'sr' and main_two != True:
            window.blit(Soul_Resurgence_icon, (355, 623))  
        elif potion_result[1] == 'hf' and main_three != True:
            window.blit(Harmony_Flow_icon, (502, 623)) 


ginkgo_icon2 = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\03_plants", 'ginkgo2.png')
ginseng_icon2 = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\03_plants", 'ginseng_root2.png')
echinacea_icon2 = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\03_plants", 'echinacea2.png')
glow_icon2 = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\03_plants", 'glow_berry2.png')

Ossirepair_icon2 = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\03_plants\potion_bottles", 'echinacea_ginkgo_small.png')
Heartmend_icon2 = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\03_plants\potion_bottles", 'ginseng_root_ginkgo_small.png')
Blissful_glow_icon2 = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\03_plants\potion_bottles", 'glow_berry_ginkgo_small.png')
Rashbane_icon2 = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\03_plants\potion_bottles", 'ginseng_root_echinacea_small.png')
Soul_Resurgence_icon2 = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\03_plants\potion_bottles", 'ginseng_root_glow_berry_small.png')
Harmony_Flow_icon2 = load_image(PROJECT_ROOT_PATH, IMAGES_PATH + r"\03_plants\potion_bottles", 'glow_berry_echinacea_small.png')
   

potions_display2 = 0


def display_main_inventory():
    """
    Displays plants in main cart inventory.
    """    
    #os.chdir(PROJECT_ROOT_PATH + r"\02_Assets\02_images\03_plants")
    global potion
    global potions_display2


    if not pot_one:
        window.blit(ginkgo_icon2,(645,540))       
    if not pot_two:
        window.blit(ginseng_icon2,(748,540)) 
    if not pot_three:
        window.blit(echinacea_icon2,(648,630)) 
    if not pot_four:
        window.blit(glow_icon2,(748,625))

    potion_result = display_potions()
    
 
    if potion:
        if potion_result[0] == 'hm' and main_one != True:
            window.blit(Heartmend_icon2,(653,537)) 
        elif potion_result[0] == 'or' and main_one != True:
            window.blit(Ossirepair_icon2,(653,537)) 
        elif potion_result[0] == 'bg' and main_one != True:
            window.blit(Blissful_glow_icon2,(653,536))
        elif potion_result[0] == 'rb' and main_two != True:
            window.blit(Rashbane_icon2,(757,537)) 
        elif potion_result[0] == 'sr' and main_two != True:
            window.blit(Soul_Resurgence_icon2,(757,537))  
        elif potion_result[0] == 'hf' and main_three != True:
            window.blit(Harmony_Flow_icon2,(653,622))  

        if potion_result[1] == 'hm' and main_one != True:
            window.blit(Heartmend_icon2,(653,537))
        elif potion_result[1] == 'or' and main_one != True:
            window.blit(Ossirepair_icon2,(653,537)) 
        elif potion_result[1] == 'bg' and main_one != True:
            window.blit(Blissful_glow_icon2,(653,536)) 
        elif potion_result[1] == 'rb' and main_two != True:
            window.blit(Rashbane_icon2,(757,537))  
        elif potion_result[1] == 'sr' and main_two != True:
            window.blit(Soul_Resurgence_icon2,(757,537)) 
        elif potion_result[1] == 'hf' and main_three != True:
            window.blit(Harmony_Flow_icon2,(653,622))


most_recent_potion_delivered = ''


def display_main_delivery():
    """
    Returns the name of the potion delivered.
    """    
    #os.chdir(PROJECT_ROOT_PATH + r"\02_Assets\02_images\03_plants")
    global potion
    global most_recent_potion_delivered
    global potion_delivered 

    potion_result = display_potions()
    box_clicked = handle_main_selection() 
    potion_delivered = None
    
    # print('display_main_delivery')

    if potion:
        # print('display_main_delivery if potion')
        if potion_result[0] == 'hm' or potion_result[1] == 'hm':
            if box_clicked == '1':
                potion_delivered = 'hm_delivery'
                # print("I'm delivering hm")
        if potion_result[0] == 'or' or potion_result[1] == 'or':
            if box_clicked == '1':
                potion_delivered = 'or_delivery' 
                # print("I'm delivering or")
        if potion_result[0] == 'bg' or potion_result[1] == 'bg':
            if box_clicked == '1':
                potion_delivered = 'bg_delivery'
                # print("I'm delivering bg")
        if potion_result[0] == 'rb' or potion_result[1] == 'rb': 
            if box_clicked == '2':
                potion_delivered = 'rb_delivery'
                # print("I'm delivering rb")
        if potion_result[0] == 'sr' or potion_result[1] == 'sr': 
            if box_clicked == '2':
                potion_delivered = 'sr_delivery'
                # print("I'm delivering sr")
        if potion_result[0] == 'hf' or potion_result[1] == 'hf': 
            if box_clicked == '3':
                potion_delivered = 'hf_delivery' 
                # print("I'm delivering hf")
    
    if potion_delivered is not None:
        most_recent_potion_delivered = potion_delivered
 
    return most_recent_potion_delivered


def display_all_cart():
    """
    Displays everything in the cart.
    """
    global convo_done

    display_back_inside_cart()
    helga.move()
    helga.draw()
    display_front_inside_cart()
    display_new_order_emoji()
    # npc.draw()
    convo.draw(0, 0, 0)
    if convo.can_play != True:
        convo_done = True


"""

THE FOLLOWING ARE ANIMATION FUNCTIONS. 

↓

"""


class Animation:
  def __init__(self, *args):
      if (isinstance(args[0], str)):
          length = len(args)
          a3 = 1 if length < 3 else args[2]
          a4 = 24 if length < 4 else args[3]
          self.init_folder(args[0], args[1], a3, a4)
      else:
          self.init_flipped(args[0], args[1])

  def init_folder(self, folder, fps, f1=1, f2=24):
    self.folder = folder
    self.reset()
    self.frame_images = []
    self.millis_between_frames = 1000 / fps  # Number of milliseconds to wait before changing to the next frame
    self.load_animation_frames(folder, f1, f2)
    self.has_ever_played = False

  def init_flipped(self, source_frame_images, fps):
      self.reset()
      self.frame_images = []
      self.millis_between_frames = 1000 / fps  # Number of milliseconds to wait before changing to the next frame
      self.init_animation_frames_flipped(source_frame_images)
      self.has_ever_played = False

  def reset(self):
    self.frame = 0
    self.last_frame_change_time = 0
    self.can_play = True  # Flag to indicate if the animation has played
    #print('------resetting animation: ' + self.folder)

  def load_animation_frames(self, animation_folder, frame_start, frame_end):
    suffixPath = "" if IS_WEB else r"\01_HELGAS_HERBS"
    prefixPath = r"01_HELGAS_HERBS" if IS_WEB else ""
    # Load the frames of the animation
    for i in range(frame_start, frame_end):  # Load frames based of f1 and f2
      frame = load_image(PROJECT_ROOT_PATH + suffixPath,
                         prefixPath + animation_folder,
                         "animation_000" + str(i) + ".png")
      self.frame_images.append(frame)

  def init_animation_frames_flipped(self, source_frame_images):
      for i in range(len(source_frame_images)):
          surface = source_frame_images[i].copy()
          self.frame_images.append(pygame.transform.flip(surface, True, False))
          
  # Call this every game frame
  def draw(self, x=0, y=0, repeat=1):
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - self.last_frame_change_time

    if repeat == 1:
      if elapsed_time >= self.millis_between_frames:
        self.last_frame_change_time = current_time
        self.frame = (self.frame + 1) % len(self.frame_images)
    else:
      if self.can_play and elapsed_time >= self.millis_between_frames:
        self.last_frame_change_time = current_time
        self.frame = (self.frame + 1) % len(self.frame_images)

        if self.frame == 0:
          self.can_play = False  # Set the flag to indicate that the animation has played


    if self.can_play:
      self.has_ever_played = True
      frame = self.frame_images[self.frame]
      #print('drawing frame: ' + str(self.frame) + ' of animation: ' + self.folder)
      window.blit(frame, (x, y))
    #elif self.has_ever_played:
    #print('-----------NOT drawing frame: ' + str(self.frame) + ' of animation: ' + self.folder + ' ')

  def can_play(self):
      return self.can_play
  
  def get_frame_images(self):
      return self.frame_images



ginkgo_frames = Animation(r"\02_Assets\03_animations\02_plants\ginkgo\Comp 1", 20)
ginseng_frames = Animation(r"\02_Assets\03_animations\02_plants\ginseng root\Comp 1", 20)
glow_frames = Animation(r"\02_Assets\03_animations\02_plants\glow berry\Comp 1", 20)
echinacea_frames = Animation(r"\02_Assets\03_animations\02_plants\echinacea\Comp 1", 20)   


class Helga:

  def __init__(self):
    self.x = 250
    self.y = 300
    self.target_x = self.x
    self.target_y = self.y
    self.idle_anim = Animation(r"\02_Assets\01_sprites\01_helga\idle",30,1,11,)
    self.idle_anim_flipped = Animation(self.idle_anim.get_frame_images(),30)
    self.state = "idle"
    self.animation = self.idle_anim
    self.move_speed = 5
    self.is_facing_left = True  # Variable to track the direction Helga is facing

  def set_state(self, new_state):
    self.state = new_state
    if self.state == "idle":
      self.animation = self.idle_anim

  def handle_move(self):  # NOTE this needs to be called form inside a handle() function since it processes event
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      mouse_x, mouse_y = pygame.mouse.get_pos()
      walkspace_rect = pygame.Rect(75, 305, 775,110)  # Create a rectangle representing the walk space behind counter

      if walkspace_rect.collidepoint(mouse_x, mouse_y):
        #correctiing the positions so here feets are at the clicked position
        self.target_x = mouse_x - 78
        self.target_y = mouse_y - 156

        # make the new target have values that are eact multiples of speed so she reaches her target exactly and does not wobble
        start_x_offset = self.x % self.move_speed
        self.target_x = (int(self.target_x / self.move_speed) *
                         self.move_speed) + start_x_offset
        start_y_offset = self.y % self.move_speed
        self.target_y = (int(self.target_y / self.move_speed) *
                         self.move_speed) + start_y_offset

        #print(int(self.target_x / self.move_speed))
        #print("I left clicked and collided in box, my position is: (x: " + str(self.x) + ", y: " + str(self.y) + ")" + "...new target is: (x: " + str(self.target_x) + ", y: " + str(self.target_y) + ")")

  def move(self):
    #print("position is: (x: " + str(self.x) + ", y: " + str(self.y) + ")" + "...target is: (x: " + str(self.target_x) + ", y: " + str(self.target_y) + ")")
    is_moving = self.x != self.target_x or self.y != self.target_y
    if is_moving:
      #print('I am moving')
      # Calculate the step size for each axis
      step_x = self.move_speed if self.target_x > self.x else -self.move_speed
      step_y = self.move_speed if self.target_y > self.y else -self.move_speed
      if self.x != self.target_x:
        self.x += step_x
      if self.y != self.target_y:
        self.y += step_y

      # Update the facing direction
      self.is_facing_left = self.target_x < self.x

  def draw(self):
      if self.is_facing_left:
          self.idle_anim.draw(self.x, self.y)
      else:
          self.idle_anim_flipped.draw(self.x, self.y)


helga = Helga()


# class MrHeart:

#   def __init__(self):
#     self.x = 0
#     self.y = 0
#     self.place_order_anim = Animation(
#       r"\02_Assets\01_sprites\02_npc\02_placing order\comp_1",
#       30,
#       0,
#       249,
#     )
#     self.state = "ordering"
#     self.animation = self.place_order_anim

#   def set_state(self, new_state):
#     self.state = new_state
#     if self.state == "ordering":
#       self.animation = self.place_order_anim

#   def draw(self):
#     self.animation.draw(self.x, self.y, 0)


# npc = MrHeart()

convo = Animation(r"\02_Assets\03_animations\03_order\comp_1", 3, 0, 115)
box_hint = Animation(r"\02_Assets\03_animations\04_box_hint\comp_1", 5, 0, 45)
controls = Animation(r"\02_Assets\03_animations\05_controls\comp_1", 10, 0, 34)

Ossirepair = Animation(r"\02_Assets\03_animations\02_plants\04_or", 1, 0, 5)
Heartmend = Animation(r"\02_Assets\03_animations\02_plants\03_hm", 1, 0, 5)
Blissful_glow = Animation(r"\02_Assets\03_animations\02_plants\01_bg", 1, 0, 5)
Rashbane = Animation(r"\02_Assets\03_animations\02_plants\05_rb", 1, 0, 5)
Soul_Resurgence = Animation(r"\02_Assets\03_animations\02_plants\06_sr", 1, 0, 5)
Harmony_Flow = Animation(r"\02_Assets\03_animations\02_plants\02_hf", 1, 0, 5)


def reset_one_shot_animations():
  Ossirepair.reset()
  Heartmend.reset()
  Blissful_glow.reset()
  Rashbane.reset()
  Soul_Resurgence.reset()
  Harmony_Flow.reset()

  ginkgo_frames.reset()
  ginseng_frames.reset()
  glow_frames.reset()
  echinacea_frames.reset()

  Ossirepair_delivery.reset()
  Heartmend_delivery.reset()
  Blissful_glow_delivery.reset()
  Rashbane_delivery.reset()
  Soul_Resurgence_delivery.reset()
  Harmony_Flow_delivery.reset()


Ossirepair_delivery = Animation(
  r"\02_Assets\03_animations\06_delivery\04_or\comp_1", 10, 0, 25)
Heartmend_delivery = Animation(
  r"\02_Assets\03_animations\06_delivery\03_hm\comp_1", 10, 0, 25)
Blissful_glow_delivery = Animation(
  r"\02_Assets\03_animations\06_delivery\01_bg\comp_1", 10, 0, 83)
Rashbane_delivery = Animation(
  r"\02_Assets\03_animations\06_delivery\05_rb\comp_1", 10, 0, 25)
Soul_Resurgence_delivery = Animation(
  r"\02_Assets\03_animations\06_delivery\06_sr\comp_1", 10, 0, 25)
Harmony_Flow_delivery = Animation(
  r"\02_Assets\03_animations\06_delivery\02_hf\comp_1", 10, 0, 25)

two_selections = []  # Initialize the list
unprocessed_potion_selection_result = ''
most_recent_potion_created = ''
second_last_created = ''



def display_potions():
    """
    Displays potion made based off last two selections.
    """
    #os.chdir(PROJECT_ROOT_PATH + r"\02_Assets\02_images\03_plants")
    global two_selections
    global unprocessed_potion_selection_result
    global most_recent_potion_created
    global second_last_created
    global potion
    
    if unprocessed_potion_selection_result is not None:  # Check if result is not None
        two_selections += unprocessed_potion_selection_result  # Create a list with the single string
        unprocessed_potion_selection_result = None # we have now processed that result, so clear it
        # print('display_potions two_selections is:' + str(two_selections))
        # print('length of two selections: ' + str(len(two_selections)))

    potion_created = None

    if len(two_selections) == 2:
        if two_selections == ['1', '2'] or two_selections == ['2', '1']:
            # print('Heartmend')
            potion_created = 'hm'
        elif two_selections == ['1', '3'] or two_selections == ['3', '1']:
            # print('Ossirepair')
            potion_created = 'or'
        elif two_selections == ['1', '4'] or two_selections == ['4', '1']:
            # print('Blissful')
            potion_created = 'bg'
        elif two_selections == ['2', '3'] or two_selections == ['3', '2']:
            # print('Rashbane')
            potion_created = 'rb'
        elif two_selections == ['2', '4'] or two_selections == ['4', '2']:
            # print('Soul')
            potion_created = 'sr'
        elif two_selections == ['3', '4'] or two_selections == ['4', '3']:
            # print('Harmony')
            potion_created = 'hf'

        second_last_created = most_recent_potion_created
        most_recent_potion_created = potion_created
        two_selections = []  # Clear the list if more than 2 items are added
        unprocessed_potion_selection_result = None
        # print ('most recent is: ' + most_recent_potion_created + '  second to last is: ' + second_last_created)

    if potion == False:
        two_selections = []
        potion_created = None
        most_recent_potion_created = potion_created
        second_last_created = ''

    return most_recent_potion_created, second_last_created



"""

THE FOLLOWING HANDLE FUNCTIONS.

↓

"""


def handle_start_button():
  """
    Handle the left click event on the "start" button to initiate the game.

    Returns True if button is clicked. 
    """

  # Check for mouse events

  if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    button_rect = pygame.Rect(230, 470, 500,90)  # Create a rectangle representing the button

    if button_rect.collidepoint(mouse_x, mouse_y):
      return True  # Return True when the button is clicked

  return False


def handle_hover_start():
    """
    Handle the collide event on the "Start" button to make the button glow.

    Returns True if button is hover overed. 
    """
    button_rect = pygame.Rect(230, 470, 500, 90)  
    mouse_x, mouse_y = pygame.mouse.get_pos()

    if button_rect.collidepoint(mouse_x, mouse_y):
        return True  


def handle_controls_button():
  """
    Handle the left click event on the "controls" button to initiate the game.

    Returns True if button is clicked. 
    """

  # Check for mouse events

  if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    button_rect = pygame.Rect(282, 565, 365,
                              65)  # Create a rectangle representing the button

    if button_rect.collidepoint(mouse_x, mouse_y):
      return True  # Return True when the button is clicked

  return False


def handle_hover_controls():
    """
    Handle the collide event on the "controls" button to make the button glow.

    Returns True if button is hover overed. 
    """
    button_rect = pygame.Rect(282, 565, 365, 65)  
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    if button_rect.collidepoint(mouse_x, mouse_y):
        return True  


def handle_yes_no():
    """
    Checks for left click on yes or no on quit screen.
    """
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        yes_rect = pygame.Rect(112, 390, 180, 100)  # Create a rectangle representing the button
        no_rect = pygame.Rect(603, 385, 144, 100)  # Create a rectangle representing the button


        if yes_rect.collidepoint(mouse_x, mouse_y):
            # print('I pressed yes')
            return "yes"

        elif no_rect.collidepoint(mouse_x, mouse_y):
            # print('I pressed no')
            return "no"
    return None 


def handle_hover_yes():
    """
    Handle the collide event on the "yes" option to make it glow.

    Returns True if button is hover overed. 
    """
    button_rect = pygame.Rect(112, 390, 180, 100) 
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    if button_rect.collidepoint(mouse_x, mouse_y):
        return True  
  

def handle_hover_no():
    """
    Handle the collide event on the "no" option to make it glow.

    Returns True if button is hover overed. 
    """
    button_rect = pygame.Rect(603, 385, 144, 100) 
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    if button_rect.collidepoint(mouse_x, mouse_y):
        return True 
    

def handle_pot_interaction():
  """
    Detect a left click on the pot to transition to the potion mixing screen.

    Returns True if pot is left clicked.
    """
  # Check for mouse events

  if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    pot_rect = pygame.Rect(220, 230, 90,
                           60)  # Create a rectangle representing the pot

    if pot_rect.collidepoint(mouse_x, mouse_y):
      #print("i clicked pot")
      return True  # Return True when the pot is clicked

  return False


pot_one = False
pot_two = False
pot_three = False
pot_four = False

main_one = False
main_two = False
main_three = False
main_four = False


def handle_potion_selection(): 
    """
    Detect if the player click item in pot inventory.
    Players will click something from their inventory which will trigger the corresponding animation. 
    """
    # INVENTORY_X = 165   #top left
    # INVENTORY_Y = 610   #top left
    # INVENTORY_WIDTH = 145 
    # INVENTORY_HEIGHT = 110
    global pot_one 
    global pot_two 
    global pot_three
    global pot_four 
    global potion

    first_box = pygame.Rect(165, 610, 145, 110)
    second_box = pygame.Rect(310, 610, 145, 110)
    third_box = pygame.Rect(455, 610, 145, 110)
    fourth_box =  pygame.Rect(600, 610, 145, 110)

    POT_X = 172   #top left
    POT_Y = 202   #top left
    POT_WIDTH = 555
    POT_HEIGHT = 165


    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        potion = True
        mouse_x, mouse_y = pygame.mouse.get_pos() 
        # Check if the player clicked within the inventory area
        if first_box.collidepoint(mouse_x, mouse_y) and pot_one != True: 
            # print ('I left clicked box one')
            pot_one = True
            return '1'
        elif second_box.collidepoint(mouse_x, mouse_y) and pot_two != True: 
            pot_two = True
            # print ('I left clicked box two')
            return '2'          
        elif third_box.collidepoint(mouse_x, mouse_y) and pot_three != True:
            pot_three = True
            # print ('I left clicked box three')
            return '3'              
        elif fourth_box.collidepoint(mouse_x, mouse_y) and  pot_four != True:
            pot_four = True
            # print ('I left clicked box four')
            return '4'   
    return None       


def handle_main_selection():
  """
    Detect if the player click item in main inventory.
    Players will click something from their inventory which will trigger the corresponding animation. 
    """
  global main_one
  global main_two
  global main_three
  global main_four

  first_box = pygame.Rect(623, 527, 104, 87)
  second_box = pygame.Rect(726, 527, 104, 87)
  third_box = pygame.Rect(623, 614, 104, 87)
  fourth_box = pygame.Rect(726, 614, 104, 87)

  if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # Check if the player clicked within the inventory area
    if first_box.collidepoint(mouse_x, mouse_y) and main_one != True:
      main_one = True
      #print('I left clicked main box one')
      return '1'
    elif second_box.collidepoint(mouse_x, mouse_y) and main_two != True:
      main_two = True
      #print('I left clicked main box two')
      return '2'
    elif third_box.collidepoint(mouse_x, mouse_y) and main_three != True:
      main_three = True
      #print('I left clicked main box three')
      return '3'
    elif fourth_box.collidepoint(mouse_x, mouse_y) and main_four != True:
      main_four = True
      #print('I left clicked main box four')
      return '4'
  return None


def handle_reset_pot_inventory():
    """
    Detect the "R" key press to open the inventory screen.

    Returns True if "R" is pressed. 
    """  
    global pot_one 
    global pot_two 
    global pot_three
    global pot_four

    global main_one 
    global main_two  
    global main_three 
    global main_four  
    global potion

    global hm_played
    global or_played
    global bg_played
    global rb_played
    global sr_played
    global hf_played

    global potion_delivered
    global most_recent_potion_delivered

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r:
            # print ("I pressed r")
            pot_one = False
            pot_two = False
            pot_three = False
            pot_four = False

            main_one = False 
            main_two = False  
            main_three = False 
            main_four = False   
            potion = False

            hm_played = False
            or_played = False
            bg_played = False
            rb_played = False
            sr_played = False
            hf_played = False
            
            most_recent_potion_delivered = None 

            return True 
        
    return False


def handle_delivery():
  """
    Detect a left click on the delivery box.

    Returns True if left click on delivery box.
    """
  # Check for mouse events

  if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    box_rect = pygame.Rect(
      570, 400, 90, 100)  # Create a rectangle representing the delivery box

    if box_rect.collidepoint(mouse_x, mouse_y):
      return True  # Return True when the delivery box is clicked

  return False


def handle_escape():
  """
    Detects escape button.

    Returns True if escpaed is pressed. 
    """
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_ESCAPE:
      #print("I pressed escape.")
      return True
  return False


def handle_inventory():
  """
    Detect the "I" key press to open the inventory screen.

    Returns True if "I" is pressed. 
    """
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_i:
      #print("I pressed I")
      return True
  return False


def handle_order_check():
  """
    Detect the "O" key press to check the orders.

    Returns True if "O" is pressed. 
    """
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_o:
      #print("I pressed O.")
      return True
  return False


def handle_plant_encyclopedia():
  """
    Detect the "E" key press to check the orders.

    Returns True if "E" is pressed. 
    """
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_e:
      #print("I pressed E.")
      return True
  return False


"""
THE FOLLOWING ARE SOUNDS/MUSIC AND THEIR HANDLE FUNCTIONS.

↓

"""


# def handle_cat_click():
#     """
#     Detects click on cat.
#     """
#     if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#         mouse_x, mouse_y = pygame.mouse.get_pos()
#         box_rect = pygame.Rect(40, 650, 117, 70)  # Create a rectangle representing the delivery box

#         if box_rect.collidepoint(mouse_x, mouse_y):
#             return True  # Return True when the delivery box is clicked

#     return False


# meow = load_sound(PROJECT_ROOT_PATH, SOUNDS_PATH + r"\02_sound\10_meow", "meow.mp3")

# def sound_meow():
#     """
#     Sound of a cat's meow.
#     """
#     meow.play()  # Play the sound effect

# start_music = load_sound(PROJECT_ROOT_PATH, SOUNDS_PATH + r"\01_music\01_start screen", "cottagecore_2.mp3")

# def music_start_screen():
#     """
#     Music for start screen.
#     """ 

#     pygame.mixer.music.set_volume(.1)
#     start_music.play(-1,0,0)



"""

THE FOLLOWING IS THE MAIN GAME LOOP.

↓

"""


# Set initial game status
game_status = "start_screen"
game_status_history_stack = LifoQueue()

def change_game_status(new_status):
    global game_status
    global game_status_history_stack

    previous_state = game_status
    #game_status_history_stack.put(game_status)
    game_status = new_status

    if (previous_state != new_status):
        reset_one_shot_animations() # allow all one shot animations to be able to play again now that we changed states

    # print('previous game_status: ' + previous_state + ', new game_status: ' + new_status)

def revert_to_previous_game_status():
    global game_status
    global game_status_history_stack

    game_status = game_status_history_stack.get()    

def handle_all(event):
    global game_status
    global running
    global unprocessed_potion_selection_result

    if game_status == "start_screen":
        # music_start_screen()
        if handle_start_button():
            change_game_status("inside_cart")
        elif handle_controls_button():
            change_game_status("controls")

    elif game_status == "controls":
        if handle_escape():
            change_game_status("start_screen")

    elif game_status == "inside_cart":
        helga.handle_move()
        if handle_delivery():
            change_game_status("delivery")
        if handle_inventory():
            change_game_status("inventory")
        elif handle_order_check(): 
            change_game_status("order_check")
        elif handle_pot_interaction():
            change_game_status("potion_screen")
        elif handle_plant_encyclopedia():
            change_game_status("plant_encyclopedia")
        elif handle_escape():
            change_game_status("quit_screen")

        # elif handle_cat_click():
        #     sound_meow()


    elif game_status == "delivery":
        helga.handle_move()
        if handle_inventory():
            change_game_status("inventory")
        elif handle_order_check(): 
            change_game_status("order_check")
        elif handle_pot_interaction():
            change_game_status("potion_screen")
        elif handle_plant_encyclopedia():
            change_game_status("plant_encyclopedia")
        elif handle_escape():
            change_game_status("quit_screen")

        # elif handle_cat_click():
        #     sound_meow()

    elif game_status == "potion_screen" or game_status ==  "1" or game_status ==  '2' or game_status ==  '3' or game_status ==  '4':
        unprocessed_potion_selection_result = handle_potion_selection()  # Store the result of handle_potion_selection
        if handle_escape():
            change_game_status("inside_cart")
        elif unprocessed_potion_selection_result == '1':
            change_game_status('1')
        elif unprocessed_potion_selection_result == '2':
            change_game_status('2')
        elif unprocessed_potion_selection_result == '3':
            change_game_status('3')
        elif unprocessed_potion_selection_result == '4':
            change_game_status('4')
        
        handle_reset_pot_inventory()

    elif game_status == "inventory":
        helga.handle_move()

        if handle_escape():
            change_game_status("inside_cart")

    elif game_status == "order_completed_screen":
        if handle_escape():
            change_game_status("inside_cart" )

    elif game_status == "order_check":
        if handle_escape():
            change_game_status("inside_cart" )

    elif game_status == "new_order":
        if handle_escape():
            change_game_status("inside_cart" )

    elif game_status == "plant_encyclopedia":
        if handle_escape():
            change_game_status("inside_cart")

    elif game_status == "quit_screen":
        yes_no = handle_yes_no()
        if yes_no == "yes":
            running = False 
        elif yes_no == "no":
            change_game_status("inside_cart")
        elif handle_escape():
            change_game_status("inside_cart")
     
hm_played = False 
or_played = False
bg_played = False
rb_played = False 
sr_played = False
hf_played = False

# Game loop
running = True
while running:

    # the one and only call to this ever:
    window.fill((0, 0, 0))  # Clear the display surface


    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue
        else:
            handle_all(event)
# DISPLAY ------------------------------------
    if game_status == "start_screen":
        display_start_screen() 
    elif game_status == "controls":
        controls.draw(0,0,1)
    elif game_status == "inside_cart":
        display_all_cart()
        delivery1 = display_main_delivery()
        if delivery1 == 'bg_delivery' and bg_played != True:
            Blissful_glow_delivery.draw(0,0,0)
            exclamation_off = True 
        if Blissful_glow_delivery.can_play != True:
            # print("bg can't play")
            bg_played = True
    elif game_status == "potion_screen":
        display_potion_screen()
        display_pot_inventory()
    elif game_status == "inventory":
        display_all_cart()
        delivery = display_main_delivery()
        # print('I delivered: ' + str(delivery))
        if delivery == 'hm_delivery' and hm_played != True:
            exclamation_off = True
            Heartmend_delivery.draw(0, 0, 0)
        if delivery == 'or_delivery' and or_played != True:
            exclamation_off = True
            Ossirepair_delivery.draw(0, 0, 0)
        if delivery == 'bg_delivery' and bg_played != True:
            change_game_status("inside_cart")
        if delivery == 'rb_delivery' and rb_played != True:
            exclamation_off = True
            Rashbane_delivery.draw(0, 0, 0)
        if delivery == 'sr_delivery' and sr_played != True:
            exclamation_off = True
            Soul_Resurgence_delivery.draw(0, 0, 0)
        if delivery == 'hf_delivery' and hf_played != True:
            exclamation_off = True
            Harmony_Flow_delivery.draw(0, 0, 0)

        if Heartmend_delivery.can_play != True:
            # print("hm can't play")
            hm_played = True
        if Ossirepair_delivery.can_play != True:
            # print("or can't play")
            or_played = True
        if Rashbane_delivery.can_play != True:
            # print("rb can't play")
            rb_played = True
        if Soul_Resurgence_delivery.can_play != True:
            # print("sr can't play")
            sr_played = True
        if Harmony_Flow_delivery.can_play != True:
            # print("hf can't play")
            hf_played = True

        display_inventory()
        display_main_inventory()
    elif game_status == "order_check":
        display_order_check()
    elif game_status == "quit_screen":
        display_quit_screen()
    elif game_status == "plant_encyclopedia":
        display_all_cart()
        display_plant_encyclopedia()
    elif game_status == "delivery":
        display_all_cart()
        box_hint.draw(0,0,0)

    if game_status == '1':
        display_potion_screen()
        display_pot_inventory()        
        ginkgo_frames.draw(0,0,0)
    elif game_status == '2': 
        display_potion_screen()
        display_pot_inventory()        
        ginseng_frames.draw(0,0,0)
    elif game_status == '3':
        display_potion_screen()
        display_pot_inventory() 
        echinacea_frames.draw(0,0,0)
    elif game_status == '4':
        display_potion_screen()
        display_pot_inventory()
        glow_frames.draw(0,0,0)
    
    if game_status == "1" or game_status == '2' or game_status == '3' or game_status == '4':
        potion_result = display_potions()
        # print('length of two selections after: ' + str(len(two_selections)))
        if potion_result[0] == 'hm' and len(two_selections) == 0:
            Heartmend.draw(260, 87, 0)
        elif potion_result[0] == 'or' and len(two_selections) == 0:
            Ossirepair.draw(272, 89, 0)
        elif potion_result[0] == 'bg' and len(two_selections) == 0:
            Blissful_glow.draw(224, 87, 0)
        elif potion_result[0] == 'rb' and len(two_selections) == 0:
            Rashbane.draw(285, 87, 0)
        elif potion_result[0] == 'sr' and len(two_selections) == 0:
            Soul_Resurgence.draw(165, 80, 0)
        elif potion_result[0] == 'hf' and len(two_selections) == 0:
            Harmony_Flow.draw(193, 87, 0)




    # print(game_status)
    # the one and only call to this ever:
    pygame.display.flip() # take all blitted images called this time through the main loop and put it onto the screen (from memory)

# Quit Pygame
pygame.quit()



