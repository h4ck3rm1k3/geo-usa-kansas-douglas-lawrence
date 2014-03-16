"""
group text into blocks 
create lines for each block
look for other text along that line that is close to the block
find for each bit of text what the closest other block of text
"""
import quadpy
from quadpy.rectangle import Rectangle
from data import load

quad = quadpy.Node(0, 0, 10700, 10700, max_depth=9)
stack = []
data = {}

## gui
import Tkinter as tkinter
root = tkinter.Tk()

#scrollbar = Scrollbar(root)
#scrollbar.pack(side=RIGHT, fill=Y)

frame = tkinter.Frame(root, bd=2, relief=tkinter.SUNKEN)

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.pack()

xscrollbar = tkinter.Scrollbar(frame, orient=tkinter.HORIZONTAL)
xscrollbar.grid(row=1, column=0, sticky=tkinter.E+tkinter.W)

yscrollbar = tkinter.Scrollbar(frame)
yscrollbar.grid(row=0, column=1, sticky=tkinter.N + tkinter.S)

#canvas = tkinter.Canvas()
canvas = tkinter.Canvas(frame, 
                        bd=0,
                        width=500, 
                        height=500, 
                        scrollregion=(0,0,5000,5000),
                        highlightthickness=0,
                        background='white',
                        xscrollcommand=xscrollbar.set,
                        yscrollcommand=yscrollbar.set)

canvas.pack( fill='y', side='left', expand=True, padx=6, pady=6)
canvas.grid(row=0, column=0, sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W)
xscrollbar.config(command=canvas.xview)
yscrollbar.config(command=canvas.yview)




#fill='both',
#frame = tkinter.Frame()
#frame.pack(side='left', fill='y', expand=True, pady=6)

class MyRect (Rectangle):
    def __repr__(self):
        return "{0} '{1}' ({2}, {3}, {4}, {5})".format(self.__class__.__name__,
                                                      self.data,
                                                      *self.bounds
                                                  )


def add_rect(minx, miny, maxx, maxy, string):
    bounds = (minx, miny, maxx, maxy)
    rect = MyRect(*bounds)

    rect.canvas_id = canvas.create_rectangle(bounds, outline='blue')

    rect.data = string
#    dlist = quad.get_overlapped_children(bounds)

    quad.insert(rect)

    # if dlist :
    #     print dlist
    #     print rect




def String(s):
    #print "Stack", stack;
    #print s[0][0],s[0][1],
    string = "".join([x[2] for x in s])
    minx = None
    miny = None
    maxx = None
    maxy = None
    for x in s:
        if not minx:
            minx = x[0]
        if not miny:
            miny = x[1]
        if not maxx:
            maxx = x[0]
        if not maxy:
            maxy = x[1]       
        if  minx > x[0]:
            minx = x[0]
        if  miny > x[1]:
            miny = x[1]
        if maxx < x[0]:
            maxx = x[0]
        if maxy < x[1]:
            maxy = x[1]
    # now we have a bbox
    if minx == maxx:
        maxx = maxx + 1

    if miny == maxy:
        maxy = maxy + 1

#    minx = int(minx) 
#    miny = int(miny)
#    maxx = int(maxx)
#    maxy = int(maxy)

    add_rect(minx, miny, maxx, maxy,string)


def vector(a, b):
    #print a,b
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    d = dx * dy
    return abs(d)


def Text(x, y, c):

    if len(c) > 1 :
        print c
        raise Exception("%s is too long" % c)
    global stack
    item = [float(x), float(y), c]
    if (len(stack) > 0):
        v = vector(item, stack[-1])
        #print item, stack, v
        #        if (v < 1):
        #            stack.append(item)
        #        else:
        #            String(stack)
        #            stack = []
        String([item])
    else:
        stack.append(item)  # first item

load()

#print(quad)
#for x in quad.get_children():
#    print x.__dict__
#    print x
                                        


root.mainloop()
