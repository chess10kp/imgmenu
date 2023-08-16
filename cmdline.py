import argparse

parser = argparse.ArgumentParser(description="A dynamic menu for images")

parser.add_argument('-c','--compress', action='store_true', help='compress images')
parser.add_argument('-d', '--directory',help='path containing files')


args = parser.parse_args()
