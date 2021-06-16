import sys

def main(lines):
    for i ,v in enumerate(lines):
        print('lines{0}: {1}'.format(i,v))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
        if 'exit'== l.rstrip('\r\n'):
            break
    main(lines)
