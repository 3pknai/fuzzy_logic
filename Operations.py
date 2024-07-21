from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Operations_Class(object):
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Операции над нечёткими множествами"))
        self.fuzzy_sets_list.setSortingEnabled(False)
        self.add_button.setText(_translate("MainWindow", "Добавить"))
        self.change_button.setText(_translate("MainWindow", "Изменить"))
        self.remove_button.setText(_translate("MainWindow", "Удалить"))
        self.label_name.setText(_translate("MainWindow", "  Название нечёткого множества:"))
        self.label_type.setText(_translate("MainWindow", "  Тип функции принадлежности:"))
        self.label_parameters.setText(_translate("MainWindow", "Параметры:"))
        self.label_a.setText(_translate("MainWindow", "a:"))
        self.label_b.setText(_translate("MainWindow", "b:"))
        self.label_c.setText(_translate("MainWindow", "c:"))
        self.label_2.setText(_translate("MainWindow", "Диапазон значений:"))
        self.label_3.setText(_translate("MainWindow", "От:"))
        self.label_4.setText(_translate("MainWindow", "До:"))
        self.label_5.setText(_translate("MainWindow", "Количество точек:"))
        self.label_name_2.setText(_translate("MainWindow",
                                     "Название нового нечёткого множества, созданного с помощью одной из указанных операций:"))
        self.label_operations.setText(_translate("MainWindow", "Операции:"))
        self.unification_button.setText(_translate("MainWindow", "Объединение"))
        self.intersection_button.setText(_translate("MainWindow", "Пересечение"))
        self.addiction_button.setText(_translate("MainWindow", "Дополнение"))
        self.difference_button.setText(_translate("MainWindow", "Разность"))
        self.symmetric_difference_button.setText(_translate("MainWindow", "Симметрическая\n"
                                                                  "разность"))
        self.algebraic_unification_button.setText(_translate("MainWindow", "Алгебраическое\n"
                                                                   "объединение"))
        self.algebraic_intersection_button.setText(_translate("MainWindow", "Алгебраическое\n"
                                                                    "пересечение"))
        self.boundary_unification_button.setText(_translate("MainWindow", "Граничное\n"
                                                                  "объединение"))
        self.boundary_intersection_button.setText(_translate("MainWindow", "Граничное\n"
                                                                   "пересечение"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.action.setText(_translate("MainWindow", "Открыть"))
        self.action_2.setText(_translate("MainWindow", "Сохранить"))
        self.action_3.setText(_translate("MainWindow", "Сохранить как"))

    def setupUi(self, MainWindow):
        # Задание шрифта с кеглем 10
        font10 = QtGui.QFont()
        font10.setFamily("Calibri")
        font10.setPointSize(10)
        font10.setBold(True)
        font10.setWeight(75)

        # Задание шрифта с кеглем 12
        font12 = QtGui.QFont()
        font12.setFamily("Calibri")
        font12.setPointSize(12)
        font12.setBold(True)
        font12.setWeight(75)

        MainWindow.resize(1325, 819)
        MainWindow.setStyleSheet("background-color: rgb(180, 241, 221);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.centralwidget)

        self.verticalLayout_8 = QtWidgets.QVBoxLayout()

        self.gridLayout = QtWidgets.QGridLayout()

        self.verticalLayout_7 = QtWidgets.QVBoxLayout()

        self.fuzzy_sets_list = QtWidgets.QListWidget(self.centralwidget)
        self.fuzzy_sets_list.setFont(font12)
        self.fuzzy_sets_list.setAutoFillBackground(False)
        self.fuzzy_sets_list.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fuzzy_sets_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.fuzzy_sets_list.setTextElideMode(QtCore.Qt.ElideRight)
        self.fuzzy_sets_list.setResizeMode(QtWidgets.QListView.Fixed)
        self.fuzzy_sets_list.setViewMode(QtWidgets.QListView.ListMode)
        self.fuzzy_sets_list.setModelColumn(0)
        self.verticalLayout_7.addWidget(self.fuzzy_sets_list)

        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setFont(font12)
        self.add_button.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.horizontalLayout.addWidget(self.add_button)

        self.change_button = QtWidgets.QPushButton(self.centralwidget)
        self.change_button.setFont(font12)
        self.change_button.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.horizontalLayout.addWidget(self.change_button)

        self.remove_button = QtWidgets.QPushButton(self.centralwidget)
        self.remove_button.setFont(font12)
        self.remove_button.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.horizontalLayout.addWidget(self.remove_button)
        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()

        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setFont(font12)
        self.label_name.setStyleSheet("background-color: rgb(180, 241, 221);")

        self.horizontalLayout_2.addWidget(self.label_name)

        self.fuzzy_set_name = QtWidgets.QLineEdit(self.centralwidget)
        self.fuzzy_set_name.setFont(font12)
        self.fuzzy_set_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.horizontalLayout_2.addWidget(self.fuzzy_set_name)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()

        self.label_type = QtWidgets.QLabel(self.centralwidget)
        self.label_type.setFont(font12)
        self.label_type.setStyleSheet("background-color: rgb(180, 241, 221);")
        self.horizontalLayout_3.addWidget(self.label_type)

        self.fp_type = QtWidgets.QComboBox(self.centralwidget)
        self.fp_type.setFont(font12)
        self.fp_type.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fp_type.addItem("trimf")
        self.fp_type.addItem("trapmf")
        self.fp_type.addItem("gaussmf")
        self.fp_type.addItem("gbellmf")
        self.fp_type.addItem("signmf")
        self.fp_type.addItem("dsigmf")
        self.fp_type.addItem("psigmf")
        self.fp_type.addItem("zmf")
        self.fp_type.addItem("smf")
        self.fp_type.addItem("pimf")
        self.horizontalLayout_3.addWidget(self.fp_type)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.label_parameters = QtWidgets.QLabel(self.centralwidget)
        self.label_parameters.setFont(font12)
        self.label_parameters.setStyleSheet("background-color: rgb(220, 255, 235);")
        self.label_parameters.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_7.addWidget(self.label_parameters)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()

        self.verticalLayout = QtWidgets.QVBoxLayout()

        self.label_a = QtWidgets.QLabel(self.centralwidget)
        self.label_a.setFont(font12)
        self.label_a.setStyleSheet("")
        self.label_a.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_a)

        self.param_a = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.param_a.setFont(font12)
        self.param_a.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.param_a.setMinimum(-10000000.0)
        self.param_a.setMaximum(10000000.0)
        self.param_a.setSingleStep(0.01)
        self.verticalLayout.addWidget(self.param_a)
        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.label_b = QtWidgets.QLabel(self.centralwidget)
        self.label_b.setFont(font12)
        self.label_b.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_2.addWidget(self.label_b)

        self.param_b = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.param_b.setFont(font12)
        self.param_b.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.param_b.setMinimum(-10000000.0)
        self.param_b.setMaximum(10000000.0)
        self.param_b.setSingleStep(0.01)
        self.param_b.setValue(0.01)
        self.verticalLayout_2.addWidget(self.param_b)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()

        self.label_c = QtWidgets.QLabel(self.centralwidget)
        self.label_c.setFont(font12)
        self.label_c.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.label_c)

        self.param_c = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.param_c.setFont(font12)
        self.param_c.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.param_c.setMinimum(-10000000.0)
        self.param_c.setMaximum(10000000.0)
        self.param_c.setSingleStep(0.01)
        self.param_c.setValue(0.02)
        self.verticalLayout_3.addWidget(self.param_c)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QtWidgets.QVBoxLayout()

        self.label_d = QtWidgets.QLabel(self.centralwidget)
        self.label_d.setFont(font12)
        self.label_d.setText("")
        self.label_d.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_4.addWidget(self.label_d)

        self.param_d = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.param_d.setFont(font12)
        self.param_d.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.param_d.setMinimum(-10000000.0)
        self.param_d.setMaximum(10000000.0)
        self.param_d.setSingleStep(0.01)
        self.param_d.setValue(0.03)
        self.verticalLayout_4.addWidget(self.param_d)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.addLayout(self.verticalLayout_12)

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setFont(font12)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_7.addWidget(self.label_2)

        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setContentsMargins(-1, 0, -1, -1)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setFont(font12)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_14.addWidget(self.label_3)

        self.fromValue = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.fromValue.setFont(font12)
        self.fromValue.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fromValue.setMinimum(-10000000.0)
        self.fromValue.setMaximum(10000000.0)
        self.verticalLayout_14.addWidget(self.fromValue)
        self.horizontalLayout_7.addLayout(self.verticalLayout_14)

        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setContentsMargins(-1, 0, -1, -1)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setFont(font12)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_16.addWidget(self.label_4)

        self.toValue = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.toValue.setFont(font12)
        self.toValue.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.toValue.setMinimum(-10000000.0)
        self.toValue.setMaximum(10000000.0)
        self.verticalLayout_16.addWidget(self.toValue)
        self.horizontalLayout_7.addLayout(self.verticalLayout_16)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setContentsMargins(-1, 0, -1, -1)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setFont(font12)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_17.addWidget(self.label_5)

        self.points = QtWidgets.QSpinBox(self.centralwidget)
        self.points.setFont(font12)
        self.points.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.points.setMinimum(20)
        self.points.setMaximum(2000)
        self.points.setValue(300)
        self.verticalLayout_17.addWidget(self.points)
        self.horizontalLayout_7.addLayout(self.verticalLayout_17)
    
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.verticalLayout_5 = QtWidgets.QVBoxLayout()

        self.label_name_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_name_2.setFont(font12)
        self.label_name_2.setStyleSheet("background-color: rgb(220, 255, 235);")
        self.label_name_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name_2.setWordWrap(True)
        self.verticalLayout_5.addWidget(self.label_name_2)

        self.new_fuzzy_set_name = QtWidgets.QLineEdit(self.centralwidget)
        self.new_fuzzy_set_name.setFont(font12)
        self.new_fuzzy_set_name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_5.addWidget(self.new_fuzzy_set_name)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout)

        self.verticalLayout_6 = QtWidgets.QVBoxLayout()

        self.label_operations = QtWidgets.QLabel(self.centralwidget)
        self.label_operations.setFont(font12)
        self.label_operations.setStyleSheet("background-color: rgb(220, 255, 235);")
        self.label_operations.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_6.addWidget(self.label_operations)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(7)

        self.addiction_button = QtWidgets.QToolButton(self.centralwidget)
        self.addiction_button.setMinimumSize(QtCore.QSize(100, 55))
        self.addiction_button.setFont(font10)
        self.addiction_button.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.horizontalLayout_5.addWidget(self.addiction_button)

        self.unification_button = QtWidgets.QToolButton(self.centralwidget)
        self.unification_button.setMinimumSize(QtCore.QSize(100, 55))
        self.unification_button.setFont(font10)
        self.unification_button.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.horizontalLayout_5.addWidget(self.unification_button)

        self.intersection_button = QtWidgets.QToolButton(self.centralwidget)
        self.intersection_button.setMinimumSize(QtCore.QSize(100, 55))
        self.intersection_button.setFont(font10)
        self.intersection_button.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.horizontalLayout_5.addWidget(self.intersection_button)

        self.difference_button = QtWidgets.QToolButton(self.centralwidget)
        self.difference_button.setMinimumSize(QtCore.QSize(100, 55))
        self.difference_button.setFont(font10)
        self.difference_button.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.horizontalLayout_5.addWidget(self.difference_button)

        self.symmetric_difference_button = QtWidgets.QToolButton(self.centralwidget)
        self.symmetric_difference_button.setMinimumSize(QtCore.QSize(100, 55))
        self.symmetric_difference_button.setFont(font10)
        self.symmetric_difference_button.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.horizontalLayout_5.addWidget(self.symmetric_difference_button)

        self.algebraic_unification_button = QtWidgets.QToolButton(self.centralwidget)
        self.algebraic_unification_button.setMinimumSize(QtCore.QSize(100, 55))
        self.algebraic_unification_button.setFont(font10)
        self.algebraic_unification_button.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.horizontalLayout_5.addWidget(self.algebraic_unification_button)

        self.algebraic_intersection_button = QtWidgets.QToolButton(self.centralwidget)
        self.algebraic_intersection_button.setMinimumSize(QtCore.QSize(100, 55))
        self.algebraic_intersection_button.setFont(font10)
        self.algebraic_intersection_button.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.horizontalLayout_5.addWidget(self.algebraic_intersection_button)

        self.boundary_unification_button = QtWidgets.QToolButton(self.centralwidget)
        self.boundary_unification_button.setMinimumSize(QtCore.QSize(100, 55))
        self.boundary_unification_button.setFont(font10)
        self.boundary_unification_button.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.horizontalLayout_5.addWidget(self.boundary_unification_button)

        self.boundary_intersection_button = QtWidgets.QToolButton(self.centralwidget)
        self.boundary_intersection_button.setMinimumSize(QtCore.QSize(100, 55))
        self.boundary_intersection_button.setFont(font10)
        self.boundary_intersection_button.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.horizontalLayout_5.addWidget(self.boundary_intersection_button)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.verticalLayout_13.addLayout(self.verticalLayout_8)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1441, 26))

        self.menu = QtWidgets.QMenu(self.menuBar)

        MainWindow.setMenuBar(self.menuBar)

        self.action = QtWidgets.QAction(MainWindow)

        self.action_2 = QtWidgets.QAction(MainWindow)

        self.action_3 = QtWidgets.QAction(MainWindow)

        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Operations_Class()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
