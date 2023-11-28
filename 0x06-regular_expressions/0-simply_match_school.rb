#!/usr/bin/env ruby
# A regular expression

string_1 = ARGV[0].scan(/School/)
string_2 = string_1.join
puts "#{string_2}"
