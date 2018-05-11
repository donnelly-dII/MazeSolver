import common
import student_code

class bcolors:
	RED    = "\x1b[31m"
	GREEN  = "\x1b[32m"
	NORMAL = "\x1b[0m"

def check_result(title, map1, map2, dim):
	result=True
	print(title)
	for y in range(0,dim.MAP_HEIGHT):
		v=""
		for x in range(0,dim.MAP_WIDTH):
			if (map1[y][x]==map2[y][x]):
				v+=bcolors.GREEN+str(map1[y][x])+bcolors.NORMAL
			else:
				result = False
				v+=bcolors.RED+str(map1[y][x])+bcolors.NORMAL
		print(v)
	if (result):
		print("Test Result: " + bcolors.GREEN+"Passed"+bcolors.NORMAL)
	else:
		print("Test Result: " + bcolors.RED+"Failed"+bcolors.NORMAL)
	return result
	
data1 = ("2000000000"
"0101111111"
"0100000000"
"0101111111"
"0101000001"
"0101010110"
"0101010000"
"0100011110"
"0011111110"
"1011111110"
"1011111111"
"1000000003")
			  
gold_df1 = ("5444444444"
  "5141111111"
  "5144444444"
  "5141111111"
  "5141444441"
  "5141414114"
  "5141414444"
  "5144411114"
  "5511111114"
  "1511111114"
  "1511111111"
  "1555555555")
					 
gold_bf1 = ("5444444444"
  "5141111111"
  "5144444444"
  "5141111111"
  "5141444441"
  "5141414110"
  "5141414440"
  "5144411110"
  "5511111110"
  "1511111110"
  "1511111111"
  "1555555555")
					 

data2 = ("0000000000"
"1111110101"
"0300010101"
"1111010101"
"0001010101"
"0100010101"
"1111010101"
"0000000101"
"0111111100"
"0000000101"
"0111111120"
"0000000010")
			  
gold_df2 = ("0000005554"
  "1111115151"
  "0555515151"
  "1111515151"
  "4441515151"
  "4144515151"
  "1111515151"
  "4444555151"
  "4111111154"
  "4444444151"
  "4111111154"
  "4444444414")
					 
gold_bf2 = ("4444445554"
  "1111115151"
  "0555515151"
  "1111515151"
  "4441515151"
  "4144515151"
  "1111515151"
  "4444555151"
  "4111111154"
  "4440000151"
  "4111111154"
  "4000000014")

data3 = ("0000000000"
"0010111111"
"0210100000"
"1110101110"
"0000101010"
"0010101010"
"0010001010"
"0011111010"
"0000000010"
"0011111110"
"0010001031"
"1000101001")
			  
gold_df3 = ("4444444444"
  "4414111111"
  "4414144444"
  "1114141114"
  "4444141414"
  "4414141414"
  "4414441414"
  "4411111414"
  "4444444414"
  "4411111114"
  "4414441031"
  "1444141001")
					 
gold_bf3 = ("4444444444"
  "4414111111"
  "4414144444"
  "1114141114"
  "4444141414"
  "4414141414"
  "4414441414"
  "4411111414"
  "4444444414"
  "4411111114"
  "4414441031"
  "1444141001")

map4 =("3200000000"
"1111111110"
"0000000010"
"0111111010"
"0100001010"
"0101101010"
"0101101010"
"0101001010"
"0101111010"
"0100000010"
"0111111110"
"0000000000")


gold_bf4 =("5540000000"
"1111111110"
"0000000010"
"0111111010"
"0100001010"
"0101101010"
"0101101010"
"0101001010"
"0101111010"
"0100000010"
"0111111110"
"0000000000")

 

gold_df4 =("5544444444"
"1111111114"
"4444444414"
"4111111414"
"4144441414"
"4141141414"
"4141141414"
"4141441414"
"4141111414"
"4144444414"
"4111111114"
"4444444444")

 

map5 = ("3000"
"1110"
"0000"
"2110")

gold_bf5 = ("5555"
"1115"
"5555"
"5114")

 

gold_df5 = ("5555"
"1115"
"5555"
"5114")

 

map6 = ("200000000000000"
"111111111111110"
"000000000000000"
"011111111111111"
"000000000000000"
"111111111111110"
"000000000000000"
"011111111111111"
"000000000000000"
"111111111111110"
"000000000000000"
"011111111111111"
"000000000000000"
"111111111111110"
"000000000000000")

 

gold_bf6 = ("444444444444444"
"111111111111114"
"444444444444444"
"411111111111111"
"444444444444444"
"111111111111114"
"444444444444444"
"411111111111111"
"444444444444444"
"111111111111114"
"444444444444444"
"411111111111111"
"444444444444444"
"111111111111114"
"444444444444444");

 

