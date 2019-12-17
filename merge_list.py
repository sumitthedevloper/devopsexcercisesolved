try:
	import sys
	import ast
	list_1 = ast.literal_eval(sys.argv[1])
	list_2 = ast.literal_eval(sys.argv[2])
	merged_list = list_1 + list_2
	print(sorted(merged_list))
except:
	print("Invalid Argument Syntax")
