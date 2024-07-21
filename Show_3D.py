from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
import sys


class Show_3D_Class(object):
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Отображение поверхности нечёткого вывода"))
        self.label_operation.setText(_translate("MainWindow", "Выберите соответствующие операции:"))
        self.intersection_label.setText(_translate("MainWindow", "для пересечения:"))
        self.implication_label.setText(_translate("MainWindow", "для импликации:"))
        self.accumulation_label.setText(_translate("MainWindow", "для аккумуляции:"))
        self.points_label.setText(_translate("MainWindow", "Количество точек (min=10, max=30):"))
        self.zadaite_points.setText(_translate("MainWindow", "Задайте количество точек:"))
        self.show_3D_button.setText(_translate("MainWindow", "Отобразить"))
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
        self.centralwidget = QWidget(MainWindow)

        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)

        self.verticalLayout_lingvars = QVBoxLayout()

        self.verticalLayout = QVBoxLayout()

        self.verticalLayout.addLayout(self.verticalLayout_lingvars)
        self.label_operation = QLabel(self.centralwidget)
        self.label_operation.setFont(font12)
        self.label_operation.setStyleSheet("background-color: rgb(180, 241, 221);")
        self.label_operation.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_operation)

        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)

        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)

        self.intersection_label = QLabel(self.centralwidget)
        self.intersection_label.setFont(font12)
        self.intersection_label.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.intersection_label.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.intersection_label)

        self.intersection_combobox = QComboBox(self.centralwidget)
        self.intersection_combobox.setFont(font12)
        self.intersection_combobox.addItems(['prod', 'min'])
        self.intersection_combobox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_3.addWidget(self.intersection_combobox)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)

        self.implication_label = QLabel(self.centralwidget)
        self.implication_label.setFont(font12)
        self.implication_label.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.implication_label.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_4.addWidget(self.implication_label)

        self.implication_combobox = QComboBox(self.centralwidget)
        self.implication_combobox.setFont(font12)
        self.implication_combobox.addItems(['prod', 'min'])
        self.implication_combobox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_4.addWidget(self.implication_combobox)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)

        self.accumulation_label = QLabel(self.centralwidget)
        self.accumulation_label.setFont(font12)
        self.accumulation_label.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.accumulation_label.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_5.addWidget(self.accumulation_label)

        self.accumulation_combobox = QComboBox(self.centralwidget)
        self.accumulation_combobox.setFont(font12)
        self.accumulation_combobox.addItems(['sum', 'max'])
        self.accumulation_combobox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_5.addWidget(self.accumulation_combobox)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.zadaite_points = QLabel(self.centralwidget)
        self.zadaite_points.setFont(font12)
        self.zadaite_points.setStyleSheet("background-color: rgb(180, 241, 221);")
        self.zadaite_points.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.zadaite_points)

        self.horizontalLayout_5 = QHBoxLayout()

        self.points_label = QLabel(self.centralwidget)
        self.points_label.setFont(font12)
        self.points_label.setStyleSheet("background-color: rgb(0, 229, 168);")
        self.points_label.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_5.addWidget(self.points_label)

        self.points_spinbox = QSpinBox(self.centralwidget)
        self.points_spinbox.setFont(font12)
        self.points_spinbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.points_spinbox.setAlignment(QtCore.Qt.AlignCenter)
        self.points_spinbox.setMinimum(10)
        self.points_spinbox.setMaximum(30)
        self.horizontalLayout_5.addWidget(self.points_spinbox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()

        self.show_3D_button = QPushButton(self.centralwidget)
        self.show_3D_button.setFont(font12)
        self.show_3D_button.setStyleSheet("background-color: rgb(220, 255, 235);")
        self.horizontalLayout.addWidget(self.show_3D_button)

        self.cancel_button = QPushButton(self.centralwidget)
        self.cancel_button.setFont(font12)
        self.cancel_button.setStyleSheet("background-color: rgb(180, 241, 221);")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_progress = QHBoxLayout()

        self.pbar = QProgressBar(self.centralwidget)
        self.pbar.setValue(0)
        self.horizontalLayout_progress.addWidget(self.pbar)
        self.verticalLayout.addLayout(self.horizontalLayout_progress)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Show_3D_Class()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())