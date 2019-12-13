#!usr/bin/ruby

n = gets.to_i
data = Array.new(n)
(0..(n-1)).each do |i|
	data[i] = gets.to_i
end

(0..(n-1)).each do |i|
	puts data[i].even?
end
