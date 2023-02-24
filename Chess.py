import math


def lisans_no_al(lisans_no_liste): #Lisans Numarası Alma fonksiyonu
    while True:
        try:
            lisans_no = int(input('\nLisans numarasını giriniz: '))
            if lisans_no in lisans_no_liste:
                print('\nBu lisans numarası daha önce girilmiş, lütfen başka bir lisans numarası giriniz!!')
            else:
                return lisans_no
        except ValueError:
            print('\nYanlış veri! Lütfen tekrar deneyiniz!!')


def ad_soyad(): #Ad soyad alma fonksiyonu
    ad_soyad = str(input('\nAd Soyad: '))
    ad_soyad = ad_soyad.replace('i', 'İ')
    return ad_soyad.upper()


def elo_al(): #Elo alma fonksiyonu
    min = 0

    while True:
        try:
            elo = int(input('\nBir ELO giriniz: '))
            while min < elo < 1000 or elo < min:
                elo = int(input("ELO 0,1000 veya 1000'den büyük bir sayı olmalı, Lütfen tekrar giriniz: "))

            if elo == ' ' or elo == min:
                elo = min
            return elo
        except ValueError:
            print('Yanlış veri, Lütfen tekrar giriniz!!!')


def ukd_al(): #Ukd alma fonksiyonu
    minimum_puan = 0
    while True:
        try:
            ukd = int(input('\nBir UKD giriniz: '))

            while minimum_puan < ukd < 1000 or ukd < minimum_puan:
                ukd = int(input("UKD 0,1000 veya 1000'den büyük bir sayı olmalı, Lütfen tekrar giriniz: "))

            if ukd == ' ' or ukd == 0:
                ukd = minimum_puan

            return ukd
        except ValueError:
            print('Yanlış veri, Lütfen tekrar giriniz!!!')


def tur_sayisi(oyuncu_sayisi): #Tur sayısı alma fonksiyonu
    while True:
        try:
            tur = int(input('\nTur sayısını giriniz: '))

            if tur < math.ceil(math.log2(oyuncu_sayisi)) or tur > (oyuncu_sayisi - 1):
                print('Yanlış veri, lütfen tur sayısını giriniz!!!')
            else:
                return tur
        except ValueError:
            print('Yanlış veri, Lütfen tekrar giriniz!!!')


def renk_al(): #İlk oyuncunun rengini alma fonksiyonu
    while True:
        renk = input('\nİlk oyuncunun rengini giriniz(s/b): ')
        if renk.lower() == 'b' or renk.lower() == 's':
            return renk.lower()
        else:
            print('Yanlış veri, ik oyuncunun rengini giriniz!!!')


def tablo_yaz(x): # Eşleştirme tablosu yazma fonksiyonu
    print(f'\n{x}. Tur Eşleştirme Listesi: ')
    print("""      Beyazlar            Siyahlar""")
    print("""MNo BSNo   LNo Puan - Puan   LNo BSNo""")
    print("""--- ---- ----- ----   ---- ----- ----""")


def mac_sonucu(x): #Maç sonucu alma fonksiyonu
    a = int(input(f'\n{x}. Masanın mac sonucunu giriniz: '))

    while True:
        try:
            if not 0 <= a <= 5:
                a = int(input('Maç sonucu 0 ile 5 arasında olmalıdır, lütfen tekrar giriniz: '))
            else:
                return a
        except ValueError:
            print('Yanlış veri Lütfen tekrar deneyiniz!!!')


def oyuncu_ara1(oyuncu, oyuncu_renk, c, liste, oyuncu_sayisi, x): # Verilen oyuncuya 1.1'ine göre rakip bulma fonksiyonu
    rakip = 'n'
    ters_renk = ''
    kriter1 = list()

    if oyuncu_renk == 'b':
        ters_renk = 's'
    elif oyuncu_renk == 's':
        ters_renk = 'b'

    for i in range(oyuncu_sayisi):
        if liste[i][6][x + 1] != oyuncu_renk and liste[i][6][x + 1] != ters_renk and liste[i][6][x + 1] != '':
            if liste[i][4] != oyuncu[4] and liste[i][0] == c and liste[i][4] not in oyuncu[7]:
                if liste[i][6].count(oyuncu_renk) - liste[i][6].count(ters_renk) != 2:
                    if liste[i][6][x] == ters_renk or liste[i][6][x] == '':
                        if liste[i][6][x] == ters_renk:
                            kriter1.append(liste[i])
                        else:
                            if x >= 1 and liste[i][6][x - 1] == ters_renk:
                                kriter1.append(liste[i])
                            elif x < 1:
                                kriter1.append(liste[i])
    if len(kriter1) > 0:
        for a in kriter1:
            if a[6][x] != '':
                rakip = a
                rakip[6][x+1] = oyuncu_renk
                return rakip
            else:
                rakip = a
                rakip[6][x+1] = oyuncu_renk
                return rakip
    else:
        rakip = 'n'
    return rakip


