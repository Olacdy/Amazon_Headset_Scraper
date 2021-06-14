# Amazon_Headset_Scraper

Contents
========

- [Description](#description)
- [Technologies](#technologies)
- [How To Use](#how-to-use)
- [License](#license)
- [Author Info](#author-info)

---

## Description

By doing this project I wanted to demonstrate my abilities to solve problems connected with Amazon product scraping.

Problem. Scraping Amazon conceals a lot of pitfalls, like adjusting scrape speed, setting the right user agent, handling missing entries, etc.

To solve that problem I've been using a framework called Scrapy. It's a powerful tool which allows user to specify target site with the list of URLs, design item holder and pipelines. It's also has a great community, which created an additional library called scrapy-fake-useragent, that allows user to switch agents, to avoid getting banned if scraping speed adjusted wisely.

The final stage is to deploy scraper in the cloud, I've tried to use Zyte, but Amazon bans scraper immediately. So, the decision was to find another solution. Heroku was an ideal choice, it's pretty straightforward and much more versatile. Firstly, I needed to make a scrapy run from Python script, then wrap it up in the Flask app, so it can be run through a web request. Secondly, I needed to create a Dockerfile and compile an image then run it locally with Docker. And finally, thirdly, deploy it on Heroku.

#### Technologies

- <img width="40px" src="https://user-images.githubusercontent.com/1499751/115736045-a513f280-a393-11eb-8dbd-ebd3eda15841.png"/>
* <img width="40px" src="https://user-images.githubusercontent.com/1499751/120819176-f9e28580-c55b-11eb-9635-93e2dc487f8e.png"/>
- <img width="40px" src="https://user-images.githubusercontent.com/1499751/121908315-90b9f980-cd35-11eb-8745-0fa8460cf199.png"/>
* <img width="40px" src="https://user-images.githubusercontent.com/1499751/121908362-9a436180-cd35-11eb-9315-35a67bc06964.png"/>

[Back To The Top](#Amazon_Headset_Scraper)

---

## How To Use

#### Installation

To start using that project on your machine, you need to have a Python 3.7+, download the repository and run command below to install all required dependencies to then use it.

`pip install -r requirements.txt`

Open app.py file, run it with Python, then create GET request on localhost with /get_items parameter to specify page limit just add ?page_lim=`YOUR NUMBER`.

You can also try to make a request on following URL: https://amazon-headset-scraper.herokuapp.com/get_items.

[Back To The Top](#Amazon_Headset_Scraper)

---

## License

```text
MIT License

Copyright (c) 2021 Didechkin Oleg

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

[Back To The Top](#Amazon_Headset_Scraper)

---

## Author Info

- Upwork - [Didechkin Oleg](https://www.upwork.com/freelancers/~01bc2c6d8b19205903)
- Fiverr - [Didechkin Oleg](https://www.fiverr.com/dbofury)

[Back To The Top](#Amazon_Headset_Scraper)
