import random
import yagmail
import json

yag = yagmail.SMTP('knapeksecretsanta@gmail.com', oauth2_file='~/Programowanie/Moje projekty/maszyna-losujaca/client_secret.json')

with open('people_data.json') as json_file:
    people_data = json.load(json_file)


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

for pair in pairs:
    people_data[pair[0]]['gift_to'] = pair[1]

message = '<h3>Cześć {}!<br><br>Maszyna losująca informuje uprzejmie, że wylosowana przez Ciebie osoba, którą obdarujesz w najbliszą Wigilię Bożego Narodzenia to:</h3><h2>{}</h2>'

secure = input('Wprowadź hasło do uruchomienia maszyny:\n')

if secure == 'secretsanta':
    for k, v in people_data.items():
        person = k
        email = v.get('email')
        gift_to = v.get('gift_to')
        yag.send(to=email, subject=f'{person}! Oto ważna wiadomość od Świątecznej Maszyny Losującej', contents=message.format(person, gift_to))
    print('Losowanie zakończone sukcesem')
elif secure == 'test':
    for k, v in people_data.items():
        person = k
        email = v.get('email')
        gift_to = v.get('gift_to')
        yag.send(to=email, subject='To jest email testowy', contents=message.format(person, gift_to))
    print('Test wypadł pomyślnie')
else:
    raise ValueError("Hasło nieprawidłowe!")
