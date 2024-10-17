#Python Programs Chapter 8 Project 1
#Write a GUI-based program that implements the tax calculator program shown in figure 8-2.


import sys
versionNumber = sys.version_info.major
if versionNumber == 3:
    import tkinter
    import tkinter.simpledialog
    Tkinter = tkinter
    tkSimpleDialog = tkinter.simpledialog
else:
    import Tkinter
    import tkSimpleDialog

N = Tkinter.N
S = Tkinter.S
E = Tkinter.E
W = Tkinter.W
CENTER = Tkinter.CENTER
END = Tkinter.END
NORMAL = Tkinter.NORMAL
DISABLED = Tkinter.DISABLED
NONE = Tkinter.NONE
WORD = Tkinter.WORD
VERTICAL = Tkinter.VERTICAL
HORIZONTAL = Tkinter.HORIZONTAL
RAISED = Tkinter.RAISED
SINGLE = Tkinter.SINGLE
ACTIVE = Tkinter.ACTIVE

class EasyFrame(Tkinter.Frame):

    def __init__(self, title = "", width = None, height = None,
                 background = "white", resizable = False):

        Tkinter.Frame.__init__(self, borderwidth = 4, relief = "sunken")
        if width and height:
            self.setSize(width, height)
        self.master.title(title)
        self.grid()

        self.master.rowconfigure(0, weight = 1)
        self.master.columnconfigure(0, weight = 1)
        self.grid(sticky = N+S+E+W)

        self.setBackground(background)
        self.setResizable(resizable)

    def setBackground(self, color):

        self["background"] = color

    def setResizable(self, state):

        self.master.resizable(state, state)

    def setSize(self, width, height):

        self.master.geometry(str(width)+ "x" + str(height))

    def setTitle(self, title):

        self.master.title(title)



    def addLabel(self, text, row, column,
                 columnspan = 1, rowspan = 1,
                 sticky = N+W, font = None,
                 background = "white", foreground = "black"):

        label = Tkinter.Label(self, text = text, font = font,
                              background = background,
                              foreground = foreground)
        self.rowconfigure(row, weight = 1)
        self.columnconfigure(column, weight = 1)
        label.grid(row = row, column = column,
                   columnspan = columnspan, rowspan = rowspan,
                   padx = 5, pady = 5, sticky = sticky)
        return label

    def addButton(self, text, row, column,
                  columnspan = 1, rowspan = 1,
                  command = lambda: None,
                  state = NORMAL):

        button = Tkinter.Button(self, text = text,
                                command = command, state = state)
        self.rowconfigure(row, weight = 1)
        self.columnconfigure(column, weight = 1)
        button.grid(row = row, column = column,
                    columnspan = columnspan, rowspan = rowspan,
                    padx = 5, pady = 5)
        return button

    def addFloatField(self, value, row, column,
                      columnspan = 1, rowspan = 1,
                      width = 20, precision = None,
                      sticky = N+E, state = NORMAL):

        field = FloatField(self, value, width, precision, state)
        self.rowconfigure(row, weight = 1)
        self.columnconfigure(column, weight = 1)
        field.grid(row = row, column = column,
                   columnspan = columnspan, rowspan = rowspan,
                   padx = 5, pady = 5, sticky = sticky)
        return field

    def addIntegerField(self, value, row, column,
                        columnspan = 1, rowspan = 1,
                        width = 10, sticky = N+E, state = NORMAL):

        field = IntegerField(self, value, width, state)
        self.rowconfigure(row, weight = 1)
        self.columnconfigure(column, weight = 1)
        field.grid(row = row, column = column,
                   columnspan = columnspan, rowspan = rowspan,
                   padx = 5, pady = 5, sticky = sticky)
        return field

    def addTextField(self, text, row, column,
                     columnspan = 1, rowspan = 1,
                     width = 20, sticky = N+E, state = NORMAL):
        """Creates and inserts a text field at the row and column,
        and returns the text field."""
        field = TextField(self, text, width, state)
        self.rowconfigure(row, weight = 1)
        self.columnconfigure(column, weight = 1)
        field.grid(row = row, column = column,
                   columnspan = columnspan, rowspan = rowspan,
                   padx = 5, pady = 5, sticky = sticky)
        return field

    def addTextArea(self, text, row, column, rowspan = 1, columnspan = 1,
                    width = 80, height = 5, wrap = NONE):

        frame = Tkinter.Frame(self)
        frame.grid(row = row, column = column,
                   columnspan = columnspan, rowspan = rowspan,
                   sticky = N+S+E+W)
        self.columnconfigure(column, weight = 1)
        self.rowconfigure(row, weight = 1)
        xScroll = Tkinter.Scrollbar(frame, orient = HORIZONTAL)
        xScroll.grid(row = 1, column = 0, sticky = E+W)
        yScroll = Tkinter.Scrollbar(frame, orient = VERTICAL)
        yScroll.grid(row = 0, column = 1, sticky = N+S)
        area = TextArea(frame, text, width, height,
                        xScroll.set, yScroll.set, wrap)
        area.grid(row = 0, column = 0,
                  padx = 5, pady = 5, sticky = N+S+E+W)
        frame.columnconfigure(0, weight = 1)
        frame.rowconfigure(0, weight = 1)
        xScroll["command"] = area.xview
        yScroll["command"] = area.yview
        return area

    def addListbox(self, row, column, rowspan = 1, columnspan = 1,
                   width = 10, height = 5, listItemSelected = lambda index: index):

        frame = Tkinter.Frame(self)
        frame.grid(row = row, column = column, columnspan = columnspan, rowspan = rowspan,
                   sticky = N+S+E+W)
        self.columnconfigure(column, weight = 1)
        self.rowconfigure(row, weight = 1)
        yScroll = Tkinter.Scrollbar(frame, orient = VERTICAL)
        yScroll.grid(row = 0, column = 1, sticky = N+S)
        listBox = EasyListbox(frame, width, height, yScroll.set, listItemSelected)
        listBox.grid(row = 0, column = 0, sticky = N+S+E+W)
        frame.columnconfigure(0, weight = 1)
        frame.rowconfigure(0, weight = 1)
        yScroll["command"] = listBox.yview
        return listBox

    def addCanvas(self, canvas = None, row = 0, column = 0,
                  rowspan = 1, columnspan = 1, width = 200, height = 100,
                  background = "white"):

        if not canvas:
            canvas = EasyCanvas(self, width = width, height = height,
                                background = background)
        canvas.grid(row = row, column = column,
                    rowspan = rowspan, columnspan = columnspan,
                    sticky = W+E+N+S)
        self.columnconfigure(column, weight = 10)
        self.rowconfigure(row, weight = 10)
        return canvas

    def addScale(self, row, column, rowspan = 1, columnspan = 1,
                 command = lambda value: value, from_ = 0, to = 0,
                 label = "", length = 100, orient = HORIZONTAL,
                 resolution = 1, tickinterval = 0):

        scale = Tkinter.Scale(self, command = command, from_ = from_, to = to,
                              label = label, length = length,
                              orient = orient, resolution = resolution,
                              tickinterval = tickinterval, relief = "sunken",
                              borderwidth = 4)
        self.rowconfigure(row, weight = 1)
        self.columnconfigure(column, weight = 1)
        scale.grid(row = row, column = column, columnspan = columnspan,
                   rowspan = rowspan, sticky = N+S+E+W)
        return scale

    def addMenuBar(self, row, column, rowspan = 1, columnspan = 1,
                   orient = "horizontal"):

        if not orient in ("horizontal", "vertical"):
            raise ValueError("orient must be horizontal or vertical")
        menuBar = EasyMenuBar(self, orient)
        menuBar.grid(row = row, column = column,
                     rowspan = rowspan, columnspan = columnspan,
                     sticky = N+W)
        return menuBar

    def addCheckbutton(self, text, row, column,
                       rowspan = 1, columnspan = 1,
                       sticky = N+S+E+W, command = lambda : 0):

        cb = EasyCheckbutton(self, text, command)
        self.rowconfigure(row, weight = 1)
        self.columnconfigure(column, weight = 1)
        cb.grid(row = row, column = column,
                columnspan = columnspan, rowspan = rowspan,
                   padx = 5, pady = 5, sticky = sticky)
        return cb

    def addRadiobuttonGroup(self, row, column,
                            rowspan = 1, columnspan = 1, orient = VERTICAL):

        return EasyRadiobuttonGroup(self, row, column, rowspan, columnspan, orient)


    def addPanel(self, row, column,
                 rowspan = 1, columnspan = 1, background = "white"):

        return EasyPanel(self, row, column, rowspan, columnspan, background)



    def messageBox(self, title = "", message = "", width = 25, height = 5):

        dlg = MessageBox(self, title, message, width, height)
        return dlg.modified()


    def prompterBox(self, title = "", promptString = "", inputText = "", fieldWidth = 20):

        dlg = PrompterBox(self, title, promptString, inputText, fieldWidth)
        return dlg.getText()



