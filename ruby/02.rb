fib =
	lambda{ a, b = 1, 2 
		lambda{ begin a ensure a, b = b, a + b end }
	}[]

x = [0]
while x.last < 4_000_000
	x << fib[]
end
puts x.max
