import pickle



path = '/Users/sf/Library/Mobile Documents/3L68KQB4HG~com~readdle~CommonDocuments/Documents/导师-组会-课题/飞桨共创/Example 3/ch_2Dxysec.pickle'

with open(path, 'rb') as f:
    f1= pickle.load(f)

print(f1)