def oyuncu_ara2(oyuncu,oyuncu_renk,c,liste,oyuncu_sayisi,x): #Verilen oyuncuya 1.2'ye göre rakip bulma fonksiyonu
    rakip = 'n'
    ters_renk = ''
    kriter1 = []

    if oyuncu_renk == 'b':
        ters_renk = 's'
    elif oyuncu_renk == 's':
        ters_renk = 'b'

    for i in range(oyuncu_sayisi):
        if liste[i][4] != oyuncu[4] and liste[i][0] == c:
            if liste[i][6][x + 1] != oyuncu_renk and liste[i][6][x + 1] != ters_renk and liste[i][6][x + 1] != '':
                if liste[i][6].count(oyuncu_renk) - liste[i][6].count(ters_renk) != 2:
                    if liste[i][6][x] == oyuncu_renk or liste[i][6][x] == '':
                        if liste[i][6][x] == oyuncu_renk and liste[i][4] not in oyuncu[7]:
                            kriter1.append(liste[i])
                        elif liste[i][6][x] == '':
                            if x >= 1 and liste[i][6][x-1] == oyuncu_renk and liste[i][4] not in oyuncu[7]:
                                kriter1.append(liste[i])
                            elif x < 1:
                                kriter1.append(liste[i])

    if x < 1:
        if len(kriter1) != 0:
            rakip = kriter1[0]
            rakip[6][x+1] = oyuncu_renk
            return rakip
    else:
        for a in kriter1:
            if a[6][x] == '':
                rakip_renkleri = []
                for q in a[6]:
                    if q == 'b' or q == 's':
                        rakip_renkleri.append(q)
                if len(rakip_renkleri) < 2:
                    rakip = a
                    rakip[6][x+1] = oyuncu_renk
                    break
                else:
                    if rakip_renkleri[-1] != rakip_renkleri[-2]:
                        rakip = a
                        rakip[6][x+1] = oyuncu_renk
                        break
            elif a[6][x] == oyuncu_renk:
                rakip_renkleri = []
                for q in a[6]:
                    if q == 'b' or q == 's':
                        rakip_renkleri.append(q)
                if len(rakip_renkleri) < 2:
                    rakip = a
                    rakip[6][x + 1] = oyuncu_renk
                    break
                else:
                    if rakip_renkleri[-1] != rakip_renkleri[-2]:
                        rakip = a
                        rakip[6][x + 1] = oyuncu_renk
                        break

    return rakip


def oyuncu_ara3(oyuncu, oyuncu_renk, c, liste, oyuncu_sayisi, x): #Verilen oyuncuya 1.3'üne göre rakip bulma fonksiyonu
    rakip = 'n'
    ters_renk = ''
    kriter1 = list()

    if oyuncu_renk == 'b':
        ters_renk = 's'
    elif oyuncu_renk == 's':
        ters_renk = 'b'

    for i in range(oyuncu_sayisi):
        if liste[i][6][x + 1] != oyuncu_renk and liste[i][6][x + 1] != ters_renk and liste[i][6][x + 1] != '':
            if liste[i][4] != oyuncu[4] and liste[i][0] == c:
                if liste[i][6].count(ters_renk) - liste[i][6].count(oyuncu_renk) != 2:
                    if liste[i][6][x] == oyuncu_renk or liste[i][6][x] == '':
                        if liste[i][4] not in oyuncu[7]:
                            if liste[i][6][x] == oyuncu_renk:
                                kriter1.append(liste[i])
                            elif liste[i][6][x] == '':
                                if x < 1:
                                    kriter1.append(liste[i])
                                else:
                                    if liste[i][6][x-1] == oyuncu_renk:
                                        kriter1.append(liste[i])
        if len(kriter1) > 0:
            rakip = kriter1[0]
            rakip[6][x + 1] = ters_renk
            return rakip
        else:
            rakip = 'n'
    return rakip



