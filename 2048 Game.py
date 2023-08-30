class Node:
    def __init__(self):
        self.start = 0
        self.end = 0
        self.len = 0
        self.suffix = None
        self.labeled = []

        self.start = self.end = self.len = -1
        self.suffix = None
        # self.labeled.__setattr__(26, None)

class EerTree:
    def __init__(self):
        self.root1 = None
        self.root2 = None
        self.current = None

        self.root1 = Node()
        self.root1.len = -1
        self.root1.suffix = self.root1

        self.root2 = Node()
        self.root2.len = 0
        self.root2.suffix = self.root1
        self.current = self.root2

    def insert(self, s, pos):
        cur = self.current
        # letter = int(s[pos] - 'a')
        print(s[pos])

        while True:
            if pos - 1 - cur.len >= 0 and s[pos - 1 - cur.len] == s[pos]:
                break
            cur = cur.suffix

        temp = Node()
        temp.len = cur.len + 2
        temp.end = pos
        temp.start = pos - temp.len + 1
#C++ TO PYTHON CONVERTER TODO TASK: The following line was determined to be a copy assignment (rather than a reference assignment) - this should be verified and a 'copy_from' method should be created:
#ORIGINAL LINE: cur->labeled[letter] = temp;
        cur.labeled[letter].copy_expert(temp)

        if temp.len == 1:
            # if cur is root1
            temp.suffix = self.root2
            self.current = temp
            return 0

        # find the suffix node

        while True:
            cur = cur.suffix
            if (pos - 1 - cur.len) >= 0 and s[pos - 1 - cur.len] == s[pos]:
                temp.suffix = cur.labeled[letter]
                break
        self.current = temp

        return 0

    def print(self, s, node):
        if node is not self.root1 or node is not self.root2:
            i = node.start
            while i <= node.end:
                print(s[i], end = '')
                i += 1
            print('\n', end = '')
        for i in range(0, 26):
            if node.labeled[i] is not None:
                self.print(s, list(node.labeled[i]))

    def printAll(self, s):
        self.print(s, self.root1)
        self.print(s, self.root2)


def main():
    s = "aabcba"
    tree = EerTree()
    i = 0
    while i < len(s):
        tree.insert(s, i)
        i += 1
    print("insertion done\n", end = '')
    tree.printAll(s)

if __name__ == "__main__":
    main()