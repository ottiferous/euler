// accumulate numbers while finding them
// no need to store in alternate data structure
// 
// will have to be adapted to a true 'generator'
// if its needed again in future problems

var x = 0
var y = 1

var sum = 0
var total = 0

while (sum < 4000000) {
   sum = x + y
   x = y
   y = sum
   if(sum % 2 == 0)
      total += sum
}
print(total)
