<div align="center" markdown>
# [Scraping Workshop](https://github.com/Mastocodeur/Tutorial_Scraping/)

Workshop to discover two Python modules for scraping: Selenium and BeautifulSoup.

[![PyPI - Version](https://img.shields.io/pypi/v/mmg?color)](https://pypi.org/project/mmg/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mmg)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ryul1206/multilingual-markdown)
[![PyPI - License](https://img.shields.io/pypi/l/mmg)](https://github.com/ryul1206/multilingual-markdown/blob/main/LICENSE)

🌏
[**French**](https://github.com/ryul1206/multilingual-markdown/blob/main/README.md) |
English |



</div>

## Table of Contents

1. [What is Scraping?](#what-is-scraping)
2. [Introduction to HTML](#introduction-to-html)
3. [Legislation Around Scraping](#legislation-around-scraping)
4. [Selenium vs BeautifulSoup](#selenium-vs-beautifulsoup)
5. [Different Ways to Locate Web Elements](#different-ways-to-locate-web-elements)
6. [Future of Scraping: LaVague](#future-of-scraping-lavague)
7. [Bonus: robots.txt](#bonus-robotstxt)
8. [Sources and Documentation](#sources-and-documentation)

## What is Scraping?

Scraping, or "web scraping," is a technique used to automatically extract data from websites. This method allows the retrieval of structured or semi-structured information available on web pages, which can then be analyzed, processed, or stored for various uses. It also allows the automation of tasks on a website. There are several Python modules for scraping: BeautifulSoup, Selenium, Scrapy, Requests, Octoparse.

We will use BeautifulSoup and Selenium in these different workshops.

## Introduction to HTML

Scraping requires interpreting the source code of web pages and thus understanding HTML.

Here is a small [HTML Form](formulaire_html.md). It quickly helps you learn or recall the main tags to read HTML and thus identify the different elements of a web page.

## Legislation Around Scraping

Web scraping is generally allowed in the following cases:
- The extracted data is publicly accessible.
- The information collected is not protected by a login.

In general, it is often necessary to be cautious when scraping, especially regarding Terms of Service, data protected by copyright, and personal data (as personal data is generally protected by intellectual property laws).

In competition law, web scraping can be considered an act of unfair competition.

For example, the CNIL fined the company Nestor €20,000 because it built its prospect database using web scraping from data accessible on the LinkedIn professional social network (For more info, see the mentioned articles).

## Selenium vs BeautifulSoup

Selenium is useful for dynamic web pages where content is generated via JavaScript, requiring user interactions such as clicks, scrolling, or text input.

BeautifulSoup is a Python library primarily used to parse HTML and XML documents. It is useful for extracting structured data from static web pages.

## Different Ways to Locate Web Elements

- ID = "id"
- NAME = "name"
- XPATH = "xpath"
- LINK_TEXT = "link text"
- PARTIAL_LINK_TEXT = "partial link text"
- TAG_NAME = "tag name"
- CLASS_NAME = "class name"
- CSS_SELECTOR = "css selector"

## Future of Scraping: LaVague

[lavague.ai](https://github.com/lavague-ai)

## Bonus: robots.txt

To access this file, type: root_url/robots.txt

This file regulates the traffic of exploration robots. Through this file, you can know the limitations imposed on exploration robots.

## Sources and Documentation

- [All About Web Scraping](https://kinsta.com/fr/base-de-connaissances/web-scraping/)

- [Is Web Scraping Legal?](https://www.captaincontrat.com/protection-des-creations/cgv-cgu-cga/web-scraping-est-ce-legal-me-marcotte)

- [Is Web Scraping Legal? What You Need to Know](https://www.iubenda.com/fr/help/111962-le-web-scraping-est-il-legal-ce-que-vous-devez-savoir#:~:text=La%20l%C3%A9galit%C3%A9%20du%20web%20scraping&text=Ne%20soyez%20pas%20trop%20enthousiaste,pas%20prot%C3%A9g%C3%A9es%20par%20un%20login)

- [The Nestor Case (1)](https://www.alerionavocats.com/condamnation-societe-nestor-prospection-commerciale-fondee-interet-legitime-responsable-traitement-enseignements-tirer/)

- [The Nestor Case (2)](https://www.plravocats.fr/blog/data-protection-rgpd/la-societe-nestor-sanctionee-par-la-cnil)

- [Introduction to the robots.txt File](https://developers.google.com/search/docs/crawling-indexing/robots/intro?hl=fr)

- [Selenium Documentation](https://selenium-python.readthedocs.io/)

- [BeautifulSoup Documentation](https://beautiful-soup-4.readthedocs.io/en/latest/)
