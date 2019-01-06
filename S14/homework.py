import urllib.request

class Webpage:
    def __init__(self, url):
        self.url = url

    def read_content(self):
        req = urllib.request
        # TODO: comple me
        return

    def get_emails(self):
        # fixme : write proper pattern here to find email addresses
        pat = ""

        return


    def get_links(self):
        """

        :return:

        reference:
        [1] https://stackoverflow.com/questions/15926142/regular-expression-for-finding-href-value-of-a-a-link
        """



site = 'http://www.google.com'
w = Webpage(site)
w.get_emails()
w.get_links()