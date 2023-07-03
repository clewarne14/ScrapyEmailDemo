# ScrapyEmailDemo
This repository includes a spider that, when given the URL of one or multiple websites, checks for every email that is written as a link or as plain text on the page. 

Run the spider on a single website by going to the 'ScrapyDemo' folder and running a command similar to the following: scrapy crawl links -O filetest.json -a w=https://example.com

Run the spider on multiple websites by either editing the file websites.txt and adding more websites, or creating your own file. Once one of these steps has been completed, run a command similar to the following: scrapy crawl links -0 filetest.json -a f=websites.txt

Unfortunately, as of now, this tool only scrapes email addresses on the page that we begin on and does not go to separate pages. In the future, if it is decided that this is a beneficial route to continue down, I will expand this tool.
