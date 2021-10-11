`timescale 1ns/1ns

module eightbit( first, second, cin,  cout,  sum );

parameter n= 1;
input [n-1:0] first;
input [n-1:0]  second;
input cin;
output cout;
output [n-1:0]  sum;
genvar i;
wire [n-1:0] cout1;
  fullAdder add1(.A(first[0]),.B(second[0]),.cin(cin), .sum(sum[0]), .cout(cout1[0]));

generate
 
 
 for(i=1; i<n; i=i+1)
  begin
 
 fullAdder hh(.A(first[i]),.B(second[i]),.cin(cout1[i-1]), .sum(sum[i]), .cout(cout1[i]));
 end

 
endgenerate


assign cout= cout1[n-1];





endmodule