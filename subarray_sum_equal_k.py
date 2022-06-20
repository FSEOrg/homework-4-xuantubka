class Solution:
    """
    C1: Sử dụng 2 vòng for để duyệt tìm các dãy có tổng = k. Cách này tốn O(n^2) thời gian.
    C2: Quan sát bài toán liên quan đến tổng chuỗi liền kề => có thể sử dụng prefix sum
    Giả sử input đầu vào là nums=[1,2,1,3] cho tổng k = 3
    prefix sum = [1,3,4,7]
    Nếu giữa 2 số bất kỳ trong mảng prefix_sum là prefix_sum[i] và prefix_sum[j], với j > i, và prefix_sum[j]- prefix_sum[i] = k 
    thì tức mảng các số từ i -> j có tổng = k. 
    Dựa theo quy luật này, ta có thể thấy với mảng prefix_sum bên trên, ta có 2 cặp là 1->4 và 4->7 có hiệu số = k (=3) thỏa mãn yêu cầu đề ra. 
    Tuy nhiên trong ví dụ thì vẫn còn 1 case bị bỏ sót, đó là mảng [1,2] ở đầu. Để xử lý trường hợp này thì ta cần set prefix_sum xuất phát từ 0, 
    tức prefix_sum trở thành [0,1,3,4,7]. Lúc đó sẽ detect đc 3 cases là từ 0->3, 1->4 và 4->7.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]*(len(nums)+1)
        for i in range(1, len(nums)+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        count = 0
        map = defaultdict(int)
        for i in prefix_sum:
            if i - k in map:
                count += map[i-k]
            map[i] = map[i]+1
        return count