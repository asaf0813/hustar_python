def tokenize(trg, N=1):
    temp = trg.split()
    ngrams_list = list()
    for i in range(0, len(temp)-N + 1):
        ngrams_list.append(' '.join(temp[i:i+N]))
    return ngrams_list

def main():
    a = "There was a farmer who had a dog ."
    print(tokenize(a))
    print(tokenize(a,2))