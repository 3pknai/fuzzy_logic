import sys 
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from fuzzy_operations import *
import Main_menu
import Operations
from fuzzy_logic import *
import themain, ling_var, ShowFunc, rules, Show_3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import shutil
import os

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

class Main_menu_dialog(QMainWindow, Main_menu.Main_menu_Class):
    '''Класс главного окна.'''
    def __init__(self):
        super().__init__()
        self.ui = Main_menu.Main_menu_Class()
        os.chdir(sys._MEIPASS)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.ui.setupUi(self)

        #connect'ы
        self.ui.operations_button.clicked.connect(self.operations_button_clicked)
        self.ui.lp_button.clicked.connect(self.lp_button_clicked)
        self.ui.download_operations.clicked.connect(self.instruction_clicked_1)
        self.ui.download_lp.clicked.connect(self.instruction_clicked_2)
        self.ui.button_info.clicked.connect(self.info)

    def info(self):
        #QMessageBox.about(self, 'Информация', 'Данную программу разработали:\nБоков Святослав Дмитриевич (slavabokov2004@mail.ru)\nМатохин Илья Георгиевич (matokhin.iklya@yandex.ru)\nв рамках летней практики 2024 г.\nРуководитель проекта: Кизим Алексей Владимирович')
        QMessageBox.about(self, 'Информация', 'Данную программу разработали:\nБоков Святослав Дмитриевич (slavabokov2004@mail.ru)\nМатохин Илья Георгиевич (matokhin.ilya@yandex.ru)\nв рамках летней практики 2024 г.\nРуководитель проекта: Кизим Алексей Владимирович')

    def operations_button_clicked(self):
        '''Метод, который активируется при нажатии на кнопку "Операции над нечёткими множествами".'''
        self.operations_window = Operations_dialog(self)
        self.operations_window.show()
        self.setEnabled(False)

    def lp_button_clicked(self):
        '''Метод, который активируется при нажатии на кнопку "Моделирование нечётких систем".'''
        ling_var_in.clear()
        ling_var_out.clear()
        all_rules.clear()

        self.main_dialog_window = The_Main_dialog(self)
        self.main_dialog_window.show()
        self.setEnabled(False)

    def instruction_clicked_1(self):
        folder = QFileDialog.getExistingDirectory(self, "Выберите директорию для сохранения инструкции", QtCore.QDir.homePath())
        if folder:
            shutil.copy2(os.getcwd() + "/operations_on_fuzzy_sets_instruction.pdf", folder + "/operations_on_fuzzy_sets_instruction.pdf")


    def instruction_clicked_2(self):
        folder = QFileDialog.getExistingDirectory(self, "Выберите директорию для сохранения инструкции", QtCore.QDir.homePath())
        if folder:
            shutil.copy2(os.getcwd() + "/modeling_of_fuzzy_systems_instruction.pdf", folder + "/modeling_of_fuzzy_systems_instruction.pdf")


