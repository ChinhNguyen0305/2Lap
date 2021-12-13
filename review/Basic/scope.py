a = 100


def test(b):
    a = 2
    print(b)
    def testb():
        nonlocal a
        a += 2
        print(a)



test(303)
print(f'globale a: {a}')
