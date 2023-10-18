# maszyna-losujaca

Projekt stworzony na potrzeby chwili, do losowania prezentów na zbliżające się Święta Bożego Narodzenia, według założeń [Secret Santa](https://en.wikipedia.org/wiki/Secret_Santa).

Dane wejściowe, czyli lista użytkowników losowania wraz z adresami email, podane są w formie pliku .json

Program konsolowy wykorzystuje moduł klienta GMAIL/SMTP [yagmail](https://github.com/kootenpv/yagmail) w celu wysłania wiadomości email z wylosowaną przez maszynę osobą i zapewnienia pełnej anonimowości losowania.
