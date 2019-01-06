class Stars:
    def __init__(self, n, pat='*', fill=True):
        self.n = n
        self.pat = pat
        self.fill = True

    def __repr__(self):
        if self.fill:
            pass
        else:
            pass

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
