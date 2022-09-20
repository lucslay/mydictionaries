def encryptMessage(code):
    infile = open('info_security.txt', 'r')
    reader = infile.read()
    outfile = open('encrypted.txt', 'w')

    for x in reader:
        if x in code:
            outfile.write(code[x])
        else:
            outfile.write(x)

    outfile.close()


def main():
    code = {'A':'%', 'a':'9', 'B':'@', 'b':'#', 'C':'1', 'c':'2', 'D':'3', 'd':'4', \
             'E':'5', 'e':'6', 'F':'7', 'f':'8', 'G':'0', 'g':'}', 'H':'{', 'h':']', 'I':'[', 'i':'Y', \
             'J':'Z', 'j':'>', 'K':'<', 'k':'/', 'L':'j', 'l':'_', 'M':'"', 'm':'i', 'N':';', \
             'n':'A', 'O':'h', 'o':'-', 'Q':'$', 'q':'V', 'R':'^', 'r':'&', 'S':'^', \
             's':'(','T':')', 't':'~', 'U':'`', 'u':'g', 'V':'\\', 'v':'+', 'W':'=', 'w':'!', \
             'X':'f', 'x':'e', 'Y':'d', 'y':'c', 'Z':'b', 'z':'a'}

    encryptMessage(code)

main()
