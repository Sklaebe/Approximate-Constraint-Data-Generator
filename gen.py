import os
import sys
import getopt
import random

def gen_unique_data(tuples, exception_rate):
	filename = "data_unique_" + str(exception_rate) + ".dat"
	buf = ''
	file = open(filename, "w")
	aggr_groups = 100000
	new_key = 0
	num_exceptions = 0
	for key in range(0, tuples):
		if random.randint(0, 100) < exception_rate:
			new_key = key % aggr_groups + tuples
			buf += str(key) +  "|" + str(new_key) + "|\n"
			num_exceptions += 1
		else:
			buf += str(key) +  "|" + str(key) + "|\n"
	file.write(buf)
	file.close()
	print 'Generated ' + str(100*float(num_exceptions)/tuples) + '% exceptions'
	
def gen_sort_data(tuples, exception_rate):
	filename = "data_sort_" + str(exception_rate) + ".dat"
	buf = ''
	file = open(filename, "w")
	new_key = 2 * tuples
	num_exceptions = 0
	for key in range(0, tuples):
		if random.randint(0, 100) < exception_rate:
			new_key = random.randint(0, 2*tuples)
			buf += str(key) +  "|" + str(new_key) + "|\n"
			num_exceptions += 1
			new_key -= 1
		else:
			buf += str(key) +  "|" + str(key) + "|\n"
	file.write(buf)
	file.close()
	print 'Generated ' + str(100*float(num_exceptions)/tuples) + '% exceptions'
	
def main(argv):
	
	tuples = 0
	exception_rate = 0
	constraint = ''
	
	try:
	  opts, args = getopt.getopt(argv,"ht:e:c:",["tuples=","exception_rate=", "constraint="])
	except getopt.GetoptError:
	  print 'gen.py -t <num_tuples> -e <exception_rate> -c <constraint(sort/unique)>'
	  sys.exit(2)
	for opt, arg in opts:
	  if opt == '-h':
		print 'gen.py -t <num_tuples> -e <exception_rate> -c <constraint(sort/unique)>'
		sys.exit()
	  elif opt in ("-t", "--tuples"):
		 tuples = int(arg)
	  elif opt in ("-e", "--exceptions"):
		 exception_rate = int(arg)
	  elif opt in ("-c", "--constraint"):
		 constraint = arg
	
	if (tuples <= 0 or exception_rate <= 0 or constraint not in ("sort", "unique")):
		print 'Invalid arguments'
		print 'gen.py -t <num_tuples> -e <exception_rate> -c <constraint(sort/unique)>'
		sys.exit()
		
	print 'Generating ', tuples, 'tuples with', exception_rate, '% exceptions for', constraint, 'constraint.'

	if constraint == 'sort':
		gen_sort_data(tuples, exception_rate)
	elif constraint == 'unique':
		gen_unique_data(tuples, exception_rate)	
	
if __name__ == "__main__":
	main(sys.argv[1:])
