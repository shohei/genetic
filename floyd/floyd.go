package main

import (
	"fmt"
	"math"
	"math/rand"
	"sort"

	"github.com/mkmik/argsort"
)

const (
	GEN_MAX         int     = 1000
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

func (p *Individual) Crossover_two_point(p1, p2 *Individual) {
	point1 := rand.Intn(RAND_MAX) % (N - 1)
	point2 := (point1 + (rand.Intn(RAND_MAX)%(N-2) + 1)) % (N - 1)
	if point1 < point2 {
		point1, point2 = point2, point1
	}
	for i := 0; i < point1; i++ {
		p.Chrom[i] = p1.Chrom[i]
	}
	for i := point1; i < point2; i++ {
		p.Chrom[i] = p2.Chrom[i]
	}
	for i := point2; i < N; i++ {
		p.Chrom[i] = p1.Chrom[i]
	}
}

func (p *Individual) Mutate() {
	for i := 0; i < N; i++ {
		if rand.Float64() < MUTATE_PROB {
			p.Chrom[i] = 1 - p.Chrom[i]
		}
	}
}

type Population struct {
	Ind     []*Individual
	NextInd []*Individual
	BestFit float64
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
		p.NextInd[i].Crossover_two_point(p.Ind[p1], p.Ind[p2])
	}
	for i := 0; i < POP_SIZE; i++ {
		p.NextInd[i].Mutate()
	}
	p.NextInd = p.Ind
	p.Evaluate()
}

func (p *Population) Select_tournament() int {
	tmp := make([]int, N)
	ret := -1
	p.BestFit = FLT_MAX
	num := 0
	for {
		r := rand.Intn(RAND_MAX) % N
		if tmp[r] == 0 {
			tmp[r] = 1
			if p.Ind[r].Fitness < p.BestFit {
				ret = r
				p.BestFit = p.Ind[r].Fitness
			}
			num += 1
			if num == TOURNAMENT_SIZE {
				break
			}
		}
	}
	return ret
}

func (p *Population) PrintResult() {
	fmt.Print("Set A:")
	for i := 0; i < N; i++ {
		if p.Ind[0].Chrom[i] == 1 {
			fmt.Printf("√%d", i+1)
		}
	}
	fmt.Println()
	fmt.Print("Set B:")
	for i := 0; i < N; i++ {
		if p.Ind[0].Chrom[i] == 0 {
			fmt.Printf("√%d", i+1)
		}
	}
	fmt.Println()
	fmt.Printf("Difference: %f\n", p.Ind[0].Fitness)
}

func main() {
	p := NewPopulation()
	for i := 0; i < GEN_MAX; i++ {
		p.Alternate()
		fmt.Printf("Generation:%d, best fitness: %f", i, p.Ind[0].Fitness)
		fmt.Println(i)
	}
	p.PrintResult()

}
