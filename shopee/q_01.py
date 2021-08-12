# 简单XML字符串，可能包含嵌套，需要输出对应的值。若不存在则返回空字符串。

def getValue(inxml, path):
	import xml.etree.ElementTree as ET
	root = ET.fromstring(inxml)
	cur =  path.split(".")[0]
	print(cur)
	cur_element = root.find(cur)
	print(cur_element.tag)
	# print(cur_element.text)
	# return cur_element


	# my_text = my_text.replace(".","/")
	# my_text = "./" + my_text
	# res = root.find(my_text)
	# if res is not None:
	# 	return res.text
	# else:
	# 	return ""


