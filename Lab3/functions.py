from itertools import permutations
import random

def grams_to_ounces(grams):
    ounces = grams * 28.3495231
    return ounces

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def solve(heads, legs):
    chickens = (legs - 2 * heads) / 2
    rabbits = heads - chickens
    return chickens, rabbits

def filter_prime(arr):
    primes = []
    for num in arr:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

def string_permutations(s):
    return list(permutations(s))

def reverse_words(s):
    return " ".join(s.split()[::-1])

def has_33(arr):
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1] == 3:
            return True
    return False

def has_007(arr):
    for i in range(len(arr) - 2):
        if arr[i] == 0 and arr[i + 1] == 0 and arr[i + 2] == 7:
            return True
    return False

def volume_of_sphere(radius):
    volume = 4/3 * 3.14159 * radius ** 3
    return volume

def unique_elements(arr):
    unique = []
    for num in arr:
        if num not in unique:
            unique.append(num)
    return unique

def is_palindrome(s):
    return s == s[::-1]

def histogram(arr):
    for num in arr:
        print("*" * num)

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    print("Take a guess.")

    number = random.randint(1, 20)

    guess = int(input())
    attempts = 1

    while guess != number:
        if guess < number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        print("Take a guess.")
        guess = int(input())
        attempts += 1

    print(f"Good job, {name}! You guessed my number in {attempts} guesses!")

def is_good_movie(movie):
    return movie["imdb"] > 5.5

def get_good_movies(movies):
    return [movie for movie in movies if is_good_movie(movie)]

def get_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

def average_movie_score(movies):
    return sum(movie["imdb"] for movie in movies) / len(movies)

def average_movie_score_category(movies, category):
    category_movies = get_category(movies, category)
    return average_movie_score(category_movies)