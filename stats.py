def get_num_words(text: str):
    words = text.split()
    return len(words)


def count_letters(text: str):
    stats: dict[str, int] = {}
    for letter in text:
        letter = letter.lower()
        if letter in stats:
            stats[letter] = stats[letter] + 1
        else:
            stats[letter] = 1
    return stats


def sort_on(dict):
    return dict["num"]


def sort_list(stats: dict[str, int]):
    unsorted = []
    for letter in stats:
        pair = {"char": letter, "num": stats[letter]}
        unsorted.append(pair)
    unsorted.sort(reverse=True, key=sort_on)

    return unsorted
