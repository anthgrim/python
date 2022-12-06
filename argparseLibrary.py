import argparse

parser = argparse.ArgumentParser(
  description="This program prints the name of my pets"
)

parser.add_argument("-c", "--color", metavar="color", required=True, choices={"red", "blue", "yellow"}, help="the color to search for")

args = parser.parse_args()

print(args.color)