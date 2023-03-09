def twosum(nums, target):
	check = False
	for i in range(1, len(nums)):
		for j in range(i):
			if nums[i] + nums[j] == target:
				check = True
				return [i,j]
		if check:
			break
