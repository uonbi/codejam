{ challenge approach }
=======================================

Challenge A:

* loop from 1...10,000 as you check if a number is divisible by both 7 and 11
* If (a) above is true, add that number to a counter. 
* Repeat the above two process till 10,000
* Return the sum of the divisible numbers found

Challenge B:

* Find the LCM of all primes >2 but <10
* Loop through numbers 1...100,000
* Only do a check for odd numbers. i.e Check if a number is odd and that it is divisible by the LCM in (a)
* Return the sum of all the numbers

Challenge C:

* Get the largest prime below 2 billion

 	{
 	
 		Create a simple function to check if a number is prime:
 		
 		{
 		
 			fn(num):
 			 if num is 1: Not prime
 			 if num % 2 is 0: check if num is 2, if so, num is prime
 			 start = 3
 			 while squared(start) <= num:
 			  if num % start is 0: not prime
 			  start += 2#increment by hops of two
 			 if by any chance the condition of the loop is not met, then num is prime
 			 
 		}
 		
 		get the largest prime by decrementing, to fasten the process since the largest prime below 2 billion,
 		is closer to 2 billion than to 1
 		
 	}
 	
* Loop from 2...1000 (since 1^n is 1)

* Initialize power to 2 and get the result = n^power

* If result is less than the largest prime, increment power by 1

* if result is greater than the largest prime, then

  	{
  	
  		~Decrement power by one(This will give a result that is less than the largest prime)
  		~get the factorial of the power and get it product with the already initialized product.
  		~reset power to 2 ready for next iteration
  		
  	}

* Finally, get the last 12 digits of the resultant product. Result % (10^12). This will give the 
  	last 12 digits.