class Operations_dialog(QMainWindow, Operations.Operations_Class):
    def __init__(self, main_menu):
        super().__init__()
        self.ui = Operations.Operations_Class()
        os.chdir(sys._MEIPASS)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.ui.setupUi(self)
        self.main_menu = main_menu

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.ui.gridLayout.addWidget(self.canvas, 0, 2, 1, 1)

        self.fp_type_changed()
        self.fromValue_changed()

        for fs in fuzzy_sets:
            self.ui.fuzzy_sets_list.addItem(fs.name)
        
        self.filename = ""

        self.ui.fp_type.currentTextChanged.connect(self.fp_type_changed)
        self.ui.param_a.valueChanged.connect(self.param_value_changed)
        self.ui.param_b.valueChanged.connect(self.param_value_changed)
        self.ui.param_c.valueChanged.connect(self.param_value_changed)
        self.ui.param_d.valueChanged.connect(self.param_value_changed)
        self.ui.fromValue.valueChanged.connect(self.fromValue_changed)
        self.ui.toValue.valueChanged.connect(self.toValue_changed)
        self.ui.points.valueChanged.connect(self.points_changed)
        self.ui.add_button.clicked.connect(self.add_button_clicked)
        self.ui.change_button.clicked.connect(self.change_button_clicked)
        self.ui.remove_button.clicked.connect(self.remove_button_clicked)
        self.ui.fuzzy_sets_list.itemClicked.connect(self.fuzzy_list_item_clicked)

        self.ui.addiction_button.clicked.connect(self.addiction_button_clicked)
        self.ui.difference_button.clicked.connect(self.difference_button_clicked)
        self.ui.symmetric_difference_button.clicked.connect(self.symmetric_difference_button_clicked)
        self.ui.unification_button.clicked.connect(self.unification_button_clicked)
        self.ui.intersection_button.clicked.connect(self.intersection_button_clicked)
        self.ui.algebraic_intersection_button.clicked.connect(self.algebraic_intersection_button_clicked)
        self.ui.algebraic_unification_button.clicked.connect(self.algebraic_unification_button_clicked)
        self.ui.boundary_intersection_button.clicked.connect(self.boundary_intersection_button_clicked)
        self.ui.boundary_unification_button.clicked.connect(self.boundary_unification_button_clicked)

        self.ui.action.triggered.connect(self.openfile)
        self.ui.action_2.triggered.connect(self.savefile)
        self.ui.action_3.triggered.connect(self.saveasfile)

    def openfile(self):
        '''Метод, который срабатывает при нажатии на кнопку "Открыть".'''
        try:
            self.filename, _ = QFileDialog.getOpenFileName(self, "Open File", QtCore.QDir.homePath(), "Text Files (*.txt);;All Files (*)")
            if self.filename:
                self.ui.fuzzy_sets_list.clear()
                self.ui.fuzzy_set_name.clear()
                self.ui.new_fuzzy_set_name.clear()
                fuzzy_sets.clear()
                self.fuzzy_list_item_clicked()

                with open(self.filename, encoding="utf-8") as f:
                    count = int(f.readline().split("=")[1])
                    names = []
                    info = []
                    for _ in range(count):
                        names += [f.readline().strip()]
                    for _ in range(count):
                        info += [f.readline().strip()]
                    for n, i in zip(names, info):
                        self.ui.fuzzy_sets_list.addItem(n)
                        if i[:2] == "fs":
                            type, params = i.split(":")
                            fs = fuzzy_set(n, type[3:], [float(x) for x in params.split()])
                            fuzzy_sets.append(fs)
                        elif i[:2] == "fo":
                            fo = fuzzy_operationship(n, fuzzy_set("", "trimf", [1, 2, 3]))
                            fo.set_info(i[3:])
                            fuzzy_sets.append(fo)
        except:
            QMessageBox.about(self, '!', 'Данный файл не совместим с текущим окном.')

    def savefile(self):
        '''Метод, который срабатывает при нажатии на кнопку "Сохранить".'''
        if self.filename == "":
            self.saveasfile()
        else:
            self.saveasfile(True) 

    def saveasfile(self, file_dialog=False):
        '''Метод, который срабатывает при нажатии на кнопку "Сохранить как..".'''
        if not file_dialog:
            self.filename, _ = QFileDialog.getSaveFileName(self, "Save File", QtCore.QDir.homePath(), "Text Files (*.txt);;All Files (*)")
        if self.filename:
            names = [fs.name for fs in fuzzy_sets]
            fp_view = []
            for fs in fuzzy_sets:
                if 'fuzzy_set' in str(type(fs)):
                    fp_view.append(f"fs={fs.type}:{fs.get_params()}")
                elif 'fuzzy_operationship' in str(type(fs)):
                    fp_view.append(f"fo={fs.get_info()}")
            with open(self.filename, "w", encoding="utf-8") as f:
                f.write(f"count={len(fuzzy_sets)}\n")
                for name in names:
                    f.write(name + "\n")
                for fp in fp_view:
                    f.write(fp + "\n")

    def fp_type_changed(self):
        _translate = QtCore.QCoreApplication.translate

        '''Метод, который в зависимости от типа ФП делает доступными определённое количество параметов.'''
        if self.ui.fp_type.currentText() == 'trimf':
            self.ui.param_c.setEnabled(True)
            self.ui.param_d.setEnabled(False)
            self.ui.param_d.setValue(0.03)

            self.ui.label_a.setText(_translate("MainWindow", "a:"))
            self.ui.label_b.setText(_translate("MainWindow", "b:"))
            self.ui.label_c.setText(_translate("MainWindow", "c:"))
            self.ui.label_d.setText(_translate("MainWindow", ""))

        elif self.ui.fp_type.currentText() == 'trapmf':
            self.ui.param_c.setEnabled(True)
            self.ui.param_d.setEnabled(True)

            self.ui.label_a.setText(_translate("MainWindow", "a:"))
            self.ui.label_b.setText(_translate("MainWindow", "b:"))
            self.ui.label_c.setText(_translate("MainWindow", "c:"))
            self.ui.label_d.setText(_translate("MainWindow", "d:"))

        elif self.ui.fp_type.currentText() == 'gaussmf':
            self.ui.param_c.setEnabled(False)
            self.ui.param_c.setValue(0.02)
            self.ui.param_d.setEnabled(False)
            self.ui.param_d.setValue(0.03)

            self.ui.label_a.setText(_translate("MainWindow", "σ:"))
            self.ui.label_b.setText(_translate("MainWindow", "c:"))
            self.ui.label_c.setText(_translate("MainWindow", ""))
            self.ui.label_d.setText(_translate("MainWindow", ""))

        elif self.ui.fp_type.currentText() == 'gbellmf':
            self.ui.param_c.setEnabled(True)
            self.ui.param_d.setEnabled(False)
            self.ui.param_d.setValue(0.03)

            self.ui.label_a.setText(_translate("MainWindow", "a:"))
            self.ui.label_b.setText(_translate("MainWindow", "b:"))
            self.ui.label_c.setText(_translate("MainWindow", "c:"))
            self.ui.label_d.setText(_translate("MainWindow", ""))

        elif self.ui.fp_type.currentText() == 'signmf':
            self.ui.param_c.setEnabled(False)
            self.ui.param_c.setValue(0.02)
            self.ui.param_d.setEnabled(False)
            self.ui.param_d.setValue(0.03)

            self.ui.label_a.setText(_translate("MainWindow", "a:"))
            self.ui.label_b.setText(_translate("MainWindow", "c:"))
            self.ui.label_c.setText(_translate("MainWindow", ""))
            self.ui.label_d.setText(_translate("MainWindow", ""))

        elif self.ui.fp_type.currentText() == 'dsigmf':
            self.ui.param_c.setEnabled(True)
            self.ui.param_d.setEnabled(True)

            self.ui.label_a.setText(_translate("MainWindow", "a₁:"))
            self.ui.label_b.setText(_translate("MainWindow", "c₁:"))
            self.ui.label_c.setText(_translate("MainWindow", "a₂:"))
            self.ui.label_d.setText(_translate("MainWindow", "c₂:"))

        elif self.ui.fp_type.currentText() == 'psigmf':
            self.ui.param_c.setEnabled(True)
            self.ui.param_d.setEnabled(True)

            self.ui.label_a.setText(_translate("MainWindow", "a₁:"))
            self.ui.label_b.setText(_translate("MainWindow", "c₁:"))
            self.ui.label_c.setText(_translate("MainWindow", "a₂:"))
            self.ui.label_d.setText(_translate("MainWindow", "c₂:"))

        elif self.ui.fp_type.currentText() == 'zmf':
            self.ui.param_c.setEnabled(False)
            self.ui.param_c.setValue(0.02)
            self.ui.param_d.setEnabled(False)
            self.ui.param_d.setValue(0.03)

            self.ui.label_a.setText(_translate("MainWindow", "a:"))
            self.ui.label_b.setText(_translate("MainWindow", "b:"))
            self.ui.label_c.setText(_translate("MainWindow", ""))
            self.ui.label_d.setText(_translate("MainWindow", ""))

        elif self.ui.fp_type.currentText() == 'smf':
            self.ui.param_c.setEnabled(False)
            self.ui.param_c.setValue(0.02)
            self.ui.param_d.setEnabled(False)
            self.ui.param_d.setValue(0.03)

            self.ui.label_a.setText(_translate("MainWindow", "a:"))
            self.ui.label_b.setText(_translate("MainWindow", "b:"))
            self.ui.label_c.setText(_translate("MainWindow", ""))
            self.ui.label_d.setText(_translate("MainWindow", ""))

        elif self.ui.fp_type.currentText() == 'pimf':
            self.ui.param_c.setEnabled(True)
            self.ui.param_d.setEnabled(True)

            self.ui.label_a.setText(_translate("MainWindow", "a:"))
            self.ui.label_b.setText(_translate("MainWindow", "b:"))
            self.ui.label_c.setText(_translate("MainWindow", "с:"))
            self.ui.label_d.setText(_translate("MainWindow", "d:"))

    def param_value_changed(self):
        '''Метод, который реагирует на изменения в параметрах с учётом условия, что a < b < c < d.'''
        if self.ui.fp_type.currentText() in ["trimf", "trapmf", "zmf", "smf", "pimf"]:
            self.ui.param_b.setMinimum(self.ui.param_a.value()+0.01)
            self.ui.param_c.setMinimum(self.ui.param_b.value()+0.01)
            self.ui.param_d.setMinimum(self.ui.param_c.value()+0.01)
        else:
            self.ui.param_b.setMinimum(-10000000.0)
            self.ui.param_c.setMinimum(-10000000.0)
            self.ui.param_d.setMinimum(-10000000.0)

    def fromValue_changed(self):
        self.ui.toValue.setMinimum(self.ui.fromValue.value()+1)
        self.fuzzy_list_item_clicked()

    def toValue_changed(self):
        self.fuzzy_list_item_clicked()

    def points_changed(self):
        self.fuzzy_list_item_clicked()

    def add_button_clicked(self):
        if self.ui.fuzzy_set_name.text() == "":
            QMessageBox.about(self, '!', 'Созданное нечёткое множество не имеет названия.')
        else:
            if self.ui.fuzzy_set_name.text() in [fs.name for fs in fuzzy_sets]:
                QMessageBox.about(self, '!', 'Нечёткое множество с таким названием уже существует!')
            else:
                if self.ui.fp_type.currentText() == "gaussmf" and self.ui.param_a.value() == 0:
                    QMessageBox.about(self, '!', 'Недопустимое значение параметра!')
                else:
                    p = [self.ui.param_a.value(), self.ui.param_b.value(), self.ui.param_c.value(), self.ui.param_d.value()]
                    if self.ui.fp_type.currentText() in ["trapmf", "dsigmf", "psigmf", "pimf"]:
                        pass
                    elif self.ui.fp_type.currentText() in ["trimf", "gbellmf"]:
                        p = p[:3]
                    else:
                        p = p[:2]
                    fuzzy_sets.append(fuzzy_set(self.ui.fuzzy_set_name.text(), self.ui.fp_type.currentText(), p))
                    self.ui.fuzzy_sets_list.addItem(self.ui.fuzzy_set_name.text())
                    self.ui.fuzzy_sets_list.setCurrentRow(len(fuzzy_sets)-1)
                    self.fuzzy_list_item_clicked()

    def change_button_clicked(self):
        if self.ui.fuzzy_set_name == '':
            QMessageBox.about(self, '!', 'Необходимо название нечёткого множества')
        else:
            ci = self.ui.fuzzy_sets_list.currentRow()
            if ci != -1:
                if len(self.ui.fuzzy_sets_list.selectedItems()) > 1:
                    QMessageBox.about(self, '!', 'Необходимо выбрать одно нечёткое множество для изменения!')
                else:
                    if "fuzzy_operationship" in str(type(fuzzy_sets[ci])):
                        QMessageBox.about(self, '!', 'Невозможно изменить данное нечёткое множество, так как оно было образовано в результате применения операций над другими нечёткими множествами!')
                    else:
                        if self.ui.fuzzy_set_name.text() in ([fs.name for fs in fuzzy_sets][:ci] + [fs.name for fs in fuzzy_sets][ci+1:]):
                            QMessageBox.about(self, '!', 'Нечёткое множество с таким названием уже существует!')
                        else:
                            if self.ui.fp_type.currentText() == "gaussmf" and self.ui.param_a.value() == 0:
                                QMessageBox.about(self, '!', 'Недопустимое значение параметра!')
                            else:
                                p = [self.ui.param_a.value(), self.ui.param_b.value(), self.ui.param_c.value(), self.ui.param_d.value()]
                                if self.ui.fp_type.currentText() in ["trapmf", "dsigmf", "psigmf", "pimf"]:
                                    pass
                                elif self.ui.fp_type.currentText() in ["trimf", "gbellmf"]:
                                    p = p[:3]
                                else:
                                    p = p[:2]
                                fuzzy_sets[ci] = fuzzy_set(self.ui.fuzzy_set_name.text(), self.ui.fp_type.currentText(), p)
                                self.ui.fuzzy_sets_list.takeItem(ci)
                                self.ui.fuzzy_sets_list.insertItem(ci, self.ui.fuzzy_set_name.text())
                                self.ui.fuzzy_sets_list.setCurrentRow(ci)
                                self.fuzzy_list_item_clicked()
            else:
                QMessageBox.about(self, '!', 'Необходимо выбрать одно нечёткое множество для изменения!')

    def remove_button_clicked(self):
        ci = self.ui.fuzzy_sets_list.currentRow()
        if ci != -1:
            if len(self.ui.fuzzy_sets_list.selectedItems()) > 1:
                QMessageBox.about(self, '!', 'Необходимо выбрать одно нечёткое множество для удаления!')
            else:
                button = QMessageBox.question(self, "?", 'Вы точно уверены в том, что хотите удалить это нечёткое множество?')
                if button == QMessageBox.Yes:
                    del fuzzy_sets[ci]
                    self.ui.fuzzy_sets_list.takeItem(ci)
                    self.fuzzy_list_item_clicked()
            self.ui.fuzzy_sets_list.setCurrentRow(-1)
        else:
            QMessageBox.about(self, '!', 'Необходимо выбрать нечёткое множество для удаления!')

    def plot(self, x1, x2, count_of_point, fs_list):
        step = (x2 - x1) / count_of_point
        x = np.arange(x1, x2+step/2, step)

        self.figure.clear()

        ax = self.figure.add_subplot(1, 1, 1)
        ax.set_xlim(x1, x2)
        ax.set_ylim(-0.05, 1.05)

        if len(fs_list) == 1:
            ax.set_title(f"Нечёткое множество «{fs_list[0].name}»")
        elif len(fs_list) == 0:
            pass
        else:
            ax.set_title(f"Нечёткие множества")

        for fs in fs_list:
            y = fs.get_value(x)
            ax.plot(x, y, label=f"{fs.name}")
        ax.legend(loc="upper right", facecolor='lightgrey', labelcolor='black')
        ax.grid(True)

        self.canvas.draw()

    def fuzzy_list_item_clicked(self):
        if self.ui.fuzzy_sets_list.currentRow() != -1:
            fs = fuzzy_sets[self.ui.fuzzy_sets_list.currentRow()]
            self.ui.fuzzy_set_name.setText(fs.name)

            if "fuzzy_set" in str(type(fs)):
                self.ui.fp_type.setCurrentText(fs.type)
                if fs.type in ["trimf", "gbellmf"]:
                    self.ui.param_a.setValue(fs.a)
                    self.ui.param_b.setValue(fs.b)
                    self.ui.param_c.setValue(fs.c)
                elif fs.type in ["gaussmf"]:
                    self.ui.param_a.setValue(fs.s)
                    self.ui.param_b.setValue(fs.c)
                elif fs.type in ["signmf"]:
                    self.ui.param_a.setValue(fs.a)
                    self.ui.param_b.setValue(fs.c)
                elif fs.type in ["trapmf", "pimf"]:
                    self.ui.param_a.setValue(fs.a)
                    self.ui.param_b.setValue(fs.b)
                    self.ui.param_c.setValue(fs.c)
                    self.ui.param_d.setValue(fs.d)
                elif fs.type in ["dsigmf", "psigmf"]:
                    self.ui.param_a.setValue(fs.a1)
                    self.ui.param_b.setValue(fs.c1)
                    self.ui.param_c.setValue(fs.a2)
                    self.ui.param_d.setValue(fs.c2)
                elif fs.type in ["zmf", "smf"]:
                    self.ui.param_a.setValue(fs.a)
                    self.ui.param_b.setValue(fs.b)
            
            inds = [item.text() for item in self.ui.fuzzy_sets_list.selectedItems()]
            elems = [fs for fs in fuzzy_sets if fs.name in inds]
            self.plot(self.ui.fromValue.value(), self.ui.toValue.value(), self.ui.points.value(), elems)
        else:
            self.figure.clear()
            ax = self.figure.add_subplot(1, 1, 1)
            ax.set_xlim(self.ui.fromValue.value(), self.ui.toValue.value())
            ax.set_ylim(-0.05, 1.05)
            ax.grid(True)
            self.canvas.draw()

        inds = self.ui.fuzzy_sets_list.selectedItems()
        if len(inds) == 1:
            self.ui.addiction_button.setEnabled(True)
            self.ui.difference_button.setEnabled(False)
            self.ui.symmetric_difference_button.setEnabled(False)
            self.ui.unification_button.setEnabled(False)
            self.ui.intersection_button.setEnabled(False)
            self.ui.algebraic_intersection_button.setEnabled(False)
            self.ui.algebraic_unification_button.setEnabled(False)
            self.ui.boundary_intersection_button.setEnabled(False)
            self.ui.boundary_unification_button.setEnabled(False)
        elif len(inds) == 2:
            self.ui.addiction_button.setEnabled(False)
            self.ui.difference_button.setEnabled(True)
            self.ui.symmetric_difference_button.setEnabled(True)
            self.ui.unification_button.setEnabled(True)
            self.ui.intersection_button.setEnabled(True)
            self.ui.algebraic_intersection_button.setEnabled(True)
            self.ui.algebraic_unification_button.setEnabled(True)
            self.ui.boundary_intersection_button.setEnabled(True)
            self.ui.boundary_unification_button.setEnabled(True)
        else:
            self.ui.addiction_button.setEnabled(False)
            self.ui.difference_button.setEnabled(False)
            self.ui.symmetric_difference_button.setEnabled(False)
            self.ui.unification_button.setEnabled(False)
            self.ui.intersection_button.setEnabled(False)
            self.ui.algebraic_intersection_button.setEnabled(False)
            self.ui.algebraic_unification_button.setEnabled(False)
            self.ui.boundary_intersection_button.setEnabled(False)
            self.ui.boundary_unification_button.setEnabled(False)

    def addiction_button_clicked(self):
        self.operation("add")
    def difference_button_clicked(self):
        self.operation("diff")
    def symmetric_difference_button_clicked(self):
        self.operation("s_diff")
    def unification_button_clicked(self):
        self.operation("unif")
    def intersection_button_clicked(self):
        self.operation("intr")
    def algebraic_intersection_button_clicked(self):
        self.operation("a_intr")
    def algebraic_unification_button_clicked(self):
        self.operation("a_unif")
    def boundary_intersection_button_clicked(self):
        self.operation("b_intr")
    def boundary_unification_button_clicked(self):
        self.operation("b_unif")
        
    def operation(self, func):
        #["unif", "intr", "add", "diff", "s_diff", "a_unif", "a_intr", "b_unif", "b_intr"]
        if self.ui.new_fuzzy_set_name.text() == "":
            QMessageBox.about(self, '!', 'Созданное нечёткое множество не имеет названия.')
        else:
            if self.ui.new_fuzzy_set_name.text() in [fs.name for fs in fuzzy_sets]:
                QMessageBox.about(self, '!', 'Нечёткое множество с таким названием уже существует!')
            else:
                if func == "add":
                    name = self.ui.new_fuzzy_set_name.text()
                    inds = [item.text() for item in self.ui.fuzzy_sets_list.selectedItems()]
                    elems = [fs for fs in fuzzy_sets if fs.name in inds]
                    fo = fuzzy_operationship(name, fuzzy_set("", "const", [1]))
                    fo.add_operation(func, elems[0])
                    ap = True
                elif func == "diff":
                    fs1, fs2 = [item.text() for item in self.ui.fuzzy_sets_list.selectedItems()]
                    button = QMessageBox.question(self, "?", f'Выберите "Yes", если согласны выбрать {fs1} в качестве первого множества, а в качестве второго - {fs2}.\n' + \
                                                  f'Выберите "No" или закройте это окно, если согласны выбрать {fs2} в качестве первого множества, а в качестве второго - {fs1}.')
                    if button == QMessageBox.Yes:
                        name = self.ui.new_fuzzy_set_name.text()
                        inds = [item.text() for item in self.ui.fuzzy_sets_list.selectedItems()]
                        elems = [fs for fs in fuzzy_sets if fs.name in inds]
                        fo = fuzzy_operationship(name, elems[0])
                        fo.add_operation(func, elems[1])
                        ap = True
                    elif button == QMessageBox.No:
                        name = self.ui.new_fuzzy_set_name.text()
                        inds = [item.text() for item in self.ui.fuzzy_sets_list.selectedItems()]
                        elems = [fs for fs in fuzzy_sets if fs.name in inds]
                        fo = fuzzy_operationship(name, elems[1])
                        fo.add_operation(func, elems[0])
                        ap = True
                    else:
                        ap = False
                else:
                    name = self.ui.new_fuzzy_set_name.text()
                    inds = [item.text() for item in self.ui.fuzzy_sets_list.selectedItems()]
                    elems = [fs for fs in fuzzy_sets if fs.name in inds]
                    fo = fuzzy_operationship(name, elems[0])
                    fo.add_operation(func, elems[1])
                    ap = True
                if ap:
                    fuzzy_sets.append(fo)
                    self.ui.fuzzy_sets_list.addItem(name)
                    self.ui.fuzzy_sets_list.setCurrentRow(len(fuzzy_sets)-1)
                    self.fuzzy_list_item_clicked()

    def closeEvent(self, event):
        '''Метод, срабатывающий при закрытии окна и предоставляющий доступ к окну главного меню.'''
        self.main_menu.setEnabled(True)
        event.accept()


