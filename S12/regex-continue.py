text = "All work and no play makes Jack a dull boy! stack"
word = "Jack"
word = "[jhtJHT]ack"

sub_strs = len(text)-len(word)+1

for i in range(sub_strs):
    if text[i + 0] == ' ':
        if text[i + 1] in ('J', 'j', 'h', 't'):
            if text[i + 2] == 'a':
                if text[i + 3] == 'c':
                    if text[i + 4] == 'k':
                        print(i)