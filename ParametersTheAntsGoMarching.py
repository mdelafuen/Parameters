fourth_lines = ["The little one stops to suck his thumb,",
                "The little one stops to tie his shoe,",
                "The little one stops to climb a tree,",
                "The little one stops to shut the door,",
                "The little one stops to take a dive,",
                "The little one stops to pick up sticks,",
                "The little one stops to pray to heaven,",
                "The little one stops to check the gate,",
                "The little one stops to check the time,",
                "The little one stops to say, 'THE END!'"]

def sing_verse(verse_num):
    print(f"The ants go marching {verse_num} by {verse_num}, hurrah, hurrah")
    print(f"The ants go marching {verse_num} by {verse_num}, hurrah, hurrah")
    print(f"The ants go marching {verse_num} by {verse_num},")
    print(fourth_lines[verse_num-1])
    print("And they all go marching down to the ground")
    print("To get out of the rain, BOOM! BOOM! BOOM!")

def main():
    for verse_num in range(1,11,1):
        sing_verse(verse_num)


main()