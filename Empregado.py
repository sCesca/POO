class Empregado:
  def __init__(self, nome, cpf, rg):
    self.nome = nome
    self.cpf = cpf
    self.rg = rg

  def pagamento(self):
    print("O pagamento é um momento de grande felicidade para o funcionáro!")
    return 0

class EmpregadoHorista(Empregado):
  def __init__(self, nome, cpf, rg, horasTrabalhadas, pagamentoPorHora):
    Empregado.__init__(self, nome, cpf, rg)
    self.horasTrabalhadas = horasTrabalhadas
    self.pagamentoPorHora = pagamentoPorHora

  def pagamento(self):
    return self.horasTrabalhadas = self.pagamentoPorHora

class EmpregadoCLT(Empregado):
  def __init__(self, nome, cpf, rg, salario):
    Empregado.__init__(self, nome, cpf, rg)
    self.salario = salario

  def pagamento(self):
    return 13.33333333 * self.salario

class PrestadorDeServico(Empregado):
  def __init(self, nome, cpf, rg, pagamentoAvulso):
    Empregado.__init__(self, nome, cpf, rg)
    self.pagamentoAvulso = pagamentoAvulso

  def pagamento(self):
    return self.pagamentoAvulso
