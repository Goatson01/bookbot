def word_count(text):
    return f"Found {len(text.split())} total words"

def character_count(text):
    text = text.lower()
    text = list(text)
    counts = dict()
    for i in text:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] = counts[i] + 1
    return counts

def sort_on(items):
    return items["num"]

def sort_count(counts):
    lister = []
    for x, y in counts.items():
        new_dict = {"char": x, "num": y}
        lister.append(new_dict)
    lister.sort(reverse=True, key=sort_on)
    return lister
