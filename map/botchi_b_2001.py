count = int(input())

word = ""
for _ in range(0, count):
    if len(word) == 0:
        word += input()
        continue
    input_word = input()
    word_len = len(word)
    input_len = len(input_word)

    if word_len <= input_len:
        word_cursor = 0
    else:
        word_cursor = word_len - input_len

    flag = False
    while word_cursor < word_len:
        flag = True
        for i in range(0, word_len - word_cursor):
            if word[word_cursor + i] != input_word[i]:
                flag = False
                break

        if flag:
            break
        else:
            word_cursor += 1
    if flag:
        word = word[0:word_cursor] + input_word
    else:
        word = word + input_word

print(word)