class AbstractField(Tkinter.Entry):


    def __init__(self, parent, value, width, state):
        self.var = Tkinter.StringVar()
        self.setValue(value)
        Tkinter.Entry.__init__(self, parent,
                               textvariable = self.var,
                               width = width, state = state)

    def setValue(self, value):
        self.var.set(value)

    def getValue(self):
        return self.var.get()


class FloatField(AbstractField):


    def __init__(self, parent, value, width, precision, state):
        self.setPrecision(precision)
        AbstractField.__init__(self, parent, value, width, state)

    def getNumber(self):

        return float(self.getValue())

    def setNumber(self, number):

        self.setValue(self._precision % number)

    def setPrecision(self, precision):

        if precision and precision >= 0:
            self._precision = "%0." + str(precision) + "f"
        else:
            self._precision = "%f"


class IntegerField(AbstractField):


    def __init__(self, parent, value, width, state):
        AbstractField.__init__(self, parent, value, width, state)

    def getNumber(self):

        return int(self.getValue())

    def setNumber(self, number):

        self.setValue(str(number))


class TextField(AbstractField):
    """Represents a single line box for I/O of strings."""

    def __init__(self, parent, value, width, state):
        AbstractField.__init__(self, parent, value, width, state)

    def getText(self):
        """Returns the string contained in the field."""
        return self.getValue()

    def setText(self, text):
        """Replaces the string contained in the field."""
        self.setValue(text)

