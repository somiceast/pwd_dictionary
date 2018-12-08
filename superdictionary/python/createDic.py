num = input('请输入关键词个数：')
list = []
for i in range(1,int(num)+1):
  list.append(input('关键词{}:'.format(i)))
def permutation(result, str, list):
  if len(list) == 1:
    result.append(str + list[0])
  else:
    uniq_dict={}
    for temp_str in list:
      temp_list = list[:]
      temp_list.remove(temp_str)
      if str == '':
        permutation(result, temp_str, temp_list)
      else:
        permutation(result, str + temp_str, temp_list)
def listToStr(list):
  str = ''
  for i in list:
    str = str+i
  return str
def saveDic(str=''):
  loc = input('请输入字典存放路径：')
  with open(loc,'a') as f:
    f.write(str)
  return
def listToTxt(list):
  txt = ''
  for i in list:
    txt = txt + i + '\n'
  return txt
if __name__ == '__main__':
  result = []
  permutation(result,'',list)
  ok = listToTxt(result)
  saveDic(ok)
