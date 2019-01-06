class Stars:
    def __init__(self, n, pat='*', fill=True):
        self.n = n
        self.pat = pat
        self.fill = True

    def __repr__(self):
        if self.fill:
            out = ''
            for i in range(self.n):
                line = self.pat * (2*i+1)
                out += line.center(2*self.n+1)
                out += '\n'
            return out
        else:
            out = ''
            out += '*'.center(2*self.n+1)
            out += '\n'
            for i in range(1, self.n-1):
                line = self.pat + ' ' * (2*i-1) + self.pat
                out += line.center(2*self.n+1)
                out += '\n'
            out += self.pat * (2*self.n+1)
            return out

s1 = Stars(2)
s1
#
#  *
# ***
s1.n = 4
s1
#
#      *
#     ***
#    *****
#   *******
#  *********
s1.fill = False
s1
#
#      *
#     * *
#    *   *
#   *     *
#  *********