class TextArea(Tkinter.Text):
    """Represents a box for I/O of multiline text."""

    def __init__(self, parent, text, width, height,
                 xscrollcommand, yscrollcommand, wrap):
        Tkinter.Text.__init__(self, parent,
                              width = width,
                              height = height,
                              wrap = wrap,
                              xscrollcommand = xscrollcommand,
                              yscrollcommand = yscrollcommand)
        self.setText(text)

    def getText(self):
        """Returns the string contained in the text area."""
        return self.get("1.0", END)

    def setText(self, text):
        """Replaces the string contained in the text area."""
        self.delete("1.0", END)
        self.insert("1.0", text)
        
    def appendText(self, text):
        """Inserts the text after the string contained in
        the text area."""
        self.insert(END, text)

class EasyListbox(Tkinter.Listbox):
    """Represents a list box."""

    def __init__(self, parent, width, height, yscrollcommand, listItemSelected):
        self._listItemSelected = listItemSelected
        Tkinter.Listbox.__init__(self, parent,
                                 width = width, height = height,
                                 yscrollcommand = yscrollcommand,
                                 selectmode = SINGLE)
        self.bind("<<ListboxSelect>>", self.triggerListItemSelected)

    def triggerListItemSelected(self, event):
    
        if self.size() == 0: return
        widget = event.widget
        index = widget.curselection()[0]
        self._listItemSelected(index)

    def getSelectedIndex(self):
    
        tup = self.curselection()
        if len(tup) == 0:
            return -1
        else:
            return int(tup[0])

    def getSelectedItem(self):
    
        index = self.getSelectedIndex()
        if index == -1:
            return ""
        else:
            return self.get(index)

    def setSelectedIndex(self, index):
    
        if index < 0 or index >= self.size(): return
        self.selection_set(index, index)

    def clear(self):

        while self.size() > 0:
            self.delete(0)

    def getIndex(self, item):

        tup = self.get(0, self.size() - 1)
        if item in tup:
            return tup.index(item)
        else:
            return -1
        
