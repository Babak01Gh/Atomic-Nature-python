import beadfinder
import sys
import os
d = open('displacements.txt', 'w')


def main(min_pixels, tau, delta, pics):
    try:
        location = os.path.dirname(os.path.abspath(
            __file__)) + '\\' + pics[:pics.find('*')-1]
        pictures = os.listdir(location)
        while len(pictures)-1:
            a = beadfinder.BeadFinder(tau, min_pixels)
            b = beadfinder.BeadFinder(tau, min_pixels)
            a.beadfinder(
                pics[:pics.find('*')-1] + '/' + pictures[0])
            b.beadfinder(
                pics[:pics.find('*')-1] + '/' + pictures[1])
            for j in a.getBeads():
                for i in b.getBeads():
                    distance = i.DistanceTo(j)
                    if distance < float(delta):
                        d.write(str(distance)+'\n')
                        print(distance)
                        break
            d.write('\n')
            del pictures[0]
    except:
        print('Please Check your input Location')


main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
d.close()
