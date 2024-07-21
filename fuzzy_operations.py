import matplotlib.pyplot as plt
import numpy as np
from math import e


# Функции для некоторых ФП
# -------------------------------------
def zmf(x, a, b):
    if x <= a:
        return 1
    elif a <= x <= (a+b)/2:
        return 1-2*((x-a)/(b-a))**2
    elif (a+b)/2 <= x <= b:
        return 2*((x-b)/(b-a))**2
    return 0


def smf(x, a, b):
    if x <= a:
        return 0
    elif a <= x <= (a+b)/2:
        return 2*((x-a)/(b-a))**2
    elif (a+b)/2 <= x <= b:
        return 1-2*((x-b)/(b-a))**2
    return 1


def pimf(x, a, b, c, d):
    if x <= a:
        return 0
    elif a <= x <= (a+b)/2:
        return 2*((x-a)/(b-a))**2
    elif (a+b)/2 <= x <= b:
        return 1-2*((x-b)/(b-a))**2
    elif b <= x <= c:
        return 1
    elif c <= x <= (c+d)/2:
        return 1-2*((x-c)/(d-c))**2
    elif (c+d)/2 <= x <= d:
        return 2*((x-d)/(d-c))**2
    return 0
# -------------------------------------


class fuzzy_set():
    '''Класс, описывающий нечёткое множество.'''
    # name_mf - названием НМ, type_mf - тип функции принадлежности (ФП) НМ, params - заданный набор параметров для ФП
    def __init__(self, name_mf, type_mf, params):
        self.name = name_mf
        self.type = type_mf
        if self.type == "trimf":
            self.a, self.b, self.c = params
        elif self.type == "trapmf":
            self.a, self.b, self.c, self.d = params
        elif self.type == "gaussmf":
            self.s, self.c = params
        elif self.type == "gbellmf":
            self.a, self.b, self.c = params
        elif self.type == "signmf":
            self.a, self.c = params
        elif self.type == "dsigmf":
            self.a1, self.c1, self.a2, self.c2 = params
        elif self.type == "psigmf":
            self.a1, self.c1, self.a2, self.c2 = params
        elif self.type == "zmf":
            self.a, self.b = params
        elif self.type == "smf":
            self.a, self.b = params
        elif self.type == "pimf":
            self.a, self.b, self.c, self.d = params
        elif self.type == "const":
            self.const = params[0]
        else:
            raise ValueError("Неизвестный тип ФП")

    def st_pr(self, x):
        '''Метод, возвращающий степень принадлежности к данному нечёткому множеству, где x - конкретное значение.'''
        if self.type == "trimf":
            y = (1-(self.b-x)/(self.b-self.a)) if self.a<=x<=self.b else ((1-(x-self.b)/(self.c-self.b)) if self.b<=x<=self.c else 0)
        elif self.type == "trapmf":
            y = (1-(self.b-x)/(self.b-self.a)) if self.a<=x<=self.b else ((1-(x-self.c)/(self.d-self.c)) if self.c<=x<=self.d else (1 if self.b<=x<=self.c else 0))
        elif self.type == "gaussmf":
            y = e**(-(x-self.c)**2/(2*self.s**2))
        elif self.type == "gbellmf":
            y = 1/(1+abs((x-self.c)/self.a)**(2*self.b))
        elif self.type == "signmf":
            y = 1/(1+e**(-self.a*(x-self.c)))
        elif self.type == "dsigmf":
            y = max(1/(1+e**(-self.a1*(x-self.c1))) - 1/(1+e**(-self.a2*(x-self.c2))), 0)
        elif self.type == "psigmf":
            y = 1/(1+e**(-self.a1*(x-self.c1))) * 1/(1+e**(-self.a2*(x-self.c2)))
        elif self.type == "zmf":
            y = zmf(x, self.a, self.b)
        elif self.type == "smf":
            y = smf(x, self.a, self.b)
        elif self.type == "pimf":
            y = pimf(x, self.a, self.b, self.c, self.d)
        elif self.type == "const":
            y = self.const
        return y
    
    def get_params(self):
        if self.type == "trimf":
            return f"{self.a} {self.b} {self.c}"
        elif self.type == "trapmf":
            return f"{self.a} {self.b} {self.c} {self.d}"
        elif self.type == "gaussmf":
            return f"{self.s} {self.c}"
        elif self.type == "gbellmf":
            return f"{self.a} {self.b} {self.c}"
        elif self.type == "signmf":
            return f"{self.a} {self.c}"
        elif self.type == "dsigmf":
            return f"{self.a1} {self.c1} {self.a2} {self.c2}"
        elif self.type == "psigmf":
            return f"{self.a1} {self.c1} {self.a2} {self.c2}"
        elif self.type == "zmf":
            return f"{self.a} {self.b}"
        elif self.type == "smf":
            return f"{self.a} {self.b}"
        elif self.type == "pimf":
            return f"{self.a} {self.b} {self.c} {self.d}"
        elif self.type == "const":
            return f"{self.const}"
        
    def get_value(self, x_list):
        if self.type == "trimf":
            y = list(map(lambda p: (1-(self.b-p)/(self.b-self.a)) if self.a<=p<=self.b else ((1-(p-self.b)/(self.c-self.b)) if self.b<=p<=self.c else 0), x_list))
        elif self.type == "trapmf":
            y = list(map(lambda p: (1-(self.b-p)/(self.b-self.a)) if self.a<=p<=self.b else ((1-(p-self.c)/(self.d-self.c)) if self.c<=p<=self.d else (1 if self.b<=p<=self.c else 0)), x_list))
        elif self.type == "gaussmf":
            y = list(map(lambda p: e**(-(p-self.c)**2/(2*self.s**2)), x_list))
        elif self.type == "gbellmf":
            y = list(map(lambda p: 1/(1+abs((p-self.c)/self.a)**(2*self.b)), x_list))
        elif self.type == "signmf":
            y = list(map(lambda p: 1/(1+e**(-self.a*(p-self.c))), x_list))
        elif self.type == "dsigmf":
            y = list(map(lambda p: max(1/(1+e**(-self.a1*(p-self.c1))) - 1/(1+e**(-self.a2*(p-self.c2))), 0), x_list))
        elif self.type == "psigmf":
            y = list(map(lambda p: 1/(1+e**(-self.a1*(p-self.c1))) * 1/(1+e**(-self.a2*(p-self.c2))), x_list))
        elif self.type == "zmf":
            y = list([zmf(p, self.a, self.b) for p in x_list])
        elif self.type == "smf":
            y = list([smf(p, self.a, self.b) for p in x_list])
        elif self.type == "pimf":
            y = list([pimf(p, self.a, self.b, self.c, self.d) for p in x_list])
        elif self.type == "const":
            y = list([self.const for _ in x_list])
        return y


