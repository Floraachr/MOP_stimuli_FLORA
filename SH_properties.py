# New code to generate pseudos words and syllables according to MOP

#Define structure and call groups
#Structure is going to be C + V + clusters V legal in Spanish + vowel

def options(structures):
    opt = open(r'structures.txt', mode='r', encoding='utf-8').read()
    return opt[int(opt.find(f'{options}: ') + len(f'{options}: ')):int(opt.find('\n', opt.find(f'{options}: ')))]

words = int(options('syllables')) #number of words
structure = options('structure').replace(" ", "").split(',')

def phonotacticon()