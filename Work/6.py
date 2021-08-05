def love6(first, second):
    if ((first == 6) or (second == 6)) and (first+second == 6) and abs(first-second) == 6:
        return True
    else:
        return False


print(love6(6,0))