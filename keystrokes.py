#newline implementation '#'
def enter(row):
    if row == len(ans) - 1:
        ans.append('')
        return [-1,0]
    else:
        ans.insert(row+1,'')
        return [row + 1, 0]


#up arrow implementation '^'
def up(row, col, lflag):
    print 'Up method running', row, col
    #print row, col, lflag
    if row > 0:
        if not lflag:
            col -= 1
            lflag = True
        col = min(len(ans[row - 1]), col)
        row -= 1
    print row, col
    return (row, col, lflag)

#down arrow implementation '?'
def down(row, col, rflag):
    print 'Down method running', row, col
    if row < len(ans)- 1:
        if not rflag:
            col -= 1
            rflag = True
        col = min(len(ans[row + 1]), col)
        row += 1
    print row, col
    return (row, col, rflag)

#cursor left shift implementation
def left(col):
    print "Left method running"
    if col>0:
        col -= 1
    return col

#cursor right shift implementation
def right(row, col):
    print "right method running"
    if col < len(ans[row]) - 1:
        col += 1
    return col

#caps lock  implementation '@'
def caps(st):
    s = ''
    cap = False
    for i in range(len(st)):
        if st[i] == '@':
            cap = not cap
            continue
        if cap:
            s += st[i].upper()
        else:
            s += st[i]
    return s

#character insertion implementation
def insert(ch,row, col = 0):
    ans[row] = ans[row][:col + 1] + ch + ans[row][col + 1:]
    col += 1
    print ans, row, col
    return col

#character deletion implementation '/'
def delete(row, col):
    print 'del running', row, col
    if col > 0:
        ans[row] = ans[row][:-1]
        col -= 1
    elif col == 0:
        if row > 0:
            del ans[row]
            row -= 1
            col = len(ans[row]) - 1
    print ans, row, col
    return (row, col)

def execute(st):
    global ans

    lst = list(caps(st))
    #print lst
    row = 0
    col = 0
    lflag = False
    rflag = False
    for i in range(len(lst)):
        if lst[i]=='#':
            row = ans.index(ans[row])
            row, col = enter(row)
        elif lst[i]=='^':
            row = ans.index(ans[row])
            (row,col,lflag) = up(row,col, lflag )
            if i+1<len(lst) and lst[i+1] != '^':
                lflag = False
            #print row,col,lflag
        elif lst[i]=='?':
            row = ans.index(ans[row])
            (row, col, rflag) = down(row, len(ans[row]) - 1, rflag)
            if i+1<len(lst) and lst[i+1]!= '?':
                rflag = False
            #print row, col,rflag
        elif lst[i]=='<':
            col = left(min(col,len(ans[row]) - 1))
            if lst[i+1] != '<':
                lflag = False
        elif lst[i]=='>':
            row = ans.index(ans[row])
            col = right(row,min(col,len(ans[row]) - 1))
        elif lst[i]=='/':
            row = ans.index(ans[row])
            (row, col) = delete(row, col)
            if i + 1 < len(lst) and lst[i+1] == '^':
                col += 1
        else:
            col = insert(lst[i], row, col)
    return ans

ans = ['']
def sol(st):
    #ans = ['']
    #st = raw_input()
    return execute(st)
