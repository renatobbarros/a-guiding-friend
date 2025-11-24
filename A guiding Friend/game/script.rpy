init:
    $ renpy.music.register_channel("ambiente", mixer="sfx", loop=True)

    define p = Character("Professor", color="#FFFFFF") 
    define c = Character("\'Criança\'", color="#FFFFFF", kind=adv)
    define cf = Character("Comadre Florzinha", what_color="#E0FFFF")
    define d = Character("???", color="#FFFFFF")
    define m = Character("Mãe", color="#FFCCCC")
    define flash_black = Fade(0.1, 0.0, 0.5, color="#000") 

    image sala = "images/bg sala.png"
    image desenho = "images/bg figo.png"
    image tela_preta = "images/tela preta.jpg"
    image rua_clara = "images/rua_clara.PNG" 
    image rua_escura = "images/apagado.png"
    image canavial_bifurcacao = "images/canavial_bifurcacao.png"
    image estrada_distante = "images/estrada_distante.png"
    image estrada_perto = "images/estrada_perto.png"
    image varanda_casa = "images/varanda_casa.png"
    image olhando_atras = "images/olhando_atras.png"

label start:
    play music "sounds/music/Ossuary 6 - Air.mp3" fadein 2.0

    scene sala
    with fade

    $ renpy.music.set_volume(0.5, channel='music')
    
    voice "sounds/falas/p1.mp3"
    p "{cps=25}A Mata, como muitos de vocês sabem, guarda segredos profundos...{w=0.4}\ne um deles é sobre a famosa Usina Velha.{nw}"
    
    voice "sounds/falas/p2.mp3"
    p "{cps=25}Um ser misterioso habita essas sombras: o Homem do Saco,{w=0.3} também\nconhecido como o Velho,{w=0.2} ou ainda o Papa-Figo.{nw}"
    
    show desenho at Transform(xzoom=1.0, yzoom=0.8)
    with dissolve
    
    voice "sounds/falas/p3.mp3"
    p "{cps=28}Ele é uma figura que provoca tanto medo quanto curiosidade.{w=0.4} \nA lenda nos conta que ele não aparece sem motivo."
    
    voice "sounds/falas/p4.mp3"
    p "{cps=28}O Velho está em busca de algo muito específico...{w=0.5} fígado!{w=0.2} Isso mesmo, fígado!{w=0.4}\nE é aí que entra a Comadre Florzinha, uma figura protetora da nossa história."
    
    voice "sounds/falas/p5.mp3"
    p "{cps=25}Ela guia e cuida das pessoas que, porventura,{w=0.3} se encontram perdidas\nou em perigo nas matas.{w=0.4} Lembrem-se: essa lenda não é apenas uma história."
    
    voice "sounds/falas/p6.mp3"
    p "{cps=25}É um ensinamento sobre respeito à natureza e os mistérios que ela abriga.{w=0.4}\nVamos discutir juntos o que essa lenda nos ensina sobre coragem e proteção!"
    
    with Pause(1.5)
    
    p "{cps=15}...ele vem. O Homem do Saco, o Velho. O Papa-Figo. Ele procura...{w=1.5} {i}fígado{/i}."

    scene tela_preta
    with dissolve
    
    stop music fadeout 1.0
    play ambiente "sounds/noises/grilos.wav" fadein 2.0
    play sound "sounds/noises/respiracao ofegante.wav" loop

    c "{cps=20}...Mãe? Pai?"
    c "{cps=15}...Já tá tarde."

    show rua_clara
    with dissolve

    play sound "sounds/noises/som eletrico.wav" loop fadein 0.8 volume 0.5

    c "{cps=25}...A história do professor..."
    play sound "sounds/noises/luz caindo.flac" volume 0.8

    scene rua_clara with flash_black
    
    show rua_escura
    with fade

    stop sound

    play sound "sounds/noises/respiracao ofegante.wav" loop

    c "{nw}NÃO!" 
    c "{cps=15}...Eu tô sozinho."

    stop sound
    
    jump cena_2_assobio

