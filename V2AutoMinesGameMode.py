#Verson2
import pyautogui as py, random, time, keyboard
from pyautogui import *
from random import SystemRandom
"""
    This program is for "Mines Game Mode" on online casinos auto mine...
    Please change bet_cashout_button & x_values & y_values if need...
    I great way to mine casino tokens...
"""
seconds = 0.8 #Time bewteen each acticon
bet_cashout_button = (1143, 747) #location of the bet button
s_random = SystemRandom()
"""
    [---------------------------------------]
    [ Mine_0, Mine_1 ,Mine_2, Mine_3, Mine_4]
    [ Mine_5, Mine_6 ,Mine_7, Mine_8, Mine_9]
    [Mine_10,Mine_11,Mine_12,Mine_13,Mine_14]
    [Mine_15,Mine_16,Mine_17,Mine_18,Mine_19]
    [Mine_20,Mine_21,Mine_22,Mine_23,Mine_24]
    [---------------------------------------]
"""
#Lists...
x_values = [670, 747, 822, 898, 971] #List of x vaulse...
y_values = [279, 346, 416, 487, 559] #List of y vaulse...
"""
    [-------------------------------------------------]
    [(670,279),(747,279),(822,279),(898,279),(971,279)]
    [(670,346),(747,346),(822,346),(898,346),(971,279)]
    [(670,416),(747,416),(822,416),(898,416),(971,279)]
    [(670,487),(747,487),(822,487),(898,487),(971,279)]
    [(670,559),(747,559),(822,559),(898,559),(971,279)]
    [-------------------------------------------------]
"""
random_list_ints_0_4_hard_coded = [0,1,2,3,4,1,2,3,4,0,2,3,4,0,1,3,4,0,1,2,4,0,1,2,3]
random_list_ints_0_4_hard_coded_even  = [x for x in random_list_ints_0_4_hard_coded if x % 2 == 0]
random_list_ints_0_4_hard_coded_old  = [x for x in random_list_ints_0_4_hard_coded if x % 2 != 0]
#Setup
sleep(seconds)
py.click()
sleep(seconds)
#Normal Random method...
def method_0():
    py.moveTo(bet_cashout_button)
    sleep(seconds)
    py.click()
    sleep(seconds)
    random_number = random.randint(0, 4)
    random_x_value = random.randint(0, random_number)
    random_y_value = random.randint(0, random_number)
    for n in str(len(x_values)):
        sleep(seconds)
        py.moveTo(x_values[random_x_value], y_values[random_y_value])
        sleep(seconds)
        py.click()
        sleep(seconds)
        py.moveTo(bet_cashout_button)
        sleep(seconds)
        py.click()
        sleep(seconds)
    main()
#System Random method...
def method_1():
    py.moveTo(bet_cashout_button)
    sleep(seconds)
    py.click()
    sleep(seconds)
    random_number = s_random.randrange(5)
    random_x_value = random.randint(0,random_number)
    random_y_value = random.randint(0,random_number)
    for n in str(len(x_values)):
        sleep(seconds)
        py.moveTo(x_values[random_x_value], y_values[random_y_value])
        sleep(seconds)
        py.click()
        sleep(seconds)
        py.moveTo(bet_cashout_button)
        sleep(seconds)
        py.click()
        sleep(seconds)
    main()
#List system random method...
def method_2():
    py.moveTo(bet_cashout_button)
    sleep(seconds)
    py.click()
    sleep(seconds)
    random_number = s_random.randrange(25)
    num = random_list_ints_0_4_hard_coded[random_number]
    random_x_value = random.randint(0, num)
    random_y_value = random.randint(0, num)
    for n in str(len(x_values)):
        sleep(seconds)
        py.moveTo(x_values[random_x_value], y_values[random_y_value])
        sleep(seconds)
        py.click()
        sleep(seconds)
        py.moveTo(bet_cashout_button)
        sleep(seconds)
        py.click()
        sleep(seconds)
    main()
#List of evens system random method...
def method_3():
    py.moveTo(bet_cashout_button)
    sleep(seconds)
    py.click()
    sleep(seconds)
    random_number = s_random.randrange(15)
    num = random_list_ints_0_4_hard_coded_even[random_number]
    random_x_value = random.randint(0, num)
    random_y_value = random.randint(0, num)
    for n in str(len(x_values)):
        sleep(seconds)
        py.moveTo(x_values[random_x_value], y_values[random_y_value])
        sleep(seconds)
        py.click()
        sleep(seconds)
        py.moveTo(bet_cashout_button)
        sleep(seconds)
        py.click()
        sleep(seconds)
    main()
#List of olds system random method...
def method_4():
    py.moveTo(bet_cashout_button)
    sleep(seconds)
    py.click()
    sleep(seconds)
    random_number = s_random.randrange(10)
    num = random_list_ints_0_4_hard_coded_old[random_number]
    random_x_value = random.randint(0, num)
    random_y_value = random.randint(0, num)
    for n in str(len(x_values)):
        sleep(seconds)
        py.moveTo(x_values[random_x_value], y_values[random_y_value])
        sleep(seconds)
        py.click()
        sleep(seconds)
        py.moveTo(bet_cashout_button)
        sleep(seconds)
        py.click()
        sleep(seconds)
    main()
#Random choose method...
def main():
    while keyboard.is_pressed('q') == False:
        random_number = s_random.randrange(25)
        num = random_list_ints_0_4_hard_coded[random_number]
        sleep(seconds)
        if num == 0:
            method_0()
        if num == 1:
            method_1()
        if num == 2:
            method_2()
        if num == 3:
            method_3()
        if num == 4:
            method_4()
#Test if its the main programs...
if __name__ == '__main__':
    main()
