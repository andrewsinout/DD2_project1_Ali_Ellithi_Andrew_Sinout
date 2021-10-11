import pdb
import hdlparse.verilog_parser as vlog
import sys, getopt
import os 
import argparse

# sys.argv[1]
vlog_ex = vlog.VerilogExtractor()
with open( "input_verilog_file.v" , 'rt') as fh:
  code = fh.read()
#vlog_mods = vlog_ex.extract_objects_from_source(code)
vlog_mods = vlog_ex.extract_objects("input_verilog_file.v")

for m in vlog_mods:
	print('Module "{}":'.format(m.name))
	print('  Parameters:')
	for p in m.generics:
		print('\t{:20}{:8}{}'.format(p.name, p.mode, p.data_type))


	print('  Ports:' )
	for p in m.ports: 
		print('\t{:20}{:8}{}'.format(p.name, p.mode, p.data_type))




###################################### Initialization
print ("________________________________________________________\n")
mont = list ()
c= sys.argv[1] .split(".")
c = c[0] + '_tb.v'
cc= sys.argv[1] .split(".")
file1 = open(c, "w")  # write mode
file1.write("`timescale 1ns/1ps \n ")

## If input wire and output reg
#for p in m.ports: 
#	if p.data_type == 'wire':
#		p.data_type = ""
#	elif p.data_type == 'reg':
#		p.data_type = ""

for p in m.ports: 
	if  "wire" in p.data_type:
		if "[" in p.data_type:
			temp = p.data_type.split("[")
			p.data_type = "[" + temp[1]
		else:
			p.data_type = ""

	elif "reg" in p.data_type:
		if "[" in p.data_type:
			p.data_type = p.data_type.spilt("[")
		else:
			p.data_type = ""
	else:
		continue



file1.write("module " + m.name +"_tb; \n" )

for p in m.generics:
		file1.write (" parameter " + p.name + " = 10; \n")

for p in m.ports: 
	if (p.mode == 'input') & (p.name != 'clk') & (p.name != 'CLK')  :
		file1.write ("reg " + p.data_type + " " + p.name + "_i" + "; \n")
	elif (p.mode == 'output'): 
		file1.write ("wire " + p.data_type + " "+ p.name + "_o" + "; \n")
	elif (p.name == 'rest') | (p.name == 'rst') | (p.name == 'CLK') | (p.name == 'clk')   :
		file1.write ( "reg  " +p.name +"; \n" )
	else:
		continue

file1.write ( "\n\n" )

################################


###### Call module 

file1.write (m.name)
file1.write (" uut ( " )

for p in m.ports: 
	if (p.mode == 'input') & (p.name != 'clk') & (p.name != 'CLK') & (p.name != 'rst') :
		file1.write ( " ." + p.name + "(" +p.name +"_i) ," )
		temp = p.name + "_i"
		mont.append (temp)
	elif (p.mode == 'output'):
		file1.write ( " ." + p.name + "(" +p.name +"_o) ," )
		temp = p.name + "_o"
		mont.append (temp)
	elif (p.name == 'rst') | (p.name == 'clk') | (p.name == 'CLK'):
		file1.write ( " ." + p.name + "(" +p.name +") ," )
		temp = p.name 
		mont.append (temp)
	


size=file1.tell()               
file1.truncate(size -1 )        
file1.write ( "); \n" )



##############################




######## Clock 
file1.write ( "parameter ts = clk_period * 20; \n" )
file1.write ( "localparam clk_period = 10; \n\n" )
for p in m.ports: 
	if p.name == 'clk':	
		file1.write ("initial \nbegin \nclk = 0; \nforever #(clk_period/2) clk = ~clk; \nend \n\n\n")
	else:
		continue
###################



## Dumpvars
file1.write("\ninitial \n begin \n$dumpfile(\"")
#c = sys.argv[1] .spilt(".")
file1.write (cc[0])
file1.write (".vcd\"); \n $dumpvars; \n ")	


file1.write ("$display ( \"  Time  \"," )
for p in mont:
	 file1.write ("\"" + p + "   \" ,")
size=file1.tell()               
file1.truncate(size -1 )
file1.write (" ); \n")

file1.write ("$monitor($time, \" ")
for p in mont: 
	file1.write (" %d,")

size=file1.tell()               
file1.truncate(size -1 )
file1.write (" \" , ")
for p in mont: 
		file1.write (p + ",")
size=file1.tell()               
file1.truncate(size -1 )
file1.write (" );")
file1.write ("\n\nend \n\n")


#################################################### Intialize the values


file1.write ( " initial  begin \n\n" )
for p in m.ports: 
	if (p.mode == 'input') & (p.name != 'clk') & (p.name != 'CLK') & (p.name != 'rst') :
		file1.write ( " " +p.name +"_i = 0; \n" )
	elif p.name == 'rst':
		file1.write ( " " +p.name +"= 0; \n" )
	else:
		continue

file1.write ( " #(clk_period) \n\n # (ts) $stop;   \n\n end" )

#file1.write ( "\n  $finish; \n end \n \n" )		
file1.write ( "\n\n" )



file1.write ( "endmodule" )

#############################

file1.close()