label cena_2_assobio:
    
    play sound "sounds/noises/assobio.wav" fadein 0.5 volume 0.8
    with Pause(4.3)

    d "{cps=25}Oxente, mas olha só quem decidiu aparecer por aqui.."
    d "{cps=25}Você se perdeu, né? Que problemão."

    menu: 
        "Responder a voz":
            c "{cps=25}Quem e você?"

            d "{cps=25}Você nunca ouviu as historias? Eu sou alguem que você conhece muito bem."

            cf "{cps=25}A Comadre Florzinha."

            $ silencio = False
        "Ficar em silêncio":
            "Você decide ficar em silencio, ignorando seja-la quem for\npara continuar procurando um caminho de volta para casa."
            
            d "{cps=25}Pelo visto, o gato comeu sua lingua. Fica muito sem graça assim!"
            d "{cps=25}Desse jeito então, eu não vou dizer quem eu sou."

            $ silencio = True
    
    if silencio != True:
        cf "{cps=25}Eu sou quem cuida de tudo isso aqui, sabia? E você caminhou para o lugar errado..\ndurante a noite, alias."
        cf "{cps=25}Afinal, {i}ele{/i} não gosta de visitas inesperadas."

        c "....!"

        cf "{cps=25}Agora você ta realmente me escutando. Que tal eu te ajudar ir pra casa?\nEu vou te mostrar o caminho."

        c "{cps=25}...Okay."
    else: 
        d "{cps=25}Eu sou quem cuida de tudo isso aqui, sabia? E você caminhou para o lugar errado.. \ndurante a noite, alias."
        d "{cps=25}Afinal, {i}ele{/i} não gosta de visitas inesperadas."
        c "....!"

        d "{cps=25}Agora você ta realmente me escutando. Que tal eu te ajudar ir pra casa?\nEu vou te mostrar o caminho."

        c "...{cps=25}Okay."
    
    jump cena_2_escolha

label cena_2_escolha:
    menu:
        "Confiar na voz e seguir a luz florescente":
            c "{cps=25}(Pelo visto, eu não tenho outra escolha...)"
            jump cena_3_canavial
        "Tentar achar outro caminho":
            if silencio != True:
                cf "{cps=25}Vai ficar ai que nem um poste esperando que alguem apareça pra te buscar?"
                cf "{cps=25}Vem logo, {i}ele{/i} ja sabe que você ta aqui."
                jump cena_2_escolha
            else: 
                d "{cps=25}Vai ficar ai que nem um poste esperando que alguem apareça pra te buscar?"
                d "{cps=25}Vem logo, {i}ele{/i} ja sabe que você ta aqui."
                jump cena_2_escolha


label cena_3_canavial:
    scene canavial_bifurcacao
    with dissolve
    play ambiente "sounds/noises/vento_canavial.mp3" fadein 2.0
    
    voice "sounds/falas/c5.mp3"
    cf "{cps=20}(sussurrando) Shhh... cuidado onde pisa. Ele odeia barulho.\nVocê tá fazendo tanto barulho..."
    
    voice "sounds/falas/c6.mp3"
    cf "{cps=30}Mais rápido! Por aqui!"

label cena_3_puzzle:
    menu:
        "Seguir a luz (Caminho da Comadre)":
            play sound "sounds/noises/passos_palha.wav"
            
            voice "sounds/falas/c7.mp3"
            cf "{cps=25}(Rindo) Oxe, tá aperreado? É só seguir o assobio!"
            
            play sound "sounds/noises/passos_palha.wav"
            jump cena_3_puzzle 
            
        "Seguir o som distante (Caminho Certo)":
            play sound "sounds/noises/passos_palha.wav"
            queue sound "sounds/noises/latido.wav"
            
            voice "sounds/falas/c8.mp3"
            cf "{cps=35}...Ei! Teimoso! O caminho não é esse! Você vai se arrepender.\nO Papa-Figo tá te esperando aí..."
            
            jump cena_5_final_estrada


label cena_5_final_estrada:
    stop ambiente fadeout 2.0
    
    scene estrada_distante
    with dissolve
    voice "sounds/falas/c15.mp3"
    cf "{cps=20}...Ah. ...Você achou o caminho. Que chato."
    
    scene estrada_perto
    with dissolve

    voice "sounds/falas/c16.mp3"
    cf "{cps=20}Tava tão divertido... Mas pode voltar quando quiser. Eu vou estar aqui. O Papa-Figo também..."
    
    scene varanda_casa
    with dissolve
    
    voice "sounds/falas/m2.mp3"
    m "{cps=35}Vem pra dentro! Rápido, vem!"

    voice "sounds/falas/c17.mp3"
    cf "{cps=10}...Até logo, figuinho."

    menu:
        "Entrar em casa correndo.":
            c "{nw}Mãe!"
            scene tela_branca
            with fade
            stop sound
            stop music
            stop ambiente
            "FIM"
            return

        "Olhar para trás.":
            scene olhando_atras
            with dissolve
        
            play sound "sounds/noises/assobio.wav"

            "FIM?"
            return