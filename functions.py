'''
Author: <Ali Kaif>
Date: <February 15th>
Class: ISTA 130
Section Leader: <Sebastian>

Description:
<Program contains 8 separate functions for HW 2>
'''

import math

def print_word(number, word):
    for i in range(1, number + 1):
        print(str(i) + " --> " + word)

def bacteria(minutes, generation):
    for i in range(1, generation + 1):
        print("after " + str(minutes * i) + " minutes" + ":  " + str(2 ** i) + " bacteria")
        

def convert_to_copper(num_gold, num_silver, num_copper):
    copper_conversion = num_copper + (5 * num_silver) + (50 * num_gold)
    print( str(num_gold) + " gp, " + str(num_silver) + " sp," + " " + str(num_copper) + " cp converted to copper is: " + str(copper_conversion) + " cp")

def convert_from_copper(copper_amount):
    whole_gold = copper_amount // 50
    remaining_gold = copper_amount % 50

    whole_silver = remaining_gold // 5
    remaining_silver = remaining_gold % 5

    whole_copper = remaining_silver 

    print(str(copper_amount) + " copper pieces is: " + str(whole_gold) + " gp, " + str(whole_silver) + " sp, " + str(whole_copper) + " cp")
    
def repeat_word(word, num_row, num_col):
    for i in range(num_row):
        print(word * num_col)

def text_triangle(number):
    for i in range(1, number + 1):
        print("x" * i)
        


def surface_area_of_cylinder(radius, height):
    sa_cylinder = 2 * math.pi * radius ** 2 + 2 * math.pi * radius * height

    print("The surface area of a cylinder with radius " + str(radius) + " and height " + str(height) + " is " + str(sa_cylinder))

def tree_height(distance, kite_string_length):
    tree_height_calc = math.sqrt((kite_string_length ** 2 - distance ** 2))
    print("Kite string: " + str(kite_string_length))
    print("Distance: " + str(distance))
    print("Height: "  + str(tree_height_calc))
    




#==========================================================

    
def main():
    '''
    Prints out a word a certain number of times based on the first
    input which is an integer, and the output is the whatever the second
    input is.
    '''
    print_word(3,"banana")
    
    '''
    Prints out the amount of bacteria present after a certain number
    of minutes have passed
    '''
    
    bacteria(10, 5)

    '''<This program takes three values, the integer amount of gold, silver and copper
    and then converts all of the amount to how much it's all worth in copper>
    '''
    convert_to_copper(5, 10, 7)

    '''
    This will take in one input, the amount of copper,
    and convert it into the amount of gold and silver it is worth
    with any copper pieces left over after the conversion
    '''
    convert_from_copper(200)

    '''<This program will print out a word a certain
    number of times on a certain number of rows>
    '''
    repeat_word("Boop", 3, 3)

    '''<This program will print out a number of triangles per
    row, forming a little stair like image>
    '''

    text_triangle(3)

    

    '''Calculates the Surface area of a cylinder
    when given the height and radius'''
    surface_area_of_cylinder(10.0, 10.0)

    tree_height(300, 500)
     
main()
