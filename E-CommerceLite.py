import os
import sys
# import mysql.connector
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QAction, QMainWindow, QMenu, QComboBox
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem

#-------------------------------------------------------------#
#---------------------------Apps------------------------------#
#-------------------------------------------------------------#

# ----------------------------------------> Stores

class Stores(QWidget):
    def __init__(self):
        super().__init__()
        self.icon = "1.ico"
        self.title = "PyQt5 Widnow"
        self.initwindow()
    def initwindow(self):
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setFixedSize(500,600)
        self.stores()
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.groupBox)
        self.setLayout(self.vbox)
        self.show()
    def stores(self):

        self.store_id = QLabel("كود المخزن")
        self.store_id_text = QLineEdit()

        self.groupBox = QGroupBox()
        self.gridLayout = QGridLayout()

        self.store_id = QLabel("كود المخزن")
        self.store_id_text = QLineEdit()
        self.gridLayout.addWidget(self.store_id, 0, 0)
        self.gridLayout.addWidget(self.store_id_text, 0, 1,1,2)


        self.store_name = QLabel("اسم المخزن")
        self.store_name_text = QLineEdit()
        self.gridLayout.addWidget(self.store_name, 1, 0)
        self.gridLayout.addWidget(self.store_name_text, 1, 1,1,2)

        self.store_per = QLabel("امين المخزن")
        self.store_per_text = QLineEdit()
        self.gridLayout.addWidget(self.store_per, 2, 0)
        self.gridLayout.addWidget(self.store_per_text, 2, 1,1,2)

        self.store_phone = QLabel("تليفون المخزن")
        self.store_phone_text = QLineEdit()
        self.gridLayout.addWidget(self.store_phone, 3, 0)
        self.gridLayout.addWidget(self.store_phone_text, 3, 1,1,2)

        self.store_address = QLabel("عنوان المخزن")
        self.store_address_text = QLineEdit()
        self.gridLayout.addWidget(self.store_address, 4, 0)
        self.gridLayout.addWidget(self.store_address_text, 4, 1,1,2)

        self.store_hints = QLabel("ملاحظات")
        self.store_hints_text = QLineEdit()
        self.gridLayout.addWidget(self.store_hints, 5, 0)
        self.gridLayout.addWidget(self.store_hints_text, 5, 1,1,2)

        self.store_add = QPushButton("اضافة")
        self.gridLayout.addWidget(self.store_add, 6, 0)

        self.store_edit = QPushButton("تعديل")
        self.gridLayout.addWidget(self.store_edit, 6, 1)

        self.store_add_for_user = QPushButton("حذف")
        self.gridLayout.addWidget(self.store_add_for_user, 6, 2)


        self.store_tableWidget = QTableWidget()
        self.store_tableWidget.setLayoutDirection(Qt.RightToLeft)
        self.store_tableWidget.verticalHeader().setVisible(False)
        self.store_tableWidget.horizontalHeader().setVisible(False)
        self.store_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.store_tableWidget.setRowCount(1000)
        self.store_tableWidget.setColumnCount(6)


        self.store_tableWidget.setItem(0, 0, QTableWidgetItem("كود المخزن"))
        self.store_tableWidget.setItem(0, 1, QTableWidgetItem("اسم المخزن"))
        self.store_tableWidget.setItem(0, 2, QTableWidgetItem("امين المخزن"))
        self.store_tableWidget.setItem(0, 3, QTableWidgetItem("تليفون المخزن"))
        self.store_tableWidget.setItem(0, 4, QTableWidgetItem("عنوان المخزن"))
        self.store_tableWidget.setItem(0, 5, QTableWidgetItem("ملاحظات"))

        self.gridLayout.addWidget(self.store_tableWidget,7,0,1,3)

        self.groupBox.setLayout(self.gridLayout)

# ----------------------------------------> Companies

