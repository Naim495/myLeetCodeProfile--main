*LeetCode Problem 27: Remove Element**

---

## 🔹 Problem টা কি বলছে?

তোমাকে একটা **array** (nums) দেওয়া হয়েছে আর একটা **value** (val) দেওয়া হয়েছে।
তোমার কাজ হলো:

1. **nums থেকে val এর সব occurrence (বারবার আসা element) মুছে ফেলতে হবে।**
2. কিন্তু নতুন array বানানো যাবে না — **in-place** কাজ করতে হবে (মানে একই array এর ভেতর পরিবর্তন করতে হবে)।
3. তোমাকে **k return করতে হবে**, যেখানে k হলো "কতগুলো element val এর সমান না"।
4. nums এর প্রথম k টা জায়গায় সেই valid element গুলো রাখতে হবে।
5. বাকি element গুলো যাই থাকুক তাতে কিছু আসে যায় না (underscore দিয়ে বোঝানো হয়)।

---

## 🔹 Example 1:

```
nums = [3, 2, 2, 3], val = 3
```

* এখানে `val = 3`
* nums থেকে সব 3 মুছে ফেলতে হবে।

Step by step:

* [3, 2, 2, 3] → 3 বাদ দাও → [2, 2] বাকি থাকে।
* বাকি জায়গা "don't care" → [2, 2, _, _]

👉 তাই k = 2 (কারণ val ছাড়া 2 টা element আছে)

---

## 🔹 Example 2:

```
nums = [0,1,2,2,3,0,4,2], val = 2
```

* val = 2
* nums থেকে সব 2 মুছে ফেলতে হবে।

Step by step:

* [0,1,2,2,3,0,4,2] → 2 গুলো বাদ দাও → [0,1,3,0,4] বাকি থাকে।
* এই 5 টা element nums এর প্রথম 5 জায়গায় বসাও → [0,1,3,0,4,*,*,_]

👉 তাই k = 5

---

## 🔹 Approach (Two Pointer Method)

আমরা **একটা pointer দিয়ে পুরো array traverse করব**, আর **অন্য pointer দিয়ে valid element রাখব**।

Algorithm:

1. একটা `i` pointer নাও যা পুরো array ঘুরবে।
2. একটা `k` pointer নাও যা valid element রাখবে।
3. যদি nums[i] != val হয়, তাহলে nums[k] = nums[i] দাও, তারপর k++ করো।
4. Traverse শেষে k রিটার্ন করো।

---

## 🔹 Python Solution

```python
class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:   # valid element
                nums[k] = nums[i]
                k += 1
        return k
```

---

## 🔹 Dry Run

Input:

```
nums = [3,2,2,3], val = 3
```

Steps:

* i=0 → nums[0]=3 → skip
* i=1 → nums[1]=2 → nums[k]=2 → nums=[2,2,2,3], k=1
* i=2 → nums[2]=2 → nums[k]=2 → nums=[2,2,2,3], k=2
* i=3 → nums[3]=3 → skip

👉 Output: k=2, nums=[2,2,*,*]

---

✅ **Final Output:** তোমার ফাংশন শুধু k return করবে, কিন্তু judge nums এর প্রথম k টা element চেক করবে।

---

তুমি কি চাও আমি এই সমাধানটা **চিত্র (diagram) দিয়ে step by step visualization** করে দেখাই, যেন একবারেই crystal clear হয়ে যায়?
