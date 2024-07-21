import matplotlib.pyplot as plt
import numpy as np
from math import e
from functools import reduce


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


class Term(): # Класс, описывающий термы заданной ЛП
    # name_mf - имя терма, type_mf - тип ФП, params - заданный набор параметров для ФП
    # x1lim, x2lim - границы (совпадают с областью определения лингвистической переменной)
    def __init__(self, name_mf, type_mf, x1lim, x2lim, params):
        self.name = name_mf
        self.type = type_mf
        self.x1lim = x1lim
        self.x2lim = x2lim
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

        else:
            raise ValueError("Неизвестный тип ФП")
        
    # Метод, формирующий набор значений по осям абцисс и ординат для заданного типа функции принадлежности
    # count_of_points - количество точек, котое будет использовано для отрисовки графиков ФП
    def _read(self, count_of_points=1000):
        x = np.arange(self.x1lim, self.x2lim, (self.x2lim - self.x1lim) / count_of_points)
        if self.type == "trimf":
            y = list(map(lambda p: (1-(self.b-p)/(self.b-self.a)) if self.a<=p<=self.b else ((1-(p-self.b)/(self.c-self.b)) if self.b<=p<=self.c else 0), x))
        elif self.type == "trapmf":
            y = list(map(lambda p: (1-(self.b-p)/(self.b-self.a)) if self.a<=p<=self.b else ((1-(p-self.c)/(self.d-self.c)) if self.c<=p<=self.d else (1 if self.b<=p<=self.c else 0)), x))
        elif self.type == "gaussmf":
            y = list(map(lambda p: e**(-(p-self.c)**2/(2*self.s**2)), x))
        elif self.type == "gbellmf":
            y = list(map(lambda p: 1/(1+abs((p-self.c)/self.a)**(2*self.b)), x))
        elif self.type == "signmf":
            y = list(map(lambda p: 1/(1+e**(-self.a*(p-self.c))), x))
        elif self.type == "dsigmf":
            y = list(map(lambda p: max(1/(1+e**(-self.a1*(p-self.c1))) - 1/(1+e**(-self.a2*(p-self.c2))), 0), x))
        elif self.type == "psigmf":
            y = list(map(lambda p: 1/(1+e**(-self.a1*(p-self.c1))) * 1/(1+e**(-self.a2*(p-self.c2))), x))
        elif self.type == "zmf":
            y = list([zmf(p, self.a, self.b) for p in x])
        elif self.type == "smf":
            y = list([smf(p, self.a, self.b) for p in x])
        elif self.type == "pimf":
            y = list([pimf(p, self.a, self.b, self.c, self.d) for p in x])

        return x, y

    # Метод для вывода графика ФП заданного терма на холст
    # plot - холст,
    # x1lim, x2lim - границы (совпадают с областью определения лингвистической переменной)
    def print(self, plot):
        x, y = self._read()
        plot.plot(x, y, label=self.name)

    # Метод, возвращающий степень принадлежности к данному терму
    # x - конкретное значение
    def st_pr(self, x):
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
    


class Ling_var(): # Класс, описывающий заданную ЛП
    def __init__(self, name, x1lim, x2lim, unit_of_measure=""):
        self.name = name
        self.x1lim = x1lim
        self.x2lim = x2lim
        self.terms = [] # термы имеют уникальные имена
        self.unit_of_measure = unit_of_measure

    # Добавление терма для ЛП
    def add_term(self, name, type, params):
        self.terms.append(Term(name, type, self.x1lim, self.x2lim, params))

    # Удаление терма для ЛП по его имени
    def delete_term(self, name_mf):
        for i in range(len(self.terms)):
            if self.terms[i].name == name_mf:
                del self.terms[i]
                break
        else:
            pass
    
    # Удаление терма для ЛП по его индексу
    def delete_term_i(self, index):
        del self.terms[index]

    # Возвращает терм по названию
    def get_term(self, name):
        for i in range(len(self.terms)):
            if self.terms[i].name == name:
                return self.terms[i]
        else:
            return
    
    # Возвращает степени принадлежности каждого терма для заданного конкретного значения x
    def get_st_pr_off_all_terms(self, x):
        return [term.st_pr(x) for term in self.terms]

    # Вывод функции принадлежности всех термов на одном графике
    def print(self, plot):
        for term in self.terms:
            term.print(plot)
        plot.set_title(f'Лингвистическая переменная "{self.name}"' + (f"({self.unit_of_measure})" if self.unit_of_measure != "" else ""))
        plot.set_xlim(self.x1lim, self.x2lim)
        plot.set_ylim(-0.05, 1.05)
        plot.grid(True) 
        plot.legend(loc="upper right", facecolor='lightgrey', labelcolor='black')

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name


