

define p = Character("Professor")
define c = Character("\'Voce\'")

image sala = "images/bg sala.png"
image desenho = "images/bg figo.png"

label start:
    #isaque, a gente vai adicionar aqui o cenario e personagens quando eles estiverem prontos

    scene sala
    with fade
    #play music "caminhomusica - terror"
    #play sound "cominhosom - corvos/ranger"

    p "{cps=15}E lembrem-se, meus filhos. A mata tem seus mistérios.\nA Usina Velha, principalmente. Dizem os antigos que..."

    #Tive que mudar o tamanho por aqui.
    show desenho at Transform(xzoom=1.0, yzoom=0.8)
    with dissolve
    # o {w} serve como um wait. ele espera 2 segundos para mostra o resto do texto.
    p "{cps=15}...ele vem. O homem do saco, o Velho. O Papa-Figo. Ele procura...{w=2} {i}fígado{/i}."

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
    c "{cps=20} ...Eu to sozinho"
    return

