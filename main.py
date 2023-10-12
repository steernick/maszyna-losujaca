import random
import yagmail

people_data = {
    'Przemek': {
        'email': 'przemyslaw.knapek@gmail.com'
    },
    'Kasia': {
        'email': 'katarzyna.rypien@gmail.com'
    },
    'Robert': {
        'email': 'rsknapek@gmail.com'
    },
    'Katia': {
        'email': 'katsiaryna.knapek@gmail.com'
    },
    'Olek': {
        'email': 'aleksanderknapek@gmail.com'
    },
    'Marta': {
        'email': 'martaolszta1989@gmail.com'
    },
    'Mama': {
        'email': ''
    },
    'Tata': {
        'email': ''
    },
    'Justyna': {
        'email': 'jusia.odair@gmail.com'
    },
    'Paweł': {
        'email': 'cader.pc@gmail.com'
    },
    'Kasieńka': {
        'email': ''
    },
}

print(people_data['Robert']['email'])
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

for item in people_data.items():
    print(item[0], item[1]['gift_to'])

for item in people_data.items():
    print(item)


yag = yagmail.SMTP('knapeksecretsanta@gmail.com', oauth2_file='~/Downloads/client_secret_182627804387-ejvvd3scnvks3on9rdmoe7orgblj7mce.apps.googleusercontent.com.json')
yag.send(to='canislupusrk@gmail.com', subject="Jeszce coś", contents='Coś zupełnie nowego')






