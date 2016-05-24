let MAX: Int = 4000000

var fibs = [Int]()
var num = 0

// seed values
fibs += [1,2]

while num < MAX {
    fibs.append(fibs.suffix(2).reduce(0, combine: {$0 + $1}))
    // coerce into type Int
    num = fibs.suffix(1).reduce(0,combine: +)
}
print(fibs)

