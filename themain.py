from PyQt5 import QtCore, QtGui, QtWidgets


class The_Main_Class(object):
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Моделирование нечётких систем"))
        self.open_button.setText(_translate("MainWindow", "Открыть"))
        self.save_button.setText(_translate("MainWindow", "Сохранить"))
        self.save_as_button.setText(_translate("MainWindow", "Сохранить как.."))
        self.label.setText(_translate("MainWindow", "Входные ЛП"))
        self.create_ling_var_in.setText(_translate("MainWindow", "Создать"))
        self.delete_ling_var_in.setText(_translate("MainWindow", "Удалить"))
        self.label_2.setText(_translate("MainWindow", "Выходные ЛП"))
        self.create_ling_var_out.setText(_translate("MainWindow", "Создать"))
        self.delete_ling_var_out.setText(_translate("MainWindow", "Удалить"))
        self.show_func_button.setText(_translate("MainWindow", "Отобразить ФП для выбранной ЛП"))
        self.rules_button.setText(_translate("MainWindow", "Редактор правил вывода"))
        self.label_5.setText(_translate("MainWindow", "Первая входная ЛП:"))
        self.label_6.setText(_translate("MainWindow", "Вторая входная ЛП:"))
        self.label_7.setText(_translate("MainWindow", "Выходная ЛП:"))
        self.show_3d_button.setText(_translate("MainWindow", "Отобразить поверхность нечёткого вывода"))

    def setupUi(self, MainWindow):
        # Задание шрифта с кеглем 12
        font12 = QtGui.QFont()
        font12.setFamily("Calibri")
        font12.setPointSize(12)
        font12.setBold(True)
        font12.setWeight(75)

        MainWindow.resize(804, 695)
        MainWindow.setStyleSheet("background-color: rgb(180, 241, 221);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)

        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()

        self.open_button = QtWidgets.QPushButton(self.centralwidget)
        self.open_button.setFont(font12)
        self.open_button.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.horizontalLayout_10.addWidget(self.open_button)

        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setFont(font12)
        self.save_button.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.horizontalLayout_10.addWidget(self.save_button)

        self.save_as_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_as_button.setFont(font12)
        self.save_as_button.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.horizontalLayout_10.addWidget(self.save_as_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.gridLayout_2 = QtWidgets.QGridLayout()

        self.verticalLayout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFont(font12)
        self.label.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label)

        self.listView_in = QtWidgets.QListWidget(self.centralwidget)
        self.listView_in.setFont(font12)
        self.listView_in.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout.addWidget(self.listView_in)

        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.create_ling_var_in = QtWidgets.QPushButton(self.centralwidget)
        self.create_ling_var_in.setFont(font12)
        self.horizontalLayout.addWidget(self.create_ling_var_in)

        self.delete_ling_var_in = QtWidgets.QPushButton(self.centralwidget)
        self.delete_ling_var_in.setFont(font12)
        self.horizontalLayout.addWidget(self.delete_ling_var_in)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setFont(font12)
        self.label_2.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_2.addWidget(self.label_2)

        self.listView_out = QtWidgets.QListWidget(self.centralwidget)
        self.listView_out.setFont(font12)
        self.listView_out.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_2.addWidget(self.listView_out)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()

        self.create_ling_var_out = QtWidgets.QPushButton(self.centralwidget)
        self.create_ling_var_out.setFont(font12)
        self.horizontalLayout_2.addWidget(self.create_ling_var_out)

        self.delete_ling_var_out = QtWidgets.QPushButton(self.centralwidget)
        self.delete_ling_var_out.setFont(font12)
        self.horizontalLayout_2.addWidget(self.delete_ling_var_out)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.show_func_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_func_button.setFont(font12)
        self.show_func_button.setStyleSheet("background-color: rgb(220, 255, 235);")
        self.verticalLayout_4.addWidget(self.show_func_button)

        self.rules_button = QtWidgets.QPushButton(self.centralwidget)
        self.rules_button.setFont(font12)
        self.rules_button.setStyleSheet("background-color: rgb(220, 255, 235);")
        self.verticalLayout_4.addWidget(self.rules_button)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setFont(font12)
        self.label_5.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.horizontalLayout_3.addWidget(self.label_5)

        self.comboBox_first_in = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_first_in.setFont(font12)
        self.comboBox_first_in.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_first_in.addItem('-')
        self.horizontalLayout_3.addWidget(self.comboBox_first_in)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setFont(font12)
        self.label_6.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.horizontalLayout_5.addWidget(self.label_6)

        self.comboBox_second_in = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_second_in.setFont(font12)
        self.comboBox_second_in.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_second_in.addItem('-')
        self.horizontalLayout_5.addWidget(self.comboBox_second_in)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setFont(font12)
        self.label_7.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.horizontalLayout_6.addWidget(self.label_7)

        self.comboBox_out = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_out.setFont(font12)
        self.comboBox_out.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_out.addItem('-')
        self.horizontalLayout_6.addWidget(self.comboBox_out)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.show_3d_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_3d_button.setFont(font12)
        self.show_3d_button.setStyleSheet("background-color: rgb(220, 255, 235);")
        self.verticalLayout_3.addWidget(self.show_3d_button)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
