from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

class Main_menu_Class(object):
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное меню"))
        self.main_label.setText(_translate("MainWindow", "Fuzzy Logic"))
        self.operations_button.setText(_translate("MainWindow", "Операции над нечёткими множествами"))
        self.lp_button.setText(_translate("MainWindow", "Моделирование нечётких систем"))
        self.download_lp.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.button_info.setText(_translate("MainWindow", "Информация о разработчиках программы"))

    def setupUi(self, MainWindow):
        # Задание шрифта с кеглем 12
        font12 = QtGui.QFont()
        font12.setFamily("Calibri")
        font12.setPointSize(12)
        font12.setBold(True)
        font12.setWeight(75)

        # Задание шрифта с кеглем 14
        font14 = QtGui.QFont()
        font14.setFamily("Calibri")
        font14.setPointSize(14)
        font14.setBold(True)
        font14.setWeight(75)

        # Задание шрифта с кеглем 24
        font24 = QtGui.QFont()
        font24.setFamily("Calibri")
        font24.setPointSize(24)
        font24.setBold(True)
        font24.setWeight(75)

        MainWindow.resize(513, 249)
        MainWindow.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.main_label = QtWidgets.QLabel(self.centralwidget)
        self.main_label.setFont(font24)
        self.main_label.setStyleSheet("background-color: rgb(0, 220, 153);")
        self.main_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_label.setWordWrap(True)
        self.verticalLayout.addWidget(self.main_label)

        self.horizontalLayout = QtWidgets.QHBoxLayout()

        spacerItem = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.operations_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.operations_button.sizePolicy().hasHeightForWidth())
        self.operations_button.setSizePolicy(sizePolicy)
        self.operations_button.setFont(font12)
        self.operations_button.setStyleSheet("background-color: rgb(220, 255, 235);")
        self.horizontalLayout.addWidget(self.operations_button)

        self.download_operations = QtWidgets.QPushButton(self.centralwidget)
        self.download_operations.setFont(font14)
        self.download_operations.setText("")
        icon = QtGui.QIcon()
        os.chdir(sys._MEIPASS)
        icon.addPixmap(QtGui.QPixmap("download-icon-png-5.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.download_operations.setIcon(icon)
        self.download_operations.setIconSize(QtCore.QSize(70, 70))
        self.horizontalLayout.addWidget(self.download_operations)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()

        spacerItem1 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)

        self.lp_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lp_button.sizePolicy().hasHeightForWidth())
        self.lp_button.resize(394, 32)
        self.lp_button.setSizePolicy(sizePolicy)
        self.lp_button.setFont(font12)
        self.lp_button.setStyleSheet("background-color: rgb(220, 255, 235);")
        self.horizontalLayout_2.addWidget(self.lp_button)

        self.download_lp = QtWidgets.QPushButton(self.centralwidget)
        self.download_lp.setFont(font14)
        self.download_lp.setIcon(icon)
        self.download_lp.setIconSize(QtCore.QSize(70, 70))
        self.horizontalLayout_2.addWidget(self.download_lp)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.button_info = QtWidgets.QPushButton(self.centralwidget)
        self.button_info.setFont(font14)
        self.button_info.setStyleSheet("background-color: rgb(220, 255, 235);")
        self.verticalLayout.addWidget(self.button_info)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Main_menu_Class()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())