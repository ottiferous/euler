(ns cleuler.02
  :use [cleuler.core])

(defn fibon [limit]
  (loop [count 1
         x 1
         a 0
         b 1]
    (if (= count limit) 
      x 
      (recur (inc count)(+ a b)(+ a b) a))))
