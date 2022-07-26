import blob
import numpy
import cv2
import operator
import sys


class BeadFinder:
    def __init__(self, tau,min_pixels):
        self.bead_list = []
        self.tau = float(tau)
        self.min_pixels = int(min_pixels)

    def isin(self, point, b):

        if tuple(map(operator.sub, point, (0, 1))) in b._Blob__px or tuple(map(operator.add, point, (0, 1))) in b._Blob__px:
            return True
        elif tuple(map(operator.sub, point, (1, 0))) in b._Blob__px or tuple(map(operator.add, point, (1, 0))) in b._Blob__px:
            return True
        elif tuple(map(operator.sub, point, (1, 1))) in b._Blob__px or tuple(map(operator.add, point, (1, 1))) in b._Blob__px:
            return True
        elif tuple(map(operator.add, point, (-1, 1))) in b._Blob__px or tuple(map(operator.add, point, (1, -1))) in b._Blob__px:
            return True
        return False

    def beadfinder(self, picture):
        try:
            img = cv2.imread(picture, 0)
            img = numpy.where(img > self.tau, 255, 0)
            beads = []
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    if img[i][j] == 255:
                        beads.append((i, j))
            while len(beads):
                b = blob.Blob()
                b.add(beads[0][0], beads[0][1])
                beads.pop(0)
                for i in beads:
                    if self.isin(i, b):
                        b.add(i[0], i[1])

                for k in b._Blob__px[1:]:
                    beads.remove(k)
                if b.mass()>=self.min_pixels:
                    self.bead_list.append(b)
        except:
            print('Please Check your pictures input')

    def getBeads(self):
        ret_beads = [ob for ob in self.bead_list if ob.mass() >= self.min_pixels]
        return ret_beads


def main(min_pixels, tau, picture):
    obj = BeadFinder(tau,min_pixels)
    obj.beadfinder(picture)
    for i in obj.getBeads():
        print(i)

if __name__ =='__main__':
    main(sys.argv[1],sys.argv[2],sys.argv[3])
