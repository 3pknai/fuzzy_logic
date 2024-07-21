from PyQt5 import QtCore, QtGui, QtWidgets


class Show_Func_Class(object):
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Отображение функций принадлежности для выбранной ЛП"))
        self.label.setText(_translate("MainWindow", "Выберите ЛП для отображения:"))
        self.show_fp_button.setText(_translate("MainWindow", "Отобразить"))
        self.cancel_button.setText(_translate("MainWindow", "Отмена"))

    def setupUi(self, MainWindow):
        # Задание шрифта с кеглем 12
        font12 = QtGui.QFont()
        font12.setFamily("Calibri")
        font12.setPointSize(12)
        font12.setBold(True)
        font12.setWeight(75)

        MainWindow.resize(358, 342)
        MainWindow.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)

        self.verticalLayout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFont(font12)
        self.label.setStyleSheet("background-color: rgb(220, 255, 235);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label)

        self.ling_var_list = QtWidgets.QListWidget(self.centralwidget)
        self.ling_var_list.setFont(font12)
        self.ling_var_list.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout.addWidget(self.ling_var_list)

        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.show_fp_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_fp_button.setFont(font12)
        self.show_fp_button.setStyleSheet("background-color: rgb(220, 255, 235);")
        self.horizontalLayout.addWidget(self.show_fp_button)

        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setFont(font12)
        self.cancel_button.setStyleSheet("background-color: rgb(180, 241, 221);")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
