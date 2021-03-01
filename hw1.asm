swap:	LSL X10, X1, #3  // reg X10 = k*8
	ADD X10, X0, X10 // reg X10 = v + (k * 8)
			// reg X10 has the address of v[k]
	LDUR X9, [X10, #0] // reg X9 = (temp) = v[k]
	LDUR X11, [X10, #8] // reg X11 = v[k+1]

	STUR X11, [X10, #0] // v[k] = reg X11
	STUR X9, [X10, #8] // v[k+1] = reg X9 (temp)

	BR LR 
