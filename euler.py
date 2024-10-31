import time
import sys
import importlib

if not len(sys.argv) > 1:
    print('Problem number not provided')
    exit()

problem_number = sys.argv[1]
file_name = f"euler-{problem_number}"

try:
    problem = importlib.import_module(file_name)
except:
    print('Module not found')
    exit()

start = time.time()
print('Result: ', problem.main())
print('Finished in ', time.time() - start, ' seconds')