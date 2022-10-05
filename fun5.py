
def marks(**data):
    with open('marks.txt','a') as f:
        for n,m in data.items():
            f.write(f'{n}:{m}\n')

marks(rajesh=20, brijesh=120)
marks(raj=130, ajay=50, suraj=90, chand=120)
marks()