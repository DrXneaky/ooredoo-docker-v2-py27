print('another message')
#exit()
print('message outside fn')

def fn():
  message = 'message inside fn'
  return message

message = fn()