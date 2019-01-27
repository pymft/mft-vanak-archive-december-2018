import urllib.request
import re


class Webpage:
    instances = []
    num = 1

    def __new__(cls, url):
        for instance in cls.instances:
            if instance.url == url:
                return url
        return super().__new__(cls)

    def __init__(self, url):
        for instance in self.instances:
            if instance.url == url:
                raise Exception

        self.__url = url
        self.__content = ''
        self.instances.append(self)

    @classmethod
    def count(cls):
        return len(cls.instances)


    @property
    def url(self):
        return self.__url

    @property
    def content(self):
        if not self.__content:
            req = urllib.request.Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
            opened_req = urllib.request.urlopen(req)
            html_bytes = opened_req.read()
            self.__content = html_bytes.decode('utf-8')

        return self.__content

    @property
    def links(self):
        pat2 = r"<a.*?href=(.*?)[\"']"
        res2 = re.findall(pat2, self.content)
        return [Webpage(r[1]) for r in res2]


site = "http://wttr.in/tehran"
w1 = Webpage(site)
w2 = Webpage("http://www.google.com")

print(Webpage.count())


# print(w1.links)
# for w in w1.links:
#
#     print(w.links)
