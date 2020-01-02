def dotproduct(v1, v2):
    res = 0
    for k1 in v1:
        if k1 in v2:
            res += v1[k1]*v2[k1]
    return res

def dotproduct2(v1, v2):
    res=0
    #s_keys= set(v1.keys()).intersect(set(v2.keys()))
    s_keys= set(v1.keys())&set(v2.keys())
    for k in s_keys:
        res+=v1[k]*v2[k]
    return res

def dotproduct3(v1, v2):
    res = 0
    for k1 in v1:
        try:
            res += v1[k1]*v2[k1]
        except KeyError:
            pass
        except ValueError:
            pass
        except:
            pass
    return res

def dotproduct4(v1, v2):
    return sum([v1[k]*v2[k] for k in v1 if k in v2])


v1={'a':5};v2={'a':3,'b':2}
v3={'c':5};v4={'a':2,'b':1}
v5={'a':5,'b':4};v6={'a':-1,'b':2}

print(dotproduct4(v1,v2))
print(dotproduct4(v3,v4))
print(dotproduct4(v5,v6))
