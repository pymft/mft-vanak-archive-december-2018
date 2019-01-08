import urllib.request


# singleton


class Webpage:
    _history = []
    # def __new__(cls):

    def __init__(self, url):
        for s in self._history:
            if s.url == url:
                print("you have created similar instance before", url)
                break
        self.url = url
        self.text = ''
        self._history.append(self)


    @property
    def content(self):
        if self.text == '':
            req = urllib.request.Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
            opened_req = urllib.request.urlopen(req)
            html_bytes = opened_req.read()
            self.text = html_bytes.decode('utf-8')

        return self.text



site = 'http://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)'
w = Webpage(site)
w1 = Webpage(site)
w2 = Webpage("http://www.google.com")
w3 = Webpage("http://www.google.com")
w4 = Webpage("http://www.google.com")
lst1 = [1, 2, 3]
print("----")
w2.content
print("----")
w3.content
print("----")
w4.content
print("----")
# lst2 = [1, 2, 3]
# lst2 = lst1
