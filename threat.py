
''' Purpose: supports simple testing of the double functions
'''

# import necessary modules
import double

# testing longer()

s1 = "abcd";    t1 = "ef"
s2 = "hij";     t2 = "klmnnop"
s3 = "str";     t3 = "int"
s4 = "int";     t4 = "str"

u1 = double.longer( s1, t1 )
u2 = double.longer( s2, t2 )
u3 = double.longer( s3, t3 )
u4 = double.longer( s4, t4 )

output1 = "longer( " + s1 + ", " + t1 + " ): " + str( u1 )
output2 = "longer( " + s2 + ", " + t2 + " ): " + str( u2 )
output3 = "longer( " + s3 + ", " + t3 + " ): " + str( u3 )
output4 = "longer( " + s4 + ", " + t4 + " ): " + str( u4 )

print( output1 )
print( output2 )
print( output3 )
print( output4 )

print( "\n-------------------------------------------------------\n" )

# testing summation()

n1 = 5
n2 = 1
n3 = 0

s1 = double.summation( n1 )
s2 = double.summation( n2 )
s3 = double.summation( n3 )

output1 = "summation( " + str( n1 ) + " ): " + str( s1 )
output2 = "summation( " + str( n2 ) + " ): " + str( s2 )
output3 = "summation( " + str( n3 ) + " ): " + str( s3 )

print( output1 )
print( output2 )
print( output3 )