class Companies(QWidget):
    def __init__(self):
        super().__init__()
        self.icon = "1.ico"
        self.title = "الشركات"
        self.initwindow()
    def initwindow(self):
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setFixedSize(500,600)
        self.companies()
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.groupBox)
        self.setLayout(self.vbox)
        self.show()
    def companies(self):
        self.groupBox = QGroupBox()
        self.gridLayout = QGridLayout()

        self.company_id = QLabel("كود الشركة")
        self.company_id_text = QLineEdit()
        self.gridLayout.addWidget(self.company_id, 0, 0)
        self.gridLayout.addWidget(self.company_id_text, 0, 1,1,2)


        self.company_name = QLabel("اسم الشركة")
        self.company_name_text = QLineEdit()
        self.gridLayout.addWidget(self.company_name, 1, 0)
        self.gridLayout.addWidget(self.company_name_text, 1, 1,1,2)

        self.company_add = QPushButton("اضافة")
        self.gridLayout.addWidget(self.company_add, 2, 0)

        self.company_edit = QPushButton("تعديل")
        self.gridLayout.addWidget(self.company_edit, 2, 1)

        self.company_add_for_user = QPushButton("حذف")
        self.gridLayout.addWidget(self.company_add_for_user, 2, 2)


        self.company_tableWidget = QTableWidget()
        self.company_tableWidget.setLayoutDirection(Qt.RightToLeft)
        self.company_tableWidget.verticalHeader().setVisible(False)
        self.company_tableWidget.horizontalHeader().setVisible(False)
        self.company_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.company_tableWidget.setRowCount(1000)
        self.company_tableWidget.setColumnCount(2)


        self.company_tableWidget.setItem(0, 0, QTableWidgetItem("كود الشركة"))
        self.company_tableWidget.setItem(0, 1, QTableWidgetItem("اسم الشركة"))
        self.company_tableWidget.setColumnWidth(1, 339)

        self.gridLayout.addWidget(self.company_tableWidget,3,0,1,3)

        self.groupBox.setLayout(self.gridLayout)

# ----------------------------------------> Types

class Types(QWidget):
    def __init__(self):
        super().__init__()
        self.icon = "1.ico"
        self.title = "الانواع"
        self.initwindow()
    def initwindow(self):
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setFixedSize(500,600)
        self.types()
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.groupBox)
        self.setLayout(self.vbox)
        self.show()
    def types(self):
        self.groupBox = QGroupBox()
        self.gridLayout = QGridLayout()

        self.type_id = QLabel("الشركة")

        self.combo = QComboBox()
        self.combo.addItem("Python")

        self.gridLayout.addWidget(self.type_id, 0, 0)
        self.gridLayout.addWidget(self.combo, 0, 1,1,2)

        self.type_name = QLabel("النوع")
        self.type_name_text = QLineEdit()
        self.gridLayout.addWidget(self.type_name, 1, 0)
        self.gridLayout.addWidget(self.type_name_text, 1, 1,1,2)

        self.type_add = QPushButton("اضافة")
        self.gridLayout.addWidget(self.type_add, 2, 0)

        self.type_edit = QPushButton("تعديل")
        self.gridLayout.addWidget(self.type_edit, 2, 1)

        self.type_add_for_user = QPushButton("حذف")
        self.gridLayout.addWidget(self.type_add_for_user, 2, 2)


        self.type_tableWidget = QTableWidget()
        self.type_tableWidget.setLayoutDirection(Qt.RightToLeft)
        self.type_tableWidget.verticalHeader().setVisible(False)
        self.type_tableWidget.horizontalHeader().setVisible(False)
        self.type_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.type_tableWidget.setRowCount(1000)
        self.type_tableWidget.setColumnCount(1)

        self.type_tableWidget.setItem(0, 0, QTableWidgetItem("الانواع المسجلة"))
        self.type_tableWidget.setColumnWidth(0, 450)

        # self.type_tableWidget.doubleClicked.connect(self.on_click)

        self.gridLayout.addWidget(self.type_tableWidget,3,0,1,3)
        self.groupBox.setLayout(self.gridLayout)

# ----------------------------------------> Units

class Units(QWidget):
    def __init__(self):
        super().__init__()
        self.icon = "1.ico"
        self.title = "الوحدات"
        self.initwindow()
    def initwindow(self):
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setFixedSize(500,600)
        self.units()
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.groupBox)
        self.setLayout(self.vbox)
        self.show()
    def units(self):
        self.groupBox = QGroupBox()
        self.gridLayout = QGridLayout()

        self.unit_id = QLabel("كود الوحدة")
        self.unit_id_text = QLineEdit()
        self.gridLayout.addWidget(self.unit_id, 0, 0)
        self.gridLayout.addWidget(self.unit_id_text, 0, 1,1,2)

        self.unit_name = QLabel("الوحدة")
        self.unit_name_text = QLineEdit()
        self.gridLayout.addWidget(self.unit_name, 1, 0)
        self.gridLayout.addWidget(self.unit_name_text, 1, 1,1,2)

        self.unit_add = QPushButton("اضافة")
        self.gridLayout.addWidget(self.unit_add, 2, 0)

        self.unit_edit = QPushButton("تعديل")
        self.gridLayout.addWidget(self.unit_edit, 2, 1)

        self.unit_add_for_user = QPushButton("حذف")
        self.gridLayout.addWidget(self.unit_add_for_user, 2, 2)


        self.unit_tableWidget = QTableWidget()
        self.unit_tableWidget.setLayoutDirection(Qt.RightToLeft)
        self.unit_tableWidget.verticalHeader().setVisible(False)
        self.unit_tableWidget.horizontalHeader().setVisible(False)
        self.unit_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.unit_tableWidget.setRowCount(1000)
        self.unit_tableWidget.setColumnCount(1)

        self.unit_tableWidget.setItem(0, 0, QTableWidgetItem("الوحدات المسجلة"))
        self.unit_tableWidget.setColumnWidth(0, 450)

        self.gridLayout.addWidget(self.unit_tableWidget,3,0,1,3)
        self.groupBox.setLayout(self.gridLayout)

