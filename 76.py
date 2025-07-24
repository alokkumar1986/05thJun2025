# def showOutput(**kwargv):
# #   print(kwargv.items())
#   for key, val in kwargv.items():
#       print(f"{key} = {val}", end=' ')


# showOutput(key1=1, key2=2, key3=3, key4=4, key5=5, key6=6)


def showOutput(**kwargv):
#   print(kwargv.items())
  print(kwargv['key2'])
  print(list(kwargv.keys())[1])
  print(list(kwargv.values())[1])
  
  


showOutput(key1=1, key2=2, key3=3, key4=4, key5=5, key6=6)