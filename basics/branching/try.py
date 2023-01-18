def fun():
  try:
      x = 7 / 0
  except Exception as e:
      print(e)
  finally:
     print('this is the fianlly block')

fun()
print('test')

