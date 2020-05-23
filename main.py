# Os 8 requisitos do desafio estão comentados
# em suas devidas posições de implementação.

from abc import ABC, abstractmethod

GET_HOURS = 8
COEFICIENTE_BONUS = 0.15

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


# 1.Proteja a classe Employee para não ser instânciada diretamente.
# 2.Torne obrigatório a implementação dos métodos da classe Employee,
# implemente-os se for necessários.
# 3.Proteja o atributo department da classe Manager para que
# seja acessado somente através do método get_department.
class Employee(ABC):
    def __init__(self, code, name, salary, department):
        self.code = code
        self.name = name
        self.salary = salary
        self._department = department

    @abstractmethod
    def calc_bonus(self):
        pass

    # 6.Implemente o método get_department que retorna o nome
    # do departamento e set_department que muda o nome do
    # departamento para as classes Manager e Seller
    def get_department(self):
        return self._department.name

    def set_department(self, dep_name):
        self._department.name = dep_name

    # 7.Padronize uma carga horária de 8 horas para todos os funcionários.
    def get_hours(self):
        return GET_HOURS


# 4.Faça a correção dos métodos para que a herança funcione corretamente.
class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(
            code, name, salary, department=Department("managers", 1)
        )

    def calc_bonus(self):
        return self.salary * COEFICIENTE_BONUS


class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(
            code, name, salary, department=Department("sellers", 2)
        )
        self._sales = 0

    # 5.Proteja o atributo sales da classe Seller para que não seja
    # acessado diretamente, crie um método chamado get_sales para retornar
    # o valor do atributo e put_sales para acrescentar valores a esse atributo.
    def get_sales(self):
        return self._sales

    def put_sales(self, value):
        self._sales += value

    # 8.O cálculo do metodo calc_bonus do Vendedor deve ser calculado pelo
    # total de suas vendas vezes 0.15
    def calc_bonus(self):
        return self._sales * COEFICIENTE_BONUS
