# one report per line
# each report list of nums called levels
# levels must either increase or decrease across the whole report
# levels can only differ by at least one and at most three
# How many reports are "safe"

def isSafe(arr):
    def is_valid(arr):
        """Check if the array is strictly increasing or decreasing with valid differences."""
        increasing = all(1 <= arr[i + 1] - arr[i] <= 3 for i in range(len(arr) - 1))
        decreasing = all(1 <= arr[i] - arr[i + 1] <= 3 for i in range(len(arr) - 1))
        return increasing or decreasing

    # If the array is already valid, return True
    if is_valid(arr):
        return True

    # Try removing each element and check if the resulting array is valid
    for i in range(len(arr)):
        modified_arr = arr[:i] + arr[i + 1:]  # Remove the i-th element
        if is_valid(modified_arr):
            return True

    # If no single removal makes the array valid, return False
    return False

def toInt(row):
  for idx, elem in enumerate(row):
    if isinstance(elem, str):
      row[idx] = int(elem)
  return row

def readFile(filename):
  twoDimData = []
  
  with open(filename) as file:
    data = file.readlines()

    for d in data:
      print(d)
      d = d.rstrip()
      d = d.split(' ')
      d = toInt(d)
      twoDimData.append(d)

  return twoDimData

if __name__ == '__main__':
  data = readFile('puzzle.txt')
  safe_reports = []

  for idx, report in enumerate(data):
    if isSafe(report):
      safe_reports.append(report)

  print(len(safe_reports))

