(ns cleuler.01
	(:use [cleuler.core]))

(reduce + (filter #(or (zero? (mod % 3))(zero? (mod % 5))) (range 1 1000)))

(println "Haha dogs look funny in hats")
