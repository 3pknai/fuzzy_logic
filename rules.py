from PyQt5 import QtCore, QtGui, QtWidgets


class Rules_Editor_Class(object):
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Редактор правил вывода"))
        self.label.setText(_translate("MainWindow", "Задание правил вывода"))
        self.label_2.setText(_translate("MainWindow", "Если:"))
        self.label_3.setText(_translate("MainWindow", "то:"))
        self.label_6.setText(_translate("MainWindow", "Соединение"))
        self.RB_AND.setText(_translate("MainWindow", "AND"))
        self.RB_OR.setText(_translate("MainWindow", "OR"))
        self.label_4.setText(_translate("MainWindow", "Вес"))
        self.label_5.setText(_translate("MainWindow", "Правила вывода"))
        self.add_button.setText(_translate("MainWindow", "Добавить"))
        self.delete_button.setText(_translate("MainWindow", "Удалить"))
        self.delete_all_button.setText(_translate("MainWindow", "Удалить всё"))
        self.label_rules_count.setText(_translate("MainWindow", "Количество правил: 0"))
        self.OK.setText(_translate("MainWindow", "OK"))
        self.exit_button.setText(_translate("MainWindow", "Отмена"))
    def setupUi(self, MainWindow):
        # Задание шрифта с кеглем 14
        font14 = QtGui.QFont()
        font14.setFamily("Calibri")
        font14.setPointSize(14)
        font14.setBold(True)
        font14.setWeight(75)

        # Задание шрифта с кеглем 12
        font12 = QtGui.QFont()
        font12.setFamily("Calibri")
        font12.setPointSize(12)
        font12.setBold(True)
        font12.setWeight(75)

        MainWindow.resize(1211, 715)
        MainWindow.setStyleSheet("background-color: rgb(220, 255, 235);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.centralwidget)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFont(font14)
        self.label.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_9.addWidget(self.label)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setFont(font14)
        self.horizontalLayout_5.addWidget(self.label_2)

        self.verticalLayout = QtWidgets.QVBoxLayout()

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setFont(font14)
        self.horizontalLayout_5.addWidget(self.label_3)

        self.verticalLayout_4 = QtWidgets.QVBoxLayout()

        self.verticalLayout_8 = QtWidgets.QVBoxLayout()

        self.verticalLayout_5 = QtWidgets.QVBoxLayout()

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setFont(font14)
        self.verticalLayout_5.addWidget(self.label_6)

        self.RB_AND = QtWidgets.QRadioButton(self.centralwidget)
        self.RB_AND.setFont(font12)
        self.RB_AND.setChecked(True)
        self.verticalLayout_5.addWidget(self.RB_AND)

        self.RB_OR = QtWidgets.QRadioButton(self.centralwidget)
        self.RB_OR.setFont(font12)
        self.verticalLayout_5.addWidget(self.RB_OR)
        self.verticalLayout_8.addLayout(self.verticalLayout_5)

        self.verticalLayout_7 = QtWidgets.QVBoxLayout()

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setFont(font14)
        self.verticalLayout_7.addWidget(self.label_4)

        self.weight = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.weight.setFont(font12)
        self.weight.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.weight.setMaximum(1.0)
        self.weight.setSingleStep(0.05)
        self.weight.setProperty("value", 1.0)
        self.verticalLayout_7.addWidget(self.weight)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.verticalLayout_6 = QtWidgets.QVBoxLayout()

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setFont(font14)
        self.label_5.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_6.addWidget(self.label_5)

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()

        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setFont(font12)
        self.add_button.setStyleSheet("background-color: rgb(180, 241, 221);")
        self.horizontalLayout_6.addWidget(self.add_button)

        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setFont(font12)
        self.delete_button.setStyleSheet("background-color: rgb(180, 241, 221);")
        self.horizontalLayout_6.addWidget(self.delete_button)

        self.delete_all_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_all_button.setFont(font12)
        self.delete_all_button.setStyleSheet("background-color: rgb(180, 241, 221);")
        self.horizontalLayout_6.addWidget(self.delete_all_button)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.listWidget_rules = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_rules.setFont(font12)
        self.listWidget_rules.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_6.addWidget(self.listWidget_rules)
        self.verticalLayout_9.addLayout(self.verticalLayout_6)

        self.label_rules_count = QtWidgets.QLabel(self.centralwidget)
        self.label_rules_count.setFont(font14)
        self.label_rules_count.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_9.addWidget(self.label_rules_count)

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()

        self.OK = QtWidgets.QPushButton(self.centralwidget)
        self.OK.setFont(font12)
        self.OK.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.horizontalLayout_7.addWidget(self.OK)

        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setFont(font12)
        self.exit_button.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.horizontalLayout_7.addWidget(self.exit_button)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