def BH1(liste,oyuncu,tur,iki_mi):  #Verilen oyuncunun BH1'ini ve BH2'sini hesaplama fonksiyonu
    rakip_puanlari = []
    bh1 = 0
    min = 0
    min2 = 0
    hayali_rakip = []

    if '' not in oyuncu[6] and 'r' not in oyuncu[8] and 'k' not in oyuncu[8]:
        for i in oyuncu[7]:
            for q in liste:
                if q[4] != oyuncu[4]:
                    if i == q[4]:
                        rakip_puanlari.append(q[0])
        c = sorted(rakip_puanlari,reverse=True)
        for a in rakip_puanlari:
            bh1 += a
        min = c[-1]
        min2 = c[-2]
        bh1 -= min
        if iki_mi:
            bh1 -= min2
            return bh1
        return bh1
    else:
        for i in oyuncu[7]:
            index = oyuncu[7].index(i)
            for q in liste:
                    if q[4] == i:
                        if oyuncu[8][index] == 'r' and q[8][index] == 'k':
                            break
                        elif oyuncu[8][index] == 'k' and q[8][index] == 'r':
                            break
                        elif oyuncu[8][index] == 'k' and q[8][index] == 'k':
                            break
                        rakip_puanlari.append(q[0])

        for a in range(tur):
            if oyuncu[8][a] == 'r' or oyuncu[8][a] == 'k' or oyuncu[8][a] == '-':
                index = a
                rakip = 0

                for e in range(index):
                    if e != index:
                        if oyuncu[8][e] == '1':
                            rakip += 1
                        elif oyuncu[8][e] == '½':
                            rakip += 0.5
                        elif oyuncu[8][e] == 'r':
                            rakip += 1
                        elif oyuncu[8][e] == '-':
                            rakip += 1
                kalan = (tur-1) - index
                sonuc = kalan * (0.5)
                rakip += sonuc
                hayali_rakip.append(rakip)

        rakip_puanlari.extend(hayali_rakip)
        rakip_puanlari = sorted(rakip_puanlari,reverse=True)
        min = rakip_puanlari[-1]
        min2 = rakip_puanlari[-2]
        for q in rakip_puanlari:
            bh1 += q
        bh1 = bh1-min
        if iki_mi:
            bh1 = bh1-min2
            return bh1
        return bh1


def sb(liste,oyuncu,tur): #Verilen oyuncunun sb'sini hesaplama fonksiyonu
    sb = 0
    rakip = 0
    rakip_puanlari = []
    hayali_rakip  = []

    if '' not in oyuncu[6] and 'r' not in oyuncu[8] and 'k' not in oyuncu[8]:
        for i in range(len(oyuncu[6])):
            for q in liste:
                if q[4] != oyuncu[4]:
                    if oyuncu[8][i] == '½':
                        if oyuncu[7][i] == q[4]:
                            rakip_puanlari.append(q[0]/2)
                    elif oyuncu[8][i] == '1':
                        if oyuncu[7][i] == q[4]:
                            rakip_puanlari.append(q[0])
        for a in rakip_puanlari:
            sb += a
        return sb
    else:
        for i in range(len(oyuncu[6])):
            for q in liste:
                if q[4] != oyuncu[4]:
                    if oyuncu[8][i] == '½':
                        if oyuncu[7][i] == q[4]:
                            rakip_puanlari.append(q[0]/2)
                    elif oyuncu[8][i] == '1':
                        if oyuncu[7][i] == q[4]:
                            rakip_puanlari.append(q[0])

        for q in range(tur):
            if oyuncu[8][q] == '-' or oyuncu[8][q] == 'r':
                index = q
                rakip = 0

                for i in range(index):
                    if oyuncu[8][i] == '1':
                        rakip += 1
                    elif oyuncu[8][i] == '½':
                        rakip += 0.5
                    elif oyuncu[8][i] == '-':
                        rakip += 1
                    elif oyuncu[8][i] == 'r':
                        rakip += 1

                kalan = (tur - 1) - index
                kalan_sonuc = (kalan * 0.5)
                rakip += kalan_sonuc
                hayali_rakip.append(rakip)

        rakip_puanlari.extend(hayali_rakip)
        for q in rakip_puanlari:
            sb += q
        return sb


