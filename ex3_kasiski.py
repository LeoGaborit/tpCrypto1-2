"""text entrée:
SBGZPLPSLA OZRLLDHAZT TSKUGGURHI UEFPGZCECA WBGOZSKHDB JACOKTDZMQ
IWVANVKEHE JIQBNQRRPP WWMDPPYIFI RSDRZTKUYF WEDSHTBQHB LTLVYFTAUE
AXRAXTNEDS TQHSVSLVZT TIIIPXRQBE ETDBOACEME QBNAJGYTKM MAPLYAVJKQ
CTYEVISQIH VMHBNASSRN GBKOWNZQXM YAUCIYSBGZ PLPSLANMKE THDVMQSDIA
VBOOPLCYWP XAJGYTKMNU HTFRBWLOGY GTROXMEHPA GIVFXNXTRQ TOGERSLVMO
GYGTROXMEH ZCFWSBAEOI WGXMCGZNJN XABTYESMTM CDGASMXYTT YOGAURIHVP
DAZFWRFUJP SMRHZNHARU ZEKHHJXUII JHEWSNTSRN GKUXDSJUVK UYEUKEUAGF
QLVTFPRQNP RRNQTIDRCD ZIXUXTFTKM SMIHVMDBOO PLCYDLBMCC VDFWSBJTVR
LHKPHCYEPM YAUTYESZKE TNKMHBNASS WOUJXQPKZN JUUPTRECUG VFDSPSWMSE
DFKEQQTHDL MEVWRHXNXC DZKRJLCYFW TEIRLCWMJB GOSLHUYUCP LRHUGFWEDA
WQIEIHVBHA ZWCONNEMOZ VIETHOKDUA TTRZOLPTZO QXNRDGQZUDN KOPIZTTMRT
LKGXPNRLBA OEDFTRBXZA VRRPKQIMAG FRLBNYHCIY

taille clé : 8
"""

def racisme_absolu(texteEntree : list) :

    # Initialisation
    i : int
    j : int
    k : int
    m : int
    n : int

    cleActuelle : str
    cleSupposee : str

    clesGardees = [str]

    # Valeurs
    i, j, m, n = 0, 0, 0, 0
    k = 2
    cleActuelle = ""
    cleSupposee = ""
    clesGardees = []

    for k in range(2, (len(texteEntree)//2) - 1) :          # On définit la taille de la clé, puis l'agrandit au cours du temps
        for i in range(0, (len(texteEntree)-k+1)):
            cleActuelle = ""
            for m in range(k) :
                cleActuelle += texteEntree[i+m]

            for j in range(i, len(texteEntree)-k+1) :
                cleSupposee = ""
                for n in range(k):
                    cleSupposee += texteEntree[j+n]

                if cleActuelle == cleSupposee :
                    print("Répétition trouvée : ", cleActuelle, " Indice : ", j)


kasiski = list("DLOMGKVVWQCUAPREOQJSTLMXQCUAPRVLFXRESIME")

racisme_absolu(kasiski)