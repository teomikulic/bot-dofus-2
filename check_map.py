from random import randint
import time
import pyautogui as pg
import do_list as dl
import check_ress as cr

def check_map():
  while cr.collect_ressources() == False:
    cr.collect_ressources()
  cr.collect_ressources()
