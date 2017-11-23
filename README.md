# NS Consumenten zuil

Aanleiding:
De Nederlandse Spoorwegen vinden het erg belangrijk dat zij goed kunnen communiceren met hun
klanten. Daarom houden ze van tijd tot tijd een enquête onder de reizigers. Het nadeel van een
enquête is dat het lang duurt voordat je de resultaten krijgt. De NS heeft gehoord dat Twitter veel
sneller werkt. Het lijkt de directie leuk dat klanten hun opmerkingen/complimenten via een
computer, aanwezig in het station kunnen invoeren en dat deze opmerkingen dan zichtbaar worden
in de stationshal.

Men is ook wel een beetje bang voor Twitter, want men is bang dat het gebruikt gaat worden als
uitlaatklep voor ontevreden reizigers. Daarom is het belangrijk dat de inhoud van de tweets worden
gelezen voordat ze worden gepost op Twitter en zichtbaar worden in de stationshal.

## Getting Started

Hieronder zijn de instructies te vinden voor het downloaden en draaien van de applicatie. 

### Prerequisites

De volgende Python modules zijn gebruikt bij het bouwen van de applicatie:

```
Python3.6.1
Tweepy 3.5.0
Forecastio 1.3.5
Pillow-Pil 0.1.dev0
```

### Installatie

Voor het starten van de applicatie moet het volgende worden uitgevoerd:

```
git clone https://www.github.com/Achraf-Ben/NS-Consumenten-zuil
pip3 install tweepy
pip3 install Pillow-Pil
pip3 install python-forecastio
```

Hierna kunnen de python bestanden gedraaid worden in Python 3. 

```
cd NS-Consumenten-zuil
cd final
python3 GUIadmin.py
python3 GUIconsumenten.py
python3 GUItwitter.py

Pas de volgende regels aan in twitterAPI.py en GUItwitter.pi:

    6 accessToken = "XXXXXXXXXXXXXXXXXXXXXXXX"
    7 accessTokenSecret = "XXXXXXXXXXXXXXXXXXXXXXXX"
    8 consumerKey = "XXXXXXXXXXXXXXXXXXXXXXXX"
    9 ownerID = "XXXXXXXXXXXXXXXXXXXXXXXX"
    10 consumerKeySecret = "XXXXXXXXXXXXXXXXXXXXXXXX"
    
    
    13  api_key = "XXXXXXXXXXXXXXXXXXXXXXXX"
```

Na het starten van de 3 GUI's is het mogelijk om in GUIconsumenten een (Twitter) bericht in te voeren. 
Deze wordt vervolgens getoond in de GUIadmin. Hier kan de administrator beslissen of deze gepushed word naar Twitter of niet.
GUItwitter toont in eerste instantie het weerbericht en als er Tweets zijn verstuurd word het weerbericht vervangen door de meest recente Tweets. 


## Deployment

Houdt er rekening mee dat alle hierboven genoemde dependencies geïnstalleerd zijn voor de applicatie word gestart.

## Built With

* [PyCharm](https://www.jetbrains.com/pycharm/) - Python IDE
* [Tweepy](https://github.com/tweepy/tweepy) - Twitter API
* [Forecastio](https://pypi.python.org/pypi/python-forecastio/) - Weather API

## Authors

* **Achraf ben Abdelkrim** - *Initial work* - [Github](https://github.com/Achraf-Ben)
* **Vera Schoonderwoerd** - *Initial work* - [Github](https://github.com/vera98x)
* **Job Nuhaan** - *Initial work* - [Github](https://github.com/jnuhaan)
* **Joël van de Rest** - *Initial work* - [Github](https://github.com/JoelvandeRest)
* **IJsbrand Sijtsema** - *Initial work* - [Github](https://github.com/IcefireSijtsema)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
