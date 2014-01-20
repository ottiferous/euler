// step 1_000 times and add the desired values
// to a total declared outside of the loop
//

var total = 0

for ( i = 0; i < 1000; i++) {
   if(( i % 3 == 0) || ( i % 5 == 0))
      total += i
}
print(total)
