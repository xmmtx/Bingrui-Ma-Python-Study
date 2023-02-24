for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                for e in range(0,10):
                    if a!=b and a!=c and a!=d and a!=e and b!=c and b!=d and b!=e and c!=d and d!=e:
                        n1=a*1000+b*100+c*10+d
                        n2=d*1000+c*100+b*10+a
                        if n1*e==n2:
                            print('',n1)
                            print('*  ',e)
                            print('—————')
                            print('',n2)