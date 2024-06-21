## Le scraping, qu'est-ce que c'est ?

Le scraping, ou "web scraping", est une technique utilisée pour extraire automatiquement des données à partir de sites web. Cette méthode permet de récupérer des informations structurées ou semi-structurées disponibles sur des pages web, que l'on peut ensuite analyser, traiter ou stocker pour divers usages. Mais il permet également d'automatiser des tâches sur un site. Il existe plusieurs module python permettant de faire du scraping : BeautifulSoup, Selenium, Scrapy, Requests, Octoparse.

Nous utiliserons BeautifulSoup et Selenium dans ces différents ateliers.


## Introduction au HTML
Scraper nécessite de savoir interpréter les codes sources des pages web, et donc comprendre le HTML.

Voici un petit [Formulaire HTML](formulaire_html.md). Il permet rapidemment d'apprendre ou se remémorer les balises principales permettant de lire du HTML et d'ainsi repérer les différents éléments d'une page web.


## Législation autour du scraping

Le scraping web est généralement autorisé dans les cas suivants :</p>
- Les données extraites sont des données accessibles au public.</li>
- Les informations recueillies ne sont pas protégées par un login.</li>

Il faut souvent être prudent lors du scraping, notamment vis-à-vis des Termes de service, des données protégées par le droit d'auteur et des données personnelles (car les données personnelles sont généralement protégées par les lois sur la vie privée). Le manque de lois explicites fait des usages du scraping une pratique juridiquement complexe.
