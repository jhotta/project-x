LDFLAGS  += `pkg-config opencv --libs`
CFLAGS   += `pkg-config opencv --cflags`
CXXFLAGS += `pkg-config opencv --cflags`

circle:
	gcc -o move-circle move-circle.c $(CXXFLAGS) $(LDFLAGS) -lm

circle2:
	g++ -o main main.cpp $(CXXFLAGS) $(LDFLAGS)
