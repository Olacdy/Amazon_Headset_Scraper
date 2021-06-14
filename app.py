import os
import crochet
from flask import Flask, request
from scraper import Scraper
from AmazonHeadSetScraping.spiders.headset_spider import HeadsetSpider


port = int(os.environ.get("PORT", 5000))
app = Flask(__name__)
crochet.setup()


@app.route('/get_items')
def get_items():
    print(request.args.get('page_lim'), flush=True)
    scraper = Scraper(HeadsetSpider, request.args.get('page_lim', default=1, type=int))
    scraper.run_spider()

    while not scraper.is_closed:
        continue

    return scraper.get_output_data()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)

