#!/usr/bin/env python
"""Advent of Code 2016: Day 01, Part 1"""

import re

def handle_sequences(sequences):
    """Handle input sequences"""
    xpos = ypos = direction = 0
    for sequence in sequences:
        if sequence[0] == 'L':
            direction = (direction - 1) if direction > 0 else 3
        elif sequence[0] == 'R':
            direction = (direction + 1) if direction < 3 else 0
        steps = int(sequence[1])
        xpos = (xpos + steps) if direction == 1 else (xpos - steps) if direction == 3 else xpos
        ypos = (ypos + steps) if direction == 0 else (ypos - steps) if direction == 2 else ypos
    return abs(xpos) + abs(ypos)

def main():
    """Main function"""
    with open('input.txt') as file:
        rmatches = re.findall(
            r"(R|L)(\d+)",
            file.readline().strip()
        )
        print(handle_sequences(rmatches))

if __name__ == '__main__':
    main()
