from functools import partial


def open(url):
    return 'url: ' + url


def browser(url):
    return partial(open, url)


print(browser['https://']())
