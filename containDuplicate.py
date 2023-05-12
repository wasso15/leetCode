def containsDuplicate(nums):
    hashset=set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

number = [1,2,3,4,1]

response=containsDuplicate(nums=number)
print(response)