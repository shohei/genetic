package main

import (
	"fmt"
)

// func (pop *Population) {

// }
type Individual struct {
}

type Population struct {
	ind     [POP_SIZE]Individual
	nextInd [POP_SIZE]Individual
}

func NewPopulation() *Population {
	pop := new(Population)
	pop.ind = [POP_SIZE]Population{}
	pop.nextInd = [POP_SIZE]Population{}
	for i := 0; i < POP_SIZE; i++ {
		pop.ind[i] = Population{}
	}
	return pop
}

func main() {
	// GEN_MAX := 1000
	// ELITE := 1
	// MUTATE_PROB := 0.01
	// N := 64
	// FLT_MAX := 1.7976931348623157e+308
	// TOURNAMENT_SIZE := 30
	// RAND_MAX := 0x7fffffff
	POP_SIZE := 1000

	fmt.Println("GA")
	pop = NewPopulation()

}
