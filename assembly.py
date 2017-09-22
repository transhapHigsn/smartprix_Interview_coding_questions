from sys import exit as quit
def set(a,b):
    var[a] = int(b)

def echo(a):
    print var[a]

def add(a,b,c):
    if a.isdigit() and not b.isdigit():
        var[c] = int(a) + var[b]
    elif b.isdigit() and not a.isdigit():
        var[c] = var[a] + int(b)
    else:
        var[c] = var[a] + var[b]

def goto(a):
    return var[a]

def label(a, idx):
    var[a] = idx

def check(a, b):
    #simple if implementation
    if var[a] == int(b):
        return True
    else:
        return False

def execute(cmds, i):
    global var
    global labelStack

    first = cmds[i].split()
    cmd = first[0]

    if cmd=='SET':
        set(first[1], first[2])

    elif cmd=='ECHO':
        echo(first[1])

    elif cmd=='ADD':
        add(first[1],first[2],first[3])

    elif cmd=='GOTO':
        it = 1
        while it<len(labelStack[first[1]]):
            idx = execute(labelStack[first[1]], it)
            if idx:
                it = idx
            it += 1

    elif cmd=='LABEL':
        idx = cmds.index(' '.join(first))
        st = 'GOTO ' + first[1]

        try:
            j = cmds[i:].index(st)
        except:
            j = len(cmds) - 1

        labelStack[first[1]] = cmds[i:i+j+1]
        label(first[1], idx)

    elif cmd=='IF':
        #nested if not impplemented
        reply = check(first[1], first[2])
        if not reply:
            idx = cmds[i:].index('END')
            idx = idx + len(cmds[:i])
            return idx

    elif cmd=='EXIT':
        print labelStack
        print var
        quit()

    elif cmd == 'CONTINUE':
        #not implemented yet
        pass

    else:
        print var

#global variables
var = {}
cmd = []
labelStack = {}

#getting input
while True:
    try:
        cmd.append(raw_input())
        if cmd[-1] == '':
            del cmd[-1]
            break
    except:
        break

#starting assembly language code execution
i = 0
while i<len(cmd):
    #print cmd
    idx = execute(cmd, i)
    c = 0
    if idx:
        i = idx
    i += 1

print labelStack
print var
