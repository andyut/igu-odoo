import npyscreen


class myEmployeeForm(npyscreen.Form):
    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def create(self):
       self.myName        = self.add(npyscreen.TitleText, name='Customer Name')
       self.myName2        = self.add(npyscreen.TitleText, name='Address')
       self.myName3        = self.add(npyscreen.TitleText, name='Ref No')
       self.myName4        = self.add(npyscreen.TitleText, name='Notes')
       self.myName5        = self.add(npyscreen.TitleText, name='Remarks')
       self.myDepartment = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=3, name='Delivery ', values = ['Delivery Morning', 'Delivery Afternoon', 'Others'])
       self.myDate        = self.add(npyscreen.TitleDateCombo, name='Date Delivery')

class MyApplication(npyscreen.NPSAppManaged):
   def onStart(self):
       self.addForm('MAIN', myEmployeeForm, name='New Order')
       # A real application might define more forms here.......

if __name__ == '__main__':
   TestApp = MyApplication().run()
   print TestApp