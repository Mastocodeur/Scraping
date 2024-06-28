## Table des Matières

1. [Qu'est-ce que le scraping ?](#qu-est-ce-que-le-scraping)
2. [Introduction au HTML](#introduction-au-html)
3. [Législation autour du scraping](#législation-autour-du-scraping)
4. [Selenium vs BeautifulSoup](#selenium-vs-beautifulsoup)
5. [Les différentes façons de localiser des éléments Web](#les-différentes-façons-de-localiser-des-éléments-web)
6. [Avenir du scraping : LaVague](#avenir-du-scraping-lavague)
7. [Bonus: robots.txt](#bonus-robots-txt)
8. [Sources et documentation](#sources-et-documentation)


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

De manière générale, il faut souvent être prudent lors du scraping, notamment vis-à-vis des Termes de service, des données protégées par le droit d'auteur et des données personnelles (car les données personnelles sont généralement protégées par les lois sur la propriété intellectuelle).

En droit de la concurrence, le web scraping peut être qualifié d'un acte de concurrence déloyale. 

La CNIL a par exemple condamné la société Nestor à une amende de 20000 euros car elle avait construit sa base de prospects en ayant recours à la pratique de web scraping à partir de données accessibles sur le réseau social professionnel Linkedin (Pour plus d'infos voir les articles mentionnés).

## Selenium vs BeautifulSoup

Selenium est utile pour les pages web dynamiques où le contenu est généré via JavaScript, nécessitant des interactions utilisateur telles que les clics, le défilement, ou la saisie de texte.

BeautifulSoup est une bibliothèque Python utilisée principalement pour parser (analyser) des documents HTML et XML. Elle est utile pour extraire des données structurées à partir de pages web statiques.

## Les différentes façon de localiser des éléments Web 

- ID = "id"
- NAME = "name"
- XPATH = "xpath"
- LINK_TEXT = "link text"
- PARTIAL_LINK_TEXT = "partial link text"
- TAG_NAME = "tag name"
- CLASS_NAME = "class name"
- CSS_SELECTOR = "css selector"


## Avenir du scraping : LaVague

[lavague.ai](https://github.com/lavague-ai)


## Bonus: robots.txt

Pour accéder à ce fichier, il s'agit de taper : url_racine/robots.txt

Ce fichier permet de cadrer le trafic des robots d'exploration. On peut grâce à ce fichier connaitre les limitations imposées aux robots d'exploration.


## Sources et documentation

- [Tout sur le web scraping](https://kinsta.com/fr/base-de-connaissances/web-scraping/)

- [Web scraping : est-ce légal](https://www.captaincontrat.com/protection-des-creations/cgv-cgu-cga/web-scraping-est-ce-legal-me-marcotte)

- [Le web scraping est-il légal ?](https://www.iubenda.com/fr/help/111962-le-web-scraping-est-il-legal-ce-que-vous-devez-savoir#:~:text=La%20l%C3%A9galit%C3%A9%20du%20web%20scraping&text=Ne%20soyez%20pas%20trop%20enthousiaste,pas%20prot%C3%A9g%C3%A9es%20par%20un%20login)


- [Le cas Nestor (1)](https://www.alerionavocats.com/condamnation-societe-nestor-prospection-commerciale-fondee-interet-legitime-responsable-traitement-enseignements-tirer/)

- [Le cas Nestor (2)](https://www.plravocats.fr/blog/data-protection-rgpd/la-societe-nestor-sanctionee-par-la-cnil)

- [Présentation du fichier robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro?hl=fr)

- [Documentation Selenium](https://selenium-python.readthedocs.io/)

- [Documentation BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/)