class EasyRadiobuttonGroup(Tkinter.Frame):

    def __init__(self, parent, row, column, rowspan, columnspan, orient):
        Tkinter.Frame.__init__(self, parent)
        self.grid(row = row, column = column,
                  rowspan = rowspan, columnspan = columnspan,
                  sticky = N+S+E+W)
        self._commonVar = Tkinter.StringVar("")
        self._buttons = dict()
        self._orient = orient
        self._buttonRow = self._buttonColumn = 0

    def addRadiobutton(self, text, command = lambda : 0):
      
        if text in self._buttons:
            raise ValueError("Button with this label already in the group")
        button = Tkinter.Radiobutton(self, text = text, value = text,
                                     command = command,
                                     variable = self._commonVar)
        self._buttons[text] = button
        button.grid(row = self._buttonRow, column = self._buttonColumn, sticky = N+W)
        if self._orient == VERTICAL:
            self.rowconfigure(self._buttonRow, weight = 1)
            self._buttonRow += 1
        else:
            self.columnconfigure(self._buttonColumn, weight = 1)
            self._buttonColumn += 1
        return button

    def getSelectedButton(self):
        if not self._commonVar.get() in self._buttons:
            raise ValueError("No button has been selected yet.")
        return self._buttons[self._commonVar.get()]

    def setSelectedButton(self, button):
        self._commonVar.set(button["value"])
    

class EasyCheckbutton(Tkinter.Checkbutton):


    def __init__(self, parent, text, command):
        self._variable = Tkinter.IntVar()
        Tkinter.Checkbutton.__init__(self, parent, text = text,
                                     variable = self._variable,
                                     command = command)

    def isChecked(self):

        return self._variable.get() != 0

class EasyMenuBar(Tkinter.Frame):


    def __init__(self, parent, orient):
        self._orient = orient
        self._row = self._column = 0
        Tkinter.Frame.__init__(self, parent, relief = RAISED, borderwidth = 1)

    def addMenu(self, text, state = NORMAL):

        menu = EasyMenubutton(self, text, state = state)
        menu.grid(row = self._row, column = self._column)
        if self._orient == "horizontal":
            self._column += 1
        else:
            self._row += 1
        return menu


class EasyMenubutton(Tkinter.Menubutton):


    def __init__(self, menuBar, text, state):
        Tkinter.Menubutton.__init__(self, menuBar,
                                    text = text, state = state)
        self.menu = Tkinter.Menu(self)
        self["menu"] = self.menu
        self._currentIndex = -1
        
    def addMenuItem(self, text, command, state = NORMAL):

        self.menu.add_command(label = text, command = command, state = state)
        self._currentIndex += 1
        return EasyMenuItem(self, self._currentIndex)


class EasyMenuItem(object):


    def __init__(self, menu, index):
        self._menu = menu
        self._index = index

    def setState(self, state):

        self._menu.menu.entryconfigure(self._index, state = state)
        

class EasyCanvas(Tkinter.Canvas):
  
    def __init__(self, parent, width = None, height = None,
                 background = "white"):
        Tkinter.Canvas.__init__(self, parent,
                                width = width, height = height,
                                background = background)
        self.bind("<Double-Button-1>", self.mouseDoubleClicked)
        self.bind("<ButtonPress-1>", self.mousePressed)
        self.bind("<ButtonRelease-1>", self.mouseReleased)
        self.bind("<B1-Motion>", self.mouseDragged)

 

    def mouseDoubleClicked(self, event):
 
        return

    def mousePressed(self, event):
 
        return
        
    def mouseReleased(self, event):
 
        return

    def mouseDragged(self, event):
 
        return

    def getWidth(self):
 
        return self["width"]

    def getHeight(self):
   
        return self["height"]

    def drawLine(self, x0, y0, x1, y1,
                 fill = "black", width = 1):
        item = self.create_line(x0, y0, x1, y1)
        self.itemconfig(item, fill = fill, width = width)
        return item

    def drawRectangle(self, x0, y0, x1, y1,
                      outline = "black", fill = None):
   
        item = self.create_rectangle(x0, y0, x1, y1)
        self.itemconfig(item, outline = outline, fill = fill)
        return item

    def drawOval(self, x0, y0, x1, y1,
                 outline = "black", fill = None):
   
        item = self.create_oval(x0, y0, x1, y1)
        self.itemconfig(item, outline = outline, fill = fill)
        return item

    def drawText(self, text, x, y, fill = "black"):
   
        item = self.create_text(x, y)
        self.itemconfig(item, text = text, fill = fill)
        return item

    def drawImage(self, image, x, y, anchor = CENTER):

        item = self.create_image(x, y, image = image,
                                 anchor = anchor)
        self.itemconfig(item, image = image, anchor = anchor)
        return item

    def deleteItem(self, item):
 
        self.delete(item)



