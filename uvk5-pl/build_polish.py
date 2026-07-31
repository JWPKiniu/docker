from pathlib import Path

root = Path('uv-k5-firmware-custom')
makefile = root / 'Makefile'
menu = root / 'ui' / 'menu.c'

# Build options requested by the user.
text = makefile.read_text(encoding='utf-8')
replacements = {
    'ENABLE_NOAA                   ?= 0': 'ENABLE_NOAA                   ?= 0',
    'ENABLE_VOICE                  ?= 0': 'ENABLE_VOICE                  ?= 0',
    'ENABLE_COPY_CHAN_TO_VFO       ?= 1': 'ENABLE_COPY_CHAN_TO_VFO       ?= 1',
    'ENABLE_SPECTRUM               ?= 1': 'ENABLE_SPECTRUM               ?= 1',
    'AUTHOR_STRING ?= EGZUMER': 'AUTHOR_STRING ?= KINIU_PL',
}
for old, new in replacements.items():
    if old not in text:
        raise RuntimeError(f'Missing Makefile marker: {old}')
    text = text.replace(old, new)
makefile.write_text(text, encoding='utf-8')

text = menu.read_text(encoding='utf-8')

# Left-side menu labels are limited to 6 visible characters.
labels = {
    '"Step"': '"Krok"',
    '"TxPwr"': '"MocTX"',
    '"RxDCS"': '"DCSodb"',
    '"RxCTCS"': '"CTodb"',
    '"TxDCS"': '"DCSnad"',
    '"TxCTCS"': '"CTnad"',
    '"TxODir"': '"KierTX"',
    '"TxOffs"': '"Offset"',
    '"W/N"': '"Szerok"',
    '"Scramb"': '"Szyfr"',
    '"BusyCL"': '"BlokTX"',
    '"Compnd"': '"Kompnd"',
    '"Demodu"': '"Demod"',
    '"ScAdd1"': '"Skan1+"',
    '"ScAdd2"': '"Skan2+"',
    '"ChSave"': '"ZapisK"',
    '"ChDele"': '"UsunK"',
    '"ChName"': '"NazwaK"',
    '"SList"': '"ListaS"',
    '"SList1"': '"Lista1"',
    '"SList2"': '"Lista2"',
    '"ScnRev"': '"TrybSk"',
    '"F1Shrt"': '"F1Krot"',
    '"F1Long"': '"F1Dlug"',
    '"F2Shrt"': '"F2Krot"',
    '"F2Long"': '"F2Dlug"',
    '"M Long"': '"MDlug"',
    '"KeyLck"': '"BlokKl"',
    '"TxTOut"': '"LimitTX"',
    '"BatSav"': '"OszczB"',
    '"Mic"': '"Mikrof"',
    '"MicBar"': '"PasekM"',
    '"ChDisp"': '"WyswK"',
    '"POnMsg"': '"Start"',
    '"BatTxt"': '"TekstB"',
    '"BackLt"': '"Podsw"',
    '"BLMin"': '"PodMin"',
    '"BLMax"': '"PodMax"',
    '"BltTRX"': '"PodTRX"',
    '"Beep"': '"Dzwiek"',
    '"Roger"': '"Roger"',
    '"STE"': '"Koniec"',
    '"RP STE"': '"KoncRP"',
    '"1 Call"': '"Wywol1"',
    '"ANI ID"': '"ANI ID"',
    '"UPCode"': '"KodGor"',
    '"DWCode"': '"KodDol"',
    '"PTT ID"': '"ID PTT"',
    '"D ST"': '"DTMFst"',
    '"D Resp"': '"DTMFod"',
    '"D Hold"': '"DTMFcz"',
    '"D Prel"': '"DTMFop"',
    '"D Decd"': '"DTMFdk"',
    '"D List"': '"DTMFlst"',
    '"D Live"': '"DTMFna"',
    '"AM Fix"': '"AM Nap"',
    '"BatVol"': '"NapBat"',
    '"RxMode"': '"TrybRX"',
    '"Sql"': '"Squelc"',
    '"F Lock"': '"BlokPas"',
    '"Tx 200"': '"TX 200"',
    '"Tx 350"': '"TX 350"',
    '"Tx 500"': '"TX 500"',
    '"350 En"': '"Odb350"',
    '"ScraEn"': '"SzyfrW"',
    '"FrCali"': '"KalFr"',
    '"BatCal"': '"KalBat"',
    '"BatTyp"': '"TypBat"',
    '"Reset"': '"Reset"',
}
for old, new in labels.items():
    text = text.replace(old, new)

# Values and explanatory texts shown on the right side.
values = {
    '"LOW"': '"NISKA"',
    '"MID"': '"SREDN"',
    '"HIGH"': '"WYSOK"',
    '"WIDE"': '"SZEROK"',
    '"NARROW"': '"WASKI"',
    '"OFF"': '"WYL"',
    '"ON"': '"WL"',
    '"MAIN\\nONLY"': '"TYLKO\\nGLOWNY"',
    '"DUAL RX\\nRESPOND"': '"PODWOJNY RX\\nODPOWIEDZ"',
    '"CROSS\\nBAND"': '"KRZYZOWY\\nPASMO"',
    '"MAIN TX\\nDUAL RX"': '"GLOWNY TX\\nPODWOJNY RX"',
    '"TIMEOUT"': '"CZAS"',
    '"CARRIER"': '"NOSNA"',
    '"STOP"': '"STOP"',
    '"FREQ"': '"CZEST"',
    '"CHANNEL\\nNUMBER"': '"NUMER\\nKANALU"',
    '"NAME"': '"NAZWA"',
    '"NAME\\n+\\nFREQ"': '"NAZWA\\n+\\nCZEST"',
    '"DO\\nNOTHING"': '"NIC\\nNIE ROB"',
    '"RING"': '"DZWON"',
    '"REPLY"': '"ODPOW"',
    '"BOTH"': '"OBA"',
    '"UP CODE"': '"KOD GORA"',
    '"DOWN CODE"': '"KOD DOL"',
    '"UP+DOWN\\nCODE"': '"KOD GORA+DOL"',
    '"FULL"': '"PELNY"',
    '"MESSAGE"': '"NAPIS"',
    '"VOLTAGE"': '"NAPIECIE"',
    '"NONE"': '"BRAK"',
    '"VFO"': '"VFO"',
    '"ALL"': '"WSZYST"',
    '"DISABLE\\nALL"': '"ZABLOKUJ\\nWSZYSTKO"',
    '"UNLOCK\\nALL"': '"ODBLOKUJ\\nWSZYSTKO"',
    '"PERCENT"': '"PROCENT"',
    '"FLASH\\nLIGHT"': '"LATARKA"',
    '"POWER"': '"MOC"',
    '"MONITOR"': '"MONITOR"',
    '"SCAN"': '"SKAN"',
    '"LOCK\\nKEYPAD"': '"BLOKADA\\nKLAWISZY"',
    '"SWITCH\\nVFO"': '"ZMIEN\\nVFO"',
    '"SWITCH\\nDEMODUL"': '"ZMIEN\\nDEMOD"',
    '"SURE?"': '"PEWNY?"',
    '"WAIT!"': '"CZEKAJ!"',
    '"READ\\nMANUAL"': '"CZYTAJ\\nINSTR."',
    '"AUTO"': '"AUTO"',
}
for old, new in values.items():
    text = text.replace(old, new)

menu.write_text(text, encoding='utf-8')
print('Polish localization patch applied.')
