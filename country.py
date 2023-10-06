from countryinfo import CountryInfo

count = input("Informe o nome do país: ")

country = CountryInfo(count)

print("A Capital é: ", country.capital())
print("A moeda é: ", country.currencies())
print("Pertence a região: ", country.region())
print("O idioma é: ", country.languages())
print("Os países vizinhos são: ", country.borders())
print("Outros nomes: ", country.alt_spellings())

