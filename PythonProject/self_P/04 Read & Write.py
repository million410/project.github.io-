filename = 'notes.txt'
# with open(filename, 'w') as f:
#     f.write('The sun dipped below the horizon.\n')
#     f.write('painting the sky in shades of amber.\n')
#     f.write('Somewhere in the distance.\n')
#     f.write('Silence finally settled over the valley.\n')
#     f.write('A valley sleeps beneath the silver moon.\n')
n_lines = sum(1 for line in open(filename))
t_words = sum(1 for line in open(filename) for word in line.split())
print(t_words)

# with open('notes.txt', 'a') as f:
#     f.write('Million\n')
#     f.write('Date : 02/06/2018 E.C\n')
with open('notes.txt', 'r') as f:
    for line in f:
        if ' in ' in line:
            line.lstrip(line)
        print(line.strip())
l = list(range(10))
l.remove(4)