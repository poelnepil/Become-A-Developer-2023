def unique_character(text):
    words = text.split()
    chars = []

    for word in words:
        counter = {}
        for char in word:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1

        uniq_chars = [c for c in word if counter[c] == 1]
        if uniq_chars:
            chars.extend(uniq_chars)

    for char in chars:
        if chars.count(char) == 1:
            return char


text = input()
res = unique_character(text)

if res:
    print(f"перший унікальний символ: {res}")
else:
    print("символ не знайдено.")