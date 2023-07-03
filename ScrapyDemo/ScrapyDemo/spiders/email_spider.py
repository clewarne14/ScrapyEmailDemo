from pathlib import Path

import scrapy


class EmailSpider(scrapy.Spider):
    name = "links"
    start_urls = []

    def __init__(self, f=None, w=None, *args, **kwargs):
        super(EmailSpider, self).__init__(*args, **kwargs)
        print(f == None)
        if f != None:
            websites = open(f,'r')
            lines = websites.readlines()
            for line in lines:
                self.start_urls.append(line.strip())
        if w != None:
            self.start_urls.append(w)
        

    def get_email(self, s):
        output = ""
        for i in range(len(s)):
            if s[i] == '@':
                output = "@"
                j = i
                while s[i] != ' ' and i < len(s)-1:
                    i = i+1
                    output = output + s[i]
                while s[j] != ' ' and j > 0 and s[j] != ':':
                    j = j-1
                    output = s[j] + output
                if '.' in output:
                    if output[-1] == ' ':
                        output = output[:-1]
                    return output[1:]
                else:
                    output = ''
        return output


    def parse(self, response):
        output = []
        links = response.css("a::attr(href)").getall()
        # print(links)
        for link in links:
            email = self.get_email(link)
            if email != '':
                output.append(email)
        text = response.css("p::text").getall()
        h1 = (response.css("h1::text").getall())
        # h2 = (response.css("h2::text").getall())
        # h3 = (response.css("h3:text").getall())
        # h4 = (response.css("h4::text").getall())

        for t in text:
            tDone = self.get_email(t)
            if tDone != '':
                output.append(tDone)
        for t in h1:
            tDone = self.get_email(t)
            if tDone != '':
                output.append(tDone)
        # for t in h2:
        #     tDone = self.get_email(t)
        #     if tDone != '':
        #         output.append(tDone)
        # for t in h3:
        #     tDone = self.get_email(t)
        #     if tDone != '':
        #         output.append(tDone)
        # for t in h4:
        #     tDone = self.get_email(t)
        #     if tDone != '':
        #         output.append(tDone)
        
        yield {
            "links": output,
        }
