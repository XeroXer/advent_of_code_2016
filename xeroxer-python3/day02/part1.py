#!/usr/bin/env python
"""Advent of Code 2016: Day 02, Part 1"""

def handle_directions(directions):
    """Handle input directions"""
    keypad = {
        0: {0: '1', 1: '2', 2: '3'},
        1: {0: '4', 1: '5', 2: '6'},
        2: {0: '7', 1: '8', 2: '9'},
    }
    xpos = ypos = 0
    passphrase = ''
    for line in directions:
        for direction in line:
            if direction == 'L':
                xposn = xpos - 1
                xpos = xposn if xposn in keypad[ypos] else xpos
            elif direction == 'R':
                xposn = xpos + 1
                xpos = xposn if xposn in keypad[ypos] else xpos
            elif direction == 'U':
                yposn = ypos - 1
                ypos = yposn if yposn in keypad and xpos in keypad[yposn] else ypos
            elif direction == 'D':
                yposn = ypos + 1
                ypos = yposn if yposn in keypad and xpos in keypad[yposn] else ypos
        passphrase += str(keypad[ypos][xpos])
    return passphrase

def main():
    """Main function"""
    with open('input.txt') as file:
        print(handle_directions([l.strip() for l in file.readlines()]))

if __name__ == '__main__':
    main()
