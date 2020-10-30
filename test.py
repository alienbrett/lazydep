import lazydep


depGraph = {
    'f1': 'seed',
    'f2': 'f1',
    'f3': ['f1','f2'],
    'f4': 'f3',
    'f5': 'f6',
    'f6': 'seed'
}

def f1(seed):
    return seed % 10

def f2(f1):
    return [f1]*f1

def f3(f1, f2):
    return (f1,sum(f2))




istate = {'seed': 42}

print(
	lazydep.resolve(depGraph, istate, {'f1': f1, 'f2': f2, 'f3': f3}, 'f3')
)