gold_df6 = ("444444444444444"
"111111111111114"
"444444444444444"
"411111111111111"
"444444444444444"
"111111111111114"
"444444444444444"
"411111111111111"
"444444444444444"
"111111111111114"
"444444444444444"
"411111111111111"
"444444444444444"
"111111111111114"
"444444444444444");

 

map7=("20000000000000000000"
"11111111111111111110"
"00000000000000000000"
"01111111111111111111"
"00000000000000000000"
"11111111111111111110"
"00000000000000000000"
"01111111111111111111"
"00000000000000000000"
"11111111111111111110"
"30000000000000000000")

 

gold_bf7=("55555555555555555555"
"11111111111111111115"
"55555555555555555555"
"51111111111111111111"
"55555555555555555555"
"11111111111111111115"
"55555555555555555555"
"51111111111111111111"
"55555555555555555555"
"11111111111111111115"
"55555555555555555555")

 

gold_df7=("55555555555555555555"
"11111111111111111115"
"55555555555555555555"
"51111111111111111111"
"55555555555555555555"
"11111111111111111115"
"55555555555555555555"
"51111111111111111111"
"55555555555555555555"
"11111111111111111115"
"55555555555555555555")

 

map8 =("200000000000000"
"010111111111111"
"010000000000000"
"011111111111110"
"000000000000010"
"011111111111110"
"000000000000010"
"011111111111010"
"000000000001010"
"011111111111010"
"000000000001010"
"011111111111010"
"310000000000010"
"111111111111110"
"000000000000000")

 

gold_bf8 =("544444444444400"
"514111111111111"
"514444444440000"
"511111111111110"
"544444444000010"
"511111111111110"
"544444400000010"
"511111111111010"
"544440000001010"
"511111111111010"
"544000000001010"
"511111111111010"
"510000000000010"
"111111111111110"
"000000000000000")

 

gold_df8 = ("544444444444444"
"514111111111111"
"514444444444444"
"511111111111114"
"544444444444414"
"511111111111114"
"544444444444414"
"511111111111414"
"544444444441414"
"511111111111414"
"544444444441414"
"511111111111414"
"514444444444414"
"111111111111114"
"444444444444444")


'''
        TEST 1

'''
dim1 = common.dimension(10,12)
gold_dfmap1 = common.init_map(dim1);
common.set_map(gold_dfmap1, gold_df1,dim1)
gold_bfmap1 = common.init_map(dim1)
common.set_map(gold_bfmap1, gold_bf1,dim1)

dfmap1 = common.init_map(dim1)
common.set_map(dfmap1, data1, dim1)
df1 = student_code.df_search(dfmap1,dim1)
tdf1 = "Simple maze first depth search results:";
cdf1 = check_result(tdf1,dfmap1,gold_dfmap1,dim1)

bfmap1 = common.init_map(dim1)
common.set_map(bfmap1, data1, dim1)
bf1 = student_code.bf_search(bfmap1,dim1)
tbf1 = "Simple maze first breadth search results:"
cbf1 = check_result(tbf1,bfmap1,gold_bfmap1, dim1)
'''
        TEST 2

'''
dim2 = common.dimension(10,12)
gold_dfmap2 = common.init_map(dim2);
common.set_map(gold_dfmap2, gold_df2,dim2)
gold_bfmap2 = common.init_map(dim2)
common.set_map(gold_bfmap2, gold_bf2,dim2)

dfmap2 = common.init_map(dim2)
common.set_map(dfmap2, data2, dim2)
df2 = student_code.df_search(dfmap2,dim2)
tdf2 = "Simple maze first depth search results:";
cdf2 = check_result(tdf2,dfmap2,gold_dfmap2,dim2)

bfmap2 = common.init_map(dim2)
common.set_map(bfmap2, data2, dim2)
bf2 = student_code.bf_search(bfmap2,dim2)
tbf2 = "Simple maze first breadth search results:"
cbf2 = check_result(tbf1,bfmap2,gold_bfmap2, dim2)
'''
        TEST 3

'''
dim3 = common.dimension(10,12)
gold_dfmap3 = common.init_map(dim3);
common.set_map(gold_dfmap3, gold_df3,dim3)
gold_bfmap3 = common.init_map(dim3)
common.set_map(gold_bfmap3, gold_bf3,dim3)

dfmap3 = common.init_map(dim3)
common.set_map(dfmap3, data3, dim3)
df3 = student_code.df_search(dfmap3,dim3)
tdf3 = "First Test depth search results:";
cdf3 = check_result(tdf3,dfmap3,gold_dfmap3,dim3)

