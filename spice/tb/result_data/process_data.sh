#paste 2 file con
paste data_ro_1.txt data_ro_2.txt > data_ro.txt

paste data_vco_with_clk_1.txt data_vco_with_clk_2.txt > data_vco_clk.txt

#paste data_vco_1.txt data_vco_2.txt > data_vco_summary.txt

#delete row and line trash
sed -i '1,5d' data_ro.txt
sed -i '1,5d' data_vco_clk.txt
#sed -i '1,5d' data_vco_summary.txt


#process data of ROs
awk '{print $3 " " $4 " " $5 " " $8 " " $9 " " $10}' data_ro.txt > data_ro_summary.txt
rm data_ro.txt
awk '{
        if($1=="1.800000e+00") 
                $0="1"
        else
                $1="0"
        print $0}' data_ro_summary.txt > ro_data.txt
rm data_ro_summary.txt


#process data of pha_vco has pha_read_out
awk '{print $3 " " $4 " " $5 " " $8 " " $9 " " $10}' data_vco_clk.txt > vco_clk_data.txt
rm data_vco_clk.txt 
#awk '{
#        if($1=="1.800000e+00") 
#                $0="1"
#        else
#                $1="0"
#        print $0}' data_vco_clk_summary.txt > vco_clk_data.txt
#rm data_vco_clk_summary.txt

#process data of vco
#awk '{print $4 " " $5 " " $8 " " $9 " " $10}' data_vco_summary.txt > vco_data.txt
#rm data_vco_summary.txt
#awk '{
#	if()
#	}'


