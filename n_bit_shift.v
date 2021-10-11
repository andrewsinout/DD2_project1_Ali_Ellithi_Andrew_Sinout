// Combinatial Logic 
// file: n_bit_shift.v

`timescale 1ns/1ns

module n_bit_shift (in, out);

parameter n=2;


input [n-1:0] in;
output [n-1:0] out;

assign out= {in[n-2:0],1'b0 };




endmodule
