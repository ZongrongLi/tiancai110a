import copy

class Solution:
# n = 5 100 len(n) = 3 "000" 101
# changeBit(string, index)  changeBit("100",2) =>  101
# bfs(s, result,visited)

def changeBit(self,s,index):
    ret = ""
    for i in range(len(s)):
        if i != index:
            ret += s[i]
        else:
            ret += '1' if s[i] =='0' else '0'
    print("=>",s,index,ret)
    return ret
    
# s = 00 target 10
# bfs('10',['00']) 
# ['00','10']
def bfs(self,s, result, visited, target):
	if target == s:
		result.append(s)
		return result
	if s in visited:
		return
	visited[s] = True

	result.append(s)
	for i in range(len(s)):
		ret = self.bfs(self.changeBit(s,i),result.copy(),visited,target)
		print("---->>>",result)
		if not ret:
		return ret
	return None   

def grayCode(self, n: int) -> List[int]:
target = '{:b}'.format(n) # '10'
length = len(target) # 2
start = '0'*length
result=[]
visited={}
return self.bfs(start,result,visited,target) 
    
s = Solution()
s.grayCode(2)