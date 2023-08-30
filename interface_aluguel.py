from sistema_de_aluguel import *


class Interface:
    def __init__(self) -> None:
        self.registroCarros = RegistroDeCarros()
        self.registroLocacoes = RegistroDeLocacoes()
        print("Sistema de Aluguel de Veículos - Bem-vindo(a)")
        while True:
            opcao = int(
                input(
                    "Escolha 1 opção:\n"
                    + "1. Registrar novo carro\n"
                    + "2. Atualizar valor de carro já registrado\n"
                    + "3. Deletar carro do sistema\n"
                    + "4. Mostrar lista de carros\n"
                    + "5. Registrar aluguel\n"
                    + "6. Registrar retorno de carro\n"
                    + "Outro para sair do sistema\n"
                )
            )

            if opcao == 1:
                carro = Carro(
                    str(input("Modelo do carro: \n")),
                    float(input("Quilometragem: \n")),
                    float(input("Valor do aluguel diário: \n")),
                )
                self.registroCarros.registraCarro(carro)
                pass

            elif opcao == 2:
                
                try:
                    self.registroCarros.atualizaValor(
                        str(input("Digite o modelo do carro que deseja atualizar: \n")),
                        float(input("Novo valor: \n")),
                    )
                    pass
                except:
                    print("Carro não registrado no sistema.")

            elif opcao == 3:
                carro = self.registroCarros.procuraCarro(
                    modelo=str(input("Digite o modelo do carro que deseja deletar: \n"))
                )
                self.registroCarros.apagaCarro(carro)
                pass

            elif opcao == 4:
                print("Lista de carros: \n")
                self.registroCarros.imprimeCarros()
                pass

            elif opcao == 5:
                print("Registro de nova locação: ")
                carro = self.registroCarros.procuraCarro(
                    modelo=str(input("Modelo do carro alugado: \n"))
                )
                try:
                    if not carro.disponivel:
                        print("Veículo não disponível para locação. Registre outro.")
                        cliente = Cliente(
                            str(input("Nome completo do locador: \n")),
                            input("CPF: \n"),
                            input("CNH: \n"),
                        )
                        pass
                    else:
                        print("\nCarro disponível")
                        locacao = Locacao(
                            cliente, carro, int(input("Dias alugados: \n"))
                        )
                        self.registroLocacoes.registraLocacao(locacao)
                        locacao.imprimeNota()
                    pass
                except:
                    print("Carro não registrado no sistema.")

            elif opcao == 6:
                try:
                    self.registroLocacoes.retornaCarro(
                        modelo=str(input("Modelo do veículo a ser devolvido: \n")),
                        novoKm=float(input("Digite a nova quilometragem: \n")),
                    )
                    pass
                except:
                    print("Carro não registrado no sistema.")
            else:
                print("Você saiu.")
                break


Interface()
