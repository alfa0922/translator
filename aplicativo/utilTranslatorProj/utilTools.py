import pygame
from gtts import gTTS
import random
import codecs
from googletrans import Translator
import time
import os
from mutagen.mp3 import MP3


# RETORNA O DIRETORIO PADRAO DO USUARIO
def get_user_path() -> str:

    return (os.path.expanduser('~')
           .replace('C:',
                    '')
            .replace('\\',
                     '/') + '/')


# CONECTA BANCO DE DADOS ORACLE 21c
def conOracleDB():
    import oracledb
    oracledb.init_oracle_client()

    con = oracledb.connect(user='app',
                           password='oracle',
                           dsn='localhost/XEPDB1')
    return con


def retDataIns(pData, pTranslate, pidmsg):

    vSql = "SELECT RTRIM('" + f'{pData}' + "')                  AS TEXT,"     \
                 + "SYSDATE                                     AS DATA_MGS," \
                 + "USER                                        AS USUARIO,"  \
                 + "DECODE('"  + f'{pTranslate}' + "','pt',0,1) AS FLG_LANG," \
                 + f'{pidmsg}' +                              " AS IDMSG "    \
         + "FROM   dual"

    return vSql


# PARAMETROS
vTransLangP = 'pt'
vTransLangE = 'en'
vtempPathMs = "/PycharmProjects/pythonProject/mensagens/"
vOraSqlAlch = "oracle+oracledb://app:oracle@localhost/?service_name=XEPDB1"
sysPurgeDir = get_user_path() + vtempPathMs
vboolean    = True

# VARIAVEIS DO SISTEMA
vHotKey = 'winleft'
vKey = 'h'