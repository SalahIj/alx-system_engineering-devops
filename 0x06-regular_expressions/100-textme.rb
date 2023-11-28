#!/usr/bin/env ruby

SENDER = ARGV[0].scan(/from:(.*?)\]/)
RECEIVER = ARGV[0].scan(/to:(.*?)\]/)
FLAGS = ARGV[0].scan(/flags:(.*?)\]/)
result = [SENDER, RECEIVER, FLAGS].join(",")
puts "#{result}"
