from collections import Counter
def no_dups(s):
    # Your code here
    s = s.split(" ")
    for i in range(0, len(s)):
        s[i] = "".join(s[i])
    
    # print(s)

    unique_word = Counter(s)
    print(unique_word)

    string = " ".join(unique_word.keys())
    return(string)
    


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))