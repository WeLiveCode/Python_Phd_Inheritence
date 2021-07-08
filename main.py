from tkinter import *
class Person:
     def __init__(self):
      self.__firstname = ''
      self.__lastname = ''
      self.__idno = ''
      self.__dob = ''

     def setfirstname(self, firstname):
       self.__firstname = firstname

     def getfirstname(self):
         return self.__firstname

     def setlastname(self, lastname):
         self.__lastname = lastname
     def getlastname(self):
         return self.__lastname
     def setidno(self, idno):
         self.__idno = idno
     def getidno(self):
         return self.__idno
     def setdob(self, dob):
         self.__dob = dob
     def getdob(self):
         return self.__dob
     firstname = property(getfirstname, setfirstname)
     lastname = property(getlastname, setlastname)
     idno = property(getidno, setidno)
     dob = property(getdob, setdob)

     def reportLines(self):
         text = "First name : " + self.firstname
         text = text + "\n" + "Surname : " + self.lastname
         text = text + "\n" + "ID Number : " + self.idno
         text = text + "\n" + "Date Of Birth : " + self.dob
         return text


class PhDStudent(Person):
      def __init__(self):
        super().__init__()
        self.__stdnum = ''
        self.__intmark = 0
        self.__extmark = 0
      def setstdnum(self,stdnum):
          self.__stdnum = stdnum
      def getstdnum(self):
          return self.__stdnum
      def setintmark(self, intmark):
          self.__intmark = intmark

      def getintmark(self):
          return self.__intmark

      def setextmark(self, extmark):
        self.__extmark = extmark
      def getextmark(self):
        return self.__extmark
      stdnum = property(getstdnum, setstdnum)
      intmark = property(getintmark, setintmark)
      extmark = property(getextmark, setextmark)
      def average(self):
       return (self.intmark+self.extmark)/2
      def reportLines(self):
       text = "PhD Student Report" + "\n"
       text = text + "\n" + super().reportLines()
       text = text + "\n" + "Student Number: " + self.stdnum
       text = text + "\n" + "Internal Mark: " + str(self.intmark)+"%"
       text = text + "\n" + "External Mark: " + str(self.extmark)+"%"
       text = text + "\n" + "The final mark:  " + str(self.average())+"%"
       return text


class PhDExaminer(Person):
    def __init__(self):
        super().__init__()
        self.__stfnum = ''
        self.__rate = 0
        self.__hours = 0

    def setstfnum(self, stfnum):
        self.__stfnum = stfnum

    def getstfnum(self):
        return self.__stfnum

    def setrate(self, rate):
        self.__rate = rate

    def getrate(self):
        return self.__rate

    def sethours(self, hours):
        self.__hours = hours

    def gethours(self):
        return self.__hours

    stfnum = property(getstfnum, setstfnum)
    rate = property(getrate, setrate)
    hours = property(gethours, sethours)

    def salary(self):
        return self.rate* self.hours

    def reportLines(self):
        text = "PhD Examiner Report"+"\n"
        text = text + "\n" + super().reportLines()
        text = text + "\n" + "Staff Number: " + self.stfnum
        text = text + "\n" + "Hourly Rate: R" + str(self.rate)
        text = text + "\n" + "Number of hours: " + str(self.hours)+" Hrs"
        text = text + "\n" + "The salary: R" + str(self.salary())
        return text
class MyWindow:
 def __init__(self, win):
  self.lblfirst = Label(win, text='First name')
  self.lblsur = Label(win, text='Surname')
  self.lblid = Label(win, text='ID Number')
  self.lbldob = Label(win, text='Date of Birth')
  self.lbl3 = Label(win, text='Report')
  self.txtfirst = Entry(bd=3)
  self.txtsur = Entry()
  self.txtid = Entry()
  self.txtdob = Entry()
  self.t3 = Text(height=10, width=40)
  self.lblfirst.place(x=100, y=50)
  self.lblsur.place(x=100, y=100)
  self.lblid.place(x=100, y=150)
  self.lbldob.place(x=100, y=200)
  self.txtfirst.place(x=200, y=50)
  self.txtsur.place(x=200, y=100)
  self.txtid.place(x=200, y=150)
  self.txtdob.place(x=200, y=200)
  self.v0 = IntVar()
  self.v0.set(1)
  self.r1 = Radiobutton(text="PhDStudent", variable=self.v0, value=1)
  self.r2 = Radiobutton(text="PhDexaminer", variable=self.v0, value=2)
  self.r1.place(x=100, y=245)
  self.r2.place(x=260, y=245)
  self.lblstdnum = Label(win, text='Student Number')
  self.lblintmark = Label(win, text='Internal Mark')
  self.lblextmark= Label(win, text='External Mark')
  self.lblstfnum = Label(win, text='Staff Number')
  self.lblrate = Label(win, text='Hourly Rate')
  self.lblhours = Label(win, text='Number Of Hours')
  self.txtstdnum = Entry()
  self.txtintmark = Entry()
  self.txtextmark = Entry()
  self.txtstfnum = Entry()
  self.txtrate= Entry()
  self.txthours = Entry()
  self.lblstdnum.place(x=100, y=330)
  self.lblintmark.place(x=100, y=360)
  self.lblextmark.place(x=100, y=390)
  self.lblstfnum.place(x=350, y=330)
  self.lblrate.place(x=350, y=360)
  self.lblhours.place(x=350, y=390)
  self.txtstdnum.place(x=200, y=330)
  self.txtintmark.place(x=200, y=360)
  self.txtextmark.place(x=200, y=390)
  self.txtstfnum.place(x=450, y=330)
  self.txtrate.place(x=450, y=360)
  self.txthours.place(x=450, y=390)
  self.b1 = Button(win, text='Show Report', command=self.showReport)
  self.b1.place(x=100, y=450)
  self.lbl3.place(x=100, y=500)
  self.t3.place(x=150, y=500)
 def showReport(self):
  fn = self.txtfirst.get()
  sn = self.txtsur.get()
  id = self.txtid.get()
  dob =self.txtdob.get()
  r = ""
  if (self.v0.get()==1):
    intmark = int(self.txtintmark.get())
    extmark = int(self.txtextmark.get())
    stdnum = self.txtstdnum.get()
    tt = PhDStudent()
    tt.firstname = fn
    tt.lastname = sn
    tt.idno = id
    tt.dob = dob
    tt.stdnum = stdnum
    tt.intmark = intmark
    tt.extmark = extmark
    r = tt.reportLines()
    self.t3.delete('1.0', END)
    self.t3.insert(INSERT, r)
  if (self.v0.get()==2):
      rate = int(self.txtrate.get())
      hours = int(self.txthours.get())
      stfnum = self.txtstfnum.get()
      tt = PhDExaminer()
      tt.firstname = fn
      tt.lastname = sn
      tt.idno = id
      tt.dob = dob
      tt.stfnum = stfnum
      tt.rate = rate
      tt.hours = hours
      r = tt.reportLines()
      self.t3.delete('1.0', END)
      self.t3.insert(INSERT, r)
def draw_win():
 window = Tk()
 MyWindow(window)
 window.title("PhDApp")
 window.geometry("600x700+10+10")
 window.mainloop()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
 draw_win()