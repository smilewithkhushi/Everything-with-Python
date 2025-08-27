class Movie:
    def __init__(self, title, director, year, genre, rating):
        self.title = title
        self.director = director
        self.year = int(year)
        self.genre = genre
        self.rating = float(rating)

    def display_info(self):
        print("\nMovie Information:")
        print(f"Title: {self.title}")
        print(f"Director: {self.director}")
        print(f"Year: {self.year}")
        print(f"Genre: {self.genre}")
        print(f"Rating: {self.rating}/10")

    def is_classic(self):
        return self.year < 2000

    def is_highly_rated(self):
        return self.rating >= 8.0


def main():
    print("Welcome to the Movie Input Program!")

    movie_list = []
    while True:
        print("\nEnter movie details:")
        title = input("Title: ")
        director = input("Director: ")
        year = input("Year: ")
        genre = input("Genre: ")
        rating = input("Rating (out of 10): ")

        movie = Movie(title, director, year, genre, rating)
        movie_list.append(movie)

        more = input("Add another movie? (y/n): ").lower()
        if more != 'y':
            break

    print("\n----- Movie Library -----")
    for m in movie_list:
        m.display_info()
        print("Classic Movie?" , "Yes" if m.is_classic() else "No")
        print("Highly Rated?" , "Yes" if m.is_highly_rated() else "No")
        print("-----------------------------")


if __name__ == "__main__":
    main()
