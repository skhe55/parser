from PyQt5 import QtCore, QtGui, QtWidgets
import resources

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(884, 382)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(884, 382))
        Dialog.setMaximumSize(QtCore.QSize(884, 382))
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main_icon"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setToolTip("")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 100, 861, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 891, 191))
        self.frame.setStyleSheet("background-color: rgb(106, 200, 104);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(240, 10, 401, 81))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(90, 60))
        self.pushButton_2.setMaximumSize(QtCore.QSize(90, 60))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(87, 150, 212);\n"
"    border: none;\n"
"    padding-top: 0px;\n"
"    color: rgb(205, 231, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(95, 166,  232);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(90, 60))
        self.pushButton.setMaximumSize(QtCore.QSize(90, 60))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(87, 150, 212);\n"
"    border: none;\n"
"    padding-top: 0px;\n"
"    color: rgb(205, 231, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(95, 166,  232);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(90, 60))
        self.pushButton_3.setMaximumSize(QtCore.QSize(90, 60))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(87, 150, 212);\n"
"    border: none;\n"
"    padding-top: 0px;\n"
"    color: rgb(205, 231, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(95, 166,  232);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(20, 10, 221, 65))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(106, 200, 104);\n"
"    border-radius: 20px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    background-color: rgb(199, 200, 188);\n"
"}\n"
"QLineEdit:hover { \n"
"    border: 2px solid rgb(112, 209, 109);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(131, 137, 255);\n"
"    background-color: rgb(106, 198, 103);\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(106, 200, 104);\n"
"    border-radius: 20px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    background-color: rgb(199, 200, 188);\n"
"}\n"
"QLineEdit:hover { \n"
"    border: 2px solid rgb(112, 209, 109);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(131, 137, 255);\n"
"    background-color: rgb(106, 198, 103);\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_3.addWidget(self.comboBox, 2, 0, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(650, 10, 77, 82))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.push_json = QtWidgets.QPushButton(self.layoutWidget)
        self.push_json.setStyleSheet("QPushButton {\n"
"    background-color: rgb(87, 150, 212);\n"
"    border: none;\n"
"    padding-top: 0px;\n"
"    color: rgb(205, 231, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(95, 166,  232);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.push_json.setObjectName("push_json")
        self.gridLayout_4.addWidget(self.push_json, 0, 0, 1, 1)
        self.push_csv = QtWidgets.QPushButton(self.layoutWidget)
        self.push_csv.setStyleSheet("QPushButton {\n"
"    background-color: rgb(87, 150, 212);\n"
"    border: none;\n"
"    padding-top: 0px;\n"
"    color: rgb(205, 231, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(95, 166,  232);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.push_csv.setObjectName("push_csv")
        self.gridLayout_4.addWidget(self.push_csv, 2, 0, 1, 1)
        self.push_xlsx = QtWidgets.QPushButton(self.layoutWidget)
        self.push_xlsx.setStyleSheet("QPushButton {\n"
"    background-color: rgb(87, 150, 212);\n"
"    border: none;\n"
"    padding-top: 0px;\n"
"    color: rgb(205, 231, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(95, 166,  232);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.push_xlsx.setObjectName("push_xlsx")
        self.gridLayout_4.addWidget(self.push_xlsx, 1, 0, 1, 1)
        self.push_db = QtWidgets.QPushButton(self.layoutWidget)
        self.push_db.setStyleSheet("QPushButton {\n"
"    background-color: rgb(87, 150, 212);\n"
"    border: none;\n"
"    padding-top: 0px;\n"
"    color: rgb(205, 231, 255);\n"
"    border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(95, 166,  232);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.push_db.setObjectName("push_db")
        self.gridLayout_4.addWidget(self.push_db, 3, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(0, 190, 901, 201))
        self.frame_2.setStyleSheet("background-color: rgb(199, 200, 188);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.raise_()
        self.frame.raise_()
        self.gridLayoutWidget.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ViewMode"))
        self.pushButton_2.setText(_translate("Dialog", "Videocards"))
        self.pushButton.setText(_translate("Dialog", "Proccesors"))
        self.pushButton_3.setText(_translate("Dialog", "RAM"))
        self.lineEdit.setText(_translate("Dialog", "0"))
        self.label.setText(_translate("Dialog", "Minimum Border"))
        self.label_2.setText(_translate("Dialog", "Maximum Border"))
        self.label_3.setText(_translate("Dialog", "Всего товаров:"))
        self.lineEdit_2.setText(_translate("Dialog", "999999"))
        self.push_json.setText(_translate("Dialog", "Save in JSON"))
        self.push_csv.setText(_translate("Dialog", "Save in CSV"))
        self.push_xlsx.setText(_translate("Dialog", "Save in XLSX"))
        self.push_db.setText(_translate("Dialog", "Save in DB"))

