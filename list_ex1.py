movies = ["Inception","The Imitation Game","Intersteller","The Red Game",
"Gravity","The Martian","Angels And Demons","Inferno","Salt",
"Event Horizon"]

print(len(movies))
print(movies)

movies.sort() # sorting is not work in mixed data
print(movies)

movies.reverse()
print(movies)

print('first movie',movies[0])
print('last movie',movies[-1])
print('first 3 movies',movies[:3])
print('all movies except first 3',movies[3:])
print('movies with even indexes',movies[::2])