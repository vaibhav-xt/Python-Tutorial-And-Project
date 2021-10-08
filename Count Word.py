""" Write a function CountHisHer() in Python which reads the contents of a text file "Story.txt" and counts the words
    His and Her (not case sensitive)."""

def CountHisHer(his, her):
    outputhis = 0
    outputher = 0
    with open("story.txt") as f:
        readline = f.readline()
        i = 0
        j = 0
        for his in readline:
            if his in readline:
                i += 1

            for her in readline:
                if her in readline:
                    j += 1

            outputher = j + outputher
            outputhis = i + outputhis
    print(outputhis)
    print(outputher)

CountHisHer("his", "her")
