ss = ["<<>><",">----<",">>>><<<<",">><<--->-",">>><<","-<-<-<-<->>-<<><<-->>--<"]
correct = [4,2,32,8,30]
def solution(s : str):
    """Returns the number of 'salutes' (2 / people meeting) from a string where '<' and '>' denote persons moving down an isle and their directions

    Args:
        s (str): a string with '<','-' or '>' characters that denote people moving or distance between them

    Returns:
        int: number of salutes
    """    
    s = s.replace("-","") #remove all dashes
    s = s.lstrip("<").rstrip(">")#remove all subordinates who don't meet anyone
    char = s[0]
    i = 0
    substr = ""
    salutes = 0
    #Counts the salutes that minions make from left to right.
    #Divides the string into parts where there is only one set of minions going right
    #and one set going left
    #
    #for ex. string >><>><< the total salutes are
    #salutes(>><) + salutes(>>>><<)
    while 1:
        if "<" not in substr and char == ">":
            substr = substr + ">"
        elif char == "<":
            substr = substr + "<"
        else:
            #the first sets of going right vs left are in the substring
            #for example: substr =  ">>><<"
            left = substr.count("<")
            right = substr.count(">")
            opposite = max([left,right])*min([left,right])
            salutes = salutes + 2*opposite
            if substr == s:
                break
            s = s.replace("<","",left)###
            substr = ""
            i = -1
        i = i + 1
        try:
            char = s[i]
        except IndexError:
            char = None
    return salutes

for s in ss:
    ans = solution(s)
    print(s,ans)
