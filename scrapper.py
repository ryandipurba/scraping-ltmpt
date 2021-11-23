import scrapy


class QuotesSpider(scrapy.Spider):
    name = "ltmpt"
    start_urls = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        url1 = 'https://top-1000-sekolah.ltmpt.ac.id/?page='
        url2 = '&per-page=100'

        for page in range(1, 11):
            self.start_urls.append(url1 + str(page) + url2)

    def parse(self, response, **kwargs):
        for i in range(1, 101):
            for sekolah in response.css('#w0 > table > tbody'):
                yield {
                    'ranking': sekolah.css('tr:nth-child(' + str(i) + ') > td:nth-child(1)::text').extract(),
                    'nama_sekolah': sekolah.css('tr:nth-child(' + str(i) + ') > td:nth-child(4)::text').extract(),
                    'provinsi': sekolah.css('tr:nth-child(' + str(i) + ') > td:nth-child(6)::text').extract(),
                    'kota/kab.': sekolah.css('tr:nth-child(' + str(i) + ') > td:nth-child(7)::text').extract(),
                    'jenis': sekolah.css('tr:nth-child(' + str(i) + ') > td:nth-child(8)::text').extract()
                }

