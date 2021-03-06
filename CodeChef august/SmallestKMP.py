def Int():
    return int(input())


def List():
    return input().split()


def Ilist():
    return list(map(int, input().split()))


def yes():
    print('YES')


def no():
    print('NO')


def main():
    TestCase = Int()
    for _ in range(TestCase):
        S = input()
        Pattern = input()
        CountDict = {}
        for char in S:
            if char in CountDict:
                CountDict[char] += 1
            else:
                CountDict[char] = 1
        for char in Pattern:
            CountDict[char] -= 1
        front = True
        i = 0
        while i < len(Pattern) and Pattern[0] == Pattern[i]:
            i += 1
        if i < len(Pattern) and ord(Pattern[i]) > ord(Pattern[0]):
            front = False

        Forward = []
        Backword = []
        for char, count in CountDict.items():
            if count > 0:
                if ord(char) < ord(Pattern[0]):
                    Forward += [char for _ in range(count)]
                elif ord(char) == ord(Pattern[0]):
                    if not front:
                        Forward += [char for _ in range(count)]
                    else:
                        Backword += [char for _ in range(count)]
                else:
                    Backword += [char for _ in range(count)]
        Forward.sort()
        Backword.sort()
        print(''.join(Forward) + Pattern + ''.join(Backword))


if __name__ == "__main__":
    main()
    exit(0)
