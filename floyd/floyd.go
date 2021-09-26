package main

import (
	"fmt"
	"math"
	"math/rand"
	"sort"

	"github.com/mkmik/argsort"
)

const (
	GEN_MAX         int     = 10
	POP_SIZE        int     = 1000
	ELITE           int     = 1
	MUTATE_PROB     float64 = 0.01
	N               int     = 64
	FLT_MAX         float64 = 9999999
	TOURNAMENT_SIZE int     = 30
	RAND_MAX        int     = N * 65536
)

type Individual struct {
	Chrom   [N]int
	Fitness float64
}

func NewIndividual() *Individual {
	n := new(Individual)
	for i := 0; i < N; i++ {
		n.Chrom[i] = rand.Intn(RAND_MAX) % 2
	}
	return n
}

func (p *Individual) Evaluate() {
	fitness := 0.0
	for i := 0; i < N; i++ {
		fitness += float64(p.Chrom[i]*2-1) * math.Sqrt(float64(i+1))
	}
	p.Fitness = math.Abs(fitness)
}

type Population struct {
	Ind     []*Individual
	NextInd []*Individual
}

func (p *Population) Evaluate() {
	for i := 0; i < POP_SIZE; i++ {
		p.Ind[i].Evaluate()
	}
	fitnesses := make([]float64, 0)
	for _, ind := range p.Ind {
		fitnesses = append(fitnesses, ind.Fitness)
	}

	orders := argsort.Sort(sort.Float64Slice(fitnesses))
	ranks := argsort.Sort(sort.IntSlice(orders)) //必要??
	tmp := p.Ind
	for i, rank := range ranks {
		p.Ind[rank] = tmp[i]
	}

}

func NewPopulation() *Population {
	p := new(Population)
	p.Ind = make([]*Individual, POP_SIZE)
	p.NextInd = make([]*Individual, POP_SIZE)
	for i := 0; i < POP_SIZE; i++ {
		p.Ind[i] = NewIndividual()
		p.NextInd[i] = NewIndividual()
	}
	p.Evaluate()
	return p
}

func (p *Population) Alternate() {
	for i := 0; i < ELITE; i++ {
		for j := 0; j < N; j++ {
			p.NextInd[i].Chrom[j] = p.Ind[i].Chrom[j]
		}
	}
	for i := ELITE; i < POP_SIZE; i++ {
		p1 := p.Select_tournament()
		p2 := p.Select_tournament()
		p.NextInd[i].Crossover_two_point(p.ind[p1], p.ind[p2])
	}
	for i := 0; i < POP_SIZE; i++ {
		p.NextInd[i].Mutate()
	}
	p.NextInd = p.Ind
	p.Evaluate()
}

func (p *Population) Select_tournament() *Population {
	newp := NewPopulation()
	return newp
}

func main() {
	p := NewPopulation()
	x := make([]int, 0)
	y := make([]float64, 0)
	for i := 0; i < GEN_MAX; i++ {
		p.Alternate()
		fmt.Printf("Generation:%d, best fitness: %f", i, p.ind[0].fitness)
		x = append(x, i)
		y = append(y, p.ind[0].fitness)
	}

	p.printResult()

}
