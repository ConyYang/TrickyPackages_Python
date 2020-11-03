import argparse
import math

parser = argparse.ArgumentParser(description='Calculate a column of a Cylinder')
parser.add_argument('-R', '--radius', metavar='', type=int, required=True, help='Radius of Cylinder')
parser.add_argument('-H', '--height', type=int, metavar='', required=True, help='Height of Cylinder')
# mutually exclusive argument
group = parser.add_argument('-q', '--quiet', action='store_true', help='print quiet')
group = parser.add_argument('-v', '--verbose', action='store_true', help='print verbose')
args = parser.parse_args()


def cylinder_volume(radius, height):
    vol = (math.pi) * (radius**2) * height
    return vol


if __name__ == '__main__':
    volume = cylinder_volume(args.radius, args.height)
    if args.quiet:
        print(volume)
    elif args.verbose:
        print("Volume is {} with radius {} and height{}".format(volume, args.radius, args.height))
    else:
        print("Volume of cylinder {}".format(volume))
