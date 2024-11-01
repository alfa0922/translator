from voiceGateway import *

def interprete(pboolean):

    # FALA EM PORTUGUES O OUVINTE RECEBE EM INGLES - PT > ENG
    msgService = sendVoz(vTransLangE, pboolean=pboolean)
    #vboolean = False

    conf = retConfig(msgService)  # TRATAMENTO SINCRONIA DA COMUNICACAO

    # FALA EM INGLES E O OUVINTE RECEBE EM PORTUGUES - ENG > PT
    sendVoz(vTransLangP, psleep=conf)