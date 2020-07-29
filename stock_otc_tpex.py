import sys
import requests
import numpy
import pandas


def main(argv):
	#df = pandas.read_csv("D:\\workspace_for_KengHua\\00.Python_Learn\\00.Stock\\test.csv");
	df = pandas.read_csv("ST43_8299_202007_utf8.csv");
	print("Over The Counter");
	print("CSV content:\n", df);
	#print("type", type(df));
	#print("info", df.info());
	#print("shape", df.shape);
	print("Extract 1 row: ", df[0:0]);

if __name__ == "__main__":
	main(sys.argv);