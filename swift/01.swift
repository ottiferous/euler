var threes = [Int]()
var fives  = [Int]()

for num in 0...1000 {
    if num % 3 == 0 {
        threes.append(num)
    }
    if num % 5 == 0 {
        fives.append(num)
    }
}

print(Set(threes+fives).sort(<))
