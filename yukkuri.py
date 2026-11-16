#%%
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import subprocess

# AquesTalkPlayerの場所を指定する.
TOOL_PATH = "AquesTalkPlayer.exe"

def usage():
	print("yukkuri.py [プリセット名] [セリフ] [出力ファイル]")

def main():
	argv = sys.argv
	argc = len(argv)
	if argc < 4:
		usage()
		return

	# プリセット.
	preset = argv[1]
	# セリフ.
	word = argv[2]
	# 保存ファイル名
	output = argv[3]
	
	cmd = ["start", TOOL_PATH, "/T", word, "/P", preset, "/W", output]

	subprocess.run(" ".join(cmd), shell=True)


if __name__  == '__main__':
	main()
#%%

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import shutil

# AquesTalkPlayerの場所を指定する.
TOOL_PATH = "AquesTalkPlayer.exe"

def usage():
	print("yukkuri.py [設定ファイル]")

def main():
	argv = sys.argv
	argc = len(argv)
	if argc < 2:
		usage()
		return
	
	input = sys.argv[1]
	f = open(input, "r", encoding="utf-8")
	data = f.read()
	f.close()
	
	# 出力フォルダがなければ作成
	outdir = "output"
	if os.path.exists(outdir):
		# いったん消す.
		shutil.rmtree(outdir)
	os.makedirs(outdir)
	
	
	# プリセット.
	preset = "れいむ"
	idx = 1
	page = 0
	for line in data.split("\n"):
		# セリフ.
		word = line
		if word.strip() == "":
			continue # 空文字.
		if word[0] == "#": # コメント行.
			# 改ページ.
			page += 1
			idx = 1
			continue
		
		# 保存ファイル名
		print(page, "-", idx, ":", word)
		output = "\"%s/%02d_%02d_%s.wav\""%(outdir, page, idx, word[:16])
		
		cmd = ["start", TOOL_PATH, "/T", "\""+word+"\"", "/P", preset, "/W", output]

		subprocess.run(" ".join(cmd), shell=True)
		idx += 1


if __name__  == '__main__':
	main()

#%%
