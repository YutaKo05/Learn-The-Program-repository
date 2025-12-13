class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out_put = 0
        # 保存用のリストがないとだめだね
        result_list=[]

        for n in nums:
            out_put += n
            result_list.append(out_put)
        
        return result_list