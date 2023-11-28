#!/usr/bin/env ruby

string_1 = ARGV[0].scan(/^\d{0,9}\d{10}/)
string_2 = string_1.join
puts "#{string_2}"
