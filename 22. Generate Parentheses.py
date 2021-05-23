class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list = ([])
        self.tracer(list,"",0,0,n)
        return list
    
    def tracer(self, list ,s, start, end, a):
       if(len(s) == a*2):
            list.append(s)
            return
       
       if start < a:
            self.tracer(list,s + "(", start+1, end, a)
        
       if end < start:
            self.tracer(list, s + ")" + start , end + 1 ,a)

        
        