# Операция пересечения нечёткого множества и числа
def peres(term, num, type="prod"):
    x_, y_ = term
    if type == "prod":
        if num == 0:
            answ = [0] * len(y_)
        else:
            answ = [y * num for y in y_]
    elif type == "min":
        if num == 0:
            answ = [0] * len(y_)
        else:
            answ = [min(y, num) for y in y_]
    return [x_, answ]

# Операция аккумуляции полученных ФП в результате правил
def accumulate(fp, type="sum"):
    ans = fp[0][1]
    if type == "sum":
        for f in fp[1:]:
            ans = [y + y_ for y, y_ in zip(ans, f[1])]
    elif type == "max":
        for f in fp[1:]:
            ans = [max(y, y_) for y, y_ in zip(ans, f[1])]
    return [fp[0][0], ans]

# функция для сохранения информации в файл
def save(filename, lp_in, lp_out, index_in_lp, index_not_in_lp, index_out, and_op, imp_op, acc_op, count_of_points1, count_of_points2, rules):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"""[General information]
NumInputs={len(lp_in)}
NumOutputs={len(lp_out)}
IndexInLp={index_in_lp[0]} {index_in_lp[1]}
IndexOutLp={index_out}
NumRules={len(rules)}
AndMethod={and_op}
ImpMethod={imp_op}
AggMethod={acc_op}
CountOfPoints1={count_of_points1}
CountOfPoints2={count_of_points2}""")
        
        for i in range(len(lp_in)):
            lp = lp_in[i]
            f.write(f"""\n\n[Input{i}]
Name={lp.name}
Range={lp.x1lim} {lp.x2lim}
NumMFs={len(lp.terms)}
""" + "\n".join([f"MF{j}={lp.terms[j].name}:{lp.terms[j].type}:{lp.terms[j].get_params()}" for j in range(len(lp.terms))]))
            
        for i in range(len(lp_out)):
            lp = lp_out[i]
            f.write(f"""\n\n[Output{i}]
Name={lp.name}
Range={lp.x1lim} {lp.x2lim}
NumMFs={len(lp.terms)}
""" + "\n".join([f"MF{j}={lp.terms[j].name}:{lp.terms[j].type}:{lp.terms[j].get_params()}" for j in range(len(lp.terms))]))
            
        f.write("\n\n[Other LP parametrs]\n")
        f.write("\n".join([f"{index}:{value}" for index, value in index_not_in_lp]))

        f.write("\n\n[Rules]\n")
        f.write("\n".join([f"{','.join([f"{term}:{not_op}" for term, not_op in rule])};{op};{weight}" for rule, op, weight in rules]))


