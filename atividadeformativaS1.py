# Início da Atividade Formativa da SEMANA 02

# Primeira Etapa: CRIAR A BASE DO ALGORITMO -> Uso de Variáveis, Operadores, print(), input(), if/elif/else
# Objetivo da Semana: CRIAR UM PROGRAMA QUE CONSIGA "OUVIR" USUÁRIO E TOMAR UMA DECISÃO SIMPLES COM BASE NO QUE FOI
# DIGITADO    PALAVRAS PARA SEREM ENTENDIDAS: ABOUT e QUIT

#  SEMPRE REALIZAR UM PASSO DE CADA VEZ -> VALIDAR -> AVANÇAR PARA O PRÓXIMO PASSO

# FLUXO DE COMANDOS:
comando = input("Digite um comando: ").upper()  #  C01 -> USUÁRIO PRECISA DIGITAR UM COMANDO (QUIT/ABOUT)
                                        #  O PROGRAMA ARMAZENA O QUE O USUÁRIO DIGITOU EM UMA VARIÁVEL
                                        #  uso do: .upper() para que caso o usuário digite "About ou about" em letras
                                        #  minúculas o programa seja executado, também, pois PYTHON diferencia maiúscu-
                                        #  las de minúsculas (case-sensitive)

print(f"O comando digitado foi: {comando}")

#  O ALGORITMO LÊ A VARIÁVEL CONTENDO O COMANDO QUE O USUÁRIO DIGITOU E TOMA UMA DECISÃO (USAR if/elif/else)
if comando == "ABOUT":  #  se ABOUT, msg: Gestor de Portifólio do André  (OBS: usar o elif no lugar do if)
    print("Gestor de Portfólio do André")
    #print("Seja Bem-Vindo!") #pensando como página inicial do programa (possibilidade de lógica)
elif comando == "QUIT":  #  senão, se o comando for QUIT, msg de despedida: Saindo do Gestor de Portifólio
    print("Saindo do Gestor de Portfólio")
else:       #  qualquer outra coisa coisa que o usuário digitar != ABOUT/QUIT : informar que o comando não foi
    print("ERRO: Comando não reconhecido")        # reconhecido, msg: ERRO: Comando NÃO reconhecido

print("Até logo!")#  Final da execução, msg: Até logo!
#if comando != "ABOUT" and comando != "QUIT":
    #print("Até logo!")#  Final da execução, msg: Até logo!(possibilidade de lógica)

########################################################################################################################

# CÓDIGO LIMPO:
comando = input("Digite um comando: ").upper()

print(f"O comando digitado foi: {comando}")

if comando == "ABOUT":
    print("Gestor de Portfólio do André")
elif comando == "QUIT":
    print("Saindo do Gestor de Portfólio")
else:
    print("ERRO: Comando não reconhecido")

print("Até logo!")



