#!/usr/bin/env python
"""Advent of Code 2016: Day 01, Part 2"""

import re

def handle_sequences(sequences):
    """Handle input sequences"""
    xpos = ypos = direction = 0
    positions = {'0_0'}
    for sequence in sequences:
        if sequence[0] == 'L':
            direction = (direction - 1) if direction > 0 else 3
        elif sequence[0] == 'R':
            direction = (direction + 1) if direction < 3 else 0
        for _ in range(int(sequence[1])):
            xpos = (xpos + 1) if direction == 1 else (xpos - 1) if direction == 3 else xpos
            ypos = (ypos + 1) if direction == 0 else (ypos - 1) if direction == 2 else ypos
            position = '%d_%d' % (xpos, ypos)
            if position in positions:
                break
            positions.add(position)
        else:
            continue
        break
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
