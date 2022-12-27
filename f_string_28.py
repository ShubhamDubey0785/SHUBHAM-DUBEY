letter="Hey my Name is {} and I am from {}"
country="India"
name="Deepak Kumar"
print(letter.format(name,country))
print(f"Hey my name is {name} and I am from {country}")

txt="For only {price:.2f} dollars!"
print(txt.format(price=1818.058000545))

rupee=48
print(f"For only this {rupee:.2f}")
print(f"{2*30}")
print(type(f"{2*30}"))