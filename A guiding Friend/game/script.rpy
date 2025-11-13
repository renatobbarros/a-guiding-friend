

define p = Character("Professor")
define c = Character("personagem_principal")

label start:
    #isaque, a gente vai adicionar aqui o cenario e personagens quando eles estiverem prontos

    #scene "caminhodacena - sala de aula"
    #play music "caminhomusica - terror"
    #play sound "cominhosom - corvos/ranger"

    p "{cps=15}...e lembrem-se, meus filhos. A mata tem seus mistérios. A Usina Velha, principalmente. Dizem os antigos que..."

    #esqueci ccomo esconde a cena
    #scene "o desenho"
    p "{cps=15}...ele vem. O homem do saco, o Velho. O Papa-Figo. Ele procura... *fígado*."

    #scene "tela preta"
    #play sound "cirene"
    #play sound "respiração ofegante"
    c "{cps=15}...Mãe? Pai?"
    c "{cps=15}...Já tá tarde."

    #scene "foto da rua"
    c "{cps=15} ...A história do professor..."
    #play sound "barulho de energia"
    #scene "foto muito escura"
    c "{cps=30} NÃO!"
    c "{CPS=20} ...Eu to sozinho"
    return