def main(): #Ana fonksiyon
    liste = [] #Oyuncu listesi
    lisans_no_liste = [] # Aynı lisans numarasının tekrar girilmemesi için açılan liste
    oyuncu_sayisi = 0

    while True: #Oyuncuların bilgilerinin alınması için açılan While döngüsü

        x = 0

        puan = 0

        lisans_no = lisans_no_al(lisans_no_liste)

        if lisans_no <= 0:
            break

        lisans_no_liste.append(lisans_no)

        oyuncu_sayisi += 1

        ad = ad_soyad()

        elo = elo_al()

        ukd = ukd_al()

        liste.append([puan, elo, ukd, ad, lisans_no])

    alphabet = " ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

    liste = sorted(liste, key=lambda x: (-x[0], -x[1], -x[2], [alphabet.index(c) for c in x[3]], x[4])) # Alınan bilgiler doğrultusunda liste alfabeye göre sıralanır

    print('\nBaşlangıç sıralama listesi') #Başlangıç sıralama listesi yazdırılır
    print("""\nBSNo   LNo   Ad-Soyad           ELO   UKD""")
    print("""----  ----   ----------------  ----  ----""")

    for i in range(oyuncu_sayisi):
        liste[i].append(i + 1)
        bosluk = 15 - len(liste[i][3])

        print(
            end=' 'f"""{format(i + 1, '3')}   {format(liste[i][4], '3')}   {format(liste[i][3], '2')} """ + ' ' * bosluk + f'{format(liste[i][1], "6")}')
        print(' ' + f'{format(liste[i][2], "5")}')

    tur = tur_sayisi(oyuncu_sayisi) #Tur sayısı alınır
    renk = renk_al() #İlk oyuncunun rengi alınır
    renk2 = ''

    if renk == 's': #İlk  oyuncunun rengine göre renk2 atanır
        renk2 = 'b'
    elif renk == 'b':
        renk2 = 's'

    masa_sayisi = 0

    for i in range(oyuncu_sayisi): # oyuncuların başlangıç sıra NO'suna göre renkleri verilir.
        if oyuncu_sayisi % 2 == 0:
            masa_sayisi = oyuncu_sayisi // 2
            if liste[i][5] % 2 != 0:
                liste[i].append([renk])
            else:
                liste[i].append([renk2])
        else:
            masa_sayisi = (oyuncu_sayisi // 2 + 1)
            if i % 2 == 0:
                if i == (oyuncu_sayisi - 1):
                    liste[i].append([''])
                else:
                    liste[i].append([renk])
            else:
                liste[i].append([renk2])

    for i in range(oyuncu_sayisi):
        liste[i].append([])
    for i in range(oyuncu_sayisi):
        liste[i].append([])

    if oyuncu_sayisi % 2 != 0: #Oyuncu sayısı Tek ise son sıradaki oyuncunun rakibine boş yazılır
        liste[-1][7].append('-')

    sayac = 0

    while True: # Her tur aynı işlemlerin yapılması için açılan while döngüsü

        mac = [] #Her turda oynana maçların depolanmaası için açılan liste

        if x == tur: #Tur sayısını geçince  while döngüsünün kırılması için açılan if
            break

        beyaz = [] # Her tur beyaz renkli oyuncuların alınması için açılan liste
        siyah = [] # Her tur siyah renkli oyuncuların alınması için açılann liste

        for i in range(oyuncu_sayisi): # Oyuncularaın renkelerine göre listelere eklenmesi
            if liste[i][6][x] == 'b':
                beyaz.append(liste[i])
            elif liste[i][6][x] == 's':
                siyah.append(liste[i])
            else:
                beyaz.append(liste[i])

        if oyuncu_sayisi % 2 != 0: # Oyuncuların rakiplerinin lisans numarasının depolanması
            for i in range(masa_sayisi - 1):
                beyaz[i][7].append(siyah[i][4])
                siyah[i][7].append(beyaz[i][4])
        else:
            for i in range(masa_sayisi):

                beyaz[i][7].append(siyah[i][4])
                siyah[i][7].append(beyaz[i][4])

        tablo_yaz(x + 1)

        if oyuncu_sayisi % 2 != 0: # Eşleştirme tablosunun yazılması
            for i in range(masa_sayisi - 1):
                print(
                    f"""{format(i + 1, '3')} {format(beyaz[i][5], '4')} {format(beyaz[i][4], '5')} {format(beyaz[i][0], '3.2f')}""",
                    end=' -')
                print(f""" {format(siyah[i][0], '2.2f')} {format(siyah[i][4], '5')} {format(siyah[i][5], '4')}""")
            for i in range((oyuncu_sayisi // 2) + 1):
                if beyaz[i][6][x] == '':
                    print(
                        f'{format(masa_sayisi, "3")}  {format(beyaz[i][5], "3")}  {format(beyaz[i][4], "4")} {format(beyaz[i][0], "0.2f")} - BYE')
                    beyaz[i][0] += 1
        else:
            for i in range(1, masa_sayisi + 1):
                print(
                    f"""{format(i, '3')} {format(beyaz[i - 1][5], '4')} {format(beyaz[i - 1][4], '5')} {format(beyaz[i - 1][0], '3.2f')}""",
                    end=' -')
                print(
                    f""" {format(siyah[i - 1][0], '2.2f')} {format(siyah[i - 1][4], '5')} {format(siyah[i - 1][5], '4')}""")

        for i in range(oyuncu_sayisi // 2): # Maç listesine sonuçların eklenmesi
            sonuc = mac_sonucu(i + 1)
            mac.append([beyaz[i][3], siyah[i][3], sonuc])

        for i in range(oyuncu_sayisi // 2): # Maç sonuçllarına ggöre oyuncu listesine puanların ve sonucların  eklenmesi
            if mac[i][2] == 0:
                beyaz[i][0] += 0.5
                siyah[i][0] += 0.5
                beyaz[i][8].append('½')
                siyah[i][8].append('½')

            elif mac[i][2] == 1:
                beyaz[i][0] += 1
                beyaz[i][8].append('1')
                siyah[i][8].append('0')

            elif mac[i][2] == 2:
                siyah[i][0] += 1
                siyah[i][8].append('1')
                beyaz[i][8].append('0')

            elif mac[i][2] == 3:
                beyaz[i][0] += 1
                beyaz[i][8].append('r')
                siyah[i][8].append('k')

            elif mac[i][2] == 4:
                siyah[i][0] += 1
                siyah[i][8].append('r')
                beyaz[i][8].append('k')

            elif mac[i][2] == 5:
                siyah[i][0] += 0
                beyaz[i][0] += 0
                beyaz[i][8].append('k')
                siyah[i][8].append('k')

        if sayac == 0:
            if oyuncu_sayisi % 2 != 0:
                sayac += 1
                liste[-1][8].append('-')

        liste.clear() # Listenin temizlenmesi ve sonuçlara göre yeniden liste oluşturulması
        liste.extend(beyaz)
        liste.extend(siyah)

        liste = sorted(liste, key=lambda x: (-x[0], -x[1], -x[2], [alphabet.index(c) for c in x[3]], x[4]))

        for i in range(oyuncu_sayisi): # Sonraki tur için renk elemanlarının oluşturulması
            if x + 1 != tur:
                liste[i][6].append('a')

        for a in range(1, oyuncu_sayisi + 1):  # Listedeki en son oyuncuya BYE verilmesi
            if x + 1 != tur:
                if '' not in liste[-a][6] and 'r' not in liste[-a][8]:
                    if oyuncu_sayisi % 2 != 0:
                        liste[-a][6][x + 1] = ''
                        liste[-a][8].append('-')
                        liste[-a][7].append('-')
                        liste.insert(-1,liste.pop(-a))
                        break

        for i in range(oyuncu_sayisi): # Oyuncuların eşleştirilmesi
            if x + 1 != tur:
                if liste[i][6][x + 1] != renk and liste[i][6][x + 1] != renk2 and liste[i][6][x + 1] != '':
                    c = liste[i][0]
                    oyuncu_renk = liste[i][6][x]

                    if oyuncu_renk == '': # Oyuncu rengine göre ters rengin belirlenmesi ve eğer oyuncu bye geçmişse önümüzdeki tur hangi rengi alacağının belirlenmesi
                        if x == 0:
                            if liste[i][5] % 2 != 0:
                                oyuncu_renk = renk2
                                ters_renk = renk
                            else:
                                oyuncu_renk = renk
                                ters_renk = renk2
                        elif x != 0:
                            oyuncu_renk = liste[i][6][x-1]

                            if oyuncu_renk == 's':
                                ters_renk = 'b'
                            elif oyuncu_renk == 'b':
                                ters_renk = 's'

                    elif oyuncu_renk == 's':
                        ters_renk = 'b'
                    elif oyuncu_renk == 'b':
                        ters_renk = 's'

                    while True:
                        oyuncu = liste[i] # Verilen oyuncuya için 1.1 kuralına göre rakip arama
                        rakip = oyuncu_ara1(oyuncu, oyuncu_renk, c, liste, oyuncu_sayisi, x)
                        if rakip != 'n':
                                if liste[i][6].count(ters_renk) - liste[i][6].count(oyuncu_renk) == 2:
                                    rakip = 'n'
                                elif liste[i][6].count(ters_renk) - liste[i][6].count(oyuncu_renk) != 2:
                                    liste[i][6][x+1] = ters_renk
                                    J = liste.index(rakip)
                                    liste.insert(i+1,liste.pop(J))
                                    break

                        elif rakip == 'n':
                            rakip = oyuncu_ara2(oyuncu,oyuncu_renk,c,liste,oyuncu_sayisi,x) # Verilen oyuncuya için 1.2 kuralına göre rakip arama
                            if rakip != 'n':
                                if liste[i][6].count(ters_renk) - liste[i][6].count(oyuncu_renk) == 2:
                                    rakip = 'n'
                                elif liste[i][6].count(ters_renk) - liste[i][6].count(renk) != 2:
                                    liste[i][6][x + 1] = ters_renk
                                    q = liste.index(rakip)
                                    liste.insert(i+1,liste.pop(q))
                                    break

                            elif rakip == 'n':
                                rakip = oyuncu_ara3(oyuncu, oyuncu_renk, c, liste, oyuncu_sayisi, x) # Verilen oyuncu  için 1.3 kuralına göre rakip arama

                                if rakip != 'n':

                                    if liste[i][6].count(oyuncu_renk) - liste[i][6].count(renk) == 2:
                                        rakip = 'n'
                                    elif liste[i][6].count(oyuncu_renk) - liste[i][6].count(renk) != 2:
                                        oyuncu_renkleri = []
                                        for i in oyuncu[6]:
                                            if i == 's' or i == 'b':
                                                oyuncu_renkleri.append(i)

                                        if len(oyuncu_renkleri) <= 2:
                                            r = liste.index(oyuncu)
                                            w = liste.index(rakip)
                                            liste[r][6][x+1] = oyuncu_renk
                                            liste.insert(r+1,liste.pop(w))
                                            break

                                        elif len(oyuncu_renkleri) > 2:
                                            if oyuncu_renkleri[-1] != oyuncu_renkleri[-2]:
                                                r = liste.index(oyuncu)
                                                w = liste.index(rakip)
                                                liste[r][6][x + 1] = oyuncu_renk
                                                liste.insert(r+1,liste.pop(w))
                                                break
                                elif rakip == 'n': # eğer rakip bulunamadıysa verilen oyuncunun puanını 0.5 azaltıp devam etmek için açılan elif
                                    c = c-0.5

        x += 1 # Bir sonraki tura geçilmesi için sayacın arttırılması

    iki_mi = False                         # BH1,BH2  ve SB'lerin oyuncu listesine eklenmesi
    for i in range(len(liste)):
        bh1 = BH1(liste,liste[i],tur,iki_mi)
        liste[i].append(bh1)

    iki_mi = True             # BH2'lerin hesaplanması, True verince BH2 aktif oluyor
    for i in range(len(liste)):
        bh1 = BH1(liste,liste[i],tur,iki_mi)
        liste[i].append(bh1)

    for i in range(len(liste)):   # SB'lerin hesaplanması
        q = sb(liste,liste[i],tur)
        liste[i].append(q)

    liste = sorted(liste,key=lambda x:(-x[0],-x[9],-x[10],-x[11])) # Listenin puan ve BH1,BH2 ve SB'ye göre sıralanması

    for i in range(len(liste)):       # oyuncuların galibiyet sayılarının eklenmesi
        galibiyet  = 0
        for q in liste[i][8]:
            if q == 'r' or q == '1':
                galibiyet += 1
        liste[i].append(galibiyet)

    print('\nNihai sıralama listesi: ') # Nihai sıralama listesinin yazdırılması

    print("""SNo  BSNo    LNo  Ad-Soyad            ELO   UKD   Puan   BH-1   BH-2    SB  GS """)
    print("""---  ----  -----  ------------       ----  ----   ----  -----  ----- -----  --""")

    for i in range(len(liste)):
        print(f"""{format((i+1),'3')}   {format(liste[i][5],'3')}    {format(liste[i][4],'3')}  {format(liste[i][3],'2')}""",end='')
        bosluk2 = (18 - len(liste[i][3]))
        print(f"""{' '*bosluk2} {format(liste[i][1],'4')} {format(liste[i][2],'5')} {format(liste[i][0],'6.2f')} {format(liste[i][9],'6.2f')}""",end='')
        print(f"""  {format(liste[i][10],'5.2f')} {format(liste[i][11],'5.2f')} {format(liste[i][12],'3')}""")

    for i in range(len(liste)):                     # Çapraz tablo yazdırmak için oyuncu listesindeki bazı sembollerin değiştirilmesi
        for q in range(len(liste[i][8])):
            if liste[i][8][q] == '-':
                liste[i][8][q] = '1'
            elif liste[i][8][q] == 'r':
                liste[i][8][q] = '+'
            elif liste[i][8][q] == 'k':
                liste[i][8][q] = '-'

    liste = sorted(liste,key=lambda x: (x[5]))                 # Listenin başlangıç sıra numarasına göre sıralanması

    for i in range(len(liste)):                    #  Oyuncuların karşılaştığı rakiplerin başlangıç sıra numaralarının alınması için liste
        liste[i].append([])

    for i in range(len(liste)):              #   Oyuncuların karşılaştığı rakiplerin başlangıç sıra numaralarının alınması
        for q in range(len(liste[i][7])):
            index = liste[i][7][q]
            for a in range(len(liste)):
                if index == liste[a][4]:
                    liste[i][13].append(liste[a][5])
                elif index == '-' and index not in liste[i][13]:
                    liste[i][13].append('-')

    liste = sorted(liste, key=lambda x: (-x[0], -x[9], -x[10], -x[11]))  # Listenin Puan BH1 BH2 ve SB'ye göre sıralanması

    for i in range(len(liste)):     # Oyuncuların son durumda sıralarını belirleyerek sıra numaralarının verilmesi
        liste[i].append(i+1)

    liste = sorted(liste, key=lambda x: (x[5])) # Listeyi tekrar başlangıç sıra numarasına göre sıralama

    print('\nÇapraz  sıralama listesi: ')                       # Çapraz sıralama listesinin yazdırılması
    print(f"""BSNo  Sno    LNo  Ad-Soyad            ELO   UKD""",end='    ')
    for w in range(tur):
        print(f"""{w+1}.Tur   """,end='  ')
    print("""Puan    BH-1    BH-2      SB GS  """)
    print("""---  ----  -----  ------------       ----  ----""",end='   ')
    for w in range(tur):
        print("""-------""",end='   ')
    print(""" ----   -----   -----   ----- --""")

    for i in range(len(liste)):
        for q in range(len(liste[i][6])):
            if liste[i][6][q] == '':
                liste[i][6][q] = '-'
    for i in liste:
        print(format(i[5], '3'), end='  ')
        print(format(i[14], '4'), end='  ')
        print(format(i[4], '5'), end='  ')
        print(format(i[3], '12'), end='  ')
        print(format(i[1], '9'), end='  ')
        print(format(i[2],'4'), end='    ')
        for w in range(tur):
            print(f"{i[13][w]:>2}",end=' ')
            print(format(i[6][w]),end=' ')
            print(format(i[8][w],'1'),end='    ')
        print(format(i[0],'3.2f'),end='   ')
        print(format(i[9],'5.2f'),end='   ')
        print(format(i[10],'5.2f'),end='   ')
        print(format(i[11],'5.2f'),end='  ')
        print(format(i[12],'1'))
main()