class MatrixIndex :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
 

class PlayFair :
    def __init__(self,plainText,k):    
        self.plainText = plainText
        self.key = self.removeSpaces(s=k).lower()
        self.cipherText = ''
        self.matrix = [[],[],[],[],[]]
        a2z = "abcdefghiklmnopqrstuvwxyz"
        temp = self.eleminateRedundancy(self.key)
        temp = self.eleminateRedundancy(temp + a2z)
        self.initMatrix(temp)
        self.encrypt()
    
    
    def removeSpaces(self,s) :
        temp = ""
        for i in range(len(s)):
            if (s[i] != ' ') :
                temp += s[i]
        return temp
    

    def eleminateRedundancy(self,s) :
        temp = ""
        for i in range(len(s)):
            x = s[i]
            if (temp.find(x) == -1) :
                temp += x
        return temp
    

    def initMatrix(self,s) :
        for i in range(5):
            for j in range(5):
                self.matrix[i].append(s[i * 5 + j])

    def addJunk(self,plainText) :
        temp = plainText[:]
        for i in range(0,len(temp),2):
            x1 = temp[i]
            if (i + 1 == len(temp)) :
                if (len(temp) % 2 != 0) :
                    z = 'x'
                    if x1 == 'x':
                        z = 'y'
                    temp = temp + "" + z
            else :
                x2 = temp[i + 1]
                if (x1 == x2) :
                    z = 'x'
                    if x1 == 'x':
                        z = 'y'
                    temp = temp[0: i + 1] + z + temp[i + 1:]
        if len(temp) % 2 == 1:
            temp+='x'
        return temp
    
    
    def indexOf(self,x) :
        if (x == 'j') :
            x = 'i'
        for i in range(5):
            for j in range(5):
                if (self.matrix[i][j] == x):
                    return MatrixIndex(i, j);
         
        return None;

    def encrypt(self) :
        temp = self.addJunk(self.removeSpaces(self.plainText)).lower();
        self.cipherText = "";
        for i in range(0,len(temp),2):
            p1 = temp[i] #same row change column
            p2 = temp[i + 1]
            a = self.indexOf(p1)
            b = self.indexOf(p2)
            if (a.x == b.x) :
                c1 = self.matrix[a.x][(a.y + 1) % 5]
                c2 = self.matrix[b.x][(b.y + 1) % 5]
            elif (a.y == b.y) :
                c1 = self.matrix[(a.x + 1) % 5][a.y]
                c2 = self.matrix[(b.x + 1) % 5][b.y]
            else :
                c1 = self.matrix[a.x][b.y]
                c2 = self.matrix[b.x][a.y]
            
            self.cipherText += c1 + "" + c2
    
print("ENTER PLAIN TEXT AND KEY (LINE SEPERATED):")
p = PlayFair(input(), input())
print("CIPHER:" + p.cipherText)
