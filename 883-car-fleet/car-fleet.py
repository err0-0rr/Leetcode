class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time=[]
        for p,s in zip(position, speed):
            time.append((p,s))
        time.sort(key=lambda x:x[0])
        for i in range(len(time)):
            time[i]=(target-time[i][0])/time[i][1]
        s=[]
        #print(time)
        for i in time:
            while s and i>=s[-1]:
                s.pop()
            s.append(i)
        return len(s)
        