bfmap3 = common.init_map(dim3)
common.set_map(bfmap3, data3, dim3)
bf3 = student_code.bf_search(bfmap3,dim3)
tbf3 = "First Test breadth search results:"
cbf3 = check_result(tbf3,bfmap3,gold_bfmap3, dim3)
'''
        TEST 4

'''
dim4 = common.dimension(10,12)
gold_dfmap4 = common.init_map(dim4);
common.set_map(gold_dfmap4, gold_df4,dim4)
gold_bfmap4 = common.init_map(dim4)
common.set_map(gold_bfmap4, gold_bf4,dim4)

dfmap4 = common.init_map(dim4)
common.set_map(dfmap4, map4, dim4)
df4 = student_code.df_search(dfmap4,dim4)
tdf4 = "Second Test depth search results:";
cdf4 = check_result(tdf4,dfmap4,gold_dfmap4,dim4)

bfmap4 = common.init_map(dim4)
common.set_map(bfmap4, map4, dim4)
bf4 = student_code.bf_search(bfmap4,dim4)
tbf4 = "Simple maze first breadth search results:"
cbf4 = check_result(tbf4,bfmap4,gold_bfmap4, dim4)

'''
        TEST 5

'''
dim5 = common.dimension(4,4)
gold_dfmap5 = common.init_map(dim5);
common.set_map(gold_dfmap5, gold_df5,dim5)
gold_bfmap5 = common.init_map(dim5)
common.set_map(gold_bfmap5, gold_bf5,dim5)

dfmap5 = common.init_map(dim5)
common.set_map(dfmap5, map5, dim5)
df5 = student_code.df_search(dfmap5,dim5)
tdf5 = "Simple maze first depth search results:";
cdf5 = check_result(tdf5,dfmap5,gold_dfmap5,dim5)

bfmap5 = common.init_map(dim5)
common.set_map(bfmap5, map5, dim5)
bf5 = student_code.bf_search(bfmap5,dim5)
tbf5 = "Simple maze first breadth search results:"
cbf5 = check_result(tbf5,bfmap5,gold_bfmap5, dim5)

'''
        TEST 6

'''
dim6 = common.dimension(15,15)
gold_dfmap6 = common.init_map(dim6);
common.set_map(gold_dfmap6, gold_df6, dim6)
gold_bfmap6 = common.init_map(dim6)
common.set_map(gold_bfmap6, gold_bf6, dim6)

dfmap6 = common.init_map(dim6)
common.set_map(dfmap6, map6, dim6)
df6 = student_code.df_search(dfmap6, dim6)
tdf6 = "Empty map first depth search results:";
cdf6 = check_result(tdf6,dfmap6,gold_dfmap6, dim6)

bfmap6 = common.init_map(dim6)
common.set_map(bfmap6, map6, dim6)
bf6 = student_code.bf_search(bfmap6, dim6)
tbf6 = "Empty map first breadth search results:"
cbf6 = check_result(tbf6,bfmap6,gold_bfmap6, dim6)

'''
        TEST 7

'''
dim7 = common.dimension(20,11)
gold_dfmap7 = common.init_map(dim7);
common.set_map(gold_dfmap7, gold_df7, dim7)
gold_bfmap7 = common.init_map(dim7)
common.set_map(gold_bfmap7, gold_bf7, dim7)

dfmap7 = common.init_map(dim7)
common.set_map(dfmap7, map7, dim7)
df5 = student_code.df_search(dfmap7, dim7)
tdf7 = "Empty map first depth search results:";
cdf7 = check_result(tdf7,dfmap7,gold_dfmap7,dim7)

bfmap7 = common.init_map(dim7)
common.set_map(bfmap7, map7, dim7)
bf7 = student_code.bf_search(bfmap7, dim7)
tbf7 = "Empty map first breadth search results:"
cbf7 = check_result(tbf7,bfmap7,gold_bfmap7,dim7)

'''
        TEST 8

'''
dim8 = common.dimension(15,15)
gold_dfmap8 = common.init_map(dim8);
common.set_map(gold_dfmap8, gold_df8, dim8)
gold_bfmap8 = common.init_map(dim8)
common.set_map(gold_bfmap8, gold_bf8, dim8)

dfmap8 = common.init_map(dim8)
common.set_map(dfmap8, map8, dim8)
df8 = student_code.df_search(dfmap8, dim8)
tdf8 = "Empty map first depth search results:";
cdf8 = check_result(tdf8,dfmap8,gold_dfmap8, dim8)

bfmap8 = common.init_map(dim8)
common.set_map(bfmap8, map8, dim8)
bf8 = student_code.bf_search(bfmap8, dim8)
tbf8 = "Empty map first breadth search results:"
cbf8 = check_result(tbf8,bfmap8,gold_bfmap8, dim8)

print "DONE"