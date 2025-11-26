init:
    $ renpy.music.register_channel("ambiente", mixer="sfx", loop=True)

    define p = Character("Professor", color="#FFFFFF") 
    define c = Character("\'Criança\'", color="#FFFFFF", kind=adv)
    define cf = Character("Comadre Florzinha", what_color="#E0FFFF")
    define d = Character("???", color="#FFFFFF")
    define m = Character("Mãe", color="#FFCCCC")
    define flash_black = Fade(0.1, 0.0, 0.5, color="#000") 
    define flash_susto = Fade(0.1, 0.0, 0.5, color="#fff")

    image sala = "images/bg sala.png"
    image desenho = "images/bg figo.png"
    image tela_preta = "images/tela preta.jpg"
    image rua_clara = "images/rua_clara.PNG" 
    image rua_escura = "images/apagado.png"
    image comadre = "images/comadre.png"
    image canavial_bifurcacao = "images/canavial_bifurcacao.png"
    image usina = "images/usina.png"
    image empilho = "images/empilho.png"
    image estrada_distante = "images/estrada_distante.png"
    image estrada_perto = "images/estrada_perto.png"
    image varanda_casa = "images/varanda_casa.png"
    image olhando_atras = "images/olhando_atras.png"
    image papa_figo_jumpscare = "images/papa_figo_jumpscare.png"
    image oferenda_cerca = "images/oferenda_cerca.png"
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

    voice "sounds/falas/oxente.wav"
    d "{cps=25}Oxente, mas olha só quem decidiu aparecer por aqui.."
    voice "sounds/falas/perdeu.wav"
    d "{cps=25}Você se perdeu, né? Que problemão."

    jump cena_2_resposta

label cena_2_resposta:
    menu: 
        "Responder a voz":
            c "{cps=25}Quem e você?"

            voice "sounds/falas/intro1.wav"
            d "{cps=25}Você nunca ouviu as historias? Eu sou alguem que você conhece muito bem."

            voice "sounds/falas/intro2.wav"
            cf "{cps=25}A Comadre Florzinha."
            show comadre at Transform(xpos=0.8, ypos=0.40, zoom=0.3)
            with dissolve
        "Ficar em silêncio":
            "Você decide ficar em silencio, ignorando seja-la quem for\npara continuar procurando um caminho de volta para casa."
            voice "sounds/falas/gato.wav"
            d "{cps=25}Pelo visto, o gato comeu sua lingua. Fica muito sem graça assim!"
            voice "sounds/falas/sem_ajuda.wav"
            d "{cps=25}Desse jeito então, você vai ficar ai sem ajuda nenhuma."
            c "{cps=25}...(Eu vou ter que responder a ela se eu quero encontrar o caminho de volta.)"
            jump cena_2_resposta
    
    voice "sounds/falas/cuida.wav"
    cf "{cps=25}Eu sou quem cuida de tudo isso aqui, sabia? E você caminhou para o lugar errado..\ndurante a noite, alias."
    voice "sounds/falas/visitas.wav"
    cf "{cps=25}Afinal, {i}ele{/i} não gosta de visitas inesperadas."
    c "....!"
    voice "sounds/falas/escutando.wav"
    cf "{cps=25}Agora você ta realmente me escutando. Que tal eu te ajudar ir pra casa?\nEu vou te mostrar o caminho."
    c "{cps=25}...Okay."
    
    jump cena_2_escolha

label cena_2_escolha:
    menu:
        "Confiar na voz e seguir a luz florescente":
            c "{cps=25}(Pelo visto, eu não tenho outra escolha...)"
            jump cena_3_canavial
        "Tentar achar outro caminho":
            voice "sounds/falas/poste.wav"
            cf "{cps=25}Vai ficar ai que nem um poste esperando que alguem apareça pra te buscar?\nVem logo, {i}ele{/i} ja sabe que você ta aqui."
            jump cena_2_escolha


label cena_3_canavial:
    scene canavial_bifurcacao
    with dissolve
    play ambiente "sounds/noises/vento_canavial.mp3" fadein 2.0
    
    voice "sounds/falas/c5.mp3"
    cf "{cps=20}(sussurrando) Shhh... cuidado onde pisa. Ele odeia barulho.\nVocê tá fazendo tanto barulho..."

    voice "sounds/falas/c6.mp3"
    cf "{cps=30}Mais rápido! Por aqui!"

default erros_canavial = 0

label cena_3_puzzle:
    menu:
        "Seguir a luz":
            play sound "sounds/noises/passos_palha.wav"
            
            $ erros_canavial += 1
            
            if erros_canavial >= 2:
                jump final_ruim_canavial
            else:
                voice "sounds/falas/c7.mp3"
                cf "{cps=25}Oxe, tá aperreado? É só seguir o assobio!"
                #adicionar voz
                cf "{cps=25}Não venha por esse caminho de novo, ou esse é o caminho certo?..."
                play sound "sounds/noises/passos_palha.wav"
                jump cena_3_puzzle 
            
        "Seguir o som distante":
            play sound "sounds/noises/passos_palha.wav"
            queue sound "sounds/noises/latido.wav"
            
            voice "sounds/falas/c8.mp3"
            cf "{cps=35}...Ei! Teimoso! O caminho não é esse! Você vai se arrepender..."
            
            jump cena_4_usina

