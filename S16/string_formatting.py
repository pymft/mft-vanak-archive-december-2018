text = "I'm %d years old"
# %d digit
# %f float
# %s string
# %o oct
# %x hex
# %e scientific

text_formatted = "string: %s" % ("dfgdfgdfgdfgd")
print(text_formatted)

text_formatted = "num=%-10d*" % (123)
print(text_formatted)

text_formatted = "the speed of light %.4e m/s" % (298000000)
print(text_formatted)

text_formatted = "I'm %d years old. I was born in %d" % (20, 2019-20)
print(text_formatted)