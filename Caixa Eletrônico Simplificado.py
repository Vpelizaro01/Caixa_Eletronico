tentativa = 3
conta ={
"Saldo": 1000, 
} 
   

while True:
    try:
        opcao = input("[1] Depositar\n[2] Sacar\n[3] Saldo\n[4] Sair\n")
 
        if opcao == "1":
            for tentativa in range(3):
                valor = float(input("Digite o valor: "))
                if valor > 0:
                    conta['Saldo'] += valor
                    print(f"Foi depositado em sua conta o valor de R${valor}\nAgora seu saldo é de: R${conta['Saldo']}")
 
                    input_do_usuario = input("Escreva pronto para terminar a função deposito.\n").strip().upper()
                    if input_do_usuario == "pronto":
                        print("Deposito completo!!")
                        break
 
                    retorno = input("Deseja voltar ao inicio? S/N: ").strip().upper()
                    if retorno == "S":
                        print("Retornando...")
                        break
                    else:
                        print("Continuando depósito...")
                        continue
                else:
                    print("Valor inválido. Insira um valor positivo.")
                    continue
        
        elif opcao == "2":
            valor = float(input ("Quanto deseja sacar ?: "))
            if valor > 0:
                if valor <= conta["Saldo"]: 
                    conta["Saldo"] -= valor
                    print(f"O valor sacado foi de {valor}.\nSeu saldo agora é de: R${conta['Saldo']}")
                else: 
                    print(f"Fundos insuficientes.\nSeu saldo agora é: R${conta['Saldo']}")
            else:                            
                    print("Quantidade invalida.\nInsira um valor positivo.")
            input_do_usuario = input(f"Escreva pronto para terminar a função saque.\n").strip().upper()
            if input_do_usuario == "pronto":
                print("Saque completo!!")
            
            retorno = input("Deseja voltar ao inicio ? S/N ?").strip().upper() 
            if retorno == "S":  
                print("retornando...")
                continue
            else:                                   
                print("Continuando função anterior...")
                continue

        elif opcao == "3": 
            print(f"Seu saldo é {conta['Saldo']}")
            
            retorno = input("Deseja voltar ao inicio ? S/N ?").strip().upper()
            if retorno == "S":  
                print("retornando...")
                continue
            else:                                   
                print("Continuando função anterior...")
                continue
        elif opcao == "4":
            print("Saindo do programa...")
            quit()
        else:
            print("Erro, tente novamente...")
            continue
    except ValueError:
        print("Erro, tente novamente...")
