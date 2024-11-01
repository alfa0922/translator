import pyautogui
from sqlalchemy import create_engine
import pandas as pd
from utilTranslatorProj.utilTools import *


# RETORNA O COMPRIMENTO DA FALA
def retCompFile(filepath):

    try:
        audio = MP3(filepath)

        # RETORNA COMPRIMENTO
        compFile = audio.info.length

        return compFile

    except FileNotFoundError:
        print("Arquivo não encontrado!")
        return None


# GERA O NOME ALEATORIO CONTROLE VOZ
def retFileName():
    filename = random.random().__str__()
    filename = "mensagem"f'{filename[2:-7]}.mp3' # GERA NOME

    return filename


# TRADUZ PT -> EN ou EN -> PT
def translate(pvoice, pTranslate, filename, psleep=0):
    translator = Translator()

    insConv = dict()
    try:
        insConv[pTranslate] = pvoice
        filename = sysPurgeDir + filename

        # TRADUCAO
        traduzido = translator.translate(pvoice, dest=pTranslate).text
        if pTranslate == vTransLangE:

            vLang = vTransLangP

        else:
            vLang = vTransLangE

        insConv[vLang] = traduzido

        vConvert = gTTS(text=traduzido, lang=pTranslate, slow=False) # AUDIO
        vConvert.save(filename)

        pygame.mixer.init()
        pygame.mixer.music.load(filename)

        pygame.mixer.music.play()

        # ARMAZENA DADOS PARA TREINO
        def capVoice(vTrain):
            vSyncEngine = create_engine(vOraSqlAlch)

            for i, h in vTrain.items():
                vData  = vTrain[i]
                vData  = vData.replace("'", "''")
                vidmsg = random.random().__str__()[8:-7]

                vIns = retDataIns(vData, i, int(vidmsg))

                df = pd.read_sql(vIns, vSyncEngine)
                df.to_sql(name='hist_msg',
                          schema='app',
                          con=vSyncEngine,
                          if_exists="append",
                          index=False)

        capVoice(insConv)

    except Exception:
        raise


# CONFIGURA SINCRONIA DA COMUNICACAO - TESTE DINAMICO
def retConfig(filepath):
    comp = round(retCompFile(filepath))

    return comp


# ENVIA E RECEBE VOZ
class voiceGateWay:
    def __init__(self, pTransLang):
        self.TransLang = pTransLang

        print("Iniciado Gateway de voz",
              self.TransLang)

    def sendRceiceVoz(self, pvoice, pTransLang, psleep=0):
        nomeFile = retFileName()

        translate(pvoice,
                  pTransLang,
                  nomeFile,
                  psleep)

        filePath = sysPurgeDir + nomeFile

        if psleep > 0:
            print("Mic Fechado.")

        return filePath


# MANUTENCAO DOS ARQUIVOS DO SISTEMA
def initEnv(dirlist):
    dir = os.listdir(dirlist)

    for file in dir:
        os.remove(str(dirlist + file))


# PARAMETRIZA IDIOMA e Synch
def sendVoz(pTransLang, pboolean=False, psleep=0):

    if pboolean:
        # INICIA O VOICE GATEWAY
        initEnv(sysPurgeDir)

    # ATIVA O MIC DO WINDOWS
    time.sleep(psleep)
    pyautogui.hotkey(vHotKey, vKey)
    print("Mic Aberto:")

    p = voiceGateWay(pTransLang) # SETUP IDIOMA TRAD

    voice = input() # CAPTA A VOZ USUARIO E ENVIA
    msgService = p.sendRceiceVoz(voice, p.TransLang, psleep)

    return msgService