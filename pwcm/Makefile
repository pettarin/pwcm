FUNC=cfunc
DRIVER=cmain

SRCS=$(DRIVER).cpp $(FUNC).cpp
CXXLIBS=

CXX=g++
CXXFLAGS=-Wall -pedantic

all: driver

$(DRIVER): $(SRCS)
	$(CXX) $(SRCS) -o $(DRIVER) $(CXXLIBS) $(CXXFLAGS)

driver: $(DRIVER)

test: $(DRIVER)
	./$(DRIVER)

clean:
	rm -f $(DRIVER)
