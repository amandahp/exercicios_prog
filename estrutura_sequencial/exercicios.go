// Faça um Programa que peça dois números e imprima a soma.

package main
import "fmt"

func main() {
  fmt.Println("Digite um valor: ")
	var first float64 

	fmt.Scanln(&first)
  fmt.Println("Digite um segundo valor: ")
	var second float64
	fmt.Scanln(&second)

	fmt.Print("A soma dos valores é: ")

	fmt.Print(first + second)
}
