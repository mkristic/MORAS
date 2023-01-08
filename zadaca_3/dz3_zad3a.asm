// DZ3 Zad 3.a

@R0
D=M
@base
M=D

@R1
D=M
@power
M=D

@j
M=1
(POW)
   @R1
   D=M
   
   @j
   D=M-D
   
   @END_POW
   D; JGE
   
   @MULT
   0; JMP
 

(MULT)
@i
M=0
	(LOOP_MULT_START)
		@R0
		D=M
		
		@i
		D=M-D // base-i
		
		@LOOP_MULT_END
		D; JGE
		
		@base 
		D=M 
		
		@k
		M=M+D
		
		@i
		M=M+1
		
		@LOOP_MULT_START
		0; JMP
	
	(LOOP_MULT_END)
	
	@k
	D=M 
	
	@base
	M=D
	
	@k
	M=0
	
	@j
	M=M+1
	
	@POW
	0; JMP
	
(END_POW)
@base
D=M
@R2 
M=D

(END)
@END 
0;JMP
   
   