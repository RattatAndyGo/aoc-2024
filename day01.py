print(sum([abs(int(sorted([p.replace('   ', ' ').split(' ')[0] for p in open('input01.txt').read().split('\n')])[i]) - int(sorted([p.replace('   ', ' ').split(' ')[1] for p in open('input01.txt').read().split('\n')])[i])) for i in range(len(open('input01.txt').read().split('\n')))]))