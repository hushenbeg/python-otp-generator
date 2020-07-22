import math, random

def otp_generate():
	digits = '0123456789'
	otp = ""
	for i in range(5):
		otp+= digits[math.floor(random.random()*10)]
	return otp

if __name__=="__main__":
	print("your 4 digit otp is:", otp_generate())
