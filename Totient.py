# The Euclidean algorithm -----------------------------------------------------
# The smallest positive value of  a(x) + b(y) is equal to gcd(a,b). 
def gcd(a,b):
    while a: # loop
            a, b = b%a, a # sets a = b mod a, and b = a
    return b # return GCD
    
# Euler's Totient Function ----------------------------------------------------
def euler_phi_function(phi): 
    number_of_gcds_equal_to_1 = 0 
    
    for positive_integers_less_than_phi in range(phi - 1,0,-1): # range(start,stop,decrement)
        the_gcd = gcd(phi,positive_integers_less_than_phi) # call gcd function
        if the_gcd == 1: 
            number_of_gcds_equal_to_1 += 1 
    
    print "Euler's totient (phi)= ", number_of_gcds_equal_to_1 
    
# Main funtion ----------------------------------------------------------------
def main(): 
    phi = input('Enter a number: ') 
    euler_phi_function(phi) # one function calls another

main()
