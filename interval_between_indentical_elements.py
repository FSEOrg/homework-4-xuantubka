class Solution:
    """
    Giả sử mảng arr có các số  1 ở các vị trí a, b, c, d, e như sau:
    a b c d e 
    1 1 1 1 1
    Xem xét số 1 ở index c. sum of intervals của 1 ở c = |c-a|+|c-b|+|c-d|+|c-e|
    Vì c > a và b, đồng thời c < d và e, nên:
    Tổng giá trị khoảng cách của các điểm bên trái c là: c-a + c-b = 2*c - (a+b) = count*currentIndex - sum 
    Trong đó count là số lần xuất hiện các số tương tự với số ở c, sum là tổng các số này.
    Tương tự với tổng giá trị khoảng cách của các điểm bên phải của c là: d -c + e -c = (d+e) - 2*c = sum - count*currentIndex
    Tổng 2 số này ta có được giá trị sum of intervals tại 1 index bất kỳ. 
    Để thực hiện thuật toán này, ta có thể dùng 2 map để chứa count và sum của index của các phần tử trong mảng, sau đó duyệt
    theo 2 chiều từ trái qua phải và từ phải qua trái để tính kết quả cần tìm
    Time: O(n)
    Space: O(n)
    """
    def getDistances(self, arr: List[int]) -> List[int]:
        ans = [0]* len(arr)
        ans = self.calculate_sum_and_count_1_way(arr, ans, reverse=False)
        ans = self.calculate_sum_and_count_1_way(arr, ans, reverse=True)
        return ans
    
    def calculate_sum_and_count_1_way(self, arr, ans, reverse=None):
        if reverse:
            enum_arr = reversed(list(enumerate(arr)))
        else:
            enum_arr = enumerate(arr)
            
        sum_map = defaultdict(int)
        count_map = defaultdict(int)
        for idx, num in enum_arr:
            if not num in sum_map:
                sum_map[num] = 0
                count_map[num] = 0
            if reverse:
                ans[idx] += sum_map[num] - count_map[num]*idx
            else:
                ans[idx] += - sum_map[num] + count_map[num]*idx
            sum_map[num] = sum_map[num] + idx
            count_map[num] = count_map[num] + 1
        return ans
        
        