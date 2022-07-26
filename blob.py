import math


class Blob():
    def __init__(self):
        self.__px = []
        self.__x = 0
        self.__y = 0

    def add(self, x, y):
        self.__px.append((x, y))
        self.__x += x
        self.__y += y

    def mass(self):
        return len(self.__px)

    def DistanceTo(self, o):
        distance = math.sqrt(((self.__x/len(self.__px))-(o.__x/len(o.__px)))
                             ** 2+(((self.__y/len(self.__px))-(o.__y/len(o.__px))))**2)
        return float('{:.4f}'.format(distance))

    def __str__(self):
        return '{} ({:.4f} , {:.4f})'.format(self.mass(), (self.__y/len(self.__px)), (self.__x/len(self.__px)))


def main():
    a, b = Blob(), Blob()
    a.add(2, 3)
    b.add(4, 3)
    print(a.mass())
    print(a.DistanceTo(b))
    print(a)


if __name__ == '__main__':
    main()