''' Class: CSE 1321L
Section: J51
Term: FALL 2024
Name: Makeba Waddy
Assignment 2 '''

animal = input("Enter the name of an animal: ").strip().lower()

Mammal = ("Dog", "cat", "human", "elephant", "whale")
Bird = ("eagle", "parrot", "penguin", "sparrow")
Reptile = ("snake", "lizard", "crocodile", "turtle")
Fish = ("salmon", "goldfish", "shark", "tuna")
Amphibian = ("frog", "toad", "salamander", "newt")


if animal in Mammal:
    print("The animal is a Mammal.")
elif animal in Bird:
    print("The animal is a Bird.")
elif animal in Fish:
    print("The animal is a Fish.")
elif animal in Amphibian:
    print("The animal is an Amphibian.")

else:
    print("Unknown Category.")


