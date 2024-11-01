from utilTranslatorProj.utilTools import *
vboolean = True
def call(vboolean):


    from sqlalchemy import create_engine
    import pandas as pd
    import FreeSimpleGUI as sg
    import utilTranslatorProj.interPrete as interPrete


    vButton = sg.popup_yes_no("Iniciar o Intérprete PT para " + vTransLangE.upper() + '?', modal=True)

    if vButton == 'Yes':
        # FALA EM PORTUGUES O OUVINTE RECEBE EM INGLES - PT > ENG
        # FALA EM INGLES E O OUVINTE RECEBE EM PORTUGUES - ENG > PT
        interPrete.interprete(vboolean)
        vboolean = False
    else:
        sg.popup("Cancelado pelo usuário")

call(vboolean)













