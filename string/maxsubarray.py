def maxsubarray(a):
  max_sum = 0
  max_begin = 0
  max_end = 0

  current_sum = 0
  current_begin =0
  current_end =0

  for current_end in range(len(a)):
    current_sum = current_sum + a[current_end]
    if current_sum > max_sum:
      max_sum = current_sum
      max_begin = current_begin
      max_end = current_end

    if current_sum <=0 :
      current_sum = 0
      current_begin = current_end +1

  return sum(a[max_begin:max_end+1])  
  
