# ops = [5,2,"C","D","+"]
op = []


def sum_data (l: list) -> int:
  sum = 0
  for i in l:
    sum += i
  return sum

def cal_points (ops) -> int:
  for i in ops:
    if (i.upper() != 'C' and i.upper() != 'D' and i != '+'):
      op.append(int(i))

    elif (i.upper() == 'C'):
      op.pop()

    elif (i.upper() == 'D'):
      op.append(op[0] * 2)

    elif (i == '+'):
      op.append(sum_data(op))

  return sum_data(op)


if __name__ == '__main__':
  line = input()
  ops = line.strip().split()
  print(line.strip().split())
  print(ops)
  print(cal_points(ops))

