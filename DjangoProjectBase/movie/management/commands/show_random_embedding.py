import random
import numpy as np
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Show the stored embedding of a random movie from the database"

    def handle(self, *args, **kwargs):
        movies = list(Movie.objects.all())
        random_movie = random.choice(movies)

        # ✅ Recuperamos el embedding guardado como binario y lo convertimos de vuelta a array
        embedding_vector = np.frombuffer(random_movie.emb, dtype=np.float32)

        self.stdout.write(f"🎲 Película al azar: '{random_movie.title}'")
        self.stdout.write(f"📐 Dimensión del embedding: {len(embedding_vector)}")
        self.stdout.write(f"🔢 Primeros 10 valores: {embedding_vector[:10]}")
        self.stdout.write(f"🔢 Embedding completo: {embedding_vector}")
