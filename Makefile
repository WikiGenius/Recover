CC =clang
CFLAGS =-c -Wall -g
LDLIBS=-lm
all: recover
recover: recover.o  
	$(CC) recover.o -o recover
recover.o: recover.c
	$(CC) $(CFLAGS)  recover.c
test: 
	python test.py
clean:
	rm -rf *.o recover *.jpg