# ----------------------------------------> Items

class DB_Items(QWidget):
    def __init__(self):
        super().__init__()
        self.icon = "1.ico"
        self.title = "قاعدة بيانات الاصناف"
        self.initwindow()
    def initwindow(self):
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setFixedSize(965,600)
        self.db_items()
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.groupBox)
        self.setLayout(self.vbox)
        self.show()
    def db_items(self):
        self.groupBox = QGroupBox()
        self.gridLayout = QGridLayout()

        self.db_items_tableWidget = QTableWidget()
        self.db_items_tableWidget.setLayoutDirection(Qt.RightToLeft)
        self.db_items_tableWidget.verticalHeader().setVisible(False)
        self.db_items_tableWidget.horizontalHeader().setVisible(False)
        self.db_items_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.db_items_tableWidget.setRowCount(1000)
        self.db_items_tableWidget.setColumnCount(7)

        self.db_items_tableWidget.setItem(0, 0, QTableWidgetItem("الكود"))
        self.db_items_tableWidget.setItem(0, 1, QTableWidgetItem("اسم الصنف"))
        self.db_items_tableWidget.setItem(0, 2, QTableWidgetItem("الشركة"))
        self.db_items_tableWidget.setItem(0, 3, QTableWidgetItem("النوع"))
        self.db_items_tableWidget.setItem(0, 4, QTableWidgetItem("الوحدة"))
        self.db_items_tableWidget.setItem(0, 5, QTableWidgetItem("السعر"))
        self.db_items_tableWidget.setItem(0, 6, QTableWidgetItem("الحد الادني"))
        self.db_items_tableWidget.setColumnWidth(1, 300)

        self.gridLayout.addWidget(self.db_items_tableWidget,1,0)
        self.groupBox.setLayout(self.gridLayout)

