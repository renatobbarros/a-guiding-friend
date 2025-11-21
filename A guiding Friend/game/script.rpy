init:
    $ renpy.music.register_channel("ambiente", mixer="sfx", loop=True)

    define p = Character("Professor", color="#FFFFFF") 
    define c = Character("\'Criança\'", color="#FFFFFF", kind=adv)
    define cf = Character("Comadre Florzinha", what_color="#E0FFFF") 
    define m = Character("Mãe", color="#FFCCCC")

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
    p "{cps=25}A Mata, como muitos de vocês sabem, guarda segredos profundos...{w=0.4} e um deles é sobre a famosa Usina Velha."
    
    voice "sounds/falas/p2.mp3"
    p "{cps=25}Um ser misterioso habita essas sombras: o Homem do Saco,{w=0.3} também conhecido como o Velho,{w=0.2} ou ainda o Papa-Figo."
    
    show desenho at Transform(xzoom=1.0, yzoom=0.8)
    with dissolve
    
    voice "sounds/falas/p3.mp3"
    p "{cps=28}Ele é uma figura que provoca tanto medo quanto curiosidade.{w=0.4} A lenda nos conta que ele não aparece sem motivo."
    
    voice "sounds/falas/p4.mp3"
    p "{cps=28}O Velho está em busca de algo muito específico...{w=0.5} fígado!{w=0.2} Isso mesmo, fígado!{w=0.4} E é aí que entra a Comadre Florzinha, uma figura protetora da nossa história."
    
    voice "sounds/falas/p5.mp3"
    p "{cps=25}Ela guia e cuida das pessoas que, porventura,{w=0.3} se encontram perdidas ou em perigo nas matas.{w=0.4} Lembrem-se: essa lenda não é apenas uma história."
    
    voice "sounds/falas/p6.mp3"
    p "{cps=25}É um ensinamento sobre respeito à natureza e os mistérios que ela abriga.{w=0.4} Vamos discutir juntos o que essa lenda nos ensina sobre coragem e proteção!"
    
    with Pause(1.5)
    
    p "{cps=15}...ele vem. O Homem do Saco, o Velho. O Papa-Figo. Ele procura...{w=1.5} {i}fígado{/i}."

    scene tela_preta
    with dissolve
    
    stop music fadeout 1.0
    play ambiente "sounds/noises/grilos.wav" fadein 2.0
    play sound "sounds/noises/respiracao ofegante.wav" loop

    c "{cps=20}...Mãe? Pai?"
    c "{cps=15}...Já tá tarde."

    scene rua_clara
    with dissolve

    play sound "sounds/noises/som eletrico.wav" loop fadein 0.5

    c "{cps=25}...A história do professor..."
    play sound "sounds/noises/luz caindo.flac" 

    scene rua_escura
    with dissolve

    stop sound

    play sound "sounds/noises/respiracao ofegante.wav" loop

    c "{nw}NÃO!" 
    c "{cps=15}...Eu tô sozinho(a)."
    
    jump cena_3_canavial


label cena_3_canavial:
    scene canavial_bifurcacao
    with dissolve
    play ambiente "sounds/noises/vento_canavial.mp3" fadein 2.0
    
    voice "sounds/falas/c5.mp3"
    cf "{cps=20}(sussurrando) Shhh... cuidado onde pisa. Ele odeia barulho. Você tá fazendo tanto barulho..."
    
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
            cf "{cps=35}...Ei! Teimosa! O caminho não é esse! Você vai se arrepender. O Papa-Figo tá te esperando aí..."
            
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