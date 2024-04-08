
def rep_char(c,n):
    print(c*n)
   
def draw_line():
    nstr = len(msg1) if (len(msg1)>len(msg2)) else len(msg2)
    rep_char('-', nstr + 2)

name = input('Input His/Her name : ')
msg1 = 'Hello ' + name
msg2 = 'Welcome to Seoul.'
draw_line()
print(f' {msg1} ')
print(f' {msg2} ')
draw_line()