class fuzzy_operationship():
    '''Задаёт нечёткое множество, образованное после применения операций к заданным нечётким множествам (fuzzy_set).'''
    def __init__(self, name, fs):
        self.name = name # Название нечёткого множества

        # Начальное НМ, от которого будет образовано новое
        if 'fuzzy_set' in str(type(fs)):
            self.operations = [fs]
        elif 'fuzzy_operationship' in str(type(fs)):
            self.operations = list(fs.operations)

    # Добавление новой операции над нечёткими множествами
    # op - операция; fs - нечёткое множество, с которым происходит операция
    # op = ["unif", "intr", "add", "diff", "s_diff", "a_unif", "a_intr", "b_unif", "b_intr"]
    def add_operation(self, op, fs):
        if 'fuzzy_set' in str(type(fs)):
            s = [fs]
        elif 'fuzzy_operationship' in str(type(fs)):
            s = list(fs.operations)
        else:
            s = "Error"
        self.operations += s
        self.operations.insert(0, op)

    # Получить значения ФП заданного НМ для списка входных значений
    def get_value(self, x_list):
        op_list = list(self.operations)
        for i in range(len(op_list)):
            if 'fuzzy_set' in str(type(op_list[i])):
                op_list[i] = [float(op_list[i].st_pr(x)) for x in x_list]

        while len(op_list) > 1:
            i = 1
            while i < len(op_list) - 1:
                if ('list' in str(type(op_list[i]))) and ('list' in str(type(op_list[i+1]))):
                    op = op_list[i-1]
                    l1 = op_list[i]
                    l2 = op_list[i+1]
                    z = zip(l1, l2)
                    if op == "unif":
                        res = [max(x, y) for x, y in z]
                    elif op == "intr":
                        res = [min(x, y) for x, y in z]
                    elif op == "add":
                        res = [x - y for x, y in z]
                    elif op == "diff":
                        res = [max(x - y, 0) for x, y in z]
                    elif op == "s_diff":
                        res = [abs(x - y) for x, y in z]
                    elif op == "a_unif":
                        res = [x + y - x * y for x, y in z]
                    elif op == "a_intr":
                        res = [x * y for x, y in z]
                    elif op == "b_unif":
                        res = [min(x + y, 1) for x, y in z]
                    elif op == "b_intr":
                        res = [max(x + y - 1, 0) for x, y in z]
                    else:
                        print("Error!!!")
                    op_list[i-1] = res
                    del op_list[i]
                    del op_list[i]
                    i -= 1
                else:
                    i += 1
        return op_list[0]
    
    # Возвращает строку для сохранения в файл вида ФП
    def get_info(self):
        res_s = []
        for i in range(len(self.operations)):
            if 'fuzzy_set' in str(type(self.operations[i])):
                res_s.append(f"{self.operations[i].type}:{self.operations[i].get_params()}")
            else:
                res_s.append(self.operations[i])
        return ";".join(res_s)
    
    def set_info(self, str):
        res_s = str.split(";")
        self.operations.clear()
        for x in res_s:
            if ":" not in x:
                self.operations.append(x)
            else:
                type, params = x.split(":")
                params = [float(y) for y in params.split()]
                self.operations.append(fuzzy_set("", type, params))

