a, b = 0, 1

x = [0]
while x.last < 4_000_000
	x << b
   a, b = b, a+b
end
puts x.select { |num| num.even? }.inject(&:+)