if __name__ == "__main__":
    # Задание области определения ЛП
    x1lim, x2lim = -10, 40

    # Создание ЛП
    lp1 = Ling_var("Температура", x1lim, x2lim)
    # Добавление термов
    lp1.add_term("Холодно", "trapmf", [-15, -10, 0, 10])
    lp1.add_term("Тепло", "trimf", [5, 15, 25])
    lp1.add_term("Жарко", "trapmf", [20, 30, 40, 45])

    # Создание ЛП
    lp2 = Ling_var("Желаемая температура", x1lim, x2lim)
    # Добавление термов
    lp2.add_term("Холодно", "trapmf", [-15, -10, 0, 10])
    lp2.add_term("Тепло", "trimf", [5, 15, 25])
    lp2.add_term("Жарко", "trapmf", [20, 30, 40, 45])

    # Создание ЛП
    lp3 = Ling_var("Действие", -1, 1)
    # Добавление термов
    lp3.add_term("Охлаждение", "trapmf", [-1.5, -1, -0.5, 0])
    lp3.add_term("Ничего", "trimf", [-0.5, 0, 0.5])
    lp3.add_term("Отопление", "trapmf", [0, 0.5, 1, 1.5])


    # База правил (если терм отсутствует, то ставить -1)
    rules = [[[(0, 0), (0, 1), (2, 0)], "AND", 1.0],
             [[(0, 0), (0, 0), (1, 0)], "AND", 1.0],
             [[(0, 1), (0, 0), (0, 0)], "AND", 1.0],
             [[(1, 0), (1, 0), (1, 0)], "AND", 1.0],
             [[(2, 0), (2, 0), (1, 0)], "AND", 1.0],
             [[(2, 0), (2, 1), (0, 0)], "AND", 1.0],
             [[(2, 1), (2, 0), (2, 0)], "AND", 1.0]]

    lp_in = [lp1, lp2] # Входные лингвистические переменные
    m_in = len(lp_in)
    index_in_lp = [0, 1] # Список индексов ЛП, относительно которых будет строиться поверхность нечёткого вывода

    index_not_lp = [] # Список индексов ЛП, относительно которых не будет строиться поверхность нечёткого вывода
    # (указывается индекс ЛП и конкретное значение для неё из области определения)

    lp_out = [lp3] # Выходные лингвистические переменные
    n_out = len(lp_out) # Количество выходных ЛП
    index_out = 0 # Индекс выходной лингвистической переменной, относительно которой будет строиться поверхность нечёткого вывода

    and_op = "min" # Операция для пересечения правил (можно ставить min и prod)
    imp_op = "min" # Операция для импликации правил (можно ставить min и prod)
    acc_op = "max" # Операция для аккумуляции правил правил (можно ставить max и sum)

    # Количество точек
    count_of_points1 = 20
    count_of_points2 = 20

    # Данные, по которым будет построена поверхность нечёткого вывода
    x_ax = []
    y_ax = []
    z_ax = []


    i = 0
    for x1 in np.arange(lp_in[index_in_lp[0]].x1lim, lp_in[index_in_lp[0]].x2lim, (lp_in[index_in_lp[0]].x2lim - lp_in[index_in_lp[0]].x1lim) / count_of_points1):
        i += 1
        print(i)
        for x2 in np.arange(lp_in[index_in_lp[1]].x1lim, lp_in[index_in_lp[1]].x2lim, (lp_in[index_in_lp[1]].x2lim - lp_in[index_in_lp[1]].x1lim) / count_of_points1):

            # Вектор входных данных
            x_in = [0] * m_in
            x_in[index_in_lp[0]] = x1
            x_in[index_in_lp[1]] = x2
            for index, value in index_not_lp:
                x_in[index] = value
    
            # Блок фазификации
            M = [lp.get_st_pr_off_all_terms(x) for lp, x in zip(lp_in, x_in)] # Определение степеней принадлежности к нечётким множествам термов конкретных ЛП

            # Блок вывода
            out_fp = [] # Выходные ФП (для дальнейшего аккумулирования)
            for rule in rules:
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

                out_term = (lp_out[index_out].terms)[lp[-n_out:][index_out][0]]._read(200)

                k = peres(out_term, muy_res, "min") # Вид выходной ФП, операция min (для импликации)
                
                if weight != 1:
                    k[1] = [x*weight for x in k[1]] # Домножение на вес правила

                out_fp.append(k)

            accumulator = accumulate(out_fp, "sum") # Аккумулирование правил

            # Блок дефазификации (метод центра сумм для дискретного случая)
            y_zv = (sum(y*muy for y, muy in zip(accumulator[0], accumulator[1]))) / (sum(muy for muy in accumulator[1]))

            # Добавление точки на график
            x_ax += [x1]
            y_ax += [x2]
            z_ax += [y_zv]

    # Отрисовка графика
    plt.close()
    fig = plt.figure(figsize=(14, 8))
    ax = fig.add_subplot(3, 2, 2)
    lp_in[index_in_lp[0]].print(ax)
    ax = fig.add_subplot(3, 2, 4)
    lp_in[index_in_lp[1]].print(ax)
    ax = fig.add_subplot(3, 2, 6)
    lp_out[index_out].print(ax)

    ax = fig.add_subplot(3, 2, (1, 5), projection='3d')
    ax.plot_trisurf(x_ax, y_ax, z_ax, cmap='viridis')
    ax.set_title('Поверхность нечёткого вывода\nпри следующих фиксированных значениях\nоставшихся лингвистических переменных\n' + \
                 "\n".join([f'"{lp_in[index].name}" = {const}' for index, const in index_not_lp]))
    ax.set_xlim(lp_in[index_in_lp[0]].x1lim, lp_in[index_in_lp[0]].x2lim)
    ax.set_ylim(lp_in[index_in_lp[1]].x1lim, lp_in[index_in_lp[1]].x2lim)
    ax.set_zlim(lp_out[index_out].x1lim, lp_out[index_out].x2lim)
    ax.set_xlabel(lp_in[index_in_lp[0]].name)
    ax.set_ylabel(lp_in[index_in_lp[1]].name)
    ax.set_zlabel(lp_out[index_out].name)
    plt.tight_layout(h_pad=4)
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0.2, hspace=0.4)
    plt.show()

    save("temp2.txt", lp_in, lp_out, index_in_lp, index_not_lp, index_out, and_op, imp_op, acc_op, count_of_points1, count_of_points2, rules)