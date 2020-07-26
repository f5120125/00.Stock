import sys
import requests
import numpy

# Insttruction:
#	py [source file] [參數1: 日期] [參數2: 股票代號]
#	py stock_test.py Date Stock_symbol
#
def main(argv):
	date = argv[1];
	stock_symbol = argv[2];
	url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?date=%s&stockNo=%s' % ( date, stock_symbol);
	#url = 'https://www.tpex.org.tw/web/stock/aftertrading/daily_trading_info/st43_print.php?l=zh-tw&d=%s&stkno=%s&s=0,asc,0' % (date, stock_symbol);
	#https://www.tpex.org.tw/web/stock/aftertrading/daily_trading_info/st43_print.php?l=zh-tw&d=109/07&stkno=8299&s=0,asc,0
	print("Your URL: ", url);

	req = requests.get(url);
	print("The response of your req: ", req);

	data_list = req.json();
	print("Data list: ", data_list);
	print("Type of data list: ", type(data_list));

	print("All dist is following:\n");
	index = 0;
	for index, item in enumerate(data_list):
		print(" ", index, item);

	print("len", len(data_list));

	numpy.array(data_list);
	cnt_of_fields = numpy.size(data_list['fields']);
	print("data list size", numpy.size(arr));
	print("cnt_of_fields", cnt_of_fields);

	cnt_of_date = len(data_list['data']);
	print("cnt_of_date", cnt_of_date);

	for i in range(cnt_of_fields):
		print("{:^18}".format(data_list['fields'][i]), end="");

	print("\n");

	for j in range(cnt_of_date):
		for i in range(cnt_of_fields):
			print("{:>20}".format(data_list['data'][j][i]), end="");
		print("\n");

if __name__ == "__main__":
	main(sys.argv);