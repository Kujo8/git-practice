words=["banana","apple","cherry","date","fig","grape"]

filtered_words = filter(lambda name: name.startswith(('a', 'b')), words)
title_words=map(lambda name: name.title(), filtered_words)

print(list(title_words))