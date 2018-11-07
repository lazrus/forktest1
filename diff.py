import re
import sys

#nothering more to be done
def loadFile(fileName) :
	"""
	Reads a file and returns a list of the lines as strings.

		@param  fileName  the file to be read
		@return 		  list of the lines in the given file
	"""
	lines = []
	with open(fileName, 'r') as inFile :
		for line in inFile :
			lines.append(line)
	return lines

def findDifference(lines1, lines2) :
	"""
	Attempts to find the minimum number of additions and deletions of
	lines in order to make the two input lists be equal. Returns two
	lists, one containing the lines which need to be changed, and
	one containing the needed change for each line.

		@param  lines1  list of strings
		@param  lines2  list of strings
		@return 		the lines which should be changed, and what
						should be done with them
	"""
	for i in range(len(lines1)) :
		if i <= len(lines2) :
			if lines1[i] == lines2[i] :
				print("0 ", lines1[i], end="")
			else :
				print("+ ", lines1[i], end="")
		else :
			print("+ ", lines1[i], end="")
	print("")
	return None, None

if __name__ == '__main__' :
	if len(sys.argv) != 3 :
		print("Usage: python3 my_diff.py <file1> <file2>")
		sys.exit()
	else :
		fileName1 = sys.argv[1]
		fileName2 = sys.argv[2]

	lines1 = loadFile(fileName1)
	lines2 = loadFile(fileName2)
	lines, changes = findDifference(lines1, lines2)