class MessageBox(tkSimpleDialog.Dialog):


    @classmethod
    def message(cls, title = "", message = "", width = 25, height = 5):
        MessageBox(Tkinter.Frame(), title, message, width, height)

    def __init__(self, parent, title, message, width, height):

        self._message = message
        self._width = width
        self._height = height
        self._modified = False
        tkSimpleDialog.Dialog.__init__(self, parent, title)

    def body(self, master):
        self.resizable(0, 0)
        yScroll = Tkinter.Scrollbar(master, orient = VERTICAL)
        yScroll.grid(row = 0, column = 1, sticky = N+S)
        output = Tkinter.Text(master, width = self._width, height = self._height,
                      padx = 5, pady = 5, wrap = WORD,
                      yscrollcommand = yScroll.set)
        output.grid(row = 0, column = 0, sticky = N+W+S+E)
        output.insert("1.0", self._message)
        output["state"] = DISABLED
        yScroll["command"] = output.yview
        return output

    def buttonbox(self):

        box = Tkinter.Frame(self)
        w = Tkinter.Button(box, text="OK", width = 10,
                           command = self.ok, default = ACTIVE)
        w.pack()
        self.bind("<Return>", self.ok)
        box.pack()

    def apply(self):

        self._modified = True

    def modified(self):
        return self._modified

class PrompterBox(tkSimpleDialog.Dialog):


    @classmethod
    def prompt(cls, title = "", promptString = "", inputText = "", fieldWidth = 20):

        dlg = PrompterBox(Tkinter.Frame(), title, promptString, inputText, fieldWidth)
        return dlg.getText()

    def __init__(self, parent, title, promptString, inputText, fieldWidth):

        self._prompt = promptString
        self._text = inputText
        self._width = fieldWidth
        self._modified = False
        tkSimpleDialog.Dialog.__init__(self, parent, title)

    def body(self, master):
        self.resizable(0, 0)
        label = Tkinter.Label(master, text = self._prompt)
        label.grid(row = 0, column = 0, padx = 5, sticky = N+W+S+E)
        self._field = TextField(master, self._text, self._width, NORMAL)
        self._field.grid(row = 1, column = 0, padx = 5, sticky = N+W+S+E)
        return self._field

    def buttonbox(self):

        box = Tkinter.Frame(self)
        w = Tkinter.Button(box, text="OK", width = 10,
                           command = self.ok, default = ACTIVE)
        w.pack()
        self.bind("<Return>", self.ok)
        box.pack()

    def apply(self):

        self._modified = True

    def modified(self):
        return self._modified

    def getText(self):

        return self._field.getText()