label final_ruim_canavial:
    stop music fadeout 0.5
    stop ambiente fadeout 0.5
    stop sound
    
    scene tela_preta
    with dissolve
    pause 1.0

    play sound "sounds/noises/susto_ataque.wav" volume 1.0 
    
    show papa_figo_jumpscare at truecenter
    with hpunch 

    with flash_susto

    pause 0.2 
    hide papa_figo_jumpscare
    scene tela_preta
    "..."
    "GAME OVER"
    return
label cena_4_usina:
    scene usina
    with fade

    "{cps=30}Seguindo o som distante, você chega em uma usina. \nPelo visto o jeito vai ser passar por ela."

    voice "sounds/falas/mora.wav"
    cf "{cps=25}E ai, gostou? E aqui onde eu moro, sabe. Muitas outras pessoas moram aqui tambem... incluindo {i}ele{/i}."
    c "{cps=30}Como que eu faço pra atravessar então? Eu.. não quero ficar aqui."
    voice "sounds/falas/explorar.wav"
    cf "{cps=25}Oxi, nunca teve aquele espirito de explorar não? Talvez você encontre algo la."


    scene tela_preta
    with fade

    play sound "sounds/noises/passos_palha.wav" loop
    "{cps=30}Chegando mais perto da usina, você tenta encontrar um caminho pra sair daqui."
    stop sound
    
    jump cena_4_escolha

label cena_4_escolha:
    menu:
        "Tentar abrir a porta principal e entrar":
            play sound "sounds/noises/porta.wav"
            "{cps=30}Você tenta abrir a porta, batendo nela com toda força que você tem pra tentar abrir."
            c "{cps=25}Trancado.. eu não vou conseguir entrar."
            voice "sounds/falas/barulhao.wav"
            cf "{cps=25}Continua batendo ai, faz um barulhão pra tu ver.. Fica melhor pra ele te achar."
            jump cena_4_escolha
        "Se esconder em algum canto e esperar virar dia":
            stop ambiente fadeout 2.0
            c "{cps=25}(Tem um monte de coisas por ali... e se eu tentar me esconder la?)"
            show empilho
            "{cps=30}Você corre para tentar achar algum lugar para esconder nesse\nempilho de coisas velhas e enferrujadas."
            cf "{cps=25}Vai ficar parado ai ate ele chegar aqui, ne? Você vai ser bem saboroso pra ele te devorar."
            play sound "sounds/noises/windchime.mp3" volume 2.0
            cf "{cps=25}...Ele chegou."
            cf "{cps=25}Corre, agora!"
            
    scene tela_preta
    "{cps=30}Ouvindo a voz, você começa a correr em uma direção aleatoria no meio da escuridão."
    jump cena_5_final_estrada

label cena_5_final_estrada:
    scene estrada_distante
    with dissolve
    voice "sounds/falas/c15.mp3"
    cf "{cps=20}...Ah. ...Você achou o caminho de volta. Que chato."
    
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
        "Entrar em casa correndo":
            c "{nw}Mãe!"
            scene tela_branca
            with fade
            stop sound
            stop music
            stop ambiente
            "FIM"
            return

        "Olhar para trás com medo":
            scene olhando_atras
            with dissolve
            play sound "sounds/noises/assobio.wav" 
            "FIM?"
            return

        "Deixar um doce na cerca para ela":
            stop music fadeout 2.0
            stop ambiente fadeout 2.0
            
            c "{cps=20}(Pensamento) Minha avó dizia... que ela é vaidosa. Que ela gosta de agrados."
            "Você para no portão de casa. Em vez de entrar, você tira um doce do bolso e coloca sobre a cerca de madeira."
            
            play sound "sounds/noises/vento_canavial.wav" fadein 2.0
            jump final_oferenda_cena5
label final_oferenda_cena5:
    scene oferenda_cerca
    with dissolve
    
    "O vento para de repente. O silêncio é total."
    
    play sound "sounds/noises/mastigar.wav"
    
    with Pause(1.5)
    
    voice "sounds/falas/c_oferenda_5.mp3"
    cf "{cps=20}Oxe... Tu lembrou de mim? Tu deixou um docinho?"
    
    play music "sounds/music/folclore_magico.wav" fadein 3.0
    
    scene olhando_atras
    with dissolve
    
    voice "sounds/falas/c_oferenda_6.mp3"
    cf "{cps=25}Ninguém nunca deixa nada... Todo mundo só corre. Só tu que não."
    
    "Você vê a porta da sua casa aberta. A luz quente. Sua mãe te esperando."
    "Mas a escuridão da estrada parece... mais acolhedora agora."
    
    voice "sounds/falas/c_oferenda_7.mp3"
    cf "{cps=20}Não entra lá não, figuinho. Lá dentro o tempo passa. Tu vai crescer, vai ficar chato..."
    
    voice "sounds/falas/c_oferenda_8.mp3"
    cf "{cps=20}Vem comigo. Eu sei onde tem mel. Eu sei onde o rio nasce. A gente brinca pra sempre."
    
    scene tela_preta
    with dissolve
    
    "Você dá as costas para a luz da varanda."
    "E caminha de volta para a escuridão."
    
    "FIM..."
    return