import npyscreen
import random


class nameField(npyscreen.TitleText):
    def when_value_edited(self):
        with open('result.txt', 'w+') as f:
            f.write(f'name: {self.value}\n')


class departmentSelect(npyscreen.TitleMultiSelect):
    def when_value_edited(self):
        with open('result.txt', 'a') as f:
            f.write(f'department: {self.value}\n')


class MyGrid(npyscreen.GridColTitles):
    # You need to override custom_print_cell to manipulate how
    # a cell is printed. In this example we change the color of the
    # text depending on the string value of cell.
    def custom_print_cell(self, actual_cell, cell_display_value):
        if cell_display_value =='FAIL':
           actual_cell.color = 'DANGER'
        elif cell_display_value == 'PASS':
           actual_cell.color = 'GOOD'
        else:
           actual_cell.color = 'DEFAULT'


class myEmployeeForm(npyscreen.Form):
    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def create(self):
        y, x = self.useable_space()
        myFW = self.add(npyscreen.TitleText)
        gd = self.add(MyGrid, col_titles=['Col1', 'Col2', 'Col3', 'Col4'], max_width=x // 10 * 7, max_height=y)

        # Adding values to the Grid, this code just randomly
        # fills a 2 x 4 grid with random PASS/FAIL strings.
        gd.values = []
        for x in range(10):
            row = []
            for y in range(4):
                if bool(random.getrandbits(1)):
                    row.append("Data1")
                else:
                    row.append("Data2")
            gd.values.append(row)
        # F.edit()

        # self.myName = self.add(nameField, name='Name')
        # self.myDepartment = self.add(departmentSelect, scroll_exit=True, max_height=3, name='Department',
        #                              values=['Department 1', 'Department 2', 'Department 3'])
        # self.myDate = self.add(npyscreen.TitleDateCombo, name='Date Employed')


        self.myTree = self.add(npyscreen.MLTreeMultiSelect,
                               name='Fields',
                               relx=x // 10 * 7 + 1,
                               rely=y,
                               max_width=x // 10 * 3,
                               max_height=y)

        treecontent = npyscreen.NPSTreeData(content='Root', selectable=True, ignoreRoot=False)
        c1 = treecontent.newChild(content='Child 1', selectable=True, selected=True)
        c2 = treecontent.newChild(content='Child 2', selectable=True)
        g1 = c1.newChild(content='Grand-child 1', selectable=True)
        g2 = c1.newChild(content='Grand-child 2', selectable=True)
        g3 = c1.newChild(content='Grand-child 3')
        gg1 = g1.newChild(content='Great Grand-child 1', selectable=True)
        gg2 = g1.newChild(content='Great Grand-child 2', selectable=True)
        gg3 = g1.newChild(content='Great Grand-child 3')
        self.myTree.values = treecontent


class MyApplication(npyscreen.NPSAppManaged):
    def onStart(self):
        npyscreen.setTheme(npyscreen.Themes.TransparentThemeDarkText)
        self.addForm('MAIN', myEmployeeForm, name='New Form')
        # A real application might define more forms here.......


if __name__ == '__main__':
    TestApp = MyApplication().run()
# import npyscreen
# import random
#
#
# class MyGrid(npyscreen.GridColTitles):
#     # You need to override custom_print_cell to manipulate how
#     # a cell is printed. In this example we change the color of the
#     # text depending on the string value of cell.
#     def custom_print_cell(self, actual_cell, cell_display_value):
#         if cell_display_value =='FAIL':
#            actual_cell.color = 'DANGER'
#         elif cell_display_value == 'PASS':
#            actual_cell.color = 'GOOD'
#         else:
#            actual_cell.color = 'DEFAULT'
#
#
# def myFunction(*args):
#     # making an example Form
#     npyscreen.setTheme(npyscreen.Themes.TransparentThemeDarkText)
#     F = npyscreen.Form(name='Data viewer')
#     myFW = F.add(npyscreen.TitleText)
#     gd = F.add(MyGrid, col_titles=['Col1', 'Col2', 'Col3', 'Col4'])
#
#     # Adding values to the Grid, this code just randomly
#     # fills a 2 x 4 grid with random PASS/FAIL strings.
#     gd.values = []
#     for x in range(2):
#         row = []
#         for y in range(4):
#             if bool(random.getrandbits(1)):
#                 row.append("Data1")
#             else:
#                 row.append("Data2")
#         gd.values.append(row)
#     F.edit()
#
# if __name__ == '__main__':
#     npyscreen.wrapper_basic(myFunction)