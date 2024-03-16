CFLAGS = -O3

all: final

final: main.o models.o 
	echo "Linking and producing the final application"
	g++ $(CFLAGS) main.o models.o -o final.exe

main.o:  main.cpp
	echo "Compiling the main file"
	g++ $(CFLAGS) -c main.cpp

models.o: models.o
	echo "Compiling the models file"
	g++ $(CFLAGS) -c models.cpp

clean:
	echo "Removing everything but the source files"
	rm main.o hello.o final.exe