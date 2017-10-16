# Compiles everything to get you going!

all:
	# cpp
	# ---
	g++ -std=c++11 MergeSortLL.cpp -o MergeSortLL.out
	g++ -std=c++11 LinkedList.cpp -o LinkedList.out
	g++ -std=c++11 Array.cpp -o Array.out

	# cpp bindings for cpython
	# ---
	cd MergeSort && python3 setup.py install
	cd MergeSortLL && python3 setup.py install
