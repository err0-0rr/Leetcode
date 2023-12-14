class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # people.sort(key=(lambda x:x[1]))
        # #print(people)
        # ans=[]
        # for i in people:
        #     count=i[1]
        #     j=0
        #     while j<len(ans):
        #         if count==0:
        #             break
        #         if ans[j][0]<i[0]:
        #             j+=1
        #         else:
        #             count-=1
        #             j+=1
                    
        #     while j<len(ans):
        #         if ans[j][0]<=i[0]:
        #             j+=1
        #         else:
        #             break
           
        #     ans.insert(j, i)
        # return ans
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = []
        
        for person in people:
            ans.insert(person[1], person)
            
        return ans