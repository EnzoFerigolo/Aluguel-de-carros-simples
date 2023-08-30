class Carro:
    def __init__(
        self, modelo, kmRodados=0.0, valorAluguel=0.0, disponivel=True
    ) -> None:
        self.modelo = modelo
        self.km = kmRodados
        self.valor = valorAluguel
        self.disponivel = disponivel

    def imprimeCarro(self):
        return f"Carro modelo {self.modelo}, \nKm rodados: {self.km},\nValor: {self.valor},\nDisponível {'Sim' if (self.disponivel) else 'Não'}\n"

    def atualizaKm(self, novoKm):
        self.km = novoKm
        return self.km


class RegistroDeCarros:
    def __init__(self):
        self.listaCarros = []

    def registraCarro(self, carro):
        if isinstance(carro, Carro):
            self.listaCarros.append(carro)
        else:
            pass

    def apagaCarro(self, carro=Carro):
        if isinstance(carro, Carro):
            self.listaCarros.remove(carro)

    def procuraCarro(self, modelo):
        for carro in self.listaCarros:
            if carro.modelo == modelo:
                return carro

    def imprimeCarros(self):
        for carro in self.listaCarros:
            print(carro.imprimeCarro())

    def atualizaValor(self, modelo, valor):
        carro = self.procuraCarro(modelo)
        index = self.listaCarros.index(carro)
        self.listaCarros[index].valor = valor
        carro.valor = float(valor)
        return carro.valor


class Cliente:
    def __init__(self, nome, cpf, cnh) -> None:
        self.nome = nome
        self.cpf = str(cpf)
        self.cnh = str(cnh)
        pass

    def imprimeCliente(self):
        return f"Cliente {self.nome}\nCPF: {self.cpf}\nCNH: {self.cnh}\n"


from datetime import date, timedelta, datetime


class Locacao:
    def __init__(self, cliente, carro, diasAlugados) -> None:
        if isinstance(cliente, Cliente):
            self.cliente = cliente
            pass
        if isinstance(carro, Carro):
            self.carro = carro
            self.carro.disponivel = False
            pass

        self.diasAlugados = diasAlugados
        self.valorLocacao = diasAlugados * carro.valor
        self.dataAluguel = date.today() + timedelta(days=self.diasAlugados)
        self.dataFormatada = "{}/{}/{}".format(
            self.dataAluguel.day,
            self.dataAluguel.month,
            self.dataAluguel.year,
        )

    def valorRetorno(self):
        diasTotais = self.dataAluguel.day - date.today().day
        return (
            self.valorLocacao
            if diasTotais <= self.diasAlugados
            else self.valorLocacao
            + (diasTotais - self.diasAlugados) * (self.carro.valor * 1.4)
        )

    def imprimeNota(self):
        print(
            f"\nLocação do Carro {self.carro.modelo} no dia {self.dataFormatada}\n{self.cliente.imprimeCliente()}Tempo de locação: {self.diasAlugados} dias, totalizando R${self.valorLocacao}\n\nRetorno:\nData de retorno: {'{}/{}/{}'.format(date.today().day, date.today().month, date.today().year)}\nData prevista: {self.dataFormatada}\nMulta por atraso: R${self.valorRetorno() - self.valorLocacao}\nTotal: R${self.valorRetorno()}\n"
        )


class RegistroDeLocacoes:
    def __init__(self):
        self.listaLocacoes = []
        pass

    def registraLocacao(self, locacao):
        if isinstance(locacao, Locacao):
            self.listaLocacoes.append(locacao)
        else:
            pass

    def removeLocacao(self, locacao=Locacao):
        if isinstance(locacao, Locacao):
            self.listaLocacoes.remove(locacao)
        else:
            pass

    def procuraLocacao(self, modelo):
        for locacao in self.listaLocacoes:
            if locacao.carro.modelo == modelo:
                print(locacao.carro.imprimeCarro())
                return locacao

    def retornaCarro(self, modelo, novoKm=float):
        locacao = self.procuraLocacao(modelo)
        index = self.listaLocacoes.index(locacao)
        carro = self.listaLocacoes[index].carro
        carro.atualizaKm(novoKm)
        carro.disponivel = True
        locacao.imprimeNota()
        self.removeLocacao(locacao)
