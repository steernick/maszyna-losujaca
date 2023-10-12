import random
import yagmail

yag = yagmail.SMTP('knapeksecretsanta@gmail.com', oauth2_file='~/Programowanie/Moje projekty/maszyna-losujaca/client_secret.json')

# people_data = {
#     'Przemek': {
#         'email': 'przemyslaw.knapek@gmail.com'
#     },
#     'Kasia': {
#         'email': 'katarzyna.rypien@gmail.com'
#     },
#     'Robert': {
#         'email': 'rsknapek@gmail.com'
#     },
#     'Katia': {
#         'email': 'katsiaryna.knapek@gmail.com'
#     },
#     'Olek': {
#         'email': 'aleksanderknapek@gmail.com'
#     },
#     'Marta': {
#         'email': 'martaolszta1989@gmail.com'
#     },
#     'Mama': {
#         'email': 'knapekbozena@gmail.com'
#     },
#     'Tata': {
#         'email': 'knapekwaldemar@gmail.com'
#     },
#     'Justyna': {
#         'email': 'jusia.odair@gmail.com'
#     },
#     'Paweł': {
#         'email': 'cader.pc@gmail.com'
#     },
#     'Kasieńka': {
#         'email': 'kasiaknapek05@gmail.com'
#     },
# }

people_data = {
    'Przemek': {
        'email': 'rsknapek@gmail.com'
    },
    'Kasia': {
        'email': 'rsknapek@gmail.com'
    },
    'Robert': {
        'email': 'rsknapek@gmail.com'
    },
    'Katia': {
        'email': 'rsknapek@gmail.com'
    },
    'Olek': {
        'email': 'rsknapek@gmail.com'
    },
    'Marta': {
        'email': 'rsknapek@gmail.com'
    },
    'Mama': {
        'email': 'rsknapek@gmail.com'
    },
    'Tata': {
        'email': 'rsknapek@gmail.com'
    },
    'Justyna': {
        'email': 'rsknapek@gmail.com'
    },
    'Paweł': {
        'email': 'rsknapek@gmail.com'
    },
    'Kasieńka': {
        'email': 'rsknapek@gmail.com'
    },
}

people = list(people_data.keys())


def random_pairs(seq):
    people_from = seq
    random.shuffle(people_from)
    people_to = people_from[:]
    pairs = []

    for p in people_from:
        r = random.choice([x for x in people_to if x != p])
        pairs.append((p, r))
        people_to.remove(r)
    return pairs

pairs = random_pairs(people)
# print(pairs)

for pair in pairs:
    people_data[pair[0]]['gift_to'] = pair[1]

# for item in people_data.items():
#     print(item[0], item[1]['gift_to'])

# for item in people_data.items():
#     print(item)

message = '<h3>Cześć {}!<br><br>Maszyna losująca informuje uprzejmie, że wylosowana przez Ciebie osoba, którą obdarujesz w najbliszą Wigilię Bożego Narodzenia to:</h3><h2>{}</h2>'

for k, v in people_data.items():
    person = k
    email = v.get('email')
    gift_to = v.get('gift_to')
    yag.send(to=email, subject=f"{person}! Oto ważna wiadomość od Świątecznej Maszyny Losującej", contents=message.format(person, gift_to))


