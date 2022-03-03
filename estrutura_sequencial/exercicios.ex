# Faça um Programa que peça dois números e imprima a soma.

n_um = IO.gets "Digite um valor: "
{int_n_um, _} = Integer.parse(n_um)
n_dois = IO.gets "Digite outro valor: "
{int_n_dois, _} = Integer.parse(n_dois)
IO.puts "A soma dos valores é: #{int_n_um+int_n_dois}"