def save_fuzzy_sets(filename, lst):
    names = [fs.name for fs in lst]
    fp_view = []
    for fs in lst:
        if 'fuzzy_set' in str(type(fs)):
            fp_view.append(f"fs={fs.type}:{fs.get_params()}")
        elif 'fuzzy_operationship' in str(type(fs)):
            fp_view.append(f"fo={fs.get_info()}")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"count={len(lst)}\n")
        for name in names:
            f.write(name + "\n")
        for fp in fp_view:
            f.write(fp + "\n")

def plot(x1, x2, count_of_point, fs_list):
    plt.close()
    step = (x2 - x1) / count_of_point
    x = np.arange(x1, x2+step/2, step)

    fig = plt.figure(figsize=(14, 8))
    ax = fig.add_subplot(1, 1, 1)

    for fs in fs_list:
        y = fs.get_value(x)
        ax.plot(x, y, label=f"{fs.name}")
    
    if len(fs_list) == 1:
        ax.set_title(f"Нечёткое множество «{fs_list[0].name}»")
    else:
        ax.set_title(f"Нечёткие множества: " + ", ".join([f"«{fs.name}»" for fs in fs_list]))

    ax.set_xlim(x1, x2)
    ax.set_ylim(-0.05, 1.05)
    plt.show()

if __name__ == "__main__":
    
    x1, x2 = -20, 50
    count_of_point = 500

    fs1 = fuzzy_set("НМ1", "trimf", [-10, 20, 30])
    fo1 = fuzzy_operationship("НМ3", fs1)
    fs2 = fuzzy_set("НМ2", "trimf", [-5, 15, 45])
    fo1.add_operation("intr", fs2)

    #plot(x1, x2, count_of_point, [fs1])
    #plot(x1, x2, count_of_point, [fs2])
    #plot(x1, x2, count_of_point, [fo1])

    plot(x1, x2, count_of_point, [fs1, fs2, fo1])

    fo2 = fuzzy_operationship("НМ5", fo1)
    fs3 = fuzzy_set("НМ4", "trimf", [-15, 0, 5])
    fo2.add_operation("unif", fs3)

    #fo1.set_info("unif;intr;trimf:-10 20 30;trimf:-5 15 45;trimf:-15 0 5")
    plot(x1, x2, count_of_point, [fo1, fs3, fo2])

    save_fuzzy_sets("test.txt", [fs1, fo1, fo2, fs3])