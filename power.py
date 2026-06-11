def main():
    name = input('What is your name? ')
    age = int(input('How old are you? '))
    fighting_style = input('Your preffered fighting style? ')
    p = power_level(age)
    power = rank(p) 
    print(character_card(name,age,fighting_style,p,power))

def power_level(age):
    return(age * 9)

def rank(power):
    if power < 100:
        return 'Geni'
    elif power < 500:
        return 'Chunin'
    else:
        return 'Kage'
    

def character_card(name, age, fighting_style, power_level, rank):
    return(f"{name} \n{age} \n{fighting_style} \n{power_level} \n{rank}")


main()