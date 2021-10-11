//Sequintial Logic output reg
	module D_FF
		(
			input wire clk, reset,
			input wire d,
			output reg q
		 );
	 
	 
		 always @(posedge clk, posedge reset)
			if (reset)
				q <= 1'b0;
			else
				q <= d;

	endmodule