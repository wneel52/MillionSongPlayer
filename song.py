class Song:

    def __init__(self, artist_name: str, song_title: str, song_id: str, duration: float, year: int):
        """

        :param artist_name: Represents the name of the artist.
        :param song_title: Denotes the title of the song.
        :param song_id: A unique identifier for the song.
        :param duration: Specifies the song's length, measured in seconds
        :param year: Indicates the year the song was released.
        :return: None -> constructor
        """

        self.artist_name = artist_name

        self.song_title = song_title

        self.song_id = song_id

        self.duration = duration

        self.year = year

    def __str__(self):
        """

        :return: returns a string containing basic song information
        """

        return f"{self.song_title} by {self.artist_name} (ID: {self.song_id}) released in {self.year}"

    def play(self):
        """

        :return: None : prints info for song while playing it
        """
        print(f"{self.song_title} is playing, with a duration of {'{:.6f}'.format(self.duration)} second(s)")