class The_Main_dialog(QMainWindow, themain.The_Main_Class):
    '''Класс окна моделирования нечётких систем'''
    def __init__(self, main_menu):
        super().__init__()
        os.chdir(sys._MEIPASS)
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        self.ui = themain.The_Main_Class()
        self.ui.setupUi(self)
        self.main_menu = main_menu

        self.filename = ""  # Название текущего файла

        # connect'ы
        self.ui.create_ling_var_in.clicked.connect(self.create_ling_var_in_clicked)
        self.ui.delete_ling_var_in.clicked.connect(self.delete_ling_var_in_clicked)
        self.ui.create_ling_var_out.clicked.connect(self.create_ling_var_out_clicked)
        self.ui.delete_ling_var_out.clicked.connect(self.delete_ling_var_out_clicked)
        self.ui.show_func_button.clicked.connect(self.show_func_clicked)
        self.ui.rules_button.clicked.connect(self.rules_clicked)
        self.ui.listView_in.itemDoubleClicked.connect(self.listView_in_itemdoubleclicked)
        self.ui.listView_out.itemDoubleClicked.connect(self.listView_out_itemdoubleclicked)
        self.ui.listView_in.itemChanged.connect(self.update_combobox_in)
        self.ui.listView_out.itemChanged.connect(self.update_combobox_out)
        self.ui.listView_in.itemClicked.connect(self.remove_cursor_from_listView_out)
        self.ui.listView_out.itemClicked.connect(self.remove_cursor_from_listView_in)
        self.ui.show_3d_button.clicked.connect(self.show_3d_button_clicked)
        self.ui.comboBox_first_in.currentTextChanged.connect(self.first_in_text_changed)
        self.ui.open_button.clicked.connect(self.open_file)
        self.ui.save_button.clicked.connect(self.save_file)
        self.ui.save_as_button.clicked.connect(self.save_as_file)

    def add_to_combobox_in(self):
        """Функция, которая добавляет элементы таблицы входных ЛП в spinbox'ы входных ЛП."""
        self.ui.comboBox_first_in.clear()
        self.ui.comboBox_second_in.clear()
        self.ui.comboBox_first_in.addItem('-')
        self.ui.comboBox_second_in.addItem('-')

        for i in range(self.ui.listView_in.count()):
            self.ui.comboBox_first_in.insertItem(i+1, self.ui.listView_in.item(i).text())
            self.ui.comboBox_second_in.insertItem(i+1, self.ui.listView_in.item(i).text())

    def add_to_combobox_out(self):
        """Функция, которая добавляет элементы таблицы выходных ЛП в spinbox'ы выходных ЛП."""
        self.ui.comboBox_out.clear()
        self.ui.comboBox_out.addItem('-')

        for i in range(self.ui.listView_out.count()):
            self.ui.comboBox_out.insertItem(i+1, self.ui.listView_out.item(i).text())

    def create_ling_var_in_clicked(self):
        '''Метод, который открывает окно для создания внешней ЛП при нажатии на кнопку "Создать"
         или при двойном нажатии на выбранную в таблице внешнюю ЛП.'''
        self.window2 = Ling_var_dialog(self, self.create_ling_var_in_clicked.__name__)
        self.window2.show()
        self.setEnabled(False)

    def delete_ling_var_in_clicked(self):
        '''Метод, который удаляет выбранную лингвистическую переменную в таблице входных ЛП.'''
        current_row = self.ui.listView_in.currentRow()
        if current_row != -1:
            list_rule = []
            for rule, op, weight in all_rules:
                list_rule.append([[tuple([x, y]) for x,y in rule], str(op), float(weight)])
            indexs_1 = [i for i in range(len(list_rule)) if  list_rule[i][0][current_row][0] != -1][::-1]
            indexs_2 = [i for i in range(len(list_rule)) if  list_rule[i][0][current_row][0] == -1]
            for i in indexs_2:
                del list_rule[i][0][current_row]
            for i in indexs_1:
                del list_rule[i]
            for i in range(len(list_rule)-1, 0, -1):
                x = ";".join([f"{x},{y}" for x, y in list_rule[i][0][:len(ling_var_in)-1]]) + ":" + list_rule[i][1]
                y = [";".join([f"{x},{y}" for x, y in list_rule[j][0][:len(ling_var_in)-1]]) + ":" + list_rule[j][1] for j in range(i)]
                if x in y:
                    del list_rule[i]
            if len(ling_var_in) - 1 == 1: # После удаления осталась одна ЛП
                for i in range(len(list_rule)-1, 0, -1):
                    x = ";".join([f"{x},{y}" for x, y in list_rule[i][0][:len(ling_var_in)-1]])
                    y = [";".join([f"{x},{y}" for x, y in list_rule[j][0][:len(ling_var_in)-1]]) for j in range(i)]
                    if x in y:
                        del list_rule[i]

            count = len(all_rules) - len(list_rule)
            msg = QMessageBox.question(self,"?", f"Вы действительно хотите удалить выбранную входную ЛП?\n \
            Данная ЛП будет удалена из всех существующих правил вывода (количество правил, которое будет удалено: \
            {count}).", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if msg == QMessageBox.Yes:
                indexs_1 = [i for i in range(len(all_rules)) if  all_rules[i][0][current_row][0] != -1][::-1]
                indexs_2 = [i for i in range(len(all_rules)) if  all_rules[i][0][current_row][0] == -1]
                for i in indexs_2:
                    del all_rules[i][0][current_row]
                for i in indexs_1:
                    del all_rules[i]
                for i in range(len(all_rules)-1, 0, -1):
                    x = ";".join([f"{x},{y}" for x, y in all_rules[i][0][:len(ling_var_in)-1]]) + ":" + all_rules[i][1]
                    y = [";".join([f"{x},{y}" for x, y in all_rules[j][0][:len(ling_var_in)-1]]) + ":" + all_rules[j][1] for j in range(i)]
                    if x in y:
                        del all_rules[i]
                if len(ling_var_in) - 1 == 1:
                    for i in range(len(all_rules)-1, 0, -1):
                        x = ";".join([f"{x},{y}" for x, y in all_rules[i][0][:len(ling_var_in)-1]])
                        y = [";".join([f"{x},{y}" for x, y in all_rules[j][0][:len(ling_var_in)-1]]) for j in range(i)]
                        if x in y:
                            del all_rules[i]

                del ling_var_in[current_row]
                self.ui.listView_in.takeItem(self.ui.listView_in.currentRow())
                self.add_to_combobox_in()

    def create_ling_var_out_clicked(self):
        '''Метод, который открывает окно для создания выходной ЛП при нажатии на кнопку "Создать"
         или при двойном нажатии на выбранную в таблице выходную ЛП.'''
        self.ui.window2 = Ling_var_dialog(self, self.create_ling_var_out_clicked.__name__)
        self.ui.window2.show()
        self.setEnabled(False)

    def delete_ling_var_out_clicked(self):
        '''Метод, который удаляет выбранную лингвистическую переменную в таблице выходных ЛП.'''
        current_row = self.ui.listView_out.currentRow()
        if current_row != -1:
            msg = QMessageBox.question(self,"?", "Вы действительно хотите удалить выбранную выходную ЛП?\n \
            Данная ЛП будет удалена из всех существующих правил вывода.", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if msg == QMessageBox.Yes:
                for i in range(len(all_rules)):
                    del all_rules[i][0][current_row+len(ling_var_in)]
                del ling_var_out[current_row]
                self.ui.listView_out.takeItem(self.ui.listView_out.currentRow())
                self.add_to_combobox_out()

    def show_func_clicked(self):
        '''Метод, который открывает окно для отображения графиков ФП определенной ЛП.'''
        self.ui.window3 = Show_Func_dialog(self, ling_var_in + ling_var_out)
        self.ui.window3.show()
        self.setEnabled(False)

    def rules_clicked(self):
        '''Метод, который при нажатии на кнопку "Редактор правил вывода" открывает окно редактора правил вывода.'''
        self.ui.window4 = Rules_dialog(self)
        self.ui.window4.show()
        self.setEnabled(False)

    def listView_in_itemdoubleclicked(self):
        '''Метод, который открывает окно для изменения лингвистической переменной при двойном нажатии на неё
        в таблице входных ЛП.'''
        curr_row = self.ui.listView_in.currentRow()
        self.ui.window2 = Ling_var_dialog(self, self.listView_in_itemdoubleclicked.__name__, ling_var_in[curr_row])
        self.ui.window2.show()
        self.setEnabled(False)

    def listView_out_itemdoubleclicked(self):
        '''Метод, который открывает окно для изменения лингвистической переменной при двойном нажатии на неё
        в таблице выходных ЛП.'''
        curr_row = self.ui.listView_out.currentRow()
        self.ui.window2 = Ling_var_dialog(self, self.listView_out_itemdoubleclicked.__name__, ling_var_out[curr_row])
        self.ui.window2.show()
        self.setEnabled(False)

    def update_combobox_in(self):
        '''Метод, который изменяет текущий список входных ЛП в ComboBox'ах в зависимости от создания/изменения/удаления
        входных ЛП.'''
        self.ui.comboBox_first_in.clear()
        self.ui.comboBox_second_in.clear()
        self.ui.comboBox_first_in.addItem('-')

        for i in range(self.ui.listView_in.count()):
            self.ui.comboBox_first_in.insertItem(i+1, self.ui.listView_in.item(i).text())
            self.ui.comboBox_second_in.insertItem(i+1, self.ui.listView_in.item(i).text())

    def update_combobox_out(self):
        '''Метод, который изменяет текущий список выходных ЛП в ComboBox'ах в зависимости от создания/изменения/удаления
        выходных ЛП.'''
        self.ui.comboBox_out.clear()
        self.ui.comboBox_out.addItem('-')

        for i in range(self.ui.listView_out.count()):
            self.ui.comboBox_out.insertItem(i+1, self.ui.listView_out.item(i).text())

    def remove_cursor_from_listView_out(self):
        '''Метод, который при переходе к другой таблице убирает курсор с элемента текущей.'''
        self.ui.listView_out.setCurrentRow(-1)

    def remove_cursor_from_listView_in(self):
        '''Метод, который при переходе к другой таблице убирает курсор с элемента текущей.'''
        self.ui.listView_in.setCurrentRow(-1)

    def show_3d_button_clicked(self):
        '''Метод, который при нажатии на кнопку "Отобразить поверхность нечёткого вывода выводит соответствующее окно.'''
        if self.ui.comboBox_first_in.currentText() == '-':
            QMessageBox.about(self, '!', "Для отображения поверхности нечёткого вывода не выбрана первая входная ЛП.")
        elif self.ui.comboBox_second_in.currentText() == '-':
            QMessageBox.about(self, '!', "Для отображения поверхности нечёткого вывода не выбрана вторая входная ЛП.")
        elif self.ui.comboBox_out.currentText() == '-':
            QMessageBox.about(self, '!', "Для отображения поверхности нечёткого вывода не выбрана выходная ЛП.")
        elif self.ui.comboBox_first_in.currentText() == self.ui.comboBox_second_in.currentText():
            QMessageBox.about(self, '!', "Первая и входная ЛП должны отличаться друг от друга.")
        else:
            self.ui.window3D = Show_3D_dialog(self, [self.ui.comboBox_first_in.currentText(), self.ui.comboBox_second_in.currentText()], self.ui.comboBox_out.currentText())
            self.ui.window3D.show()
            self.setEnabled(False)

    def changing_second_combobox(self):
        """Функция, которая удаляет текущие элементы из второго ComboBox'а и заполняет его новыми входными ЛП из
        ListView_in, не учитывая то ЛП, которое является элементом первого ComboBox'а."""
        for _ in range(self.ui.listView_in.count()):
            self.ui.comboBox_second_in.removeItem(1)
        for i in range(self.ui.listView_in.count()):
            if self.ui.listView_in.item(i).text() != self.ui.comboBox_first_in.currentText():
                self.ui.comboBox_second_in.addItem(self.ui.listView_in.item(i).text())

    def first_in_text_changed(self):
        '''Метод, который позволяет оставлять текущий текст первого и второго ComboBox'ов различными.'''
        if self.ui.comboBox_first_in.count() > 1:
            was_in_second = self.ui.comboBox_second_in.currentText()
            if self.ui.comboBox_second_in.currentText() == '-':
                self.changing_second_combobox()
            else:
                if self.ui.comboBox_first_in.currentText() == was_in_second:
                    self.changing_second_combobox()
                    self.ui.comboBox_second_in.setCurrentIndex(1)
                else:
                    self.changing_second_combobox()
                    self.ui.comboBox_second_in.setCurrentText(was_in_second)

    def save_file(self):
        '''Метод, который срабатывает при нажатии на кнопку "Сохранить".'''
        if self.filename == "":
            self.save_as_file()
        else:
            self.save_as_file(True)        

    def save_as_file(self, file_dialog=False):
        '''Метод, который срабатывает при нажатии на кнопку "Сохранить как..".'''
        if not file_dialog:
            self.filename, _ = QFileDialog.getSaveFileName(self, "Save File", QtCore.QDir.homePath(), "Text Files (*.txt);;All Files (*)")
        if self.filename:
            with open(self.filename, "w", encoding="utf-8") as f:
                f.write(f"""[General information]
NumInputs={len(ling_var_in)}
NumOutputs={len(ling_var_out)}
NumRules={len(all_rules)}""")                
                for i in range(len(ling_var_in)):
                    lp = ling_var_in[i]
                    f.write(f"""\n\n[Input{i}]
Name={lp.name}
Range={lp.x1lim} {lp.x2lim}
UnitOfMeasure={lp.unit_of_measure}
NumMFs={len(lp.terms)}
""" + "\n".join([f"MF{j}={lp.terms[j].name}:{lp.terms[j].type}:{lp.terms[j].get_params()}" for j in range(len(lp.terms))]))
                for i in range(len(ling_var_out)):
                    lp = ling_var_out[i]
                    f.write(f"""\n\n[Output{i}]
Name={lp.name}
Range={lp.x1lim} {lp.x2lim}
UnitOfMeasure={lp.unit_of_measure}
NumMFs={len(lp.terms)}
""" + "\n".join([f"MF{j}={lp.terms[j].name}:{lp.terms[j].type}:{lp.terms[j].get_params()}" for j in range(len(lp.terms))]))
                f.write("\n\n[Rules]\n")
                f.write("\n".join([f"{','.join([f"{term}:{not_op}" for term, not_op in rule])};{op};{weight}" for rule, op, weight in all_rules]))

    def open_file(self):
        try:
            '''Метод, который срабатывает при нажатии на кнопку "Открыть".'''
            self.filename, _ = QFileDialog.getOpenFileName(self, "Open File", QtCore.QDir.homePath(), "Text Files (*.txt);;All Files (*)")
            if self.filename:
                self.ui.comboBox_first_in.clear()
                self.ui.comboBox_second_in.clear()
                self.ui.listView_in.clear()
                self.ui.listView_out.clear()
                self.ui.comboBox_out.clear()
                self.ui.comboBox_first_in.addItem("-")
                self.ui.comboBox_second_in.addItem("-")
                self.ui.comboBox_out.addItem("-")
                with open(self.filename, encoding='UTF-8') as f:
                    ling_var_in.clear()
                    ling_var_out.clear()
                    all_rules.clear()

                    a = [x.rstrip() for x in f.readlines()]

                    # Считывание основной информации
                    n = int(a[1][10:]) # Количество входных ЛП
                    m = int(a[2][11:]) # Количество выходных ЛП
                    r = int(a[3][9:]) # Количество правил

                    i = 5
                    # Считывание входных ЛП
                    for _ in range(n):
                        name = a[i+1][5:]
                        x1lim, x2lim = (int(x) for x in ((a[i+2].split("="))[1]).split())
                        unit_of_measure = a[i+3][14:]
                        lp = Ling_var(name, x1lim, x2lim, unit_of_measure)
                        mfs = int(a[i+4][7])
                        for i in range(i+5, i+5+mfs):
                            s = a[i][a[i].find("=")+1:].split(":")
                            name = s[0]
                            type = s[1]
                            params = [float(x) for x in s[2].split()]
                            lp.add_term(name, type, params)
                        ling_var_in.append(lp)
                        self.ui.listView_in.addItem(lp.name)
                        self.ui.comboBox_first_in.addItem(lp.name)
                        self.ui.comboBox_second_in.addItem(lp.name)
                        i += 2

                    # Считывание выходных ЛП
                    for _ in range(m):
                        name = a[i+1][5:]
                        x1lim, x2lim = (int(x) for x in ((a[i+2].split("="))[1]).split())
                        unit_of_measure = a[i+3][14:]
                        lp = Ling_var(name, x1lim, x2lim, unit_of_measure)
                        mfs = int(a[i+4][7])
                        for i in range(i+5, i+5+mfs):
                            s = a[i][a[i].find("=")+1:].split(":")
                            name = s[0]
                            type = s[1]
                            params = [float(x) for x in s[2].split()]
                            lp.add_term(name, type, params)
                        ling_var_out.append(lp)
                        self.ui.listView_out.addItem(lp.name)
                        self.ui.comboBox_out.addItem(lp.name)
                        i += 2

                    # Считывание правил
                    for i in range(i+1, i+1+r):
                        s = a[i].split(";")
                        rule = [(int(term.split(":")[0]), int(term.split(":")[1]))for term in s[0].split(",")]
                        op = s[1]
                        weight = float(s[2])
                        all_rules.append([rule, op, weight])
        except:
            QMessageBox.about(self, '!', 'Данный файл не совместим с текущим окном.')

    def closeEvent(self, event):
        '''Метод, срабатывающий при закрытии окна и предоставляющий доступ к окну главного меню.'''
        self.main_menu.setEnabled(True)
        event.accept()


class Ling_var_dialog(QMainWindow, ling_var.Ling_Var_Class):
    '''Класс создания лингвистической переменной.'''
    def __init__(self, main_window, what_func, lp=False):
        super().__init__()
        os.chdir(sys._MEIPASS)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setupUi(self)
        self.main_window = main_window
        self.what_func = what_func # строка с названием функции в The_Main_Dialog, из которой создавалось окно

        # Значения по умолчанию
        self.param_d.setEnabled(False) # параметр d изначально не доступен.
        self.current_ling_var = ['', [0, 1], '', []] # [name - название, (0, 1) - диапазон, % - ед. изм, [[term_name, fp_type, params] - терм, ...]

        # Блок кода, который активируется в случае, если изменяем уже существующую ЛП
        if lp:
            self.delete_from_rules = True
            self.lp_name = lp.name # Запоминаем информацию о ЛП
            self.ling_var_name.setText(lp.name)
            self.current_ling_var[0] = self.ling_var_name.text()
            self.fromValue.setValue(lp.x1lim)
            self.toValue.setValue(lp.x2lim)

            self.current_ling_var[1] = [self.fromValue.value(), self.toValue.value()]
            self.unit_of_measure.setCurrentText(lp.unit_of_measure)
            self.current_ling_var[2] = self.unit_of_measure.currentText()

            for i in lp.terms:
                last_row = self.terms_table.rowCount()
                self.terms_table.setRowCount(last_row+1)
                self.terms_table.setItem(last_row, 0, QTableWidgetItem(i.name))
                self.terms_table.setItem(last_row, 1, QTableWidgetItem(i.type))
                self.terms_table.setItem(last_row, 2, QTableWidgetItem(i.get_params()))
                self.current_ling_var[3].append([i.name, i.type, [float(x) for x in i.get_params().split()]])
        else:
            self.delete_from_rules = False

        # connect'ы
        self.ling_var_name.textChanged.connect(self.ling_var_name_changed)
        self.fromValue.valueChanged.connect(self.from_value_changed)
        self.toValue.valueChanged.connect(self.to_value_changed)
        self.unit_of_measure.currentIndexChanged.connect(self.unit_of_measure_changed)
        self.fp_type.currentIndexChanged.connect(self.fp_type_changed)
        self.param_a.valueChanged.connect(self.param_value_changed)
        self.param_b.valueChanged.connect(self.param_value_changed)
        self.param_c.valueChanged.connect(self.param_value_changed)
        self.param_d.valueChanged.connect(self.param_value_changed)
        self.add_term.clicked.connect(self.add_term_clicked)
        self.terms_table.itemClicked.connect(self.terms_table_item_clicked)
        self.change_term.clicked.connect(self.change_term_clicked)
        self.delete_term.clicked.connect(self.delete_term_clicked)
        self.ling_var_OK.clicked.connect(self.ok_clicked)
        self.ling_var_cancel.clicked.connect(self.cancel_clicked)
        self.terms_table.itemDoubleClicked.connect(self.terms_table_itemdoubleclicked)

    def add_to_combobox_in(self):
        """Функция, которая добавляет элементы таблицы входных ЛП в combobox'ы входных ЛП."""
        self.main_window.ui.comboBox_first_in.clear()
        self.main_window.ui.comboBox_second_in.clear()
        self.main_window.ui.comboBox_first_in.addItem('-')
        self.main_window.ui.comboBox_second_in.addItem('-')

        for i in range(self.main_window.ui.listView_in.count()):
            self.main_window.ui.comboBox_first_in.insertItem(i+1, self.main_window.ui.listView_in.item(i).text())
            self.main_window.ui.comboBox_second_in.insertItem(i+1, self.main_window.ui.listView_in.item(i).text())

    def add_to_combobox_out(self):
        """Функция, которая добавляет элементы таблицы входных ЛП в combobox'ы выходных ЛП."""
        self.main_window.ui.comboBox_out.clear()
        self.main_window.ui.comboBox_out.addItem('-')
        for i in range(self.main_window.ui.listView_out.count()):
            self.main_window.ui.comboBox_out.insertItem(i+1, self.main_window.ui.listView_out.item(i).text())
    def ling_var_name_changed(self):
        '''Метод, который вносит в список свойств текущей ЛП её название, указанное в дочернем окне.'''
        self.current_ling_var[0] = self.ling_var_name.text()

    def from_value_changed(self):
        '''Метод, который устанавливает минимальное значение для максимального значения из диапазона равное
         значению минимального значения из диапазона + 1. Помимо того, данный метод вносит в список свойств
         текущей ЛП минимальное значение из диапазона, указанное в дочернем окне.'''
        self.toValue.setMinimum(self.fromValue.value()+1)
        self.current_ling_var[1][0] = self.fromValue.value()

    def to_value_changed(self):
        '''Метод, который вносит в список свойств текущей ЛП максимальное значение из диапазона,
        указанное в дочернем окне.'''
        self.current_ling_var[1][1] = self.toValue.value()

    def unit_of_measure_changed(self):
        '''Метод, который вносит в список свойств текущей ЛП единицы измерения, указанные в дочернем окне.'''
        self.current_ling_var[2] = self.unit_of_measure.currentText()

    def fp_type_changed(self):
        '''Метод, который в зависимости от типа ФП делает доступными определённое количество параметов.'''
        _translate = QtCore.QCoreApplication.translate
        if self.fp_type.currentText() == 'trimf':
            self.param_c.setEnabled(True)
            self.param_d.setEnabled(False)
            self.param_d.setValue(0.03)

            self.label_a.setText(_translate("MainWindow", "a:"))
            self.label_b.setText(_translate("MainWindow", "b:"))
            self.label_c.setText(_translate("MainWindow", "c:"))
            self.label_d.setText(_translate("MainWindow", ""))

        elif self.fp_type.currentText() == 'trapmf':
            self.param_c.setEnabled(True)
            self.param_d.setEnabled(True)

            self.label_a.setText(_translate("MainWindow", "a:"))
            self.label_b.setText(_translate("MainWindow", "b:"))
            self.label_c.setText(_translate("MainWindow", "c:"))
            self.label_d.setText(_translate("MainWindow", "d:"))

        elif self.fp_type.currentText() == 'gaussmf':
            self.param_c.setEnabled(False)
            self.param_c.setValue(0.02)
            self.param_d.setEnabled(False)
            self.param_d.setValue(0.03)

            self.label_a.setText(_translate("MainWindow", "σ:"))
            self.label_b.setText(_translate("MainWindow", "c:"))
            self.label_c.setText(_translate("MainWindow", ""))
            self.label_d.setText(_translate("MainWindow", ""))

        elif self.fp_type.currentText() == 'gbellmf':
            self.param_c.setEnabled(True)
            self.param_d.setEnabled(False)
            self.param_d.setValue(0.03)

            self.label_a.setText(_translate("MainWindow", "a:"))
            self.label_b.setText(_translate("MainWindow", "b:"))
            self.label_c.setText(_translate("MainWindow", "c:"))
            self.label_d.setText(_translate("MainWindow", ""))

        elif self.fp_type.currentText() == 'signmf':
            self.param_c.setEnabled(False)
            self.param_c.setValue(0.02)
            self.param_d.setEnabled(False)
            self.param_d.setValue(0.03)

            self.label_a.setText(_translate("MainWindow", "a:"))
            self.label_b.setText(_translate("MainWindow", "c:"))
            self.label_c.setText(_translate("MainWindow", ""))
            self.label_d.setText(_translate("MainWindow", ""))

        elif self.fp_type.currentText() == 'dsigmf':
            self.param_c.setEnabled(True)
            self.param_d.setEnabled(True)

            self.label_a.setText(_translate("MainWindow", "a₁:"))
            self.label_b.setText(_translate("MainWindow", "c₁:"))
            self.label_c.setText(_translate("MainWindow", "a₂:"))
            self.label_d.setText(_translate("MainWindow", "c₂:"))

        elif self.fp_type.currentText() == 'psigmf':
            self.param_c.setEnabled(True)
            self.param_d.setEnabled(True)

            self.label_a.setText(_translate("MainWindow", "a₁:"))
            self.label_b.setText(_translate("MainWindow", "c₁:"))
            self.label_c.setText(_translate("MainWindow", "a₂:"))
            self.label_d.setText(_translate("MainWindow", "c₂:"))

        elif self.fp_type.currentText() == 'zmf':
            self.param_c.setEnabled(False)
            self.param_c.setValue(0.02)
            self.param_d.setEnabled(False)
            self.param_d.setValue(0.03)

            self.label_a.setText(_translate("MainWindow", "a:"))
            self.label_b.setText(_translate("MainWindow", "b:"))
            self.label_c.setText(_translate("MainWindow", ""))
            self.label_d.setText(_translate("MainWindow", ""))

        elif self.fp_type.currentText() == 'smf':
            self.param_c.setEnabled(False)
            self.param_c.setValue(0.02)
            self.param_d.setEnabled(False)
            self.param_d.setValue(0.03)

            self.label_a.setText(_translate("MainWindow", "a:"))
            self.label_b.setText(_translate("MainWindow", "b:"))
            self.label_c.setText(_translate("MainWindow", ""))
            self.label_d.setText(_translate("MainWindow", ""))

        elif self.fp_type.currentText() == 'pimf':
            self.param_c.setEnabled(True)
            self.param_d.setEnabled(True)

            self.label_a.setText(_translate("MainWindow", "a:"))
            self.label_b.setText(_translate("MainWindow", "b:"))
            self.label_c.setText(_translate("MainWindow", "с:"))
            self.label_d.setText(_translate("MainWindow", "d:"))

    def param_value_changed(self):
        '''Метод, который реагирует на изменения в параметрах с учётом условия, что a < b < c < d.'''
        if self.fp_type.currentText() in ["trimf", "trapmf", "zmf", "smf", "pimf"]:
            self.param_b.setMinimum(self.param_a.value()+0.01)
            self.param_c.setMinimum(self.param_b.value()+0.01)
            self.param_d.setMinimum(self.param_c.value()+0.01)
        else:
            self.param_b.setMinimum(-10000000.0)
            self.param_c.setMinimum(-10000000.0)
            self.param_d.setMinimum(-10000000.0)
        
    def set_params(self, params):
        '''Функция, которая изменяет список "params", заполняя его определёнными параметрами
        в зависимости от выбранного типа ФП.'''
        a = round(self.param_a.value(), 2)
        b = round(self.param_b.value(), 2)
        c = round(self.param_c.value(), 2)
        d = round(self.param_d.value(), 2)
        if self.fp_type.currentText() in ('trapmf', 'dsigmf', 'psigmf', 'pimf'):
            params[:] = [a, b, c, d]
        elif self.fp_type.currentText() in ('trimf', 'gbellmf'):
            params[:] = [a, b, c]
        else:
            params[:] = [a, b]

    def terms_table_itemdoubleclicked(self):
        '''Метод, который срабатывает при двойном нажатии на элемент таблицы терм-множеств и отображает график терма.'''
        curr_row = self.terms_table.currentRow()
        name = self.terms_table.item(curr_row, 0).text()
        type = self.terms_table.item(curr_row, 1).text()
        params = [float(x) for x in self.terms_table.item(curr_row, 2).text().split()]
        x1lim = self.fromValue.value()
        x2lim = self.toValue.value()

        lp = Ling_var(self.ling_var_name.text(), x1lim, x2lim)
        lp.add_term(name, type, params)

        plt.close()
        fig = plt.figure(f"Терм «{name}»", figsize=(14, 8))
        ax = fig.add_subplot(1, 1, 1)
        lp.print(ax)
        plt.show()

    def add_term_clicked(self):
        '''Метод, который добавляет в таблицу терм-множеств заданный терм (название, тип ФП, параметры).'''
        params = []
        self.set_params(params)
        if self.term_name.text() == '':
            QMessageBox.about(self, "Недопустимое название терма.", "Введите корректное название терма, состоящее хотя бы из одного символа.")
        elif self.term_name.text() in [i[0] for i in self.current_ling_var[3]]:
            QMessageBox.about(self, "Недопустимый терм.", "Терм с таким названием уже находится в таблице терм-множеств.")
        else:
            last_row = self.terms_table.rowCount()
            self.terms_table.setRowCount(last_row+1)
            self.terms_table.setItem(last_row, 0, QTableWidgetItem(self.term_name.text()))
            self.terms_table.setItem(last_row, 1, QTableWidgetItem(self.fp_type.currentText()))
            self.terms_table.setItem(last_row, 2, QTableWidgetItem(f'{' '.join([str(i) for i in params])}'))
            self.current_ling_var[3].append([self.term_name.text(), self.fp_type.currentText(), params])

    def terms_table_item_clicked(self):
        '''Метод, который срабатывает при нажатии на элемент таблицы терм-множств и заполняет некоторые виджеты
        окна данными из текущей строки таблицы.'''
        self.term_name.setText(self.terms_table.item(self.terms_table.currentRow(), 0).text())
        self.fp_type.setCurrentText(self.terms_table.item(self.terms_table.currentRow(), 1).text())
        curr_params = list(map(float, self.terms_table.item(self.terms_table.currentRow(), 2).text().split()))
        try:
            self.param_a.setValue(curr_params[0])
            self.param_b.setValue(curr_params[1])
            self.param_c.setValue(curr_params[2])
            self.param_d.setValue(curr_params[3])
        except:
            pass

    def change_term_clicked(self):
        '''Метод, который позволяет изменить выбранный в таблице терм-множеств терм.'''
        current_row = self.terms_table.currentRow()
        if current_row != -1:
            params = []
            self.set_params(params)
            self.current_ling_var[3][current_row] = [self.term_name.text(), self.fp_type.currentText(), params]
            self.terms_table.setItem(current_row, 0, QTableWidgetItem(self.term_name.text()))
            self.terms_table.setItem(current_row, 1, QTableWidgetItem(self.fp_type.currentText()))
            self.terms_table.setItem(current_row, 2, QTableWidgetItem(f'{' '.join([str(i) for i in params])}'))

    def delete_term_clicked(self):
        '''Метод, который позволяет удалить выбранный в таблице терм-множеств терм.'''
        current_row = self.terms_table.currentRow()
        if current_row != -1:
            if self.delete_from_rules:
                all_lp = ling_var_in + ling_var_out
                for i in range(len(all_lp)):
                    if all_lp[i].name == self.lp_name:
                        lp_index = i
                        break
                count = 0
                for rule, *other in all_rules:
                    if rule[lp_index][0] == current_row:
                        count += 1
                if count: # Спрашиваем - удалить или нет
                    msg = QMessageBox.question(self,"?", f"Вы действительно хотите удалить выбранный терм?\n \
                    Данный терм будет удалён из всех существующих правил вывода (количество правил, которое будет удалено: \
                    {count}).", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if msg == QMessageBox.Yes:
                        indexs = []
                        for i in range(len(all_rules)):
                            term = all_rules[i][0][lp_index][0]
                            if term == current_row:
                                indexs.append(i)
                            elif term > current_row:
                                all_rules[i][0][lp_index] = (all_rules[i][0][lp_index][0] - 1, all_rules[i][0][lp_index][1])
                        for i in indexs[::-1]:
                            del all_rules[i]
                        del self.current_ling_var[3][current_row]
                        self.terms_table.removeRow(current_row)
                        if lp_index >= len(ling_var_in):
                            ling_var_out[lp_index-len(ling_var_in)].delete_term_i(term)
                        else:
                            ling_var_in[lp_index].delete_term_i(term)
                else:
                    del self.current_ling_var[3][current_row]
                    self.terms_table.removeRow(current_row)
            else:                
                del self.current_ling_var[3][current_row]
                self.terms_table.removeRow(current_row)

    def ok_clicked(self):
        '''Метод, который сохраняет данные о созданной ЛП в список, а также выводит название созданной
        определённой ЛП в определённую таблицу ЛП родительского окна.'''
        if self.what_func == "listView_in_itemdoubleclicked":
            curr_listview_in_row = self.main_window.ui.listView_in.currentRow()
            # Создание ЛП
            lp = Ling_var(self.current_ling_var[0], self.current_ling_var[1][0], self.current_ling_var[1][1], self.current_ling_var[2])
            # Добавление термов
            for name, type, parameters in self.current_ling_var[3]:
                lp.add_term(name, type, parameters)
            ling_var_in[curr_listview_in_row] = lp
            self.main_window.ui.listView_in.item(curr_listview_in_row).setText(lp.name)
            self.close()
            self.add_to_combobox_in()

        elif self.what_func == "listView_out_itemdoubleclicked":
            curr_listview_out_row = self.main_window.ui.listView_out.currentRow()
            # Создание ЛП
            lp = Ling_var(self.current_ling_var[0], self.current_ling_var[1][0], self.current_ling_var[1][1], self.current_ling_var[2])
            # Добавление термов
            for name, type, parameters in self.current_ling_var[3]:
                lp.add_term(name, type, parameters)
            ling_var_out[curr_listview_out_row] = lp
            self.main_window.ui.listView_out.item(curr_listview_out_row).setText(lp.name)
            self.close()
            self.add_to_combobox_out()

        elif self.ling_var_name.text() == '':
            QMessageBox.about(self, 'Недопустимая ЛП', 'Введите корректное название ЛП, состоящее хотя бы из одного символа.')

        # Если созданная ЛП с таким названием уже находится в таблице входных ЛП
        elif self.ling_var_name.text() in [self.main_window.ui.listView_in.item(i).text() for i in range(self.main_window.ui.listView_in.count())]:
            QMessageBox.about(self, 'Недопустимая ЛП', 'Входная ЛП с таким названием уже существует.')

        # Если созданная ЛП с таким названием уже находится в таблице выходных ЛП
        elif self.ling_var_name.text() in [self.main_window.ui.listView_out.item(i).text() for i in range(self.main_window.ui.listView_out.count())]:
            QMessageBox.about(self, 'Недопустимая ЛП', 'Выходная ЛП с таким названием уже существует.')

        else:
            if self.what_func == "create_ling_var_in_clicked":
                # Создание ЛП
                lp = Ling_var(self.current_ling_var[0], self.current_ling_var[1][0], self.current_ling_var[1][1], self.current_ling_var[2])
                # Добавление термов
                for name, type, parameters in self.current_ling_var[3]:
                    lp.add_term(name, type, parameters)
                ling_var_in.append(lp)
                self.main_window.ui.listView_in.addItem(lp.name)
                self.add_to_combobox_in()

                for i in range(len(all_rules)):
                    all_rules[i][0] = all_rules[i][0][:len(ling_var_in)-1] + [(-1, 0)] + all_rules[i][0][len(ling_var_in)-1:]
            else:
                # Создание ЛП
                lp = Ling_var(self.current_ling_var[0], self.current_ling_var[1][0], self.current_ling_var[1][1], self.current_ling_var[2])
                # Добавление термов
                for name, type, parameters in self.current_ling_var[3]:
                    lp.add_term(name, type, parameters)
                ling_var_out.append(lp)
                self.main_window.ui.listView_out.addItem(lp.name)
                self.add_to_combobox_out()

                for i in range(len(all_rules)):
                    all_rules[i][0] += [(-1, 0)]

            self.close()

    def cancel_clicked(self):
        '''Метод, который позволяет закрыть дочернее окно, не сохраняя изменения, если они были сделаны.'''
        self.close()

    def closeEvent(self, event):
        '''Метод, срабатывающий при закрытии дочернего окна и предоставляющий доступ к родительскому окну.'''
        self.main_window.setEnabled(True)
        event.accept()


class Show_Func_dialog(QMainWindow, ShowFunc.Show_Func_Class):
    '''Класс отображения функций принадлежности для выбранной лингвистической переменной.'''
    def __init__(self, main_window, ling_vars):
        super().__init__()
        os.chdir(sys._MEIPASS)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setupUi(self)
        self.main_window = main_window
        self.ling_vars = ling_vars

        for i in self.ling_vars:
            self.ling_var_list.addItem(i.name)

        # connect'ы
        self.cancel_button.clicked.connect(self.cancel_button_clicked)
        self.show_fp_button.clicked.connect(self.show_fp_button_clicked)

    def cancel_button_clicked(self):
        '''Метод, который отвечает за закрытие дочернего окна.'''
        self.close()

    def show_fp_button_clicked(self):
        '''Метод, который отвечаает за показ функций принадлежности текущей выбранной ЛП из ListView.'''
        current_row = self.ling_var_list.currentRow()
        if current_row != -1:
            lp = self.ling_vars[current_row]
            if len(lp.terms) == 0:
                QMessageBox.about(self, "!", "Невозможно отобразить функции принадлежности термов данной \
                лингвистической переменной, т.к. у данной лингвистической переменной нет ни одного терма!")
            else:
                # Отрисовка графика
                plt.close()
                fig = plt.figure(f"Функции принадлежности отдельных термов лингвистической переменной «{lp.name}»", figsize=(14, 8))
                ax = fig.add_subplot(1, 1, 1)
                lp.print(ax)
                plt.show()

    def closeEvent(self, event):
        '''Метод, срабатывающий при закрытии дочернего окна и предоставляющий доступ к родительскому окну.'''
        self.main_window.setEnabled(True)
        event.accept()


class Rules_dialog(QMainWindow, rules.Rules_Editor_Class):
    '''Класс редактора правил вывода.'''
    def ling_var_plus_term_layout(self, lp, widgets_array):
        '''Функция, которая добавляет шаблон, в котором выбирается ЛП и её терм, к-ый участвует в правилах вывода.'''
        self.verticalLayout = QVBoxLayout(self.centralwidget)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setFont(font12)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setText(lp.name)
        self.verticalLayout.addWidget(self.lineEdit)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setFont(font12)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.addItem('----')
        for term in lp.terms:
            self.comboBox.addItem(term.name)
        self.verticalLayout.addWidget(self.comboBox)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setFont(font12)
        self.checkBox.setChecked(False)
        self.checkBox.setText("not")
        self.verticalLayout.addWidget(self.checkBox)

        self.horizontalLayout_5.addLayout(self.verticalLayout)

        widgets_array.append([self.lineEdit, self.comboBox, self.checkBox])

    def __init__(self, main_window):
        super().__init__()
        os.chdir(sys._MEIPASS)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setupUi(self)
        self.main_window = main_window

        self.ling_var_in_array = []
        self.ling_var_out_array = []

        # Удаляем лишние компоненты horizontal layout'а, которые после заново добавим
        self.horizontalLayout_5.removeWidget(self.label_3) # "то"
        self.horizontalLayout_5.removeItem(self.verticalLayout_8) # AND, OR, вес

        # Добавляем (входные ЛП и их термы)
        for i in range(len(ling_var_in)):
            self.ling_var_plus_term_layout(ling_var_in[i], self.ling_var_in_array)
            # print(self.ling_var_in_array, self.ling_var_out_array)

        # Добавляем label: "то"
        self.horizontalLayout_5.addWidget(self.label_3)

        # Добавляем (выходные ЛП и их термы)
        for i in range(len(ling_var_out)):
            self.ling_var_plus_term_layout(ling_var_out[i], self.ling_var_out_array)
            #print(self.ling_var_in_array, self.ling_var_out_array)

        # Добавляем vertical_layout: "AND, OR, вес"
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)

        self.all_rules = all_rules
        self.all_rules_timed = list(self.all_rules) # Создаём вспомогательный массив правил для случая, если пользователь не нажмёт в конце "OK"

        # Вывести все имеющиеся правила
        self.show_rules(self.all_rules_timed)

        # connect'ы
        self.add_button.clicked.connect(self.add_button_clicked)
        self.exit_button.clicked.connect(self.exit_button_clicked)
        self.delete_button.clicked.connect(self.delete_button_clicked)
        self.delete_all_button.clicked.connect(self.delete_all_button_clicked)
        self.OK.clicked.connect(self.ok_clicked)

    def show_rules(self, rules):
        '''Функция, которая выводит все имеющиеся правила в ListView.'''
        n = len(ling_var_in) # Количество входных ЛП

        self.listWidget_rules.clear()

        j = 1
        for rule, op, weight in rules:
            rule_str = f"{j}: IF " + \
                (f" {op} ").join(["NOT"*rule[i][1]+f"({ling_var_in[i].name} IS " + (f"{ling_var_in[i].terms[rule[i][0]].name})" if rule[i][0] != -1 else "----)") for i in range(len(ling_var_in))]) + \
                " THEN " + \
                (f" ").join(["NOT"*rule[i+n][1]+f"({ling_var_out[i].name} IS " + (f"{ling_var_out[i].terms[rule[i+n][0]].name})" if rule[i+n][0] != -1 else "----)") for i in range(len(ling_var_out))]) + \
                f" weight={round(weight, 2)}"
            self.listWidget_rules.addItem(rule_str)
            j += 1

        self.label_rules_count.setText(f'Количество правил: {len(rules)}')


    def add_button_clicked(self):
        '''Метод, который добавляет созданное правило в ListView.'''
        if not(self.ling_var_in_array):
            QMessageBox.about(self, "!", "Невозможно добавить правило вывода, т.к. не создано ни одной входной ЛП.")
        elif not(self.ling_var_out_array):
            QMessageBox.about(self, "!", "Невозможно добавить правило вывода, т.к. не создано ни одной выходной ЛП.")
        else:
            if self.RB_AND.isChecked():
                op = 'AND'
            else:
                op = 'OR'
            rule = [(comboBox.currentIndex() - 1, 1 if checkBox.isChecked() else 0) for _, comboBox, checkBox in self.ling_var_in_array]
            if (rule, op) in [(x[0][:len(ling_var_in)], x[1]) for x in self.all_rules_timed]: # Берём из правила, то что касается входных ЛП - если такой набор входных термов уже есть, вывести соответствующее сообщение
                QMessageBox.about(self, 'Невозможно добавить правило вывода.', 'Данное правило уже существует.')
            else:
                rule += [(comboBox.currentIndex() - 1, 1 if checkBox.isChecked() else 0) for _, comboBox, checkBox in self.ling_var_out_array]
                self.all_rules_timed.append([rule, op, self.weight.value()])
                self.show_rules(self.all_rules_timed)
                self.label_rules_count.setText(f'Количество правил: {len(self.all_rules_timed)}')

    def delete_button_clicked(self):
        '''Метод, который при нажатии на кнопку "Удалить" удаляет выбранное в ListView правило.'''
        current_row = self.listWidget_rules.currentRow()
        if current_row != -1:
            del self.all_rules_timed[current_row]
            self.listWidget_rules.takeItem(self.listWidget_rules.currentRow())
            self.show_rules(self.all_rules_timed)
            self.label_rules_count.setText(f'Количество правил: {len(self.all_rules_timed)}')

    def delete_all_button_clicked(self):
        '''Метод, который при нажатии на кнопку "Удалить всё" удаляет все правила из ListView.'''
        msg = QMessageBox.question(self, "?", "Вы действительно хотите удалить все созданные правила вывода?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if msg == QMessageBox.Yes:
            self.all_rules_timed.clear()
            self.listWidget_rules.clear()
            self.label_rules_count.setText(f'Количество правил: 0')

    def ok_clicked(self):
        '''Метод, который срабатывает при нажатии на кнопку "ОК" и закрывает дочернее окно, сохраняя данные из него.'''
        self.all_rules.clear()
        for x in self.all_rules_timed:
            self.all_rules.append(x)
        self.close()

    def exit_button_clicked(self):
        '''Метод, который отвечает за закрытие дочернего окна.'''
        self.close()

    def closeEvent(self, event):
        '''Метод, срабатывающий при закрытии дочернего окна и предоставляющий доступ к родительскому окну.'''
        self.main_window.setEnabled(True)
        event.accept()


class Show_3D_dialog(QMainWindow, Show_3D.Show_3D_Class):
    '''Класс отображения поверхности нечёткого вывода.'''
    def __init__(self, main_window, ling_vars_in_comboBoxes, out_name):
        super().__init__()
        os.chdir(sys._MEIPASS)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setupUi(self)
        self.main_window = main_window
        self.label_operation.setStyleSheet("background-color: rgb(220, 255, 235);")
        is_any_ling_var_there = True

        self.widgets = []

        # Заполнение виджетов окна названиями ЛП и задание значений из их диапазона:
        for i in ling_var_in:
            if i.name not in ling_vars_in_comboBoxes:
                self.label_operation.setStyleSheet("background-color: rgb(180, 241, 221);")
                if is_any_ling_var_there:
                    self.label = QLabel(self.centralwidget)
                    self.label.setFont(font12)
                    self.label.setStyleSheet("background-color: rgb(220, 255, 235);")
                    self.label.setAlignment(QtCore.Qt.AlignCenter)
                    self.label.setText("Задайте значение следующих ЛП:")
                    self.verticalLayout_lingvars.addWidget(self.label)
                    is_any_ling_var_there = False

                self.horizontalLayout_1 = QHBoxLayout(self.centralwidget)

                self.line_edit = QLineEdit(self.centralwidget)
                self.line_edit.setFont(font12)
                self.line_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.line_edit.setAlignment(QtCore.Qt.AlignCenter)
                self.line_edit.setReadOnly(True)
                self.horizontalLayout_1.addWidget(self.line_edit)

                self.doublespinbox = QDoubleSpinBox(self.centralwidget)
                self.doublespinbox.setFont(font12)
                self.doublespinbox.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.doublespinbox.setAlignment(QtCore.Qt.AlignCenter)
                self.doublespinbox.setSingleStep(0.01)
                self.horizontalLayout_1.addWidget(self.doublespinbox)
                self.verticalLayout_lingvars.addLayout(self.horizontalLayout_1)

                self.line_edit.setText(i.name)
                self.doublespinbox.setValue(i.x1lim)
                self.doublespinbox.setMinimum(i.x1lim)
                self.doublespinbox.setMaximum(i.x2lim)

                self.widgets.append(self.doublespinbox)
            else:
                self.widgets.append(None)

        self.lp_in_1_name = ling_vars_in_comboBoxes[0]
        self.lp_in_2_name = ling_vars_in_comboBoxes[1]
        self.lp_out_name = out_name

        # connect'ы
        self.show_3D_button.clicked.connect(self.show_3d_button_clicked)
        self.cancel_button.clicked.connect(self.cancel_button_clicked)

    def show_3d_button_clicked(self):
        '''Метод, который открывает окно, в котором можно рассмотреть поверхность нечёткого вывода с учетом
        заданных значений и параметров.'''
        if all_rules:

            # Входные лингвистические переменные (ling_var_in)
            m_in = len(ling_var_in)
            # Список индексов ЛП, относительно которых будет строиться поверхность нечёткого вывода
            index_in_lp = [i for i in range(m_in) if ling_var_in[i].name in [self.lp_in_1_name, self.lp_in_2_name]]
            # Список индексов ЛП, относительно которых не будет строиться поверхность нечёткого вывода
            # (указывается индекс ЛП и конкретное значение для неё из области определения)
            index_not_lp = [(i, self.widgets[i].value()) for i in range(m_in) if i not in index_in_lp] 

            # Выходные лингвистические переменные (ling_var_out)
            n_out = len(ling_var_out) # Количество выходных ЛП
            # Индекс выходной лингвистической переменной, относительно которой будет строиться поверхность нечёткого вывода
            for i in range(n_out):
                if ling_var_out[i].name == self.lp_out_name:
                    index_out = i

            and_op = self.intersection_combobox.currentText() # Операция для пересечения правил (можно ставить min и prod)
            imp_op = self.implication_combobox.currentText() # Операция для импликации правил (можно ставить min и prod)
            acc_op = self.accumulation_combobox.currentText() # Операция для аккумуляции правил правил (можно ставить max и sum)

            count_of_points = self.points_spinbox.value()+1 # Количество точек

            # Данные, по которым будет построена поверхность нечёткого вывода
            x_ax = []
            y_ax = []
            z_ax = []

            step1 = (ling_var_in[index_in_lp[0]].x2lim - ling_var_in[index_in_lp[0]].x1lim) / count_of_points
            step2 = (ling_var_in[index_in_lp[1]].x2lim - ling_var_in[index_in_lp[1]].x1lim) / count_of_points

            n = len(np.arange(ling_var_in[index_in_lp[0]].x1lim, ling_var_in[index_in_lp[0]].x2lim+step1/2, step1))
            i = 0
            for x1 in np.arange(ling_var_in[index_in_lp[0]].x1lim, ling_var_in[index_in_lp[0]].x2lim+step1/2, step1):
                self.pbar.setValue(int(i/n * 100))
                i += 1
                for x2 in np.arange(ling_var_in[index_in_lp[1]].x1lim, ling_var_in[index_in_lp[1]].x2lim+step2/2, step2):
                    # Вектор входных данных
                    x_in = [0] * m_in
                    x_in[index_in_lp[0]] = x1
                    x_in[index_in_lp[1]] = x2
                    for index, value in index_not_lp:
                        x_in[index] = value
            
                    # Блок фазификации
                    M = [lp.get_st_pr_off_all_terms(x) for lp, x in zip(ling_var_in, x_in)] # Определение степеней принадлежности к нечётким множествам термов конкретных ЛП

                    # Блок вывода
                    out_fp = [] # Выходные ФП (для дальнейшего аккумулирования)
                    for rule in all_rules:
                        lp = rule[0]
                        op = rule[1] # Операция только 1 (AND)
                        weight = rule[2]

                        if op == "AND":
                            # Операция для пересечения
                            if and_op == "prod": # PROD
                                muy_res = reduce(lambda x,y: x*y, [(M[k][lp[k][0]] if lp[k][1] == 0 else (1 - M[k][lp[k][0]])) if lp[k][0] != -1 else 1.0 for k in range(m_in)], 1)
                            else: # MIN
                                muy_res = min([(M[k][lp[k][0]] if lp[k][1] == 0 else (1 - M[k][lp[k][0]])) if lp[k][0] != -1 else 1.0 for k in range(m_in)])
                        else: # MAX
                            muy_res = max([(M[k][lp[k][0]] if lp[k][1] == 0 else (1 - M[k][lp[k][0]])) if lp[k][0] != -1 else 1.0 for k in range(m_in)])
                    
                        if lp[m_in + index_out][0] == -1: # В случае, если терм у выходной переменной не выбран
                            muy_res = 0
                        elif lp[m_in + index_out][1] == 1: # В случае, если стоит not у выходной переменной
                            muy_res = 1 - muy_res

                        out_term = (ling_var_out[index_out].terms)[lp[-n_out:][index_out][0]]._read(200)

                        k = peres(out_term, muy_res, imp_op) # Вид выходной ФП, операция min (для импликации)
                        
                        if weight != 1:
                            k[1] = [x*weight for x in k[1]] # Домножение на вес правила

                        out_fp.append(k)

                    accumulator = accumulate(out_fp, acc_op) # Аккумулирование правил

                    # Блок дефазификации (метод центра сумм для дискретного случая)
                    y_zv = (sum(y*muy for y, muy in zip(accumulator[0], accumulator[1]))) / (sum(muy for muy in accumulator[1]))

                    # Добавление точки на график
                    x_ax += [x1]
                    y_ax += [x2]
                    z_ax += [y_zv]

            self.pbar.setValue(100)

            # Отрисовка графика
            plt.close()
            fig = plt.figure(f"Поверхность нечёткого вывода", figsize=(14, 8))
            ax = fig.add_subplot(3, 2, 2)
            ling_var_in[index_in_lp[0]].print(ax)
            ax = fig.add_subplot(3, 2, 4)
            ling_var_in[index_in_lp[1]].print(ax)
            ax = fig.add_subplot(3, 2, 6)
            ling_var_out[index_out].print(ax)

            ax = fig.add_subplot(3, 2, (1, 5), projection='3d')
            ax.plot_trisurf(x_ax, y_ax, z_ax, cmap='viridis')
            ax.set_title('Поверхность нечёткого вывода\nпри следующих фиксированных значениях\nоставшихся лингвистических переменных\n' + \
                        "\n".join([f'"{ling_var_in[index].name}" = {const}' for index, const in index_not_lp]))
            ax.set_xlim(ling_var_in[index_in_lp[0]].x1lim, ling_var_in[index_in_lp[0]].x2lim)
            ax.set_ylim(ling_var_in[index_in_lp[1]].x1lim, ling_var_in[index_in_lp[1]].x2lim)
            ax.set_zlim(ling_var_out[index_out].x1lim, ling_var_out[index_out].x2lim)
            ax.set_xlabel(ling_var_in[index_in_lp[0]].name)
            ax.set_ylabel(ling_var_in[index_in_lp[1]].name)
            ax.set_zlabel(ling_var_out[index_out].name)
            plt.tight_layout(h_pad=4)
            plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0.2, hspace=0.4)
            plt.show()
            self.pbar.setValue(0)
        else:
            QMessageBox.about(self, "!", "Задано недостаточное количество правил!")

    def cancel_button_clicked(self):
        '''Метод, который отвечает за закрытие дочернего окна.'''
        self.close()

    def closeEvent(self, event):
        '''Метод, срабатывающий при закрытии дочернего окна и предоставляющий доступ к родительскому окну.'''
        self.main_window.setEnabled(True)
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window1 = Main_menu_dialog()
    window1.show()

    # Моделирование нечётких систем
    ling_var_in = []
    ling_var_out = []
    all_rules = []

    # Операции над нечёткими множествами
    fuzzy_sets = []

    app.exec_()