#!/usr/bin/env python
"""Advent of Code 2016: Day 02, Part 2"""

def handle_directions(directions):
    """Handle input directions"""
    keypad = {
        -2: {0: '1'},
        -1: {-1: '2', 0: '3', 1: '4'},
        0: {-2: '5', -1: '6', 0: '7', 1: '8', 2: '9'},
        1: {-1: 'A', 0: 'B', 1: 'C'},
        2: {0: 'D'},
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
        passphrase += keypad[ypos][xpos]
    return passphrase

def main():
    """Main function"""
    with open('input.txt') as file:
        print(handle_directions([l.strip() for l in file.readlines()]))

if __name__ == '__main__':
    main()
