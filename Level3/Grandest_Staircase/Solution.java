/**
 * Solution to try
 Given n bricks for example, m is the first staircase,
 if we want to get the most staircases, it must follow this arrangement:
 m + (m-1)+ (m-2)...+1 = (m+1)*m/2 = n;
 (m+1)*m/2 >= m*m/2 
 So we got m<=sqrt(2*n); 
 Conclusion : The height of the first staircase must be smaller than sqrt(2*n);
 */
 