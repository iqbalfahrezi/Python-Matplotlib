arr = [1, 2, 3, 4, 5, 6];
start = 0;
end = size(arr) - 1;

while (start < end) {
  temp = arr[start];
  arr[start] = arr[end];
  arr[end] = temp;
  start++;
  end--;
}

print(arr);
