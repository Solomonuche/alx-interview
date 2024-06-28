#!/usr/bin/python3
"""
Module that provides a function for determining if
all boxes in a given list can be opened
"""


def canUnlockAll(boxes):
    """
    Function to check whether all boxes can be opened by list of keyes

    box (list): The list of lists containing keys reps boxes.

    returns:
        bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    checked_boxes = set([0])
    unchecked_boxes = set(boxes[0]).difference(set([0]))
    while len(unchecked_boxes) > 0:
        boxId = unchecked_boxes.pop()
        if not boxId or boxId >= n or boxId < 0:
            continue
        if boxId not in checked_boxes:
            unchecked_boxes = unchecked_boxes.union(boxes[boxId])

            checked_boxes.add(boxId)

    return n == len(checked_boxes)
