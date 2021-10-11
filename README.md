# DD2_project1_Ali_Ellithi_Andrew_Sinout

How to use the tool:

Get Verilog file from previous LABs, internet, or your own one. Then, move it to the same directory as the python file.

How to compile:

After inserting the .v file. You will open the terminal in MAC, Linux, and WSL windows. Run the
python command and then mention the name of the .v file that you want to generate one from
it.

Dependencies:

The program requires a python3 installed. In addition to, you will need to download WSL if you
have windows and use it to download terminal and use it or use the terminal in MAC and Linux.
Then, you will need to download the HDLparse library from the pip command from the terminal.
You can check the validity of the testbench through Icarus Verilog that you can download from
the terminal or use online sources like CloudV.

Code Structure:

We used the python3 to write the testbench project. We used it in order to take advantage of
the HDL parse library. This library enabled parse the .v file automatically. Then, we write into file
that should contain the testbench. The main principle of the code that we iterate over the
ports that contain the name, datatype, and mode. Then, we use this for loops to initialize
variables and call the module. Furthermore, we created some lines that responsible for creating
clock and dump the values and monitor them.

Problems:

First of all the major problem was parsing the file and extract the inputs and the outputs; but
with the use of the given library, we solved this problem and handle it. Also, we faced a problem
in dealing with datatype that contains wire and reg. We solved it by spilt command that discard the
wire and reg in the data_type. We add the clock that responsible for the sequential logic only if needed.
