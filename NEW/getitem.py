import functools


class Browser:
    def __init__(self, url):
        self.url = url

    def open(self, url, domain):
        return 'url: ' + domain + ' '+ url

    def __getitem__(self, url):
        return functools.partial(self.open, url)


b = Browser('Https://')
print(b['www']('Egor'))
