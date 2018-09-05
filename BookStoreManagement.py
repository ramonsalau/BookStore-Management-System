import sqlite3
from PyQt4 import QtCore, QtGui

#Create and connect database
conn = sqlite3.connect("books.db")
c = conn.cursor()


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(830, 673)
        self.Main_Frame = QtGui.QFrame(Form)
        self.Main_Frame.setEnabled(True)
        self.Main_Frame.setGeometry(QtCore.QRect(10, 20, 801, 581))
        self.Main_Frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.Main_Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.Main_Frame.setObjectName(_fromUtf8("Main_Frame"))
        self.table = QtGui.QTableWidget(self.Main_Frame)
        self.table.setGeometry(QtCore.QRect(0, 0, 541, 581))
        self.table.setObjectName(_fromUtf8("table"))
        self.table.setColumnCount(4)
        self.table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        self.add_button = QtGui.QPushButton(self.Main_Frame)
        self.add_button.setGeometry(QtCore. QRect(640, 230, 75, 23))
        self.add_button.setObjectName(_fromUtf8("add_button"))
        self.label_2 = QtGui.QLabel(self.Main_Frame)
        self.label_2.setGeometry(QtCore.QRect(580, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.Main_Frame)
        self.label_3.setGeometry(QtCore.QRect(580, 20, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.Main_Frame)
        self.label_4.setGeometry(QtCore.QRect(580, 110, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.Main_Frame)
        self.label_5.setGeometry(QtCore.QRect(580, 170, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.title_text = QtGui.QLineEdit(self.Main_Frame)
        self.title_text.setGeometry(QtCore.QRect(580, 70, 201, 21))
        self.title_text.setObjectName(_fromUtf8("title_text"))
        self.author_text = QtGui.QLineEdit(self.Main_Frame)
        self.author_text.setGeometry(QtCore.QRect(580, 130, 201, 21))
        self.author_text.setObjectName(_fromUtf8("author_text"))
        self.year_text = QtGui.QLineEdit(self.Main_Frame)
        self.year_text.setGeometry(QtCore.QRect(580, 190, 101, 21))
        self.year_text.setObjectName(_fromUtf8("year_text"))
        self.table.raise_()
        self.add_button.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.title_text.raise_()
        self.author_text.raise_()
        self.year_text.raise_()
        self.del_button = QtGui.QPushButton(Form)
        self.del_button.setGeometry(QtCore.QRect(260, 640, 75, 23))
        self.del_button.setObjectName(_fromUtf8("del_button"))
        self.del_ID_text = QtGui.QLineEdit(Form)
        self.del_ID_text.setGeometry(QtCore.QRect(140, 640, 111, 21))
        self.del_ID_text.setObjectName(_fromUtf8("del_ID_text"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 640, 121, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Book Store Management System", None))
        self.table.setSortingEnabled(True)
        self.add_button.setText(_translate("Form", "Add Book", None))
        self.label_2.setText(_translate("Form", "Book Title", None))
        self.label_3.setText(_translate("Form", "Enter Details of the book to add", None))
        self.label_4.setText(_translate("Form", "Book Author", None))
        self.label_5.setText(_translate("Form", "Year of Publsihing", None))
        self.del_button.setText(_translate("Form", "Delete Book", None))
        self.label.setText(_translate("Form", "Enter Book ID to delete", None))

#update table for every change in database
def update_table():
    ui.table.clear()
    ui.table.setRowCount(0)
    rows = list(c.execute("SELECT * FROM books"))
    for rowPosition in range(len(rows)):
        ui.table.insertRow(rowPosition)
        ui.table.setItem(rowPosition , 0, QtGui.QTableWidgetItem(rows[rowPosition][0]))
        ui.table.setItem(rowPosition , 1, QtGui.QTableWidgetItem(str(rows[rowPosition][1])))
        ui.table.setItem(rowPosition , 2, QtGui.QTableWidgetItem(rows[rowPosition][2]))
        ui.table.setItem(rowPosition , 3, QtGui.QTableWidgetItem(rows[rowPosition][3]))
    ui.table.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem("Book Title"))
    ui.table.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem("Book ID"))
    ui.table.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem("Book Author"))
    ui.table.setHorizontalHeaderItem(3, QtGui.QTableWidgetItem("Year of Publishing"))

#add book to database
def add_book():
    c.execute("INSERT INTO books(book_title,book_author,book_year) VALUES('%s','%s','%s')" %(ui.title_text.text(),ui.author_text.text(),ui.year_text.text()))
    conn.commit()
    update_table()

#delete book from database
def del_book():
    book_id = ui.del_ID_text.text()
    c.execute("DELETE FROM books WHERE book_id = '%s'" % book_id)
    conn.commit()
    update_table()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.add_button.clicked.connect(add_book)
    ui.del_button.clicked.connect(del_book)
    Form.show()
    update_table()
    sys.exit(app.exec_())
    
