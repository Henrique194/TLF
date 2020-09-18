sums = dict([ (3, 0),
              (4, 0),
              (5, 0),
              (6, 0),
              (7, 0),
              (8, 0),
              (9, 0),
              (10, 0),
              (11, 0),
              (12, 0),
              (13, 0),
              (14, 0),
              (15, 0),
              (16, 0),
              (17, 0),
              (18, 0) ])

for s in range(3, 19) :
    for i in range(1, 7) :
        for j in range(1, 7) :
            for k in range(1, 7) :
                if i + j + k == s :
                    sums[s] += 1

print(sums)
