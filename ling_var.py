from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import *


class Ling_Var_Class(object):
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Создание лингвистической переменной"))

        self.label_3.setText(_translate("MainWindow", "Диапазон значений:"))
        self.label_9.setText(_translate("MainWindow", "От:"))
        self.label_10.setText(_translate("MainWindow", "До:"))
        self.label_4.setText(_translate("MainWindow", "Ед. измерения"))
        self.label_a.setText(_translate("MainWindow", "a:"))
        self.label_b.setText(_translate("MainWindow", "b:"))
        self.label_c.setText(_translate("MainWindow", "c:"))
        self.label_d.setText(_translate("MainWindow", ""))
        self.unit_of_measure.addItems(['', '%', '°C', 'К', 'кг', 'м', 'см', 'с', 'мин', 'Н', 'Дж', 'м/c', 'год'])

        self.label_11.setText(_translate("MainWindow", "Таблица терм-множества"))
        self.terms_table.setSortingEnabled(False)

        item = self.terms_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Название"))

        item = self.terms_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Тип ФП"))

        item = self.terms_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Параметры"))

        self.label.setText(_translate("MainWindow", "Создание лингвистической переменной"))
        self.label_2.setText(_translate("MainWindow", "Название:"))
        self.label_5.setText(_translate("MainWindow", "Задание терм-множества"))
        self.label_6.setText(_translate("MainWindow", "Название терма:"))
        self.label_7.setText(_translate("MainWindow", "Тип ФП:"))

        self.fp_type.addItems(['trimf', 'trapmf', 'gaussmf', 'gbellmf', 'signmf', 'dsigmf', 'psigmf', 'zmf', 'smf', 'pimf'])

        self.label_8.setText(_translate("MainWindow", "Параметры:"))
        self.add_term.setText(_translate("MainWindow", "Добавить"))
        self.change_term.setText(_translate("MainWindow", "Изменить"))
        self.delete_term.setText(_translate("MainWindow", "Удалить"))
        self.ling_var_OK.setText(_translate("MainWindow", "OK"))
        self.ling_var_cancel.setText(_translate("MainWindow", "Отмена"))

    def setupUi(self, MainWindow):
        # Задание шрифта с кеглем 14
        font14 = QFont()
        font14.setFamily("Calibri")
        font14.setPointSize(14)
        font14.setBold(True)
        font14.setWeight(75)

        # Задание шрифта с кеглем 12
        font12 = QFont()
        font12.setFamily("Calibri")
        font12.setPointSize(12)
        font12.setBold(True)
        font12.setWeight(75)

        MainWindow.resize(1000, 676)
        MainWindow.setStyleSheet("background-color: rgb(180, 241, 221);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setFont(font14)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addWidget(self.label_3)

        self.verticalLayout_4 = QtWidgets.QVBoxLayout()

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setFont(font12)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_4.addWidget(self.label_9)

        self.fromValue = QtWidgets.QSpinBox(self.centralwidget)
        self.fromValue.setFont(font12)
        self.fromValue.setMinimum(-10000000)
        self.fromValue.setMaximum(9999999)
        self.fromValue.setValue(0)
        self.fromValue.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_4.addWidget(self.fromValue)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setFont(font12)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.label_10)

        self.toValue = QtWidgets.QSpinBox(self.centralwidget)
        self.toValue.setFont(font12)
        self.toValue.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.toValue.setMinimum(-10000000)
        self.toValue.setMaximum(10000000)
        self.toValue.setValue(1)
        self.verticalLayout_3.addWidget(self.toValue)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setFont(font12)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_2.addWidget(self.label_4)

        self.unit_of_measure = QtWidgets.QComboBox(self.centralwidget)
        self.unit_of_measure.setFont(font12)
        self.unit_of_measure.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_2.addWidget(self.unit_of_measure)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.verticalLayout_10 = QtWidgets.QVBoxLayout()

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setFont(font14)
        self.label_11.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_10.addWidget(self.label_11)

        self.terms_table = QtWidgets.QTableWidget(self.centralwidget)
        self.terms_table.setFont(font12)
        self.terms_table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.terms_table.setAutoFillBackground(False)
        self.terms_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.terms_table.setAlternatingRowColors(False)
        self.terms_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows) # Выделение строки целиком
        self.terms_table.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.terms_table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.terms_table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.terms_table.setGridStyle(QtCore.Qt.SolidLine)
        self.terms_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.terms_table.setColumnCount(3)
        self.terms_table.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFont(font12)
        self.terms_table.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFont(font12)
        self.terms_table.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFont(font12)
        self.terms_table.setHorizontalHeaderItem(2, item)

        self.terms_table.horizontalHeader().setVisible(True)
        self.terms_table.horizontalHeader().setCascadingSectionResizes(False)
        self.terms_table.horizontalHeader().setDefaultSectionSize(324)
        self.terms_table.horizontalHeader().setHighlightSections(True)
        self.verticalLayout_10.addWidget(self.terms_table)
        self.gridLayout.addLayout(self.verticalLayout_10, 3, 1, 1, 1)

        self.verticalLayout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFont(font14)
        self.label.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setFont(font14)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.label_2)

        self.ling_var_name = QtWidgets.QLineEdit(self.centralwidget)
        self.ling_var_name.setFont(font12)
        self.ling_var_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizontalLayout.addWidget(self.ling_var_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.verticalLayout_9 = QtWidgets.QVBoxLayout()

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setFont(font14)
        self.label_5.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_9.addWidget(self.label_5)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()

        self.verticalLayout_7 = QtWidgets.QVBoxLayout()

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setFont(font14)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_7.addWidget(self.label_6)

        self.term_name = QtWidgets.QLineEdit(self.centralwidget)
        self.term_name.setFont(font12)
        self.term_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_7.addWidget(self.term_name)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QtWidgets.QVBoxLayout()

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setFont(font14)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_6.addWidget(self.label_7)

        self.fp_type = QtWidgets.QComboBox(self.centralwidget)
        self.fp_type.setFont(font12)
        self.fp_type.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_6.addWidget(self.fp_type)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QtWidgets.QVBoxLayout()

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setFont(font14)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_5.addWidget(self.label_8)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()

        self.verticalLayout_11 = QtWidgets.QVBoxLayout()

        self.label_a = QtWidgets.QLabel(self.centralwidget)
        self.label_a.setFont(font14)
        self.label_a.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_11.addWidget(self.label_a)

        self.param_a = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.param_a.setFont(font12)
        self.param_a.setMinimum(-10000000.0)
        self.param_a.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.param_a.setMaximum(1000000.0)
        self.param_a.setSingleStep(0.01)
        self.verticalLayout_11.addWidget(self.param_a)
        self.horizontalLayout_3.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QtWidgets.QVBoxLayout()

        self.label_b = QtWidgets.QLabel(self.centralwidget)
        self.label_b.setFont(font14)
        self.label_b.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_12.addWidget(self.label_b)

        self.param_b = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.param_b.setFont(font12)
        self.param_b.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.param_b.setMaximum(1000000.0)
        self.param_b.setValue(0.01)
        self.param_b.setSingleStep(0.01)
        self.verticalLayout_12.addWidget(self.param_b)
        self.horizontalLayout_3.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QtWidgets.QVBoxLayout()

        self.label_c = QtWidgets.QLabel(self.centralwidget)
        self.label_c.setFont(font14)
        self.label_c.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_13.addWidget(self.label_c)

        self.param_c = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.param_c.setFont(font12)
        self.param_c.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.param_c.setMaximum(1000000.0)
        self.param_c.setValue(0.02)
        self.param_c.setSingleStep(0.01)
        self.verticalLayout_13.addWidget(self.param_c)
        self.horizontalLayout_3.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QtWidgets.QVBoxLayout()

        self.label_d = QtWidgets.QLabel(self.centralwidget)
        self.label_d.setFont(font14)
        self.label_d.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_14.addWidget(self.label_d)

        self.param_d = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.param_d.setFont(font12)
        self.param_d.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.param_d.setMaximum(1000000.0)
        self.param_d.setValue(0.03)
        self.param_d.setSingleStep(0.01)
        self.verticalLayout_14.addWidget(self.param_d)
        self.horizontalLayout_3.addLayout(self.verticalLayout_14)

        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()

        self.add_term = QtWidgets.QPushButton(self.centralwidget)
        self.add_term.setFont(font12)
        self.add_term.setStyleSheet("background-color: rgb(220, 255, 235);")
        self.horizontalLayout_4.addWidget(self.add_term)

        self.change_term = QtWidgets.QPushButton(self.centralwidget)
        self.change_term.setFont(font12)
        self.change_term.setStyleSheet("background-color: rgb(220, 255, 235);")
        self.horizontalLayout_4.addWidget(self.change_term)

        self.delete_term = QtWidgets.QPushButton(self.centralwidget)
        self.delete_term.setFont(font12)
        self.delete_term.setStyleSheet("background-color: rgb(220, 255, 235);")
        self.horizontalLayout_4.addWidget(self.delete_term)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_9, 2, 1, 1, 1)

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()

        self.ling_var_OK = QtWidgets.QPushButton(self.centralwidget)
        self.ling_var_OK.setFont(font12)
        self.ling_var_OK.setStyleSheet("background-color: rgb(220, 255, 235);")
        self.horizontalLayout_6.addWidget(self.ling_var_OK)

        self.ling_var_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.ling_var_cancel.setFont(font12)
        self.ling_var_cancel.setStyleSheet("background-color: rgb(220, 255, 235);")
        self.horizontalLayout_6.addWidget(self.ling_var_cancel)
        self.gridLayout.addLayout(self.horizontalLayout_6, 4, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
