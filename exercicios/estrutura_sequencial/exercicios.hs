-- Faça um Programa que peça dois números e imprima a soma.
{-#LANGUAGE ScopedTypeVariables#-}
theAnswerNumber :: Float -> Float 
theAnswerNumber r  = r 

main = do 
    putStrLn "Digite um numero "
    nUm :: Float <- readLn
    putStrLn "Digite outro numero "
    nDois :: Float <- readLn
    print (theAnswerNumber nUm+nDois)