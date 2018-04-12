#_*_ coding:utf-8 _*_
'''
#0007:有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
'''
import os

'''
os.walk(top, topdown=True, onerror=None, followlinks=False)
this can help us traverse the whole dir
in this functon we search all the file which end with '.py' in path
'''
def walk_dir(path):
	re_file=[]
	for root,dirs,files in os.walk(path):
		for file in files:
			if file.endswith('.py'):
				re_file.append(os.path.join(root,file))
	return re_file

def count_code(file):
	flag_note = False
	line_num = 0
	empty_line_num = 0
	note_num = 0
	code_num = 0
	with open(file,'r',encoding='utf-8') as f:
		text=f.read().split('\n')
		for line in text:
			if line.strip().startswith('\'\'\'') or line.strip().startswith("\"\"\""):
				if flag_note:
					flag_note=True
					note_num+=1
				else:
					flag_note=False
					note_num+=1
			elif line.strip().startswith('#') or flag_note:
				note_num+=1
			elif len(line) == 0:
				empty_line_num+=1
			else:
				code_num+=1
		print('there is %s code lines, %s empty lines and %s note lines in %s'%(code_num,empty_line_num,note_num,f))

def main():
	for file in walk_dir('.'):
		count_code(file)
	
main()