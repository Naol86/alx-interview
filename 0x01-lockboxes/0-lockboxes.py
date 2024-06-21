#!/usr/bin/python3

def canUnlockAll(boxes):
    unlocked = set()
    key = [0]
    while key:
        box = key.pop()
        unlocked.add(box)
        for k in boxes[box]:
            if k not in unlocked:
                key.append(k)
    return len(unlocked) == len(boxes)
