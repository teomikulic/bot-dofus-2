import pyautogui as pg
import do_list as dl
import time
from random import randint


FILES = dl.check_elements()

def collect_ressources():
  print("Recherche des ressources")
  for img_path in FILES:
    try:
      img = pg.locateOnScreen(img_path, confidence=0.90)
      
      if img != None:
        print(f'Ressource trouvée: {img_path[11:-6]}')
        pg.click(img[0]+dl.IMAGE_OFFSET, img[1]+dl.IMAGE_OFFSET)
        time.sleep(randint(4,6))
        result = True
      else:
        result = False
    except:
      return "Erreur"
  return result