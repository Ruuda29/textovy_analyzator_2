TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

uzivatele = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}

oddelovac = "-" * 40

username = input("username: ")
password = input("password: ")

if username in uzivatele and uzivatele[username] == password:
    print(f"""{oddelovac}
Welcome to the app, {username} 
We have 3 texts to be analyzed.
{oddelovac}""")
else:
    print("unregistered user, terminating the program...")
    quit()

zvoleny_text = input("Enter a number btw. 1 and 3 to select: ")

if zvoleny_text.isnumeric() and int(zvoleny_text) >= 1 and int(zvoleny_text) <= 3:
    seznam_slov = TEXTS[int(zvoleny_text) - 1].split()
    ocisteny_seznam_slov = []
    for slovo in seznam_slov:
        ocistene_slovo = slovo.strip(".,")
        ocisteny_seznam_slov.append(ocistene_slovo)
else:
    print("Nezadal si číslo v určeném rozsahu. Ukončuji...")
    quit()

pocet_slov = len(ocisteny_seznam_slov)
zacatek_velke_pismeno = 0
vsechna_velke_pismeno = 0
vsechna_male_pismeno = 0
je_cislo = 0
suma_cisel = 0

for slovo in ocisteny_seznam_slov:
    if slovo.istitle():
        zacatek_velke_pismeno = zacatek_velke_pismeno + 1
    elif slovo.isupper():
        vsechna_velke_pismeno = vsechna_velke_pismeno + 1
    elif slovo.islower():
        vsechna_male_pismeno = vsechna_male_pismeno + 1
    elif slovo.isnumeric():
        je_cislo = je_cislo + 1
        suma_cisel = suma_cisel + int(slovo)

print(f"""{oddelovac}
There are {pocet_slov} words in the selected text.
There are {zacatek_velke_pismeno} titlecase words.
There are {vsechna_velke_pismeno} uppercase words.
There are {vsechna_male_pismeno} lowercase words.
There are {je_cislo} numeric strings.
The sum of all the numbers {suma_cisel}.
{oddelovac}""")

slovnik_delky_slov = dict()

for slovo in ocisteny_seznam_slov:
    delka_slova = len(slovo)
    if delka_slova not in slovnik_delky_slov:
        slovnik_delky_slov[delka_slova] = 1
    else:
        slovnik_delky_slov[delka_slova] = (slovnik_delky_slov[delka_slova]) + 1

serazeny_slovnik_delky_slov = dict(sorted(slovnik_delky_slov.items()))

maximalni_hodnota = max(serazeny_slovnik_delky_slov.values())

print(f"LEN|{"OCCURENCES".center(maximalni_hodnota + 3)}{"|NR.".rjust(2)}")
print(oddelovac)

for item in serazeny_slovnik_delky_slov:
    aktualni_hodnota = serazeny_slovnik_delky_slov[item]
    print(
f"{str(item).rjust(3)}| {(aktualni_hodnota) * "*"} "
f"{"|".rjust(maximalni_hodnota - aktualni_hodnota + 2)}{aktualni_hodnota}"
)
