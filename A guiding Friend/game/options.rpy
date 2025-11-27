define config.name = _("A Guiding Friend")


define gui.show_name = True


## A versão do jogo.

define config.version = "1.0 - Release"



define gui.about = _p("""
{b}A Guiding Friend{/b}
Uma experiência de horror psicológico no interior de Pernambuco. Criado como avaliação da segunda V.A de Principios de Programação.

Criado por: {b}Isaque Lucas e Renato Barros{/b}
Roteiro e Direção: {b}Isaque Lucas e Renato Barros{/b}

Agradecimentos Especiais:
- UFRPE
- Professor Cleyton
- ElevenLabs & Freesound

{i}Versão 1.0 - 2025{/i}
""")

define build.name = "AGuidingFriend"
define build.directory_name = "AGuidingFriend-1.0"

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.main_menu_music = "sounds/music/Gathering Darkness.mp3"
define config.enter_transition = dissolve
define config.exit_transition = dissolve


define config.intra_transition = dissolve



define config.after_load_transition = None



define config.end_game_transition = None


## Não existe uma variável para definir a transição usada quando o jogo começa.
## Em vez disso, use uma instrução with depois de mostrar a cena inicial.


## Gerenciamento de janelas ####################################################
##
## Isso controla quando a janela de diálogo é exibida. Se for "show", ela será
## sempre exibida. Se for "hide" (ocultar), ela só será exibida quando o diálogo
## estiver presente. Se for "auto", a janela será ocultada antes das declarações
## de cena e mostrada novamente quando o diálogo for exibido.
##
## Após o início do jogo, isso pode ser alterado com as instruções "window
## show", "window hide" e "window auto".

define config.window = "auto"


## Transições usadas para mostrar e ocultar a janela de diálogo

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Padrões de preferência ######################################################

## Controla a velocidade padrão do texto. O padrão, 0, é infinito, enquanto
## qualquer outro número é o número de caracteres por segundo a serem digitados.

default preferences.text_cps = 0


## O atraso padrão do encaminhamento automático. Números maiores levam a
## esperas mais longas, sendo 0 a 30 o intervalo válido.

default preferences.afm_time = 15


## Salvar diretório ############################################################
##
## Controla o local específico da plataforma onde o Ren'Py colocará os arquivos
## salvos para este jogo. Os arquivos de salvamento serão colocados em:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## Isso geralmente não deve ser alterado e, se for, deve ser sempre uma string
## literal, não uma expressão.

define config.save_directory = "AGuidingFriend-1763044378"


## Ícone #######################################################################
##
## O ícone exibido na barra de tarefas ou no dock.

define config.window_icon = "gui/window_icon.png"


## Configuração de compilação ##################################################
##
## Esta seção controla como o Ren'Py transforma o seu projeto em arquivos de
## distribuição.

init python:

    ## As funções a seguir aceitam padrões de arquivos. Os padrões de
    ## arquivos não diferenciam maiúsculas de minúsculas e são comparados com
    ## o caminho relativo ao diretório base, com e sem um /. Se vários padrões
    ## corresponderem, o primeiro será usado.
    ##
    ## Em um padrão:
    ##
    ## / é o separador de diretórios.
    ##
    ## * corresponde a todos os caracteres, exceto o separador de diretório.
    ##
    ## ** corresponde a todos os caracteres, inclusive o separador de diretório.
    ##
    ## Por exemplo, "*.txt" corresponde a arquivos txt no diretório base,
    ## "game/**.ogg" corresponde a arquivos ogg no diretório do jogo ou em
    ## qualquer um de seus subdiretórios e "**.psd" corresponde a arquivos psd
    ## em qualquer lugar do projeto.

    ## Classifique os arquivos como None (Nenhum) para excluí-los das
    ## distribuições criadas.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## Para arquivar arquivos, classifique-os como "arquivo".

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Os arquivos que correspondem aos padrões de documentação são duplicados
    ## em uma compilação de aplicativo para Mac, de modo que aparecem tanto no
    ## aplicativo quanto no arquivo zip.

    build.documentation('*.html')
    build.documentation('*.txt')


## É necessária uma chave de licença do Google Play para realizar compras no
## aplicativo. Ela pode ser encontrada no console do desenvolvedor do Google
## Play, em "Monetizar" > "Configuração de monetização" > "Licenciamento".

# define build.google_play_key = "..."


## O nome de usuário e o nome do projeto associados a um projeto itch.io,
## separados por uma barra.

# define build.itch_project = "renpytom/test-project"
