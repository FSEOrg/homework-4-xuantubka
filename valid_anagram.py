class Solution:
    """
    - Hai chuỗi là anagram của nhau khi chúng có cùng số ký tự unique và tần suất xuất hiện của các ký tự trong 2 chuỗi cũng phải tương đồng nhau. 
    Do đó ta có thể sử dụng 1 map để chứa tần suất của các ký tự của 2 string. Sau đó so sánh 2 map này để kiểm tra điều kiện anagram  
    Time: O(max(len(s), len(t)))
    Space: O(max(len(s), len(t)))
    """
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(list(s))
        t_counter = Counter(list(t))
        if len(s_counter) != len(t_counter):
            return False
        for char in s_counter.keys():
            if  not char in t_counter or s_counter[char] != t_counter[char]:
                return False
        return True