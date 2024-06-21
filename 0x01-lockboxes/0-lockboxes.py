#!/usr/bin/python3

def canUnlockAll(boxes):
    unlocked = set()
    for i in range(len(boxes)):
        if i in unlocked:
            continue
        key = i
        while key < len(boxes) and key not in unlocked:
            unlocked.add(key)
            key = boxes[key][0]
    if len(unlocked) == len(boxes):
        return True
    return False