class EasyDialog(tkSimpleDialog.Dialog):


    def __init__(self, parent, title = ""):

        self._modified = False
        tkSimpleDialog.Dialog.__init__(self, parent, title)

    def modified(self):

        return self._modified

    def setModified(self):
        self._modified = True

    def addLabel(self, master, text, row, column,
                 columnspan = 1, rowspan = 1,
                 sticky = N+W, font = None):

        label = Tkinter.Label(master, text = text, font = font)
        master.rowconfigure(row, weight = 1)
        master.columnconfigure(column, weight = 1)
        label.grid(row = row, column = column,
                   columnspan = columnspan, rowspan = rowspan,
                   padx = 5, pady = 5, sticky = sticky)
        return label

    def addButton(self, master, text, row, column,
                  columnspan = 1, rowspan = 1,
                  command = lambda: None,
                  state = NORMAL):

        button = Tkinter.Button(master, text = text,
                                command = command, state = state)
        master.rowconfigure(row, weight = 1)
        master.columnconfigure(column, weight = 1)
        button.grid(row = row, column = column,
                    columnspan = columnspan, rowspan = rowspan,
                    padx = 5, pady = 5)
        return button

    def addFloatField(self, master, value, row, column,
                      columnspan = 1, rowspan = 1,
                      width = 20, precision = None,
                      sticky = N+E, state = NORMAL):

        field = FloatField(master, value, width, precision, state)
        master.rowconfigure(row, weight = 1)
        master.columnconfigure(column, weight = 1)
        field.grid(row = row, column = column,
                   columnspan = columnspan, rowspan = rowspan,
                   padx = 5, pady = 5, sticky = sticky)
        return field

    def addIntegerField(self, master, value, row, column,
                        columnspan = 1, rowspan = 1,
                        width = 10, sticky = N+E, state = NORMAL):

        field = IntegerField(master, value, width, state)
        master.rowconfigure(row, weight = 1)
        master.columnconfigure(column, weight = 1)
        field.grid(row = row, column = column,
                   columnspan = columnspan, rowspan = rowspan,
                   padx = 5, pady = 5, sticky = sticky)
        return field

    def addTextField(self, master, text, row, column,
                     columnspan = 1, rowspan = 1,
                     width = 20, sticky = N+E, state = NORMAL):

        field = TextField(master, text, width, state)
        master.rowconfigure(row, weight = 1)
        master.columnconfigure(column, weight = 1)
        field.grid(row = row, column = column,
                   columnspan = columnspan, rowspan = rowspan,
                   padx = 5, pady = 5, sticky = sticky)
        return field

    def addCheckbutton(self, master, text, row, column,
                       rowspan = 1, columnspan = 1,
                       sticky = N+S+E+W, command = lambda : 0):

        cb = EasyCheckbutton(master, text, command)
        master.rowconfigure(row, weight = 1)
        master.columnconfigure(column, weight = 1)
        cb.grid(row = row, column = column,
                columnspan = columnspan, rowspan = rowspan,
                   padx = 5, pady = 5, sticky = sticky)
        return cb

    def addRadiobuttonGroup(self, master, row, column,
                            rowspan = 1, columnspan = 1, orient = VERTICAL):

        return EasyRadiobuttonGroup(master, row, column, rowspan, columnspan, orient)

    def addScale(self, master, row, column, rowspan = 1, columnspan = 1,
                 command = lambda value: value, from_ = 0, to = 0,
                 label = "", length = 100, orient = HORIZONTAL,
                 resolution = 1, tickinterval = 0):

        scale = Tkinter.Scale(master, command = command, from_ = from_, to = to,
                              label = label, length = length,
                              orient = orient, resolution = resolution,
                              tickinterval = tickinterval, relief = "sunken",
                              borderwidth = 4)
        master.rowconfigure(row, weight = 1)
        master.columnconfigure(column, weight = 1)
        scale.grid(row = row, column = column, columnspan = columnspan,
                   rowspan = rowspan, sticky = N+S+E+W)
        return scale

    def addTextArea(self, master, text, row, column, rowspan = 1, columnspan = 1,
                    width = 80, height = 5, wrap = NONE):

        frame = Tkinter.Frame(master)
        frame.grid(row = row, column = column,
                   columnspan = columnspan, rowspan = rowspan,
                   sticky = N+S+E+W)
        master.columnconfigure(column, weight = 1)
        master.rowconfigure(row, weight = 1)
        xScroll = Tkinter.Scrollbar(frame, orient = HORIZONTAL)
        xScroll.grid(row = 1, column = 0, sticky = E+W)
        yScroll = Tkinter.Scrollbar(frame, orient = VERTICAL)
        yScroll.grid(row = 0, column = 1, sticky = N+S)
        area = TextArea(frame, text, width, height,
                        xScroll.set, yScroll.set, wrap)
        area.grid(row = 0, column = 0,
                  padx = 5, pady = 5, sticky = N+S+E+W)
        frame.columnconfigure(0, weight = 1)
        frame.rowconfigure(0, weight = 1)
        xScroll["command"] = area.xview
        yScroll["command"] = area.yview
        return area

    def addListbox(self, master, row, column, rowspan = 1, columnspan = 1,
                   width = 10, height = 5, listItemSelected = lambda index: index):

        frame = Tkinter.Frame(master)
        frame.grid(row = row, column = column, columnspan = columnspan, rowspan = rowspan,
                   sticky = N+S+E+W)
        master.columnconfigure(column, weight = 1)
        master.rowconfigure(row, weight = 1)
        yScroll = Tkinter.Scrollbar(frame, orient = VERTICAL)
        yScroll.grid(row = 0, column = 1, sticky = N+S)
        listBox = EasyListbox(frame, width, height, yScroll.set, listItemSelected)
        listBox.grid(row = 0, column = 0, sticky = N+S+E+W)
        frame.columnconfigure(0, weight = 1)
        frame.rowconfigure(0, weight = 1)
        yScroll["command"] = listBox.yview
        return listBox

    def addCanvas(self, master, canvas = None, row = 0, column = 0,
                  rowspan = 1, columnspan = 1, width = 200, height = 100,
                  background = "white"):

        if not canvas:
            canvas = EasyCanvas(master, width = width, height = height,
                                background = background)
        canvas.grid(row = row, column = column,
                    rowspan = rowspan, columnspan = columnspan,
                    sticky = W+E+N+S)
        master.columnconfigure(column, weight = 10)
        master.rowconfigure(row, weight = 10)
        return canvas

    def addMenuBar(self, master, row, column, rowspan = 1, columnspan = 1,
                   orient = "horizontal"):

        if not orient in ("horizontal", "vertical"):
            raise ValueError("orient must be horizontal or vertical")
        menuBar = EasyMenuBar(master, orient)
        menuBar.grid(row = row, column = column,
                     rowspan = rowspan, columnspan = columnspan,
                     sticky = N+W)
        return menuBar

    def messageBox(self, title = "", message = "", width = 25, height = 5):

        dlg = MessageBox(self, title, message, width, height)
        return dlg.modified()


    def addPanel(self, master, row, column,
                 rowspan = 1, columnspan = 1, background = "white"):

        return EasyPanel(master, row, column, rowspan, columnspan, background)


 
