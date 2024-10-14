from random import Random



def options(option):
    opt = open(r'options_NEW.txt', mode='r', encoding='utf-8').read()
    return opt[int(opt.find(f'{option}: ') + len(f'{option}: ')):int(opt.find('\n', opt.find(f'{option}: ')))]


words = int(options('syllables'))

structure = options('structure').replace(" ", "").split(',')

groups = {}

groupsfile = open(r'groups_NEW.txt', mode='r', encoding='utf-8')
grp = groupsfile.readlines()
for g in grp:
    g = g.replace(" ", "").replace("\n", "")
    groups[g[:g.find(':')]] = []
    for l in g[g.find(':')+1:].split(','):
        groups[g[:g.find(':')]].append(l)
groupsfile.close()

rules = []

rulesfile = open(r'rules_NEW.txt', mode='r', encoding='utf-8')
rls = rulesfile.readlines()
for r in rls:
    r = r.replace(' ', '').replace('\n', '')
    rules.append(r)
rulesfile.close()

random = Random()

for i in range(words):
    output = ''
    forbbiden = [] # forbidden letters
    next = '' # next letter has to be this

    for s in structure: # s: group allowed in this spot
        if next != '':
            output += next
        
        allowed = [l for l in groups[s.replace('*', '')] if l not in forbbiden] # remove forbidden from allowed
        tmp = allowed if s[0] == '*' else allowed.append('') # first letter is '*'
        output += random.choice(tmp if tmp is not None or len(allowed) <= 0 else ['']) # add '' to choices if optional

        forbbiden = []
        next = ''

        # -- rules -- #
        for r in rules:
            y = r.find('~')
            n = r.find('!')
            if n != -1: # a cannot come after b
                if len(output) > 0 and output[-1] in groups[r[:n]]: # if last choice is part of 'a' group
                    forbbiden.extend(groups[r[n+1:]]) # make 'b' group forbidden
            elif y != -1: # a must come after b
                if output[-1] in groups[r[:y]]: # if last choice is part of 'a' group
                    next = random.choice(groups[r[y+1:]]) # set next letter as group 'b'

    print(options('display').replace("'", '').replace('{index}', f'{i+1}').replace('{syllable}', f'{output}').replace('\\n', '\n'), end='')
input('Program has ended.')