class Items(QWidget):
    def __init__(self):
        super().__init__()
        self.icon = "1.ico"
        self.title = "الاصناف"
        self.initwindow()
    def initwindow(self):
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setFixedSize(800,600)
        self.items()
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.groupBox)
        self.setLayout(self.vbox)
        self.show()
    def items(self):
        self.groupBox = QGroupBox()
        self.gridLayout = QGridLayout()

        self.item_id = QLabel("كود الصنف")
        self.item_id_text = QLineEdit()
        self.gridLayout.addWidget(self.item_id, 0, 0)
        self.gridLayout.addWidget(self.item_id_text, 0, 1)

        self.item_name = QLabel("اسم الصنف")
        self.item_name_text = QLineEdit()
        self.gridLayout.addWidget(self.item_name, 1, 0)
        self.gridLayout.addWidget(self.item_name_text, 1, 1)

        self.item_company = QLabel("الشركة")
        self.combo_item_company = QComboBox()
        self.combo_item_company.addItem("Python")
        self.gridLayout.addWidget(self.item_company, 2, 0)
        self.gridLayout.addWidget(self.combo_item_company, 2, 1)


        self.item_type = QLabel("النوع")
        self.combo_item_type = QComboBox()
        self.combo_item_type.addItem("Python")
        self.gridLayout.addWidget(self.item_type, 3, 0)
        self.gridLayout.addWidget(self.combo_item_type, 3, 1)

        self.item_unit = QLabel("الوحدة")
        self.combo_item_unit = QComboBox()
        self.combo_item_unit.addItem("Python")
        self.gridLayout.addWidget(self.item_unit, 4, 0)
        self.gridLayout.addWidget(self.combo_item_unit, 4, 1)


        self.item_sale = QLabel("سعر البيع")
        self.item_sale_text = QLineEdit()
        self.gridLayout.addWidget(self.item_sale, 0, 2)
        self.gridLayout.addWidget(self.item_sale_text, 0, 3)

        self.item_wholesale = QLabel("سعر الجملة")
        self.item_wholesale_text = QLineEdit()
        self.gridLayout.addWidget(self.item_wholesale, 1, 2)
        self.gridLayout.addWidget(self.item_wholesale_text, 1, 3)

        self.item_buy = QLabel("سعر الشراء")
        self.item_buy_text = QLineEdit()
        self.gridLayout.addWidget(self.item_buy, 2, 2)
        self.gridLayout.addWidget(self.item_buy_text, 2, 3)

        self.item_discount = QLabel("أقصي نسبة خصم")
        self.item_discount_text = QLineEdit()
        self.gridLayout.addWidget(self.item_discount, 3, 2)
        self.gridLayout.addWidget(self.item_discount_text, 3, 3)

        self.item_quantity = QLabel("الحد الادني للكمية")
        self.item_quantity_text = QLineEdit()
        self.gridLayout.addWidget(self.item_quantity, 4, 2)
        self.gridLayout.addWidget(self.item_quantity_text, 4, 3)

        self.item_hints = QLabel("ملاحظات")
        self.item_hints_plain = QPlainTextEdit(self)
        self.item_hints_plain.resize(400,400)
        self.gridLayout.addWidget(self.item_hints, 5,0)
        self.gridLayout.addWidget(self.item_hints_plain,5,1,1,3)

        self.item_store = QLabel("المخزن")

        self.combo_item_store = QComboBox()
        self.combo_item_store.addItem("Python")

        self.gridLayout.addWidget(self.item_store, 6, 0)
        self.gridLayout.addWidget(self.combo_item_store, 6, 1)

        self.item_quantity_store = QLabel("الكمية بالمخزن")
        self.item_quantity_store_text = QLineEdit()
        self.gridLayout.addWidget(self.item_quantity_store, 6, 2)
        self.gridLayout.addWidget(self.item_quantity_store_text, 6, 3)

        self.item_add_quantity_store = QPushButton("الاصناف")
        self.item_add_quantity_store.clicked.connect(self.show_db_item)
        self.gridLayout.addWidget(self.item_add_quantity_store,7,1)

        self.item_add_quantity_store = QPushButton("اضافة")
        self.gridLayout.addWidget(self.item_add_quantity_store,7,3)


        self.item_tableWidget = QTableWidget()
        self.item_tableWidget.setLayoutDirection(Qt.RightToLeft)
        self.item_tableWidget.verticalHeader().setVisible(False)
        self.item_tableWidget.horizontalHeader().setVisible(False)
        self.item_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.item_tableWidget.setRowCount(1000)
        self.item_tableWidget.setColumnCount(2)

        self.item_tableWidget.setItem(0, 0, QTableWidgetItem("المخزن"))
        self.item_tableWidget.setItem(0, 1, QTableWidgetItem("الكمية"))
        self.item_tableWidget.setColumnWidth(0, 450)
        self.item_tableWidget.setColumnWidth(1, 289)

        self.gridLayout.addWidget(self.item_tableWidget,8,0,1,4)


        self.groupBox.setLayout(self.gridLayout)

    def show_db_item(self, checked):
        self.show_db_item = DB_Items()
        self.show_db_item.show()

#-------------------------------------------------------------#
#---------------------------Main------------------------------#
#-------------------------------------------------------------#

class Window(QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.title = "الرئيسية"
        self.top = 200
        self.left = 500
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setFixedSize(800,600)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        Stores_Button = QPushButton("المخازن",self)
        Stores_Button.setGeometry(QRect(680,20,100,30))
        # button.setIcon(QtGui.QIcon("1.png"))
        # button.setToolTip("<h1>This Click Me Button<h1>")
        Stores_Button.clicked.connect(self.Show_Stores)

        Companies_Button = QPushButton("الشركات",self)
        Companies_Button.setGeometry(QRect(570,20,100,30))
        Companies_Button.clicked.connect(self.Show_Companies)

        Types_Button = QPushButton("الانواع",self)
        Types_Button.setGeometry(QRect(460,20,100,30))
        Types_Button.clicked.connect(self.Show_Types)

        Types_Button = QPushButton("الوحدات",self)
        Types_Button.setGeometry(QRect(350,20,100,30))
        Types_Button.clicked.connect(self.Show_Units)

        Items_Button = QPushButton("الاصناف",self)
        Items_Button.setGeometry(QRect(240,20,100,30))
        Items_Button.clicked.connect(self.Show_Items)

    def Show_Stores(self, checked):
        self.show_stores = Stores()
        self.show_stores.show()

    def Show_Companies(self, checked):
        self.show_companies = Companies()
        self.show_companies.show()

    def Show_Types(self, checked):
        self.show_types = Types()
        self.show_types.show()

    def Show_Units(self, checked):
        self.show_units = Units()
        self.show_units.show()

    def Show_Items(self, checked):
        self.show_items = Items()
        self.show_items.show()




if __name__== "__main__":
    App = QApplication(sys.argv)
    App.setLayoutDirection(Qt.RightToLeft)
    window = Window()
    sys.exit(App.exec())