class EasyPanel(Tkinter.Frame):


    def __init__(self, parent, row, column, rowspan, columnspan, background):
        Tkinter.Frame.__init__(self, parent)
        parent.rowconfigure(row, weight = 1)
        parent.columnconfigure(column, weight = 1)
        self.grid(row = row, column = column,
                  rowspan = rowspan, columnspan = columnspan,
                  sticky = N+S+E+W)
        self.setBackground(background)

    def setBackground(self, color):

        self["background"] = color

    def addButton(self, text, row, column,
                  columnspan = 1, rowspan = 1,
                  command = lambda: None,
                  state = NORMAL):

        button = Tkinter.Button(self, text = text,
                                command = command, state = state)
        self.rowconfigure(row, weight = 1)
        self.columnconfigure(column, weight = 1)
        button.grid(row = row, column = column,
                    columnspan = columnspan, rowspan = rowspan,
                    padx = 5, pady = 5)
        return button

    def addLabel(self, text, row, column,
                 columnspan = 1, rowspan = 1,
                 sticky = N+W, font = None,
                 background = "white", foreground = "black"):

        label = Tkinter.Label(self, text = text, font = font,
                              background = background,
                              foreground = foreground)
        self.rowconfigure(row, weight = 1)
        self.columnconfigure(column, weight = 1)
        label.grid(row = row, column = column,
                   columnspan = columnspan, rowspan = rowspan,
                   padx = 5, pady = 5, sticky = sticky)
        return label

    def addFloatField(self, value, row, column,
                      columnspan = 1, rowspan = 1,
                      width = 20, precision = None,
                      sticky = N+E, state = NORMAL):

        field = FloatField(self, value, width, precision, state)
        self.rowconfigure(row, weight = 1)
        self.columnconfigure(column, weight = 1)
        field.grid(row = row, column = column,
                   columnspan = columnspan, rowspan = rowspan,
                   padx = 5, pady = 5, sticky = sticky)
        return field

    def addIntegerField(self, value, row, column,
                        columnspan = 1, rowspan = 1,
                        width = 10, sticky = N+E, state = NORMAL):

        field = IntegerField(self, value, width, state)
        self.rowconfigure(row, weight = 1)
        self.columnconfigure(column, weight = 1)
        field.grid(row = row, column = column,
                   columnspan = columnspan, rowspan = rowspan,
                   padx = 5, pady = 5, sticky = sticky)
        return field

    def addTextField(self, text, row, column,
                     columnspan = 1, rowspan = 1,
                     width = 20, sticky = N+E, state = NORMAL):

        field = TextField(self, text, width, state)
        self.rowconfigure(row, weight = 1)
        self.columnconfigure(column, weight = 1)
        field.grid(row = row, column = column,
                   columnspan = columnspan, rowspan = rowspan,
                   padx = 5, pady = 5, sticky = sticky)
        return field

    def addTextArea(self, text, row, column, rowspan = 1, columnspan = 1,
                    width = 80, height = 5, wrap = NONE):

        frame = Tkinter.Frame(self)
        frame.grid(row = row, column = column,
                   columnspan = columnspan, rowspan = rowspan,
                   sticky = N+S+E+W)
        self.columnconfigure(column, weight = 1)
        self.rowconfigure(row, weight = 1)
        xScroll = Tkinter.Scrollbar(frame, orient = HORIZONTAL)
        xScroll.grid(row = 1, column = 0, sticky = E+W)
        yScroll = Tkinter.Scrollbar(frame, orient = VERTICAL)
        yScroll.grid(row = 0, column = 1, sticky = N+S)
        area = TextArea(frame, text, width, height,
                        xScroll.set, yScroll.set, wrap)
        area.grid(row = 0, column = 0,
                  padx = 5, pady = 5, sticky = N+S+E+W)
        frame.columnconfigure(0, weight = 1)
        frame.rowconfigure(0, weight = 1)
        xScroll["command"] = area.xview
        yScroll["command"] = area.yview
        return area

    def addListbox(self, row, column, rowspan = 1, columnspan = 1,
                   width = 10, height = 5, listItemSelected = lambda index: index):

        frame = Tkinter.Frame(self)
        frame.grid(row = row, column = column, columnspan = columnspan, rowspan = rowspan,
                   sticky = N+S+E+W)
        self.columnconfigure(column, weight = 1)
        self.rowconfigure(row, weight = 1)
        yScroll = Tkinter.Scrollbar(frame, orient = VERTICAL)
        yScroll.grid(row = 0, column = 1, sticky = N+S)
        listBox = EasyListbox(frame, width, height, yScroll.set, listItemSelected)
        listBox.grid(row = 0, column = 0, sticky = N+S+E+W)
        frame.columnconfigure(0, weight = 1)
        frame.rowconfigure(0, weight = 1)
        yScroll["command"] = listBox.yview
        return listBox

    def addCanvas(self, canvas = None, row = 0, column = 0,
                  rowspan = 1, columnspan = 1, width = 200, height = 100,
                  background = "white"):

        if not canvas:
            canvas = EasyCanvas(self, width = width, height = height,
                                background = background)
        canvas.grid(row = row, column = column,
                    rowspan = rowspan, columnspan = columnspan,
                    sticky = W+E+N+S)
        self.columnconfigure(column, weight = 10)
        self.rowconfigure(row, weight = 10)
        return canvas

    def addScale(self, row, column, rowspan = 1, columnspan = 1,
                 command = lambda value: value, from_ = 0, to = 0,
                 label = "", length = 100, orient = HORIZONTAL,
                 resolution = 1, tickinterval = 0):

        scale = Tkinter.Scale(self, command = command, from_ = from_, to = to,
                              label = label, length = length,
                              orient = orient, resolution = resolution,
                              tickinterval = tickinterval, relief = "sunken",
                              borderwidth = 4)
        self.rowconfigure(row, weight = 1)
        self.columnconfigure(column, weight = 1)
        scale.grid(row = row, column = column, columnspan = columnspan,
                   rowspan = rowspan, sticky = N+S+E+W)
        return scale

    def addMenuBar(self, row, column, rowspan = 1, columnspan = 1,
                   orient = "horizontal"):

        if not orient in ("horizontal", "vertical"):
            raise ValueError("orient must be horizontal or vertical")
        menuBar = EasyMenuBar(self, orient)
        menuBar.grid(row = row, column = column,
                     rowspan = rowspan, columnspan = columnspan,
                     sticky = N+W)
        return menuBar

    def addCheckbutton(self, text, row, column,
                       rowspan = 1, columnspan = 1,
                       sticky = N+S+E+W, command = lambda : 0):

        cb = EasyCheckbutton(self, text, command)
        self.rowconfigure(row, weight = 1)
        self.columnconfigure(column, weight = 1)
        cb.grid(row = row, column = column,
                columnspan = columnspan, rowspan = rowspan,
                   padx = 5, pady = 5, sticky = sticky)
        return cb

    def addRadiobuttonGroup(self, row, column,
                            rowspan = 1, columnspan = 1, orient = VERTICAL):

        return EasyRadiobuttonGroup(self, row, column, rowspan, columnspan, orient)
    
    def addPanel(self, row, column,
                 rowspan = 1, columnspan = 1, background = "white"):

        return EasyPanel(self, row, column, rowspan, columnspan, background)

