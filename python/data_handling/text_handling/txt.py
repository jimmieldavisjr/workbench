with open(r"text_handling\data\names.txt", 'r') as file:
    content = file.read().split()

sentence = " ".join(content)
print(sentence)
