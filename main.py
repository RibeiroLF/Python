saldo_conta=[]
extrato_total = []
def saida2():
    print('Deseja realizar outra operação?')
    opcoes = input('1.Sim\n2.Não\n')
    if opcoes == '2':
        return ('Obrigado por escolher nosso banco!')
    if opcoes == '1':
        print('Qual operação deseja realizar?')
        operacao = (int(input('1.Deposito \n2.Saque \n3.Extrato \n4.Sair\n')))
        if operacao == 1:
            return deposito()
        if operacao == 2:
            return saque()
        if operacao == 3:
            return extrato()
        if operacao == 4:
            return sair()
def sair():
    return ('Obrigado por escolher nosso banco!')
def saida():
    print('\nA operação foi concluída \nDeseja realizar outra operação?')
    opcoes=input('1.Sim\n2.Não\n')
    if opcoes == '2':
        return('Obrigado por escolher nosso banco!')
    if opcoes == '1':
        print('Qual operação deseja realizar?')
        operacao = (int(input('1.Deposito \n2.Saque \n3.Extrato \n4.Sair\n')))
        if operacao == 1:
            return deposito()
        if operacao == 2:
            return saque()
        if operacao == 3:
            return extrato()
        if operacao == 4:
            return sair()
def saque():
    saque_valor = None
    if len(saldo_conta) == 0:
        print('Seu saldo é zero ou não disponível no momento.')
        saida2()
    else:
        print(f'Seu saldo é de R${sum(saldo_conta):.2f}')
        saque_valor = input(f'Quanto deseja sacar?\n(Digite "x" para cancelar)\n')
    if saque_valor is not None:
        if saque_valor.lower() == 'x':
            print('Cancelando operação...')
            conta_bancaria()
        saque_valor = float(saque_valor)
        saldo_total = sum(saldo_conta)
        while saque_valor > saldo_total:
            saque_valor = input(
                f'Digite um valor de saque menor ou igual a R${saldo_total:.2f}.\n(Digite "x" para cancelar)\n')
            if saque_valor.lower() == 'x':
                print('Cancelando operação...')
                conta_bancaria()
            saque_valor = float(saque_valor)
        if saque_valor <= saldo_total:
            saldo_restante = saldo_total - saque_valor
            print(f'Seu saldo restante é de R${saldo_restante:.2f}')
            extrato_total.append(f'Saque de R${saque_valor:.2f}')
            novo_total = saldo_total - saque_valor
            saldo_conta.pop(0)
            saldo_conta.append(novo_total)
            saida()
def deposito():
    deposito_valor = input('Quanto deseja depositar? \n\n\n(Digite "x" para cancelar)\n')
    if deposito_valor.lower() == 'x':
        print('Cancelando operação')
        conta_bancaria()
    deposito_valor = float(deposito_valor)
    if deposito_valor > 0:
        saldo_conta.append(deposito_valor)
        saldo_total = sum(saldo_conta)
        print(f'Depósito realizado!\nO seu saldo agora é de {saldo_total:.2f}')
        extrato_total.append(f'Deposito de R${deposito_valor:.2f}')
        saida()
    while deposito_valor <= 0:
        deposito_valor=float(input('Insira um valor válido\n'))
    if deposito_valor > 0:
        saldo_conta.append(deposito_valor)
        saldo_total = sum(saldo_conta)
        print(f'Depósito realizado!\nO seu saldo agora é de {saldo_total:.2f}')
        extrato_total.append(f'Deposito de R${deposito_valor:.2f}')
        saida()
def extrato():
    if len(extrato_total) == 0:
        print('Não foram realizadas movimentações')
    if len(extrato_total) != 0:
        for operacoes in extrato_total:
            print(operacoes)
    print(f'Saldo atual da conta:R${sum(saldo_conta):.2f}')
    saida()
def conta_bancaria():
    print('Bem vindo a sua conta Bancária')
    print('Qual operação deseja realizar?')
    operacao=(int(input('1.Deposito \n2.Saque \n3.Extrato \n4.Sair\n')))
    if operacao == 1:
        return deposito()
    if operacao == 2:
        return saque()
    if operacao == 3:
        return extrato()
    if operacao == 4:
        return sair()
    if operacao >= 5:
        conta_bancaria()
conta_bancaria()



