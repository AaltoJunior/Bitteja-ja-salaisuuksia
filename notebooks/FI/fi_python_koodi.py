# HUOM TÄMÄ ON VÄÄRÄ TIEDOSTO TYÖPAJAA VARTEN! TÄMÄ ON VAIN ARKISTO LÄHDEKOODISTA!

# Python-algoritmi "Salaisuuksia ja bittejä" -työpajaa varten:
# @ Author: Jaakko Takala, Aalto Junior

# Python-koodissa funktiot kirjoitetaan aina ajettavan koodin yläpuolelle.
# Alla kaikki salaukseen tarvittavat funktiot.
# Näitä funktioita ei kannata lähteä muokkaamaan ellei ole edistynyt koodari.
# Funktioiden alta löytyy ajettava koodi, johon salattava/purettava viesti syötetään.
def alkulukutesti(n: int) -> bool:
    # Funktio testaa 6k+-1 - alkulukutestillä onko luku alkuluku
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    juuri = int(n ** 0.5)
    while i <= juuri:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def alkulukuparin_luonti(r, s) -> (int, int):
    # Funktio luo salausavaimien luontiin vaadittavat alkuluvut.
    # Huom! Oikeissa sovelluskohteissa alkuluvut generoidaan käyttäen satunnaislukugeneraattoria.
    # Avainten koot ovat myös paljon isompia nykyään, yleensä 1024, 2048 tai jopa 4096 bittiä.
    # Käytettävät alkuluvut ovat siis suuruusluokkaa 10^150.

    # Valitaan käyttäjän antamien lukujen läheisyydestä alkuluvut.
    # On syytä huomata, että menetelmä ei tuota täysin satunnaisia alkulukuja.
    while alkulukutesti(r) == False:
        r += 1
    while alkulukutesti(s) == False:
        s += -1
    return r, s

def syt(a: int, b: int) -> int:
    # Funktio laskee lukujen suurin yhteinen tekijä Eukleideen algoritmilla.
    if b == 0:
        return a
    else:
        return syt(b, a % b)

def pyj(a: int, b: int) -> int:
    # Funktio määrittää lukujen pienimmän yhteisen jaettavan
    # ab = syt(a,b) * pyj(a,b) <-> pyj(a,b) = ab / syt(a,b)
    return int(a * b / syt(a, b))


# Seuraavien funktioiden avulla määritetään julkinen ja salainen avainpari
def julkinen_e(m: int) -> int:
    for x in range(2, m):
        if syt(m, x) == 1:
            return x
def salainen_d(m, e) -> int:
    for x in range(2, m):
        if (e * x) % m == 1:
            return x

def avainparien_luonti(alkuluku1: int, alkuluku2: int) -> (int, int, int, int):
    n = alkuluku1 * alkuluku2
    m = pyj(alkuluku1 - 1, alkuluku2 - 1)
    e = julkinen_e(m)
    d = salainen_d(m, e)
    print("Julkinen avainparisi: (", n, ",", e, ")")
    print("Salainen avainparisi: (", n, ",", d, ")")
    return n, m, e, d

# Alla on vielä viestin salaus- ja purkufunktiot.
def viestin_salaus(viesti: str, n: int, e: int) -> str:
    merkkilista = []
    for str in viesti.split():
        num = int(str, 2)
        merkkilista.append(num)
    i = 0
    merkkilistastr = []
    for merkki in merkkilista:
        # Pow-komento on verrattain nopea tapa laskea suuria potensseja modulossa.
        salattu_merkki = pow(merkki, e, n)
        salattu_merkki_str = f"{salattu_merkki}"
        merkkilistastr.append(salattu_merkki_str)
        i += 1
    salattu_viesti = " ".join(merkkilistastr)
    return salattu_viesti

def viestin_purku(salattu_viesti: str, n: int, d: int) -> str:
    merkkilista = []
    for str in salattu_viesti.split():
        num = int(str)
        merkkilista.append(num)
    i = 0
    for merkki in merkkilista:
        purettu_merkki = pow(merkki, d, n)
        purettu_bin = ('{0:b}'.format(purettu_merkki).zfill(8))
        merkkilista[i] = f"{(purettu_bin)}"
        i += 1
    purettu_viesti= ' '.join(merkkilista)
    return purettu_viesti

# ------ GENEROI AVAINPARIT ---------
# Syötä kaksi lukua väliltä 1000-10000:
luku1 = 1234
luku2 = 2345

alkuluku1, alkuluku2 = alkulukuparin_luonti(luku1, luku2)
n, m, e, d = avainparien_luonti(alkuluku1, alkuluku2)

# ------ VIESTIN SALAUS -------------
# Kopioi salattava viesti utf-8-muodossa tähän:
salattava_viesti = "01001101 01101111 11101001 00100001"

# Kirjoita viestin vastaanottajan julkinen avainpari tähän:
avainpari = (2895817, 7)

salattu_viesti = viestin_salaus(salattava_viesti, avainpari[0], avainpari[1])
print("Salattu viesti:", salattu_viesti)

# ------ SALAUKSEN PURKU ------------
# Kopioi purettava viesti tähän:
purettava_viesti = "1014814 1373040 2317731 704188"

purettu_viesti = viestin_purku(purettava_viesti, n, d)
print("Purettu viesti:", purettu_viesti)

# ------ VIESTIN HAKKEROINTI -------------
# Ratkaise ensin hakkeroitavan henkilön alkuluvut omalla Python-koodillasi.
# Voit kirjoittaa koodin esim. näiden ohjeiden tilalle.
# Ohjeet:

# Luo muuttuja johon sijoitat hakkeroitavan hekilön julkisen avainparin luvun n
# Käy kokonaislukuja x yksitellen läpi while: tai for: -rakenteella
# Testaa jakaako luku x luvun n
# Jos x|n ja 1 < x < n, x on toinen luvuista p ja q. Printtaa x!

# Kun olet löytänyt luvut p ja q, käytä tätä koodia viestin hakkeroimiseen.
# Syötä hakkeroitava viesti, p ja q sekä poista hipsut.
'''
hakkeroitava_viesti = ...
p = ...
q = ...
nh, mh, eh, dh = avainparien_luonti(p, q)
hakkeroitu_viesti = viestin_purku(hakkeroitava_viesti, nh, dh)
print("Hakkeroitu viesti:", hakkeroitu_viesti)
'''
