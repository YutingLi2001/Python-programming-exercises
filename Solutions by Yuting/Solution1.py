from typing import List
def find_numbers(nums: List[int], divisible_by: int, not_multiple_of: int) -> str:
    if len(nums) == 0: return ""
    return ",".join((str(num) for num in nums if num % divisible_by == 0 and num % not_multiple_of != 0))
if __name__ == "__main__":
    sample_entry = list(range(2000,3201))
    sample_result = find_numbers(nums = sample_entry, divisible_by=7, not_multiple_of=5)
    print(sample_result)
