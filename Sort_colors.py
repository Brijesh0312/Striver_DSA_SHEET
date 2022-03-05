# counting_sort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n0=0
        n1=0
        n2=0
        for i in nums:
            if(i==0):
                n0+=1
            elif(i==1):
                n1+=1
            else:
                n2+=1
        print(n0,"",n1,"",n2)
        for i in range(n0):
            nums[i]=0
        for j in range(n0,n0+n1):
            nums[j]=1
        for k in range(n0+n1,n0+n1+n2):
            nums[k]=2

# Dutch's national flag algorithm
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1
        while (mid <= high):
            if (nums[mid] == 0):
                t = nums[low]
                nums[low] = nums[mid]
                nums[mid] = t
                mid += 1
                low += 1
            elif (nums[mid] == 1):
                mid += 1
            else:
                t = nums[high]
                nums[high] = nums[mid]
                nums[mid] = t
                high -= 1

