import string


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


word_set = set()

with open('words.txt', 'r') as f:
    for line in f:
        line = line.strip()
        word_set.add(line.lower())

letters = list(string.ascii_lowercase)


def get_neighbors(word):
    neighbors = []
    word_letters = list(word)
    for i in range(len(word_letters)):
        for letter in letters:
            t = list(word_letters)
            t[i] = letter
            w = "".join(t)
            if w != word and w in word_set:
                neighbors.append(w)
    return neighbors


def find_word_ladders(begin_word, end_word):
    visited = set()
    q = Queue()
    q.enqueue([begin_word])
    while q.size() > 0:
        path = q.dequeue()
        cur_word = path[-1]
        if cur_word not in visited:
            visited.add(cur_word)
            if cur_word == end_word:
                return path

            for neighbor in get_neighbors(cur_word):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)
    return None


print(find_word_ladders('hit', 'cog'))
print(get_neighbors('food'))
